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
