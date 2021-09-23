def sigmoid(x): # シグモイド関数
    return 1/(1+np.exp(-x))

def inner_product(X, w, b): # ここは内積とバイアスを足し合わせる
    return np.dot(X, w)+ b

def activation(X, w, b):
    return sigmoid(inner_product(X, w, b))

# 層ごとの計算結果を格納した配列を返す
def calculate(X, w_list, b_list, t):
    val_list = {}
    a_1 = inner_product(X, w_list[0], b_list[0]) # (N, 1000)
    y_1 = sigmoid(a_1) # (N, 100)
    a_2 = inner_product(y_1, w_list[1], b_list[1]) # (N, 10)
    # これが本来は求めたい値。(N,10)
    y_2 = sigmoid(a_2)
    # ここで簡単な正規化を挟む
    y_2 /= np.sum(y_2, axis=1, keepdims=True)
    S = 1/(2*len(y_2))*(y_2 - t)**2
    L = np.sum(S)
    val_list['a_1'] = a_1
    val_list['y_1'] = y_1
    val_list['a_2'] = a_2
    val_list['y_2'] = y_2
    val_list['S'] = S
    val_list['L'] = L
    return val_list

# ここで予想を行う
def predict(X, w_list, b_list, t):
    val_list = calculate(X, w_list, b_list, t)
    y_2 = val_list['y_2']
    result = np.zeros_like(y_2)
    # サンプル数に当たる
    for i in range(y_2.shape[0]):
        result[i, np.argmax(y_2[i])] = 1
    return result

