# encoding: utf-8
import urlparse
from bs4 import BeautifulSoup
from bone_spider import config
import re

class HtmlParser(object):

    def get_new_urls(self,soup):
        image_urls=set()
        image_links=soup.find_all('img', src=re.compile(r"JPEGimages/.+/.+/.+\.jpg"))
        for image_link in image_links:
            image_url=urlparse.urljoin(config.url,image_link["src"])
            image_urls.add(image_url)
        return image_urls

    def get_data(self,soup):
        res_data = []
        #item={}
        item=[]
        tables=soup.find('form').find_all('table',bgcolor=False)
        for table in tables:
            tds=table.find_all('td')
            item = []
            for i in range(0,len(tds)):
                if i == 0:
                    image_name=tds[i].find('a').get_text()
                    #item['image_name']=image_name
                    item.append(image_name)
                elif i == 1:
                    #item['race']=tds[i].get_text()
                    item.append(tds[i].get_text())
                elif i == 2:
                    #item['gender'] = tds[i].get_text()
                    item.append(tds[i].get_text())
                elif i == 3:
                    #item['chr_age']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
                elif i == 4:
                    #item['dob']=tds[i].get_text()
                    item.append(tds[i].get_text())
                elif i == 5:
                    #item['exam_date']=tds[i].get_text()
                    item.append(tds[i].get_text())
                elif i == 6:
                    #item['tanner']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
                elif i == 7:
                    #item['height']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
                elif i == 8:
                    #item['weight']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
                elif i == 9:
                    #item['trunk_ht']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
                elif i == 10:
                    #item['reading1']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
                elif i == 11:
                    #item['reading2']=float(tds[i].get_text())
                    item.append(float(tds[i].get_text()))
            res_data.append(item)
        return res_data

    def parse(self,html_cont):
        if config.url is None or html_cont is None:
            return
        #soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'html.parser')
        image_urls=self.get_new_urls(soup)
        #res_data=self.get_data(soup)
        #return image_urls, res_data
        return image_urls