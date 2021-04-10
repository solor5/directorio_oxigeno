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
        try:
            self.cnx = mysql.connector.connect(**config)
            self.cursor = self.cnx.cursor()
            self.st.text("Connecction success")
            st.text("Connecction success")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.st.text("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.st.text("Database does not exist")
            else:
                self.st.text('Unknown error')

    def get_all_data(self) :
        try :
            self.cursor.execute("SELECT * FROM  company INNER JOIN citys ON citys.idCitys = company.citys_id")
        except mysql.connector.Error as err:
            return False, str(err.errno) + " : " + sql

        result = self.cursor.fetchall()
        if not result :
            return {"state": False, "response": "Record not found"}
        else :
            return {"state": True, "response": result}