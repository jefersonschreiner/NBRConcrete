import math
from Geometria_Viga import geobeam

class adm:

    def __init__(self):
        pass

    def admmat(self, grupo, fck):
        if grupo == 1:
            ac = 0.85
            cc = 0.8
            nc = ac
            ecu = 3.5/1000
            return(cc, nc, ecu)
    
        else:
            ac = 0.85 * ( 1 - ((fck - 50)/200))
            cc = 0.8 - ((fck-50)/400)
            nc = ac
            ecu = (2.6/100) + ((35/1000) * (((90 -fck)/100)**4))

            return(cc, nc, ecu)

    def admb(self):
        pass

#Variáveis da Classe
adimensionais = adm()
cc, nc, ecu = adm.admmat()

#Outras Classes
geo = geobeam()
geo.t_math(cc, nc)
