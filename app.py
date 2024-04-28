"""
[name] app.py
[purpose] word to csv for anki
[reference]

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
