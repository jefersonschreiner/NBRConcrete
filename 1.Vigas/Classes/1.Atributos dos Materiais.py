import math

class Matbeam:

    def __init__(self):
        self.fck = None
        self.fyk = None
        self.comb = None
        self.yc = None
        self.ys = None
        self.group = None

    def data(self):
        print("Verificação da Viga - Defina o Material")
        print("\nInforme os valores do material:")

        self.fck = float(input("Valor do Fck (MPa): "))
        self.fyk = float(input("Valor do Fyk (MPa): "))
        self.comb = input("Combinações das Forças: ")

        self.set_coef()
        self.group = self.group_definer()

# Caso o Fck seja <= 50 grupo 1 se >50 grupo 2
    def group_definer(self):
        return 1 if self.fck <= 50 else 2

# Valores de Coeficiente de Segurança p/ cada combinação
    def set_coef(self):
        if self.comb.lower() == 'normal':
            self.yc = 1.4
            self.ys = 1.15
        elif self.comb.lower() == 'especial':
            self.yc = 1.2
            self.ys = 1.15
        elif self.comb.lower() == 'excepcional':
            self.yc = 1.2
            self.ys = 1.0
        elif self.comb.lower() == 'serviço':
            self.yc = 1.0
            self.ys = 1.0
        else:
            raise ValueError(
                "Combinação inválida: Normal, Especial, Excepcional ou Serviço")

# Contas para cada grupo
    def c_math_exec(self):
        if self.group == 1:
            fcd = (self.fck / self.yc)/10
            fctksup = (0.39 * (self.fck ** (2/3)))/10
            fctkinf = (0.21 * (self.fck ** (2/3)))/10

            return (fcd, fctkinf, fctksup)

        else:
            fcd = (self.fck / self.yc)/10
            fctksup = 2.756 * math.log(1 + 0.11 * self.fck)/10
            fctkinf = 1.484 * math.log(1 + 0.11 * self.fck)/10

            return (fcd, fctkinf, fctksup)

    def s_math_exec(self):
        fyd = self.fyk / self.ys
        es = 21000

        return (fyd, es)


#Teste de Funcionamento

viga = Matbeam()

viga.data()

fcd, fctkinf, fctksup = viga.c_math_exec()
fyd, es = viga.s_math_exec()


print(f"Fcd = {fcd:.3f} kN/cm²")
print(f"FctkInf = {fctkinf:.3f} kN/cm²")
print(f"FctkSup = {fctksup:.3f} kN/cm²")
print(f"Fyd = {fyd:.3f} kN/cm²")
print(f"Es = {es:.0f} mPa")

