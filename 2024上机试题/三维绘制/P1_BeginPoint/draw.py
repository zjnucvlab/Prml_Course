from argparse import ArgumentParser
import os
from off_io import write_off_file, AssetData
from geom_impl import (
    cube_impl,
    pyramid_impl,
    poly17_impl,
    prism5_impl,
    cylinder_impl,
    prism_star_impl,
    custom1_impl,
    custom2_impl,
)


DrawImpl = {
    'cube': cube_impl,
    'pyramid': pyramid_impl,
    'poly17': poly17_impl,
    'prism5': prism5_impl,
    'cylinder': cylinder_impl,
    'prism_star': prism_star_impl,
    'custom1': custom1_impl,
    'custom2': custom2_impl,
}

def draw(args):
    draw_data: AssetData = DrawImpl[args.geom](args)
    print(draw_data)
    write_off_file(args.dst, draw_data)


if __name__ == "__main__":
    parser = ArgumentParser()
    # TODO: 理解代码结构后，增加draw.py的命令行参数
    # 根据要求    
    args = parser.parse_args()
    
    
    # TODO：解析完参数后，应该根据不同的参数情况，进行处理
    # 根据不同的参数条件，调用 draw(args) 传入参数，进行几何体绘制
