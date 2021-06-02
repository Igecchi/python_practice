#反復法
def Trib(n):
    a, b, c = 0, 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    else:
        for i in range(n-2):
            a, b, c = b, c, a + b + c
        return c

print([Trib(n) for n in range(15)])
# [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927]

def Tetra(n):
    a, b, c, d = 0, 0, 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    elif n == 3:
        return d
    else:
        for i in range(n-3):
            a, b, c, d = b, c, d, a + b + c + d
        return d

print([Tetra(n) for n in range(15)])
# [0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773]


##再帰法
def Trib(n):  
    if n in [0,1]:
        return 0
    elif n == 2:
        return 1
    else:
        return Trib(n-1) + Trib(n-2) + Trib(n-3)

print([Trib(n) for n in range(15)])
# [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927]

def Tetra(n):  
    if n in [0,1,2]:
        return 0
    elif n == 3:
        return 1
    else:
        return Tetra(n-1) + Tetra(n-2) + Tetra(n-3) + Tetra(n-4)

print([Tetra(n) for n in range(15)])
# [0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773]