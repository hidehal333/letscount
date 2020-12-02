from django.shortcuts import render
import re
import string
import requests
from bs4 import BeautifulSoup

# Create your views here.
from django.views.generic import TemplateView
#ホームページ用
class HomePageView(TemplateView):
    template_name = 'word_counter/index.html'


#カウンター
def counter(request):
    # テキストを取得
    text = request.POST['count_text']

    #前処理-------------------------
    #テキストを小文字にする
    text = text.lower()
    #改行を空白に
    text = re.sub('\n', ' ', text)
    #\rを削除
    #text = re.sub('\r', '', text)
    #数字を削除
    text = re.sub(r'\d+', '', text)
    # text = bytes(text, "UTF-8")
    # text = text.decode("ascii", "ignore")
    #空白で単語を分ける（→リスト）
    text = text.split(' ')
    #単語の両端にある句読点( !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)と空白(' \t\n\r\x0b\x0c')を削除
    print("text")
    print(text)
    sentence=[]
    for word in text:
        sentence.append(word.strip(string.punctuation+string.whitespace))
    ##i と a 以外の 1 文字の単語を削除
    cleaned_text=[]
    for word in sentence:
        if (len(word) > 1 or (word.lower() == 'a' or word.lower() == 'i')) and word !='':
            cleaned_text.append(word)

    print("cleaned_text")
    print(cleaned_text)
    #総単語数
    sum_word=len(cleaned_text)
    print(sum_word)

    # 単語カウント-------------------------
    # 単語を数える辞書を作成
    words = {}
    # split()でスペースと改行で分割したリストから単語を取り出す
    for word in cleaned_text:
        # 単語をキーとして値に1を足していく。
        # 辞書に単語がない、すなわち初めて辞書に登録するときは0+1になる。
        words[word] = words.get(word, 0) + 1  #
    # del words['']


    print("words")
    print(words)

    # リストに取り出して単語の出現回数でソート
    d = [[v, k] for k, v in words.items()]
    d.sort(key= lambda x: x[1])
    d.sort(key= lambda x: x[0], reverse=True)

    #翻訳する
    word_list=[r[1] for r in d]

    translate_list = '\n'.join(word_list)
    translated_list = translate(translate_list)
    t=str(translated_list).split('\n')
    print(t)

    # data=[]
    # for i , translated_word in zip(d, translated_list):
    #     print(i)
    #     print(translated_word)
    #     data.append(i.append(translated_word))
    # print(data)
    data=[]
    for i , k in zip(d, t):
        i.append(k)
        print(i)
        data.append(i)

    print(data)

    #theの訳の処理
    for r in data:
        if r[1] == 'the':
            r[2] = 'その'


    # # 標準出力-------------------------
    # for count, word in d[:100]:
    #     print(count, word)
    return render(request, 'word_counter/index.html', {'data':d, 'sum_word':sum_word})


#翻訳用関数
def translate(content):
    #翻訳用URLを作作成
    if content:
        url = "https://script.google.com/macros/s/AKfycbwU1c-SrdusLY-cjzAKbwnoXB8r2qBwjOwXjqj7c_zS4nIW74s/exec?text=" + content+ "&source=en&target=ja"
        soup = get_soup(url)

        return soup

#翻訳ページスクレイピング
def get_soup(url):
    try:
        # データ取得
        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding
        # 要素の抽出
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup
    except Exception as e:
        return print("スクレイピングできませんでした。")
