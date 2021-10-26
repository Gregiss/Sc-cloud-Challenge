#Ele tem a complexidade de tempo (On)
def fibo(n):
    if n==0:
        return 0
    i=0
    j=1
    for k in range(1,n):
        t=i+j
        i=j
        j=t 
    return j
a=int(input("Quantas posições voce necessita?"))
res=fibo(a)
print('Na posição %dª o valor é \033[1;033m%d' % (a,res))
