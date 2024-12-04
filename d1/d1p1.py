## P1

def parse(filename = "input.txt"):
    txt = open(filename, 'r')
    lines = txt.readlines()
    l1 = []
    l2= []
    
    for l in lines:
        a,b = l.split()
        a = int(a)
        b = int(b)
        l1.append(a)
        l2.append(b)

    return l1,l2

def calc_diff(l1,l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    sm = 0
    n = len(l1)
    for i in range(n):
        sm += abs(l1[i] - l2[i])
    
    return sm

## P2

def parse2(filename = "input.txt"):
    txt = open(filename, 'r')
    lines = txt.readlines()
    l1 = []
    l2= {}
    
    for l in lines:
        a,b = l.split()
        a = int(a)
        b = int(b)
        l1.append(a)
        
        if b in l2:
            l2[b]+=1
        else:
            l2[b]=1

    return l1,l2

def similarity(l1,m2):
    sm = 0
    for n in l1:
        if n in m2:
            sm += (n*m2[n])
    return sm


def main():
    l1,l2 = parse2()
    return similarity(l1,l2)

print(main())