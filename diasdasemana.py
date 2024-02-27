diadasemana = int (input ("Digite o valor que condiz com o número da semana:"))

if diadasemana<1 and  diadasemana>7 : print ("Valor não condiz com o numero de dias na semana!") 
else: 
    if diadasemana==1 : resultado = "Domingo"
    if diadasemana==2 : resultado = "Segunda-feira"
    if diadasemana==3 : resultado = "Terça-feira"
    if diadasemana==4 : resultado = "Quarta-feira"
    if diadasemana==5 : resultado = "Quinta-feira"
    if diadasemana==6 : resultado = "Sexta-feira"
    if diadasemana==7 : resultado = "Sábado"
    if diadasemana<1 or diadasemana>7 : resultado = "Valor não condiz com o numero de dias na semana!" 

print(" Resultado :" , resultado)


 