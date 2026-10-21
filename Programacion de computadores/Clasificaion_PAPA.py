Edad = ent(imput('ingrese su edad por favor = '))
if Edad > 100
   print('error en la franja de edad')
elif 80 <= Edad < 99 
   print('anciano')
elif 60 <= Edad < 80
   print('adulto mayor')
elif 30 <= Edad < 60 
   print('adulto')
elif 18 <= Edad < 30
   print('joven mayor')
elif 15 <= Edad < 18 
   print('joven menor')
elif 12 <= Edad < 15
   print('Adolecente')
elif 10 <= Edad < 12 
   print('Preadolecente')
elif 0 <= Edad < 10
   print('Niño')
else Edad < 0
   print('error por edad negativa') 

print('fin del programa')