from typing import List

## P1
def parse(inputfile = "input.txt") -> List[List[int]]:
    txt = open(inputfile,'r')
    lines = txt.readlines()
    reports = []
    for l in lines:
        report = list(map( lambda x : int(x) ,  l.split()))
        reports.append(report)
    return reports

def is_report_safe(report : List[int]) -> bool:
    # is safe if decreasing or increasing
    # differ by 1-3
    dec = True
    inc = True
    for i in range(len(report)-1):
        if not (1<=abs(report[i]-report[i+1])<=3):
            return False
        if report[i] < report[i+1]:
            dec = False
        if report[i] > report[i+1]:
            inc = False
    
    return inc or dec

def wrapper(report : List[int]) -> int:
    return 1 if is_report_safe(report) else 0

### More efficient, single pass

def parse_and_solve(inputfile = "input.txt") -> int:
    txt = open(inputfile,'r')
    lines = txt.readlines()
    sm = 0
    for l in lines:
        report = list(map( lambda x : int(x) ,  l.split()))
        sm += wrapper(report)
    return sm

### P2

def is_dampened_report_safe(report : List[int], removed_levels = 0) -> bool:
    # is safe if decreasing or increasing
    # differ by 1-3
    # remove element and use normal f to check if safe
    dec = True
    inc = True
    safe = False
    i = 0
    while i+1 < len(report):
        cur, nxt = report[i] , report[i+1]
        diff = abs(nxt-cur)
        if cur < nxt:
            dec = False
        elif cur > nxt:
            inc = False
        if (1<=diff<=3) and (inc or dec):
            i+=1
        else:
            # either diff too big, or not inc or not dec
            removed_levels +=1
            new_report3 = report[:i-1] + report[i:]
            new_report_1 = report[:i] + report[i+1:]
            new_report_2 = report[:i+1] + report[i+2:]
            return is_report_safe(new_report_1) or is_report_safe(new_report_2) or is_report_safe(new_report3)
        
    return (removed_levels <=1)
    
def wrapper2(report : List[int]) -> int:
    res = is_dampened_report_safe(report)
    if (not res):
        print(f"{report} is {'safe' if res else 'not safe'}")
    return 1 if is_dampened_report_safe(report) else 0

### More efficient, single pass

def parse_and_solve2(inputfile = "input.txt") -> int:
    txt = open(inputfile,'r')
    lines = txt.readlines()
    sm = 0
    for l in lines:
        report = list(map( lambda x : int(x) ,  l.split()))
        sm += wrapper2(report)
    return sm


def main():
    r = parse_and_solve2()
    print(r)


main()