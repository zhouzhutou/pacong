# encoding: utf-8
from bone_spider import config
from bone_spider import util
import httplib
params = {"Race":"ASI", "Gender":"F", "Age":11}
params=util.gen_play_load(params)
print(params)
conn = httplib.HTTPConnection(config.host)
headers = {
    'cache-control': config.cache_control,
    'content-type': config.content_type
}
conn.request(config.method, config.path,params, headers)
try:
    res = conn.getresponse()
    print(res.read().decode('utf-8'))
except  Exception as e:
    raise e