age:int = 18
carga:bool = True

# Programa que decide si dar licencia de conducir o permiso de menor a un sujeto

if age < 16:
    print('No puede tener licencia ni permiso de menor')
elif age < 18:
    print('Se le puede dar permiso de menor')
elif not carga:
    print('Se le puede dar licencia de automovilista')
else:
    print('Se le asigna licencia de chofer')