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

# 川崎フロンターレがホームの場合
print(data.set_index('Home').loc['Kawasaki-F'])

# 川崎フロンターレがホームの試合のスタッツ
print(data.set_index('Home').loc['Kawasaki-F'].mean())

# 各チームのホーム側の1試合当たりの得点、失点
# teamList = []
# for team in data.set_index('Home').index:
#     if team not in teamList:
#         teamList.append(team)
#     team_summary = {}
#     for teams in range(len(teamList)):
#         team_summary[teamList[teams]] = data.set_index('Home').loc[teamList[teams]].mean()
#         print('team : ' + team)
#         print(team_summary[teamList[teams]])

# 2017年の川崎フロンターレのホームの1試合平均
print(data.query('Home == "Kawasaki-F" & Year == 2017').mean())
