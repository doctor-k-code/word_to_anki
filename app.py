"""
[name] app.py
[purpose] word to csv for anki
[reference]
    https://docs.streamlit.io/develop/api-reference

written by Dr.K, 2024/4/28
"""
import datetime

import pytz
import streamlit as st

from utils import file_to_table, table_to_csv


'''
# wordファイルをanki用のCSVファイルに変換します
## 前提
* 教科書などの暗記事項をwordファイルにまとめます
* それを自動で[anki](https://apps.ankiweb.net/)用のCSVファイルに変換します
* ankiカードのフィールドは"Front", "Back", "Title", "Page"です
* Front: カードの表
* Back: カードの裏
* Title: 教科書名などを想定
* Page: ページ番号
## 使用方法
### まずは以下のようなwordファイルを作成します
example.docx
'''

word_example = '''p.1
このサイトを開発したのは誰か答えよ。
Dr.K

p.3
このサイトの開発者のブログURLを答えよ。
https://doctor-k.net

p.5
このサイトのコードはどこで見られるか答えよ。
https://github.com/doctor-k-code
'''
st.code(word_example)

'''
* ページ番号、カードの表、カードの裏の順番で記載し、それぞれ改行して下さい
* 改行が不適切だと"段落数が一致しません"というメッセージが表示されます
* 簡単な例で一度試してみることをおすすめします
### 教科書名などのタイトルを入力してwordファイルをアップロードします
'''

title = st.text_input("タイトル")

uploaded_files = st.file_uploader(
    "wordファイルをアップロード", type="docx", accept_multiple_files=True)

if st.button("実行"):
    if not title:
        st.write("**タイトル**を入力して下さい")
    else:
        time_stamp = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        time_stamp = time_stamp.strftime('%m%d%H%M')
        table = None
        for uploaded_file in uploaded_files:
            table = file_to_table(uploaded_file, table=table, title=title)
        st.dataframe(table)

        result_csv = table_to_csv(table)
        file_name = '_'.join(['for_anki', time_stamp+'.csv'])
        st.download_button(label="ダウンロード", data=result_csv, file_name=file_name)
