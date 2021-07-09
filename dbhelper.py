import mysql.connector
class DBHelper:
    def __init__(self):
        try:
            self._connection=mysql.connector.connect(host="127.0.0.1",user="root", password="", database="FBlike")
            self._mycursor=self._connection.cursor()
        except:
            print("Could not connect.Try again")

    def search(self, key1, value1, key2, value2, table):
        query = "SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE'{}'".format(table,key1,value1,key2,value2)
        self._mycursor.execute(query)
        response = self._mycursor.fetchall()
        return response

    def searchOne(self, key1, value1, table, type):
        query = "SELECT * FROM `{}` WHERE `{}` {}' {}'".format(table,key1,type,value1)
        self._mycursor.execute(query)
        response = self._mycursor.fetchall()
        return response

    def insert(self, mydict, table):
        cols = ""
        vals = ""
        for i in mydict:
            cols = cols + "`" + i + "`" + ","
        vals = vals + "'" + str(mydict[i]) + "'" + ","
        cols = cols[:-1]
        vals = vals[:-1]
        query = "INSERT INTO `{}` ({}) VALUES ({})".format(table,cols,vals)
        try:
            self._mycursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0

