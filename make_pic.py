# encoding: utf-8
# @Time : 2021/11/29 15:13 
# @Author : LJtion
# @File : make_pic.py 
# @Software: PyCharm

import matplotlib.pyplot as plt
import pandas as pd



# 对每100个step的reward取均值，并按照每隔100个step采样值然后绘制其reward图：
def make_img(data, name):
    plt.figure()
    plt.plot(data, 'r-o', lw=1, ms=5)
    # plt.plot(x, y, color='r', linestyle='-.', marker='*', lw=1, ms=5) #和上面的语句表达的意思一样
    plt.title(name)
    plt.show()

def get_ax(file):
    y = []
    sum = 0
    for i in range(0, len(file)):
        sum += int(file['reward'][i])
        if i % 100 == 0:
            y.append(sum)
            sum = 0
    print(y)
    return y

if __name__ == "__main__":
    # 读取文件

    q_act = pd.read_csv('result/qaction.csv', header=0, index_col=0)
    s_act = pd.read_csv('result/saction2.csv', header=0, index_col=0)
    # print(q_act['reward'][:10])
    data_Q = get_ax(q_act)
    data_S = get_ax(s_act)
    make_img(data_Q, 'q-learing')
    make_img(data_S, 'SArSA')