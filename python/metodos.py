#métodos de ordenamientos
v_a=0
v_b=0
v_c=0
v_a=int(input("valor de a: "))
v_b=int(input("valor de b: "))
v_c=int(input("valor de c: "))
if v_a>v_b and v_a>v_c:
    print(v_a)
elif v_b>v_a and v_b>v_c:
    print(v_b)
else:
    print(v_c);

#sueldos(intercambio)
sueldos=[]
for x in range (5):
    v_valSuel=int(input("valor del sueldo: "))
    sueldos.append(v_valSuel)
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("lsita ordenada")
print(sueldos)