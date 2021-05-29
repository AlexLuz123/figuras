import matplotlib.pyplot as plt

def algoritmoDDA(x1, y1, x2, y2, x3, y3):
    xn = x1
    yn = y1
    x = -1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    if dx > dy:
        steps = dx
    else:
        steps = dy

    xinc = dx / steps
    yinc = dy / steps

    for i in range(x, steps):
        plt.plot(round(x1), round(y1), marker=".", color="blue")
        print(x1,",",y1)
        x1 = x1 + xinc
        y1 = y1 + yinc

    
    dx = abs(x3 - xn)
    dy = abs(y3 - yn)
    
    if dx > dy:
        steps = dx
    else:
        steps = dy

    xinc = dx / steps
    yinc = dy / steps

    for i in range(x, steps):
        plt.plot(round(xn), round(yn), marker=".", color="blue")
        print(xn,",",yn)
        xn = xn + xinc
        yn = yn + yinc


    dx = abs(x2 - x3)
    dy = abs(y2 - y3)
    
    if dx > dy:
        steps = dx
    else:
        steps = dy

    xinc = dx / steps
    yinc = dy / steps

    for i in range(x, steps):
        plt.plot(round(x3), round(y3), marker=".", color="blue")
        print(x3,",",y3)
        x3 = x3 + xinc
        y3 = y3 + yinc
        
    plt.show()


def algoritmoBresenhams(x1, y1, x2, y2, x3, y3):
    x = x1
    y = y1
    xn = x1
    yn = y1
    xn1 = x3
    yn1 = y3

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = (2 * dy) - dx
    x2 = x2 + 1

    for i in range(x, x2):
        plt.plot(round(x), round(y), marker=".", color="blue")
        print(x,",",y)
        x = x + 1
        if p < 0:
            p = p + (2 * dy)
        else:
            p = p + (2 * dy) - (2 * dx)
            y = y + 1
        

    dx = abs(x3 - x1)
    dy = abs(y3 - y1)
    p = (2 * dy) - dx
    x3 = x3 + 1

    for i in range(xn, x3):
        plt.plot(round(xn), round(yn), marker=".", color="blue")
        print(xn,",",yn)
        xn = xn + 1
        if p < 0:
            p = p + (2 * dy)
        else:
            p = p + (2 * dy) - (2 * dx)
            yn = yn + 1

    
    dx = abs(x2 - x3)
    dy = abs(y2 - y3)
    p = (2 * dy) - dx
    y2 = y2 + 1

    for i in range(yn1, y2):
        plt.plot(round(xn1), round(yn1), marker=".", color="blue")
        print(xn1,",",yn1)
        if p < 0:
            p = p + (2 * dy)
        else:
            p = p + (2 * dy) - (2 * dx)
            yn1 = yn1 + 1

    plt.show() 

if __name__ == '__main__':
    tipo = int(input("1.DDA \n2.Bresenhams \nSelecciona el algoritmo con el cual quieres trabajar: "))
    if tipo == 1:
        x1 = int(input("Ingresa el valor para x1: "))
        y1 = int(input("Ingresa el valor para y1: "))
        x2 = int(input("Ingresa el valor para x2: "))
        y2 = int(input("Ingresa el valor para y2: "))
        x3 = int(input("Ingresa el valor para x3: "))
        y3 = int(input("Ingresa el valor para y3: "))
        algoritmoDDA(x1, y1, x2, y2, x3, y3)
        print("\nUtilize DDA\n")
    elif tipo == 2:
        x1 = int(input("Ingresa el valor para x1: "))
        y1 = int(input("Ingresa el valor para y1: "))
        x2 = int(input("Ingresa el valor para x2: "))
        y2 = int(input("Ingresa el valor para y2: "))
        x3 = int(input("Ingresa el valor para x3: "))
        y3 = int(input("Ingresa el valor para y3: "))
        algoritmoBresenhams(x1, y1, x2, y2, x3, y3)
        print("\nUtilize Bresenhams\n")
    else:
        print("\nEse algoritmo no existe\n")