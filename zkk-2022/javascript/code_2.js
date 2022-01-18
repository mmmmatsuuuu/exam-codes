/********************************************************************
 * yoko   : 横線の本数を表す変数
 * Yokosen: 横線の位置の情報を表す整数の配列
 *          例) Yokosen[y] = x <=> 上からy番目の横線が左からx番目の縦線と
 *              x+1番目の縦線を結ぶことを意味する。
 * Koma   : コマの番号を順番に格納した配列
 * 
 * 配列の番号は１から始まっているのでどの配列も最初の要素は捨て要素になっている。
 ********************************************************************/
const yoko    = 4;
const Yokosen = ["捨て要素", 2, 1, 2, 1];
const Koma    = ["捨て要素", 1, 2, 3];

/********************************************************************
 * 図６　関数：配列を表示する
 * 引数　: arr: 配列
 * 返り値: なし
 ********************************************************************/
 function printArray(arr) {
    for (let j=1; j<arr.length; j++) {
        process.stdout.write(arr[j] + " ");
    }
    console.log("");
}

/********************************************************************
 * 図７　関数：あみだくじを表示する
 * 引数　: tate: 縦線の本数, yoko: 横線の本数, Yokosen: 配列
 * 返り値: なし
 ********************************************************************/
 function printAmidakuji(tate, yoko, Yokosen) {
    for (let y=1; y<=yoko; y++) {
        var x = 1;
        while (x <= tate) {
            if (Yokosen[y] == x) {
                process.stdout.write("┣");
                process.stdout.write("┫");
                x = x + 2;
            } else {
                process.stdout.write("┃");
                x = x + 1;
            }
        }
        console.log("");
    }
}

/********************************************************************
 * 図５
 ********************************************************************/
printArray(Koma);
printAmidakuji(Koma.length - 1, yoko, Yokosen);

for (let y=1; y<Yokosen.length; y++) {
    var t = Koma[Yokosen[y]]
    Koma[Yokosen[y]] = Koma[Yokosen[y] + 1]
    Koma[Yokosen[y] + 1] = t
}

printArray(Koma);