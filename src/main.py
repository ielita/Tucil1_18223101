from time import time

def color_checker(color, list, init_list, l):
    # Check if the color area already has queen in it or not
    for i in range(l):
        for j in range(l):
            if ((init_list[i][j] == color) and (list[i][j]!= color)):
                return True
    return False

"""ini color checkernya masih bisa diubah ke 
method1: bikin list isi color nya ada apa aja, kan kalau di board baru, pasti warnanya baru semua, 
jadi warna yang ditemuin pertama tama itu mostly warnanya masih kosong

"""

def column_checker(column, list, l): # column: idx column, l: board size
    # Check if the column area already has queen in it or not
    for i in range(l):
        if (list[i][column] == "#"): 
            return True
    return False

def row_checker(row, list, l): # row: idx row
    # Check if the row area already has queen in it or not
    for i in range(l):
        if (list[row][i] == "#"): 
            return True
    return False

def t_area(row_idx, col_idx, list):
    return list[row_idx][col_idx+1] != "#"
    
def tg_area(row_idx, col_idx, list):
    return list[row_idx+1][col_idx+1] != "#"

def s_area(row_idx, col_idx, list):
    return list[row_idx+1][col_idx] != "#"

def bd_area(row_idx, col_idx, list):
    return list[row_idx+1][col_idx-1] != "#"

def b_area(row_idx, col_idx, list):
    return list[row_idx][col_idx-1] != "#"

def bl_area(row_idx, col_idx, list):
    return list[row_idx-1][col_idx-1] != "#"

def u_area(row_idx, col_idx, list):
    return list[row_idx-1][col_idx] != "#"

def tl_area(row_idx, col_idx, list):
    return list[row_idx-1][col_idx+1] != "#"

def surroundings_checker (row_idx, col_idx, list, l):
    # Check if the surroundings of the current position has queen(s) or not
    if (row_idx == 0):
        if (col_idx == 0):
            return t_area(row_idx, col_idx, list) and tg_area(row_idx, col_idx, list) and s_area(row_idx, col_idx, list)
        elif (col_idx == l-1):
            return s_area(row_idx, col_idx, list) and bd_area(row_idx, col_idx, list) and b_area(row_idx, col_idx, list)
        else:
            return b_area(row_idx, col_idx, list) and bd_area(row_idx, col_idx, list) and s_area(row_idx, col_idx, list) and tg_area(row_idx, col_idx, list) and t_area(row_idx, col_idx, list)
    elif (row_idx == l-1):
        if (col_idx == 0):
            return u_area(row_idx, col_idx, list) and tl_area(row_idx, col_idx, list) and t_area(row_idx, col_idx, list)
        elif (col_idx == l-1):
            return u_area(row_idx, col_idx, list) and bl_area(row_idx, col_idx, list) and b_area(row_idx, col_idx, list)
        else:
            return b_area(row_idx, col_idx, list) and bl_area(row_idx, col_idx, list) and u_area(row_idx, col_idx, list) and tl_area(row_idx, col_idx, list) and t_area(row_idx, col_idx, list)
    else:
        if (col_idx == 0):
            return u_area(row_idx, col_idx, list) and tl_area(row_idx, col_idx, list) and t_area(row_idx, col_idx, list) and tg_area(row_idx, col_idx, list) and s_area(row_idx, col_idx, list)
        elif (col_idx == l-1):
            return u_area(row_idx, col_idx, list) and bl_area(row_idx, col_idx, list) and b_area(row_idx, col_idx, list) and bd_area(row_idx, col_idx, list) and s_area(row_idx, col_idx, list)
        else:
            return bl_area(row_idx, col_idx, list) and u_area(row_idx, col_idx, list) and tl_area(row_idx, col_idx, list) and t_area(row_idx, col_idx, list) and tg_area(row_idx, col_idx, list) and s_area(row_idx, col_idx, list) and bd_area(row_idx, col_idx, list) and b_area(row_idx, col_idx, list) and bl_area(row_idx, col_idx, list)

def check_queen(color, row_idx, column_idx, list, init_list, l):
    return color_checker(color, list, init_list, l) and column_checker(column_idx, list, l) and row_checker(row_idx, list, l) and surroundings_checker(row_idx, column_idx, list, l)

def coronate_queen(row_idx, col_idx, list, color_palette): #menobatkan queen posisi idx x
    list[row_idx][col_idx] = "#"
    color_palette

def check_palette(color_palette, color): # periksa apakah warnanya udah di-discover atau belum
    throned = False
    if (len(color_palette) == 0):
        color_palette.append([color, throned])
    else:
        for i in range (len(color_palette)):
            if (color_palette != color):
                color_palette.append([color, throned])
    return throned

def main():
    chicken = []
    try:
        with open('../test/contoh.txt', 'r') as colors:
            for line in colors:
                line = line.strip()
                chicken.append(line)
    except Exception as e:
        print("There is a Problem", str(e))
        
    print()
    
    while True:
        init_list = chicken.copy()
        palette = []
        l = len(chicken)
        for i in range(l):
            for j in range(l):
                color_area = chicken[i][j]
                if (check_queen(color_area, i, j, chicken, init_list, l)):
                    coronate_queen()

        
    
    
    
        

start = time()

main()

end = time()
timespent = end - start
print("Waktu pencarian: ", timespent)



