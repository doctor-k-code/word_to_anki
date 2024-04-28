"""
[name] app.py
[purpose] word to csv for anki
[reference]
    https://docs.streamlit.io/develop/api-reference

written by Dr.K, 2024/4/28
"""
import datetime
import glob
import os
import shutil

import docx
import numpy as np
import pandas as pd
import streamlit as st


st.title("wordファイルをanki用のCSVファイルに変換します")

uploaded_files = st.file_uploader(
    "wordファイルをアップロードして下さい。", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    byte_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    
