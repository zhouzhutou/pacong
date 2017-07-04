# encoding: utf-8
import urllib2,urllib,socket
import os
from config import pic_loc


def callbackfunc(blocknum, blocksize, totalsize):
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%" % percent

class PicDownload(object):

    def downloadPic(self,image_url):
        #response = urllib2.urlopen(image_url,data=None,timeout=20)
        list = image_url.split("/")
        image_name=list[len(list)-1]
        print image_name
        image_save_path = os.path.join(pic_loc, image_name).strip()
        urllib.urlretrieve(image_url,image_save_path,callbackfunc)
        #f = open(image_save_path, 'wb')
        #f.write(response.read())
        #f.close()

    def downloadPics(self,image_urls):
        for image_url in image_urls:
            try:
                self.downloadPic(image_url)
            except urllib2.URLError as e:
                print image_url
                continue
