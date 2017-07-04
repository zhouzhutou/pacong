# encoding: utf-8
class Operation(object):

    def insertManyPersonInfos(self,conn,person_infos):
        cur=conn.cursor()
        sql="insert into people_info(imageName,race,gender,chrAge,dob,examDate,tanner,height," \
            "weight,trunkHT,reading1,reading2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cur.executemany(sql,person_infos)
        finally:
            cur.close();

    def getImageNameAndAge(self,conn):
        cur=conn.cursor()
        sql="select imageName, floor(chrAge) as age from people_info WHERE race='ASI'"
        try:
            cur.execute(sql)
            res = list()
            for item in cur:
                print("imageName:%s  age:%d" % (item[0],item[1]))
                item = {"imageName": item[0], "age": int(item[1])}
                res.append(item)
            return res
        finally:
            cur.close()
