import os
os.system('cls')

salario = float(input("Qual seu salário? (Para números com virgula, substitua a mesma por '.')\n-> "))

def truncate(num):
    integer = int(num * (10 ** 2)) / (10 ** 2)
    return float(integer)
salarioHora = truncate(salario / 220)

def horaExtra(salarioHora):
    global he50, he100
    hora50 = int(input('Quantas horas extras 50%?\n-> '))
    hora100 = int(input('Quantas horas extras 100%?\n-> '))
    he50 = hora50 * truncate((salarioHora + (salarioHora / 2)))
    he100 = hora100 * truncate(salarioHora * 2)
    het = he50 + he100
    return het

def adicionalNoturno(salarioHora):
    global adcNot
    horaNot = int(input('Quantas horas de adicional noturno?\n-> '))
    adcNot = horaNot * truncate((salarioHora + (salarioHora / 2)))
    return adcNot

def insalubridade(salario):
    global insalubre
    while True:
        insa = str(input('Tem adicional de insalubridade? [s/n]\n-> ')).lower()
        if insa not in ['s','n']:
            print('Responda com "S" ou "N"')
        if insa == 's':
            insalubre = salario * 0.2
            True
            return insalubre
        elif insa == 'n':
            insalubre = '0.00'
            return True
    
def vencimentos(salario):
    global vencimentos  
    vencimentos = salario + horaExtra(salarioHora) + adicionalNoturno(salarioHora) + insalubridade(salario)
    return vencimentos

def valeTransporte(salario):
    global valet
    while True:
        vt = str(input('Tem vale transporte? [s/n]\n-> ')).lower()
        if vt not in ['s','n']:
            print('Responda com "S" ou "N"')
        if vt == 's':
            valet = salario * 0.06
            True
            return valet
        elif vt == 'n':
            valet = '0.00'
            return True
        
def valeAlimentacao():
    global vr
    vreal = int(input('Quanto você recebe de Vale Refeição?\n-> '))
    if vreal == 0:
        vr = "0"
    else:
        vr = (vreal * 22) * 0.2
    return vr
    

def inss(salarioTotal):
    global soma
    if salarioTotal < 1320.00:
        inss = truncate(salarioTotal * 7.5 / 100)
        soma = inss
    elif salarioTotal >= 1320.01 and salarioTotal < 2571.29:
        inss = truncate((salarioTotal - 1320))* 9  / 100
        soma = inss + 99
    elif salarioTotal > 2571.30 and salarioTotal < 3856.94:
        inss = truncate((salarioTotal - 2571.29)) * 12 / 100
        soma = 99 + 112.61 + inss
    elif salarioTotal > 3856.95 and salarioTotal < 7507.49:
        inss = truncate((salarioTotal - 3856.94)) * 14 / 100
        soma = 99 + 112.61 + 154.27 + inss
    elif salarioTotal > 7507.49:
        soma = 876.95        

vencimentos(salario)
valeTransporte(salario)
valeAlimentacao()
inss(vencimentos)
tabela = print(f'''
TABELA COMPLETA
               
 Vencimentos:
Salário(S)                  -> {float(salario):,.2f}
Hora Extra 50%(HE50)        -> {float(he50):,.2f}
Hora Extra 100%(HE100)      -> {float(he100):,.2f}
Adicional Noturno(AdcN)     -> {float(adcNot):,.2f}
Insalubridade(I)            -> {float(insalubre):,.2f}
Total                       -> {float(vencimentos):,.2f}
Descontos:
Vale Transporte(VT)         -> {float(valet):,.2f}
Vale Refeição(VR)           -> {float(vr):,.2f}
Faltas e Atrasos(FA)        ->
Assistência Médica(AM)      ->
Adiantamento Quinzenal(AQ)  ->
Pensão Alimentícia(PA)      ->
INSS                        -> {float(soma):,.2f}
Imposto de Renda(IR)        ->
               ''')