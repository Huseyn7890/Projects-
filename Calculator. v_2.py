def topla(x, y):
    return x + y

def cix(x, y):
    return x - y

def vur(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        return "Sıfıra bölmək olmaz!"
    return x / y

def yuk(x, y):
    return x ** y

x = int(input("Birinci ededi daxil edin: "))  
emel = input("Emeli daxil edin (+, -, ×, ÷, /, ^): ")  
y = int(input("Ikinci ededi daxil edin: "))  

if emel == "+":
    print(topla(x, y))
elif emel == "-":
    print(cix(x, y))
elif emel == "×":
    print(vur(x, y))
elif emel == "÷" or emel == "/":
    print(bol(x, y))
elif emel == "^":
    print(yuk(x, y))
else:
    print("Nə isə səhv getdi, zəhmət olmasa bir daha cəhd edin!")