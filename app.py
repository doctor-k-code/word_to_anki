"""
[name] app.py
[purpose] word to csv for anki
[reference]
    https://docs.streamlit.io/develop/api-reference

written by Dr.K, 2024/4/28
"""
import streamlit as st

from utils import file_to_table


st.title("wordファイルをanki用のCSVファイルに変換します")

title = st.text_input("タイトル")

uploaded_files = st.file_uploader(
    "wordファイルをアップロード", type="docx", accept_multiple_files=True)

table = None
for uploaded_file in uploaded_files:
    table = file_to_table(uploaded_file, title=title)
    