from off_io import AssetData
from geom_calc import (
    calc_prism_geom,
    calc_polygon_geom,
    calc_my_geom,
    calc_prism_star_geom
)

def cube_impl(args) -> AssetData:
    vertices = [
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [-0.5, 0.0, 0.0],
        [0.0, -0.5, 0.0],
        [0.5, 0.0, 0.5],
        [0.0, 0.5, 0.5],
        [-0.5, 0.0, 0.5],
        [0.0, -0.5, 0.5],
    ]
    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [1, 0, 4, 5],
        [3, 2, 6, 7],
        [2, 1, 5, 6],
        [0, 3, 7, 4],
    ]
    colors = [[233, 0, 62] for _ in range(len(faces))]

    return AssetData(args.dst, vertices, faces, colors)


def pyramid_impl(args) -> AssetData:
    #TODO：计算金字塔四棱锥的几何数据
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)


def poly17_impl(args) -> AssetData:
    #TODO：计算正17边形的几何数据
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)


def prism5_impl(args) -> AssetData:
    #TODO：计算正五棱柱的几何数据
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)


def cylinder_impl(args) -> AssetData:
    #TODO： 计算圆柱体的几何数据
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)


def prism_star_impl(args) -> AssetData:
    #TODO：计算星柱的几何数据
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)


def custom1_impl(args) -> AssetData:
    #TODO：喜欢什么就算什么，搞点复杂的看看实力，要不来个球体？:P
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)


def custom2_impl(args) -> AssetData:
    #TODO：上面那个这么复杂的都搞出来了，再来一个！这次要不试试……椭球？XD
    vertices, faces, colors = [], [], []
    return AssetData(args.dst, vertices, faces, colors)
