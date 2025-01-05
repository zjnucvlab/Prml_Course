from argparse import ArgumentParser
from typing import Union

class AssetData:
    def __init__(self, path: str, vertices: list, faces: list, colors: list):
        self.path = path
        self.vertices = vertices
        self.faces = faces
        self.colors = colors

    def __str__(self):
        return f"{self.path}: {len(self.vertices)} vertices, {len(self.faces)} faces"


def read_off_file(off_file: str) -> AssetData:
    # TODO： 实现off文件的读取
    # vertex_data = []
    # face_vert = []
    # face_color = []
    with open(off_file, 'r') as f:
        #TODO 打开文件后，读取内容，将数据整理为，顶点数据，面片数据，颜色数据
        pass
    # 最后将读取、整理好的数据打包为AssetData类，返回备用
    return AssetData()

def write_off_file(off_file: str, off_data: Union[AssetData, None]):
    # TODO：给定AssetData，实现off文件的写入
    with open(off_file, "w") as f:
        # TODO：打开文件指针后，将AssetData中存储的数据，输出成符合OFF文件格式的内容
        pass


if __name__ == '__main__':
    parser = ArgumentParser()
    # TODO：添加命令行参数，并进行解析。
    args = parser.parse_args()

    # 下面是样例测试代码，可以根据自己的想法，设计多个测试样例
    test_data: AssetData = read_off_file(args.src)
    print(test_data)
    write_off_file(args.dst, test_data)
