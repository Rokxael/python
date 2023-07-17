edad = input('ingresa tu edad: ')
edad = int(edad)

if (edad >=18):
    print('eres mayor de edad')
    print(f'pronto tendras {edad+1} a;os')
else:
    print('eres menor de edad')
    print(f'te faltan {18-edad} para ser mayor')

print('Gracias por usar mi programa')