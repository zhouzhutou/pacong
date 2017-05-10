import urllib
import urlparse
import os
from config import pic_loc
image_url="http://www.ipilab.org/BAAweb/JPEGimages/ASIF/ASIF04/5132.jpg";
#os.chdir(r"F:\bonePic")
response=urllib.urlopen(image_url)
list = image_url.split("/")
image_name = list[len(list) - 1]
print image_name
image_name=os.path.join(pic_loc,image_name).strip()
f=open(image_name,'wb')
f.write(response.read())
f.close()
