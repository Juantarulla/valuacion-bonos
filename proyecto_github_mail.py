import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

print("las opciones de bonos a valuar son :")
print("\tfrances")
print("\taleman")
print("\tbullet")

bono = input("por favor escriba que tipo de bono quiere valuar : ")

bono = bono.lower()

while True:
    if bono == "frances":
        break
    elif bono == "aleman":
        break
    elif bono == "bullet":
        break
    else:
        bono = input("por favor escriba una opcion disponible! : ")
        continue


t = int(input("escriba si quiere que la base sea de  365 o 360 dias : "))

while True:
    if t == 365:
        break
    elif t == 360:
        break
    else:
        t = int(input("porfavor escriba solo 365 0 360 : "))
        continue





print("\nde donde quieres sacar la tasa de interes efectiva ?\n ")
inf = str(input("opciones TNA(tna), la tasa de interes efectiva viene dada(ie) ,tasa de interes efectiva que necesita modificar su periodo(im)" + " : "))          
i = float(input("escriba la tasa de interes : "))

if i < 1:
    print(i)
else:
    i = i/100
    
    print(str(i) + "\n")
    
c = int(input("cada cuantos dias se pagan los cupones: "))  
  
while True:     
    if inf == "tna":
      i = round(float(i)*c/t,10)
              
      print("la tasa de interes efectiva es del " + str(i*100) + "% .")
      break
    elif inf == "ie":
      print("la tasa de interes efectiva es del " + str(i*100) + "% .")
      break
    elif inf == "im":
    
        ce = float(input("cada cauntos dias se paga la i original efectiva? "))
        i = (1 + float(i))**(c/ce)-1
        print("la tasa de interes efectiva es del " + str(i*100) + "% .")
        break
    else:
        inf = str(input("opcion " + str(inf) + " no encontrada,\npor favor escriba una opcion disponible : "))
        continue
va = float(input("cual es el valor actual del bono a valuar : "))
ca = int(input(("por cuantos dias se paga el cupon : ")))
io = i
ci = int(ca/c)


if bono == "frances" :         
    
        
   precio_cupon = (va/((1-(1+i)**(-ca/c))/i))
    
    
   bonos = [precio_cupon]*ci
            
   print(bonos)
        
elif bono == "aleman":
     cv = va/ci
     bonos = []
    
    
     while float(va) > int(1):
          p = cv + va*i
          va = va - cv
          bonos.append(p)
    
     print("los cupones son : ")
     print(bonos)
     
elif bono == "bullet":
    ci = int(ca/c)
    interes = va*i
    bonos = []
    while len(bonos) < (ci-1):
        bonos.append(interes)
    
    ult_bono = interes + va
    bonos.append(ult_bono)
    print(bonos)
    
    
l = int(ca/c)

hoy = dt.date.today()
print(hoy)
dia_1 = dt.timedelta(days=c)
n = hoy + dia_1
dias_pagos = []

while l>0:
    dias_pagos.append(n)
    n += dia_1
    l = l -1


x = pd.DataFrame(index = [dias_pagos])

x["cupones"] = bonos
   
graficar = str(input("quieres ver el grafico con los dias y los cupones a pagar?\n(si)/(no):"))

if graficar == "si": 
    x.loc[:,"cupones"].plot(kind="bar")

data = str(input("quieres ver el data frame?\n(si)/(no):"))
    
if data == "si":
    print(x)

valuar = input(("quieres valuar el bono a valor presente : \n(si)/(no)"))



if valuar == "si":
    

    n = int(input("en que periodo quieres valuar : "))

    s = n-1

    for bono in bonos:
        if bonos.index(bono) <= s:
            bonos[bonos.index(bono)] = 0
        
    while 0 in bonos:
        bonos.remove(0)
    
    valor_mercado = []
    print("\nde donde quieres sacar la tasa de interes efectiva ?\n ")
    inf = str(input("opciones TNA(tna), la tasa de interes efectiva viene dada(ie) ,tasa de interes efectiva que necesita modificar su periodo(im)" + " : "))
    i = float(input("tasa interes : "))
    if i < 1:
        print(i)
    else:
        i = i/100
        
        print(str(i) + "\n")
        
    while True:     
        if inf == "tna":
          i = round(float(i)*c/t,10)
                  
          print("la tasa de interes efectiva es del " + str(i*100) + "% .")
          break
        elif inf == "ie":
          print("la tasa de interes efectiva es del " + str(i*100) + "% .")
          break
        elif inf == "im":
        
            ce = float(input("cada cauntos dias se paga la i original efectiva? "))
            i = (1 + float(i))**(c/ce)-1
            print("la tasa de interes efectiva es del " + str(i*100) + "% .")
            break
        else:
            inf = str(input("opcion " + str(inf) + " no encontrada,\npor favor escriba una opcion disponible : "))
            continue
    
    
    dias_cupon = c
    print("\nejemplo si quieres 20 dias despues del periodo que elejiste, escribe 20")
    dias_valuar = int(input("cuantos dias despues del periodo lo quiere valuar : "))
    l = 0
    for bono in bonos:
            
            per = dias_cupon + l
            valor = (bono/(1 + i)**(per/dias_cupon))*(1 + i)**(dias_valuar/dias_cupon)
            l += dias_cupon
            valor_mercado.append(valor)
    
    valor_tecnico = []
    
    q = 0
    for bono in bonos:
            
            per = dias_cupon + q
            valor = bono/(1 + io)**(per/dias_cupon)
            q += dias_cupon
            valor_tecnico.append(valor)
        
    
    
    print("\nel valor tecnico en " + str(n) + " es " + str(sum(valor_tecnico)))
    print("\nel valor de mercado en " + str(n) + " es " + str(sum(valor_mercado)))
    
    interes_corrido = sum(valor_tecnico)*io*dias_valuar/dias_cupon
    paridad_tecnica = sum(valor_mercado)/(sum(valor_tecnico) + interes_corrido)    
    print("la paridad tecnica es de " + str(round(paridad_tecnica*100,4)) + "%")
    
    print("el precio sucio es de " + str(sum(valor_mercado) - interes_corrido))
              