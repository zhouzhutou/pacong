# encoding: utf-8
from bone_spider import html_downloader
from bone_spider import url_manager
from bone_spider import config
from bone_spider import html_parser
from bone_spider import mysql_op
from bone_spider import mysql_manage
from bone_spider import pic_download
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.manage=mysql_manage.Connection()
        self.operation=mysql_op.Operation()
        self.picDownload=pic_download.PicDownload()

    def craw(self):
        # self.urls.add_new_url(root_url)
        person_infos = []
        img_urls=[]
        '''
        for race in config.races:
        '''

        for gender in config.genders:
            for age in config.ages:
                params={"Race":config.races[0],"Gender":gender,"Age":age}
                html_content = self.downloader.download(params)
                image_urls=self.parser.parse(html_content)
                #image_urls, res_data=self.parser.parse(html_content)
                #print("%d\n" % len(image_urls))
                #print("%d\n" % len(res_data))
                #for item in res_data:
                    #person_infos.append(tuple(item))
                    #print item
                for image_url in image_urls:
                    img_urls.append(image_url)
                    print image_url

        # 保存数据到数据库
        '''
        conn = self.manage.getCon()
        try:
            self.operation.insertManyPersonInfos(conn, person_infos)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        self.manage.close(conn)
        '''
        # 下载图片
        self.picDownload.downloadPics(img_urls)
        #for img_url in img_urls:
            #self.picDownload.downloadPic(img_url)
        #while self.urls.has_new_url():
            #self.picDownload.downloadPic(self.urls.get_new_url())


if __name__=="__main__":
    obj_spider=SpiderMain()
    obj_spider.craw()