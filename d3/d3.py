import re

test_p1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

test_p2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def mul(x,y):
    return x*y

def main_p1(input_file = "input.txt"):
    file = open(input_file, 'r')
    lines = file.readlines()
    pattern_mul = "mul\([0-9]+,[0-9]+\)"
    sm = 0
    for l in lines:
        xs = re.findall(pattern_mul,l)
        for x in xs:
            sm += eval(x)
    return sm

def main_p2(input_file = "input.txt"):
    file = open(input_file, 'r')
    lines = file.readlines()
    pattern_mul = "mul\([0-9]+,[0-9]+\)"
    pattern_enable = "don't\(\)|do\(\)"
    pattern = pattern_enable + '|' + pattern_mul
    sm = 0
    enable = 1 # multiplier to remove mul()'s precedeed by don't()
    for l in lines:
        xs = re.findall(pattern,l)
        for x in xs:
            if x == "don't()":
                enable = 0
            elif x == "do()":
                enable = 1
            else:
                sm += eval(x) * enable
    return sm

print(main_p2())