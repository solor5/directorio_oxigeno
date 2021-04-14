import mysql.connector
from mysql.connector import errorcode

config = {
'user': 'b3cb85ced16c06',
'password':'2f6fcd42',
'host': 'us-cdbr-east-03.cleardb.com',
'database':'heroku_44f49ac0efa1594',
'raise_on_warnings': True
}

class MySQL(object):
    def __init__(self, st):
        self.st = st
        self.get_connection()

    def get_connection(self):
        try:
            self.cnx = mysql.connector.connect(**config)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.st.text("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.st.text("Database does not exist")
            else:
                self.st.text('Unknown error')

    def get_all_data(self) :
        try :
            self.cursor.execute("SELECT company.name, celphone1, celphone2, aparments.name, city, price, latitude, longitude FROM  company INNER JOIN aparments ON aparments.idAparment = company.aparments_id")
        except mysql.connector.Error as err:
            return False, str(err.errno)

        result = self.cursor.fetchall()
        print(result)
        if result :
            return {"state": True, "response": result}
        else :
            return {"state": False, "response": "Record not found"}

    def get_citys(self):
        try :
            self.cursor.execute("SELECT * FROM  aparments")
        except mysql.connector.Error as err:
            return False, str(err.errno)

        result = self.cursor.fetchall()
        if result :
            return {"state": True, "response": result}
        else :
            return {"state": False, "response": "Record not found"}

    def add_data(self,company,celphone1,celphone2,address,price,aparment_id,city) :
        self.get_connection()
        sql = "INSERT INTO company (name, celphone1, celphone2, address, price, city, aparments_id) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        val = (company,celphone1,celphone2,address,price,city,aparment_id)
        try :
            self.cursor.execute(sql,val)
        except mysql.connector.Error as err:
            print(str(err.errno))
            return False
        self.cnx.commit()
        self.cnx.close()
        return True

