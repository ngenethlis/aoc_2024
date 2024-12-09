import warnings
import re

def parse(infile = 'input.txt'):
    lines = open(infile, 'r').readlines()
    r = 0
    p = r"\d+"
    for l in lines:
        # print(l)
        t = re.findall(p,l)
        digits = list(map(int,t))
        target,nums = digits[0],digits[1:]
        # s = int(s)
        if valid2(target,nums):
            print(f'valid {l}')
            r+=digits[0]
    return r


def valid(target,nums,acc=0):
    if len(nums)==1:
        return target== nums[0] + acc or target == nums[0] * acc
    else:
        acc_add = acc + nums[0]
        acc_mult = acc * nums[0]
        nums = nums[1:]
        return valid(target,nums,acc_add) or valid(target,nums,acc_mult)

def valid2(target,nums,acc=0):
    # print(f"nums : {nums} acc : {acc}")
    if len(nums)==1:
        concat = int(str(acc) + str(nums[0]))
        return target== nums[0] + acc or target == nums[0] * acc or target == concat
    else:
        acc_add = acc + nums[0]
        acc_mult = acc * nums[0]
        acc_concat = int(str(acc)+str(nums[0]))
        nums = nums[1:]
        return valid2(target,nums,acc_add) or valid2(target,nums,acc_mult) or valid2(target,nums,acc_concat)

   

# v = valid2(156,[15,6])
# print(v)


print(parse("input.txt"))