# データ読み込み-------------------------
# ファイルを開く
with open('botchan.txt') as f:
    # ファイルの内容を読み出す
    data = f.read()
    # data = data.lower()  # 小文字にするならこのタイミングが楽


# 単語カウント-------------------------
import collections

# 引数にiterableオブジェクトまたはmappingオブジェクトを渡すと
# 要素と出現回数の組み合わせのオブジェクトを返す
counter = collections.Counter(data.split())

# 出現回数が大きい順に並べたタプルのリストを返す
# 例：[('the', 2480), ('I', 1661), ('to', 1427)]
d = counter.most_common()+ 1  #

# リストに取り出して単語の出現回数でソート
d = [(v, k) for k, v in words.items()]
d.sort()
d.reverse()

# 標準出力-------------------------
for count, word in d[:100]:
    print(count, word)

# グラフ化
import matplotlib.pyplot as plt

x = [d[:100][i][1] for i in range(0,100)]
y = [d[:100][i][0] for i in range(0,100)]

plt.figure(figsize=(17,5))
plt.bar(x, y)
plt.xticks(rotation=90)
plt.xlim(-1,100)
plt.show()
