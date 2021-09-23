import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y1 = np.sin(x) # まずは元の信号に
y2 = y1 + np.random.randn(500)*0.3 # ノイズを混ぜる
v = np.ones(5)/5.0 # 移動平均をとるための配列vを設定する。ここでは前後 5 つの値を用いて平均をとる

y3 = np.convolve(y2, v, mode='same')
# グラフを描く都合上'same'を設定する

plt.plot(x, y1, 'k', linestyle='solid', linewidth=2)
plt.plot(x, y2, 'b', linestyle='dotted',linewidth=1)
plt.plot(x, y3, 'b', linestyle='solid', linewidth=2)
plt.show()

