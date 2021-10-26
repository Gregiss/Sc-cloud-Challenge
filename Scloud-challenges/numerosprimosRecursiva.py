num= int(input('Digite um numero: '))
primos= []

for a in range(1, num + 1 )
   if num % a == 0:
       primos.append(a)
    else:
        pass

if len(primos) == 2:
    print('O numero {num} é primo')
  else:
      print('O numero {num}  não é primo')                