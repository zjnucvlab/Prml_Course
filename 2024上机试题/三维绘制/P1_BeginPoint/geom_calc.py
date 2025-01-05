import math

# 提示：为了结构清晰，把所有数学计算过程全部整理到这个文件里了
# 可以根据需要自己定义 函数 参数，有想法可以不使用这里的函数名定义
# 函数中只给出了顶点和面片的空列表，有需要也可以在此计算颜色，记得返回计算的结果即可

def calc_polygon_geom(ne: int, r: float):
    vertices, faces = [], []
    # TODO：这里实现 正多边形 的几何体计算，ne表示边数，r表示中心到顶点的半径
    # 提示：圆形的 参数方程

    return vertices, faces


def calc_prism_geom(ne: int, r: float):
    vertices, faces = [], []
    # TODO：这里实现 棱柱 的几何体计算，ne表示边数，r表示中心到顶点的半径，可以自己增加高度等参数
    # 提示：关键是弄清楚顶点编号，以及如何组织顶点编号形成面的规律
    return vertices, faces


def calc_prism_star_geom(R: float):
    vertices, faces = [], []
    # TODO：这里实现 星形棱柱 的几何体计算，可以自己增加星的角数量，棱柱高度等参数
    # 提示：长短不一如何程序化？
    return vertices, faces


def calc_my_geom(extra):
    # TODO：自由发挥，展示实力
    vertices, faces = [], []
    if extra:
        print(extra)
    return vertices, faces

