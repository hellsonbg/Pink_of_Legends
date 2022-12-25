from db_campeoes import *

class consulta_classe:
    consulta = ''
    lista = []
    def __init__(self,con_classe):
        self.consulta = con_classe
        c = 0
        for i in db_campeoes:
            if self.consulta in db_campeoes[c].classes:
                self.lista.append(db_campeoes[c].nome)
            else:
                pass
            c +=1    

class consulta_funcao:
    consulta = ''
    lista = []
    def __init__(self,con_funcao):
        self.consulta = con_funcao
        c = 0
        for i in db_campeoes:
            if self.consulta in db_campeoes[c].funcoes:
                self.lista.append(db_campeoes[c].nome)
            else:
                pass
            c +=1   

class consulta_regiao:
    consulta = ''
    lista = []
    def __init__(self,con_regiao):
        self.consulta = con_regiao
        c = 0
        for i in db_campeoes:
            if self.consulta in db_campeoes[c].regioes:
                self.lista.append(db_campeoes[c].nome)
            else:
                pass
            c +=1   







