from Banco import Banco

class Model():
    def __init__(self, tbName):
        self.banco = Banco(tbName)

    def read_one_sensor(self, codigo_idSensor):
        return self.banco.selectOne(codigo_idSensor)

    def delete_one_sensor(self, codigo_idSensor):
        self.banco.deleteOne(codigo_idSensor)

    def insert_one_sensor(self, codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        return self.banco.insertOne(codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude);

    def update_one_sensor(self, codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        self.banco.updateOne(codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude);

    def commitBanco(self):
        self.model.commit_changes()