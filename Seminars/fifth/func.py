
def serchFibanachi(n) :
    if n in [0, 1] :
        return n
    return serchFibanachi( n -1) + serchFibanachi(n - 2)



def prostoe(num) :
    if num > 2 and (num % 2) != 0 :
        for i in range(3, num // 2) :
            if num % i == 0 :
                return False
        return True
    return False


def ReverseRange(num) :
    print(num, end= ' ') 
    if num > 0 :
        ReverseRange(num - 1)
       
    
