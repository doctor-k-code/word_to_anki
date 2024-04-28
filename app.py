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


st.title("wordファイルをanki用のCSVファイルに変換します")

title = st.text_input("タイトル", help="必須項目")

uploaded_files = st.file_uploader(
    "wordファイルをアップロード", type="docx", accept_multiple_files=True)

if st.button("実行"):
    if not title:
        st.write("タイトルを入力して下さい。")
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
