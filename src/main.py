import time
import copy

# def color_checker(color, board, init_board, l):
#     # Check if the color area already has queen in it or not
#     for i in range(l):
#         for j in range(l):
#             if ((init_board[i][j] == color) and (board[i][j]!= color)):
#                 return True
#     return False

# """ini color checkernya masih bisa diubah ke 
# method1: bikin list isi color nya ada apa aja, kan kalau di board baru, pasti warnanya baru semua, 
# jadi warna yang ditemuin pertama tama itu mostly warnanya masih kosong

# """

def column_checker(column, board, l): # column: idx column, l: board size
    # Check if the column area already has queen in it or not
    # Return true if area is not occupied
    for i in range(l):
        if (board[i][column] == "#"): 
            return False
    return True

def row_checker(row, board, l): # row: idx row
    # Check if the row area already has queen in it or not
    # Return true if area is not occupied
    for i in range(l):
        if (board[row][i] == "#"): 
            return False
    return True

def t_area(row_idx, col_idx, board):
    return board[row_idx][col_idx+1] != "#"
    
def tg_area(row_idx, col_idx, board):
    return board[row_idx+1][col_idx+1] != "#"

def s_area(row_idx, col_idx, board):
    return board[row_idx+1][col_idx] != "#"

def bd_area(row_idx, col_idx, board):
    return board[row_idx+1][col_idx-1] != "#"

def b_area(row_idx, col_idx, board):
    return board[row_idx][col_idx-1] != "#"

def bl_area(row_idx, col_idx, board):
    return board[row_idx-1][col_idx-1] != "#"

def u_area(row_idx, col_idx, board):
    return board[row_idx-1][col_idx] != "#"

def tl_area(row_idx, col_idx, board):
    return board[row_idx-1][col_idx+1] != "#"

def surroundings_checker (row_idx, col_idx, board, l):
    # Check if the surroundings of the current position has queen(s) or not
    # Return true if surroundings area is not occupied
    if (row_idx == 0):
        if (col_idx == 0):
            return t_area(row_idx, col_idx, board) and tg_area(row_idx, col_idx, board) and s_area(row_idx, col_idx, board)
        elif (col_idx == l-1):
            return s_area(row_idx, col_idx, board) and bd_area(row_idx, col_idx, board) and b_area(row_idx, col_idx, board)
        else:
            return b_area(row_idx, col_idx, board) and bd_area(row_idx, col_idx, board) and s_area(row_idx, col_idx, board) and tg_area(row_idx, col_idx, board) and t_area(row_idx, col_idx, board)
    elif (row_idx == l-1):
        if (col_idx == 0):
            return u_area(row_idx, col_idx, board) and tl_area(row_idx, col_idx, board) and t_area(row_idx, col_idx, board)
        elif (col_idx == l-1):
            return u_area(row_idx, col_idx, board) and bl_area(row_idx, col_idx, board) and b_area(row_idx, col_idx, board)
        else:
            return b_area(row_idx, col_idx, board) and bl_area(row_idx, col_idx, board) and u_area(row_idx, col_idx, board) and tl_area(row_idx, col_idx, board) and t_area(row_idx, col_idx, board)
    else:
        if (col_idx == 0):
            return u_area(row_idx, col_idx, board) and tl_area(row_idx, col_idx, board) and t_area(row_idx, col_idx, board) and tg_area(row_idx, col_idx, board) and s_area(row_idx, col_idx, board)
        elif (col_idx == l-1):
            return u_area(row_idx, col_idx, board) and bl_area(row_idx, col_idx, board) and b_area(row_idx, col_idx, board) and bd_area(row_idx, col_idx, board) and s_area(row_idx, col_idx, board)
        else:
            return bl_area(row_idx, col_idx, board) and u_area(row_idx, col_idx, board) and tl_area(row_idx, col_idx, board) and t_area(row_idx, col_idx, board) and tg_area(row_idx, col_idx, board) and s_area(row_idx, col_idx, board) and bd_area(row_idx, col_idx, board) and b_area(row_idx, col_idx, board) and bl_area(row_idx, col_idx, board)

def check_palette(color_palette, color): # periksa apakah warnanya udah di-discover atau belum
    throned = False
    ada = False
    if (len(color_palette) == 0):
        color_palette.append([color, throned])
    else:
        for i in range (len(color_palette)):
            if (color_palette[i] == color):
                ada = True
        if (ada == False):
            color_palette.append([color, throned])
    return throned

def check_queen(color, colors_used, row_idx, column_idx, board, l):
    if (colors_used[color] == True):
        return False
    return column_checker(column_idx, board, l) and row_checker(row_idx, board, l) and surroundings_checker(row_idx, column_idx, board, l)

def main():
    print(r"_\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_")
    print(r"_\|/                                                  __\|/_")
    print(r"_\|/                 CROWN THE QUEENS                 __\|/_")
    print(r"_\|/                                                  __\|/_")
    print(r"_\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_")
    print("\n")
    
    file_name = input("Masukkan nama file txt (tanpa '.txt'): ")
    
    start = time.perf_counter()
    chicken = []
    try:
        with open(f'../test/{file_name}.txt', 'r') as colors:
            for line in colors:
                line = line.strip()
                chicken.append(list(line.strip()))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
        return
    except Exception as e:
        print("There is a problem", str(e))
    
    l = len(chicken)
    
    palette = set()
    for row in chicken:
        for color in row:
            palette.add(color)
    
    colors_used = {warna: False for warna in palette}
    
    init_board = copy.deepcopy(chicken)
    
    iterazi = 0
    row = 0
    col = 0
    queen_throne_col = [-1] * l
    while row < l:
        throned = False
        for j in range(col, l):
            iterazi += 1
            current_color = init_board[row][j]
            if check_queen(current_color, colors_used, row, j, chicken, l):
                chicken[row][j] = "#"
                colors_used[current_color] = True
                queen_throne_col[row] = j
                throned = True
                break
        if throned:
            row += 1
            col = 0
        else:
            row -= 1
            if row < 0:
                print("Solusi tidak ditemukan")
                print("\n")
                print(r"_\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_")
                print(r"_\|/                                                  __\|/_")
                print(r"_\|/             CORONATION INTERRUPTED               __\|/_")
                print(r"_\|/                                                  __\|/_")
                print(r"_\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_")
                print("\n")
                return
            
            # start lagi dari tempat queen di iterasi terakhir
            prev_col = queen_throne_col[row]
            prev_color = init_board[row][prev_col]
            chicken[row][prev_col] = prev_color
            colors_used[prev_color] = False
            
            col = prev_col + 1
    
    end = time.perf_counter()
    timespent = (end - start) * 1000
    for r in chicken:
        print(" ".join(r))

    print(f"\nWaktu pencarian: {timespent:} ms")
    
    print(f"Banyak kasus yang ditinjau: {iterazi}")
    
    save = input("Apakah Anda ingin menyimpan solusi? (Ya/Tidak) ")
    
    if (save.lower() == "ya"):
        try:
            with open(f"../bin/ans_{file_name}.txt", "w") as f:
                for row in chicken:
                    line = " ".join(row) + "\n"
                    f.write(line)
            print(f"Solusi berhasil disimpan di bin/ans_{file_name}.txt")

        except Exception as e:
            print(f"Failed to save file: {e}")
        
        print("\n")
        print(r"_\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_")
        print(r"_\|/                                                  __\|/_")
        print(r"_\|/               CORONATION IS OVER                 __\|/_")
        print(r"_\|/                                                  __\|/_")
        print(r"_\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_")
        print("\n")
    
    
    
if __name__ == "__main__":
    main()