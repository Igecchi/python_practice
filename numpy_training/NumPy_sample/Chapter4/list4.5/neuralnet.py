import numpy as np

# shape_list = [784, 100, 10]のように層ごとにニューロンの数を配列にしたものを入力する
def make_params(shape_list):
    weight_list = []
    bias_list = []
    for i in range(len(shape_list)-1):
        # 標準正規分布に従った乱数を初期値とする
        weight = np.random.randn(shape_list[i], shape_list[i+1])
        # 初期値はすべて0.1にする
        bias = np.ones(shape_list[i+1])/10.0
        weight_list.append(weight)
        bias_list.append(bias)
    return weight_list, bias_list