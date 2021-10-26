def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

a=int(input("Quantas posições voce necessita?"))
res=fibo(a)
print('Na posição %dª o valor é \033[1;033m%d' % (a,res))

    