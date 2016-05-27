import pprint
from reddit.models import db_connect, Image
from sqlalchemy.orm import sessionmaker

__author__ = 'ramon'


from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

from multiprocessing.pool import Pool
from os import listdir
from os.path import isfile, join

pp = pprint.PrettyPrinter(indent=4)


PIC_DIR = 'reddit/amin_pic/'


amin_pic = [join(PIC_DIR, f) for f in listdir(PIC_DIR) if isfile(join(PIC_DIR, f))]


es = Elasticsearch()

ses = SignatureES(es,timeout='30s')


def test():

    #all_images = retrieve_images_url()

    #all_images = [image.image_link for image in all_images]
    #all_images = retrieve_missing_pic()

    #write_to_elastic(all_images)

    search_pic(amin_pic)


def retrieve_images_url():
    engine = db_connect()

    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Image).all()


def retrieve_missing_pic():
    lines=[]
    with open('amin1_missing_pic.txt') as f:
        lines = f.read().splitlines()
    results =  [line.split(':',1) for line in lines]
    return [result[1].strip(' ') for result in results]


def store_image(url):
    try:
        ses.add_image(url)
    except IOError:
        print "could retrieve this pic : %s " %url



def search_pic(pic_list):
    result_list =[]
    for file in pic_list:
        result = ses.search_image(file)
        result_list.append({"file":file,"result":result})
    pp.pprint(result_list)



def write_to_elastic(all_images):

    p = Pool(processes=10)
    result = p.map(store_image, all_images)
    p.close()
    p.join()








if __name__ == '__main__':
    test()
