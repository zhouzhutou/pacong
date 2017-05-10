# encoding: utf-8
import pymysql
from bone_spider import mysql_config
class Connection(object):

    def getCon(self):
        try:
            self.conn=pymysql.connect(host=mysql_config.host,
                                      user=mysql_config.username,
                                      password=mysql_config.password,
                                      db=mysql_config.db)
            #self.cur=self.conn.cursor();
            print "connect to DB successfully"
            return self.conn
        except Exception as e:
            raise e


    def close(self,conn):
        conn.close()

#con=Connection()
#con.getCon()