/********************************************************************
 * Yokosen: 横線の位置の情報を表す整数の配列
 *          例) Yokosen[y] = x <=> 上からy番目の横線が左からx番目の縦線と
 *              x+1番目の縦線を結ぶことを意味する。
 * Koma   : コマの番号を順番に格納した配列
 * 
 * 配列の番号は１から始まっているのでどの配列も最初の要素は捨て要素になっている。
 ********************************************************************/
const Yokosen = new Array(100);
const Koma    = ["捨て要素", 5, 2, 4, 3, 1];

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
 * 図８
 ********************************************************************/
printArray(Koma);

let yoko = 0;

for (let p=1; p<Koma.length-1; p++) {
    for (let q=1; q<Koma.length-p; q++) {
        if (Koma[q] > Koma[q+1]) {
            var t = Koma[q];
            Koma[q] = Koma[q+1];
            Koma[q+1] = t;
            
            yoko = yoko + 1;
            Yokosen[yoko] = q;
        }
    }
}

printAmidakuji(Koma.length-1, yoko, Yokosen);
printArray(Koma);