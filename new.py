map_num = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def find_max(n):
    max_num = 0
    n = str(n)
    for e in n:
        e.upper()
        if e in map_num:
            max_num = max(max_num,int(map_num[e]))
        else: 
            max_num = max(max_num,int(e,10))
    return max_num

def find_base(n):
    base  = 0
    if n < 2:
        base = 2
    else:
        base = (n+1) % 16
    return base

def get_num(n,base):
    n = str(n)
    result = 0
    level = 0
    for e in n[::-1]:
        e.upper()
        if e in map_num:
            result += int(map_num[e]) * (base ** level)
        else:
            result += int(e) * (base ** level)
        level += 1
    return result

def f(s:str):
    for i in range(len(s)-1,-1,-1):
        a = s[i+1:]
        b = a[::-1]
        if a == b:
            c = s[i+1:]
            c = c[::-1]
            print(c)
            print(c + a +c[::-1])
    s1 = s[1:]
    s = s1[::-1] + s
    print(s)
    print(s)

m = 'abcd'
s = f(m)
print(s)
# print(len(func(m)))
        
b = 'B95'
a = '101101'
# x_max = find_max(b)
# y_max = find_max(a)
# x_base = find_base(x_max)
# y_base = find_base(y_max)

# print(get_num(a,y_base) + get_num(b,x_base))







