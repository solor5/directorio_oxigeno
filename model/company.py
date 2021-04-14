
### Aún no implementado
def get_all_data(self) :
        print('iniciando llamada')
        self.cursor.execute("SELECT company.name, celphone1, celphone2, aparments.name, city, price, latitude, longitude FROM  company INNER JOIN aparments ON aparments.idAparment = company.aparments_id")
        # try :
        # except mysql.connector.Error as err:
        #     return False, str(err.errno)

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
        sql = "INSERT INTO company (name, celphone1, celphone2, address, price, aparment_id, city) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        val = (company,celphone1,celphone2,address,price,aparment_id,city)
        try :
            self.cursor.execute(sql,val)
        except mysql.connector.Error as err:
            return False, str(err.errno)
        self.cnx.commit()
        self.cnx.close()
        return True
