import sys
import os
import importlib.util

# Sistema Path
caminho_classes = os.path.join(os.path.dirname(__file__), 'Classes')
sys.path.append(caminho_classes)
    
# Caminho completo do arquivo
caminho_arquivo = os.path.join(caminho_classes, '1.Atributos dos Materiais.py')
    
# Carregando o módulo
spec = importlib.util.spec_from_file_location("atributos_materiais", caminho_arquivo)
modulo_materiais = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo_materiais)
    
#Contas
Material = modulo_materiais.Material

material = Material()

material.data()

fcd, fctkinf, fctksup = material.c_math_exec()
fyd, es = material.s_math_exec()

print(f"Fcd = {fcd:.3f} kN/cm²")
print(f"FctkInf = {fctkinf:.3f} kN/cm²")
print(f"FctkSup = {fctksup:.3f} kN/cm²")
print(f"Fyd = {fyd:.3f} kN/cm²")
print(f"Es = {es:.0f} mPa")