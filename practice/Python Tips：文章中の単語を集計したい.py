import re
from collections import Counter

# 00 テキストの取得
# target_text = """
with open('botchan.txt') as f:
    # ファイルの内容を読み出す
    target_text = f.read()
    # target_text = target_text.lower()  # 小文字にするならこのタイミングが楽


# 01 文章を単語に分ける
# 複数の区切り文字を指定するため re.split を使う
words = re.split(r'\s|\,|\.|\(|\)', target_text.lower())

# 02 集計する
counter = Counter(words)

# 03 表示する
# Counter#most_common を使って出現頻度の降順に csv 形式で表示する
for word, count in counter.most_common():
    if len(word) > 0:
        print("%s,%d" % (word, count))
# => csv 形式の単語出現回数
