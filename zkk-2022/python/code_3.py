# =================================================================
# Yokosen: 横線の位置の情報を表す整数の配列
#          例) Yokosen[y] = x <=> 上からy番目の横線が左からx番目の縦線と
#              x+1番目の縦線を結ぶことを意味する。
# Koma   : コマの番号を順番に格納した配列
# 
# 配列の番号は１から始まっているのでどの配列も最初の要素は捨て要素になっている。
# =================================================================
Yokosen = [0] * 100
Koma    = ["捨て要素", 5, 2, 4, 3, 1]

# =================================================================
# 図６　関数：配列を表示する
# 引数　: arr: 配列
# 返り値: なし
# =================================================================
def print_array(arr):
    for j in range(1, len(arr), 1):
        print("{} ".format(arr[j]), end="") # あみだくじが全角のため半角空白を入れている
        
    print("")  # 改行

# =================================================================
# 図７　関数：あみだくじを表示する
# 引数　: tate: 縦線の本数, yoko: 横線の本数, Yokosen: 配列
# 返り値: なし
# =================================================================
def print_amidakuji(tate, yoko, Yokosen):
    for y in range(1, yoko+1, 1):
        x = 1
        while x <= tate:
            if Yokosen[y] == x:
                print("┣", end="")
                print("┫", end="")
                x = x + 2
            else:
                print("┃", end="")
                x = x + 1
        
        print("")  # 改行

# =================================================================
# 図８
# =================================================================
print_array(Koma)

yoko = 0
for p in range(1, len(Koma)-1, 1):
    for q in range(1, len(Koma)-p, 1):
        if Koma[q] > Koma[q+1]:
            t = Koma[q]
            Koma[q] = Koma[q+1]
            Koma[q+1] = t
            
            yoko = yoko + 1
            Yokosen[yoko] = q

print_amidakuji(len(Koma)-1, yoko, Yokosen)
print_array(Koma)