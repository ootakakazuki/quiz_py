
import pandas as pd
import numpy as np
import random

# クイズアプリ

# CSVデータ読み込み
# 1行目は問題文、2~4行目は選択肢、5行目は答え
datas1 = pd.read_csv("mondai.csv", names=["問題", "s1", "s2", "s3", "Ans"])
#print(datas[["s1","s2", "s3"]])

datas = datas1.reindex(np.random.permutation(datas1.index))
print(datas)


# 正解数数える用
count = 0

print("スタート")
print()  # 改行
for i in range(len(datas)):  # for文で1行ずつ読み込んでゆく

    # 問題番号表示
    print("第" + str(i+1) + "問")

    # 問題文を表示(CSVファイルの1列目)
    print(datas.ix[i, 0])

    a = [1, 2, 3]
    random.shuffle(a)

    # 3つの選択肢を表示
    q1 = "1:" + datas.ix[i, a[0]]
    q2 = "2:" + datas.ix[i, a[1]]
    q3 = "3:" + datas.ix[i, a[2]]

    print(q1)
    print(q2)
    print(q3)

    # 標準入力
    inp = input()
    # inp = "q" + inp
    if int(inp) == 1:
        inp = q1
    elif int(inp) == 2:
        inp = q2
    elif int(inp) == 3:
        inp = q3
    else:
        print("1から3を選びましょう")

    # 正誤確認
    if inp[2:] == datas.ix[i, 4]:
        print("正解")
        # 正解数カウント
        count += 1
    else:
        print("は？")
    print() # 改行

# 正解数を表示
print(str(count) + "問正解！")
