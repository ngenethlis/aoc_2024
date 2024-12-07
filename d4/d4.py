def get_lines(input_file = "input.txt"):
    file = open(input_file, 'r')
    lines = file.readlines()
    return lines

def count_p1(input_file="input.txt"):
    lines = get_lines()
    ROWS = len(lines)
    COLS = len(lines[0])
    print(f"matrix is {ROWS} by {COLS}")
    res = 0
    # print(lines)
    for r in range(ROWS):
        normal = lines[r].count("XMAS")
        backwards = lines[r].count("SAMX")
        res+= normal + backwards
    print(f"horizontally total {res}")
    r=0
    while r+3 < ROWS:
        print(f"last line checked at r = {r} is \n{lines[r+3]}")
        for c in range(len(lines[r+3])):
            word_dr = word_dl = "" # diag right diag left
            word_vert = lines[r][c] + lines[r+1][c] + lines[r+2][c] + lines[r+3][c]
            if c+3<len(lines[r+3]):
                word_dr = lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2] + lines[r+3][c+3]
            if c-3>=0:
                word_dl =lines[r][c] + lines[r+1][c-1] + lines[r+2][c-2] + lines[r+3][c-3] 
            if (word_vert == "XMAS" or word_vert == "SAMX"):
                print(f" vert starts at row col: {r},{c}")
                res+=1
            if (word_dr == "XMAS" or word_dr == "SAMX"):
                res+=1
                print(f"d right starts at {r},{c} ends at {r+3}, {c+3}")
            if (word_dl == "XMAS" or word_dl == "SAMX"):
                print(f"d left starts at {r},{c} ends at {r+3}, {c-3}")
                res+=1
        r+=1
    return res


def count_p2(input_file = "input.txt"):
    # looking at 3x3 squares
    lines = get_lines(input_file)
    ROWS = len(lines)
    r = 0
    res = 0
    while r+2 < ROWS:
        c = 0
        while c+2 < len(lines[r+2]):
            word_dr = lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2]
            word_dl = lines[r][c+2] + lines[r+1][c+1] + lines[r+2][c]
            if (word_dr == "MAS" or word_dr == "SAM") and (word_dl == "MAS" or word_dl == "SAM"):
                print(f"square {r},{c} to {r+2},{c+2}")
                res+=1
            c+=1
        r+=1
    return res



def main():
    c = count_p2("input.txt")
    print(c)
    return 0

main()