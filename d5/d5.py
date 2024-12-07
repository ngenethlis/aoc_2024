# x|y x must be printed before y (even if y is never printed)
# a,b,c,d,e.. change the order s.t they follow rules
## add up middle numbers
from collections import defaultdict, deque, Counter
pages = set()
BEF=defaultdict(set)
AFT=defaultdict(set)

def parse(input_file = "input.txt"):
    file = open(input_file,'r')
    lines = file.read().strip()
    edges, querries = lines.split('\n\n')
    for edge in edges.split('\n'):
        x,y = edge.split('|')
        x,y = int(x),int(y)
        BEF[y].add(x)
        AFT[x].add(y)

    return querries

def p1(querries):
    res = 0
    for q in querries.split('\n'):
        vs = [int(x) for x in q.split(',')]
        valid = True
        for (i,x) in enumerate(vs):
            for (j,y) in enumerate(vs):
                if i<j and y in BEF[x]:
                    valid = False
        if valid:
            res+=vs[len(vs)//2]
    return res

def p2(querries):
    res = 0
    for q in querries.split('\n'):
        vs = [int(x) for x in q.split(',')]
        valid = True
        for (i,x) in enumerate(vs):
            for (j,y) in enumerate(vs):
                if i<j and y in BEF[x]:
                    valid = False

        if not valid:
            good = []
            Q = deque([])
            S = {v : len(BEF[v] & set(vs)) for v in vs}
            for v in vs:
                if S[v] ==0:
                    Q.append(v)
            while Q:
                x = Q.popleft()
                good.append(x)
                for y in AFT[x]:
                    if y in S:
                        S[y] -=1
                        if S[y] ==0:
                            Q.append(y)

            res += good[len(good)//2]
    return res

       
def main():
    querries = parse("input.txt")
    pa1 = p1(querries)
    pa2 = p2(querries)
    print(f' p1 : {pa1} , p2 : {pa2}')


main()

