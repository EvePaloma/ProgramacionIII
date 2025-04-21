def invertir(x):
    limIn = -2**31
    limSup = 2**31 - 1

    if x < 0:
        signo = -1
        x = -x
    else:
        signo = 1

    resultado = 0

    while x != 0:
        num = x % 10
        x = x // 10

        if resultado > (limSup - num) // 10:
            return 0
        
        resultado = resultado * 10 + num

    resultado *= signo

    if resultado < limIn or resultado > limSup:
        return 0
    
    return resultado
    
print(invertir(123))  #321
print(invertir(-123)) #-321
print(invertir(120))  #21
print(invertir(52063)) #36025
print(invertir(1534236469)) #0 
print(invertir(-1534236469)) #0  
