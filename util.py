# encoding: utf-8
#拼接参数方法
def gen_play_load(d):
    res=""
    i=0
    for key,value in d.items():
        if i!=0:
            res+="&"
        if isinstance(value,int):
            value=str(value)
        item=(key+"="+value)
        res=res+item
        i=i+1
    return res;