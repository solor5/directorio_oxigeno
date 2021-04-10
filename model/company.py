

def get_all_data(self) :
        try :
            self.cursor.execute("SELECT company.name, celphone1, celphone2, citys.name, price, latitude, longitude FROM  company INNER JOIN citys ON citys.idCitys = company.citys_id")
        except mysql.connector.Error as err:
            return False, str(err.errno)

        result = self.cursor.fetchall()
        if result :
            return {"state": True, "response": result}
        else :
            return {"state": False, "response": "Record not found"}

    def get_citys(self):
        try :
            self.cursor.execute("SELECT * FROM  citys")
        except mysql.connector.Error as err:
            return False, str(err.errno)

        result = self.cursor.fetchall()
        if result :
            return {"state": True, "response": result}
        else :
            return {"state": False, "response": "Record not found"}

    def add_data(self,company,celphone1,celphone2,address,price,citys_id) :
        self.get_connection()
        sql = "INSERT INTO company (name, celphone1, celphone2, address, price, citys_id) VALUES (%s, %s, %s, %s, %s,%s)"
        val = (company,celphone1,celphone2,address,price,citys_id)
        try :
            self.cursor.execute(sql,val)
        except mysql.connector.Error as err:
            return False, str(err.errno)
        self.cnx.commit()
        self.cnx.close()
        return True
