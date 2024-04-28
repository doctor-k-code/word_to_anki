"""
[name] utils.py
[purpose] functions for word_to_anki
[reference]
    https://docs.streamlit.io/develop/api-reference

written by Dr.K, 2024/4/28
"""
import docx
import numpy as np
import pandas as pd
import streamlit as st


COLUMNS = ['Front', 'Back', 'Title', 'Page']  # Front, Back, Title, Pageで管理する


# リストから表を作る関数
def  list_to_table(title, all_paragraph, columns=COLUMNS):
    n_cards = len(all_paragraph) // 3
    cards = np.array(all_paragraph)
    cards = cards.reshape(-1, 3)
    title_arr = np.full((n_cards, 1), title)
    cards = np.concatenate([cards, title_arr], axis=1)
    cards = cards[:, [1, 2, 3, 0]]
    return pd.DataFrame(cards, columns=columns)


# アップロードされたファイルからankiに登録する用の表を作る関数
def file_to_table(uploaded_file, table=None):
    doc = docx.Document(uploaded_file)

    # 空白を除き、各段落をリストで管理する。
    all_paragraph = []
    for par in doc.paragraphs:
        text = par.text
        if text:
            all_paragraph.append(text)

    # 表（front）、裏（back）、ページ数（page）のペアになるはずである
    # 3の倍数になっていることを確認する
    rest_par_num = len(all_paragraph) % 3
    if rest_par_num != 0:
        # どこかに過不足があるためにズレが生じていると考えられる
        # 余りを除いて表を作成し、Debugの参考にする
        all_paragraph = all_paragraph[:-rest_par_num]
        st.write(f'段落数が一致しません。ファイルを確認して下さい。: {uploaded_file.name}')
