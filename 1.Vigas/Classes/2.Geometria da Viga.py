import math

class Geobeam:

    def __init__ (self):
        self.type_beam = None
        self.bw = None
        self.h = None
        self.hf = None
        self.bf = None
 
    #Função de Definição da Geometria da Viga
    def geo_define(self):
        print("Verificação da Viga - Defina a Geometria")

        while True:
            self.type_beam = input("Qual o tipo de Vigaw? (Q/T): ").upper()

            if self.type_beam == 'Q':
                print("\nInforme as dimensões da viga quadrangular:")
                self.bw = float(input("Largura da Viga (bw) em cm: "))
                self.h = float(input("Altura da Viga (h) em cm: "))
                break
            
            elif self.type_beam == 'T':
                print("\nInforme as dimensões da viga em T:")
                self.bw = float(input("Largura da Alma (bw) em cm: "))
                self.h = float(input("Altura Total da Viga (h) em cm: "))
                self.hf = float(input("Altura da Mesa (hf) em cm: "))
                self.bf = float(input("Lrgura da Mesa (bf) em cm: "))
                break

            else:
                print("Opção inválida!")

    #Cálculo dos parâmetros da Viga Retangular
    def quad_math(self):
        if self.type_beam != 'Q':
            print("Erro")
            return None
        
        wo = (self.bw * (self.h ** 2))/6

        return (wo)
    
    def t_math(self):
        
        #Cálculo do Wo
        aw = self.bw * self.h
        aa = (self.bf - self.bw)*self.hf
        at = aw + aa
        c = ((aw * self.h)/(2 * at)) + ((aa / (2 * at))*(2 * self.h - self.hf))
        clinha = self.h - c
        wo1 = aw / (3 * c)
        wo2 = (self.h ** 2) + 3 * (c ** 2)
        wo3 = aa / (3 * c)
        wo4 = (self.hf ** 2) + 3 * (clinha ** 2)
        wo = (wo1 * wo2) + (wo3 * wo4)

        #Verificação das Forças da  Mesa
        '''
        mrda = 
        mrdf =

        '''
        return (wo)

    def calculate_wo(self):
        if self.type_beam == 'Q':
            return self.quad_math()
        elif self.type_beam == 'T':
            return self.t_math()
        else:
            print("Tipo de viga não definido")
            return None

#Teste

geometria = Geobeam()

geometria.geo_define()
wo = geometria.calculate_wo()

print(f"Wo = {wo:.3f} cm³")
