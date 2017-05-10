import httplib
#encoding: utf-8
from bone_spider import config
from bone_spider import util
class HtmlDownloader(object):

    def download(self,params):
        if config.host is None:
            return
        conn=httplib.HTTPConnection(config.host)
        param_data=util.gen_play_load(params)
        headers = {
            'cache-control': config.cache_control,
            'content-type': config.content_type
        }
        conn.request(config.method, config.path, param_data, headers)
        try:
            res=conn.getresponse()
            return res.read().decode('utf-8')
        except  Exception as e:
            return None

        

