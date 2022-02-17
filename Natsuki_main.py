##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## csvデータの読み込み書き換えのために使うもの
import glob
import pandas as pd

## 図示のために使うもの
import seaborn as sns
import matplotlib.pyplot as plt

def MakeGraph(x,y):
    # Figureの初期化
    fig = plt.figure(figsize=(12, 8)) #...1

    # Figure内にAxesを追加()
    ax = fig.add_subplot(1, 1, 1) #...2
    ax.scatter(x, y, label=file,color="r", ls=":", marker="o"    ) #...3

    # 凡例の表示
    plt.legend()

    # 軸範囲の設定
    ax.set_xlim(0, 20)
    ax.set_ylim(-0.1, 1.4)

    # プロット表示(設定の反映)
    plt.show()

    # データの出力
    fig.savefig(file[:-4]+".png") #グラフ画像の出力


#------------ここからメイン関数--------------------------

# pythonファイルがあるディレクトリから、末尾が4桁の数字で拡張子がcsvのファイルをすべて持ってくる
#サブディレクトリは探さない
list = glob.glob('*[0-9][0-9][0-9][0-9].csv') 
counter = 0
for file in list: #該当するcsvデータ全てに以下の処理を繰り返す

    print(file) #実行前にファイル名確認

    csv1 = pd.read_csv(file, index_col=0, header=None) #csvデータの読み込み
    csv1 = csv1.T #csvデータ列と行の変換
    csv1 = csv1.iloc[range(446), :] #時間範囲 
    x1 = csv1[csv1.keys()[0]] #x軸(時間)
    y1 = csv1[csv1.keys()[205]] #y軸(ある波長における吸光度変化)

    array = pd.concat([x1,y1],axis=1) #x軸y軸の配列を結合

    MakeGraph(x1,y1)

    array.to_csv(file[:-4]+'_453nm.txt', header=False, index=False) #x軸y軸の配列を出力
    
    if counter == 0:
        arrayall = array
        counter= counter + 1
    elif counter > 0:
        arrayall = pd.concat([arrayall,y1],axis=1)
        counter= counter + 1

# 全データの出力 
arrayall.to_csv(file[:-9]+'_453nm_all.txt', header=False, index=False)
