import numpy as np
import matplotlib.pyplot as plt

#1を2に変えながら粒子を動かす
def move_part(s):
    n = len(s)
    for i in range(n):
        if s[i] == 1:
            s[i] = 0
            for j in range(i + 1, n):
                if s[j] == 0:
                    s[j] = 2
                    return s

#2を1に変換する
def exchange_2_to_1(s):
    n = len(s)
    for i in range(n):
        if s[i] == 2:
            s[i] = 1
    return s

#stringをintに変更
def str_to_int(s):
    n = len(s)
    for i in range(n):
        s[i] = int(s[i])
    return s

#intをstringに変更
def int_to_str(s):
    n = len(s)
    for i in range(n):
        s[i] = str(s[i])
    return s

#数直線として描画
def plot_part(s, SOLITON):
    part_position = []
    for i in range(len(s)):
        if s[i] == "1":
            part_position += [i]
    fig,ax=plt.subplots(figsize=(10,10))
    fig.set_figheight(1)
    ax.tick_params(labelbottom=True, bottom=False)
    ax.tick_params(labelleft=False, left=False)
    ax.axes.xaxis.set_visible(False)
    y = [0] * len(part_position)
    plt.tick_params(length=0)
    plt.tight_layout()
    plt.scatter(part_position,y,c='r')
    plt.hlines(y=0, xmin=0 , xmax=len(SOLITON))

#メイン
def soliton(s):
    while 1:
        if s[-1] != 0:
            return
        while 1 in s:
            s = move_part(s)
            if not s:
                return
        exchange_2_to_1(s)
        t = s.copy()
        t = int_to_str(t)
        #print(''.join(t))
        plot_part(t, s)
    t = s.copy()
    t = int_to_str(t)
    print(''.join(t))

def main():
    #粒子のない箇所は「0」で、粒子のある箇所は「1」で表現してください。
    SOLITON = "11100001000000000000"
    s = str_to_int(list(SOLITON))
    plot_part(SOLITON, SOLITON)
    soliton(s)

main()