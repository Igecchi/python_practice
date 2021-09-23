import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 3次元グラフを描く時に使う

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

xx, yy = np.meshgrid(x, y) # 格子点となるx、y座標を作成する
ret = np.sin(xx**2+yy**2)
def plot1():
    plt.gca().set_aspect('equal', adjustable='box') # グラフの縦横の比を揃えるコマンド
    plt.contourf(xx, yy, ret>0, cmap=plt.cm.bone) # 条件(ret>0)を満たす部分を白、満たさない部分を黒とする
    plt.show()
def plot2():
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(xx, yy, ret)
    ax.axis("equal")
    plt.show()

plot1()
plot2()