# -*= encoding: utf-8 -*-
import pandas as pd

# csvファイルのパス(任意)
csv_path = '/Users/app/csv/J. League Data Site.csv'

# csvファイルを読み込む
data = pd.read_csv(csv_path)

# 出力
print(data)

# "Year"の列だけ出力
print(data['Year'])

# ホームチームの1試合当たりのゴール数を計算（Score_Homeより）
print(data['Score_Home'].mean())

# ホームチームのゴール数の合計を計算（Score_Homeより）
print(data['Score_Home'].sum())
