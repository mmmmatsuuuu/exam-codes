# ======================================================================
# 与えられた初期値
# Namae   : 生徒の名前が格納された配列
# Kibo    : クジの順位と希望順位を希望順位を添字として希望するグループが番号が格納されて
#           いる２次元配列
# ninzu   : 生徒全員の人数を格納した変数
# Gninzu  : それぞれのグループに振り分けられた人数を格納する
# Huriwake: そのグループに振り分けられた生徒の名前を格納する
# Kibosu  : 各グループのに対する第１希望の人数を格納する
# Gteiin  : 各グループの人数の上限を格納する
# 
# 配列の番号は１から始まっているのでどの配列も最初の要素は捨て要素になっている。
# ======================================================================
Namae    = ["捨て要素", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
Kibo     = [
    ["捨て配列"],
    ["捨て要素", 1, 3, 2, 4],
    ["捨て要素", 3, 1, 4, 2],
    ["捨て要素", 1, 3, 2, 4],
    ["捨て要素", 1, 3, 4, 2],
    ["捨て要素", 1, 2, 4, 3],
    ["捨て要素", 2, 1, 3, 4],
    ["捨て要素", 1, 2, 3, 4],
    ["捨て要素", 3, 1, 2, 4],
    ["捨て要素", 1, 3, 4, 2],
    ["捨て要素", 1, 2, 3, 4],
]
ninzu    = 10
Gninzu   = ["捨て要素", 0, 0, 0, 0]
Huriwake = [
    ["捨て配列"],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
]

Kibosu   = ["捨て要素", 0, 0, 0, 0]
Gteiin   = ["捨て要素", 0, 0, 0, 0]

# ======================================================================
# 方法２の実装
# ======================================================================
syo   = ninzu // 4
amari = ninzu % 4

for i in range(1, ninzu+1, 1):
    g         = Kibo[i][1]
    Kibosu[g] = Kibosu[g] + 1

for i in range(1, 4+1, 1):
    Gteiin[i] = syo

for i in range(1, amari+1, 1):
    s = -1
    for j in range(1, 4+1, 1):
        if s < Kibosu[j] and Gteiin[j] ==syo:
            s = Kibosu[j]
            g = j
  
    Gteiin[g] = Gteiin[g] + 1

for i in range(1, ninzu+1, 1):
    owari = 0
    j     = 1

    while owari != 1:
        koho = Kibo[i][j]
        if Gninzu[koho] < Gteiin[koho]:
            x                 = Gninzu[koho] + 1
            Gninzu[koho]      = x
            Huriwake[koho][x] = Namae[i]
            owari             = 1
    
        j = j + 1

# ここから下は問題には記述されていない。
for i in range(1, 4+1, 1):
    print("グループ" + str(i) + "のメンバー: ")
    for j in range(1, Gninzu[i] + 1, 1):
        print(Huriwake[i][j])