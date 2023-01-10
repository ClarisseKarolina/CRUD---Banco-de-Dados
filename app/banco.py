import psycopg2

class Banco():

    def __init__(self, tbName):
        self.conn = psycopg2.connect(database='pabd', 
                        host='localhost', 
                        user='postgres', 
                        password='ifrn123', 
                        port='5432')
        self.cursor = self.conn.cursor()
        self.tbName = tbName

    def selectOne(self, codigo_idSensor):
        self.cursor.execute("SELECT * FROM {} WHERE codigo_idsensor = {};".format(self.tbName, codigo_idSensor))
        return self.cursor.fetchone()

    def deleteOne(self, codigo_idSensor):
        self.cursor.execute("DELETE FROM {} WHERE codigo_idsensor = {};".format(self.tbName, codigo_idSensor))

    def insertOne(self, codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        self.cursor.execute("INSERT INTO {} VALUES ({},'{}',{},'{}','{}',{},{}) RETURNING codigo_idSensor;".format(self.tbName, codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude))    
        return self.cursor.fetchone()

    def updateOne(self, codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        self.cursor.execute("UPDATE {} SET variavel='{}', medicao={}, unidade='{}', registro='{}', latitude={}, longitude={} WHERE codigo_idSensor = {};".format(self.tbName, variavel, medicao, unidade, registro, latitude, longitude,codigo_idSensor))

    def commitChanges(self):
        self.conn.commit()