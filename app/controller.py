from tkinter import *

class Controller():

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setCommandSearch(self.buscarSensor)
        self.view.setCommandInsert(self.insertSensor)
        self.view.setCommandDelete(self.deleteSensor)
        self.view.setCommandUpdate(self.updateSensor)
        self.view.setCommandCommit(self.commitBanco)

    def buscarSensor(self):
        codigo_idSensor = self.view.txtcodigo_idSensor.get()
        sensor  = self.model.read_one_sensor(codigo_idSensor)
        self.view.updateBySearch(sensor)

    def insertSensor(self):
        idSensor = self.view.txtcodigo_idSensor.get()
        variavel = self.view.txtVariavel.get()
        medicao = self.view.txtMedicao.get()
        unidade = self.view.txtUnidade.get()
        registro = self.view.txtRegistro.get()
        latitude = self.view.txtLatitude.get()
        longitude = self.view.txtLongitude.get()

        self.model.insert_one_sensor(codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude)
        self.view.logUpdate(codigo_idSensor)

    def deleteSensor(self):
        codigo_idSensor = self.view.txtcodigo_idSensor.get()
        self.model.delete_one_sensor(codigo_idSensor)

    #Crie aqui o método para atualizar os dados
    def updateSensor(self):
        codigo_idSensor = self.view.txtcodigo_idSensor.get()
        variavel = self.view.txtVariavel.get()
        medicao = self.view.txtMedicao.get()
        unidade = self.view.txtUnidade.get()
        registro = self.view.txtRegistro.get()
        latitude = self.view.txtLatitude.get()
        longitude = self.view.txtLongitude.get()

        self.model.read_one_sensor(codigo_idSensor)
        self.model.update_one_sensor(codigo_idSensor, variavel, medicao, unidade, registro, latitude, longitude)
        self.view.alterar(codigo_dSensor)

    def commitBanco(self):
        self.model.commit_changes()
        self.view.comit()