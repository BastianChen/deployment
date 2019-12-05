import socket  # 导入 socket 模块
import struct
from PIL import Image
import io

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 8080  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)

    c.send('欢迎访问菜鸟教程！'.encode("utf-8"))
    title = c.recv(1024)
    print(title.decode("utf-8"))
    desc = c.recv(1024)
    print(desc.decode("utf-8"))
    c.send('有可能！'.encode("utf-8"))

    # data = c.recv(1024)
    # print(data)
    type_name = struct.unpack(f">{5}s", c.recv(5))[0]
    print(type_name.decode("utf-8"))
    # print(hex(type_name))
    length = struct.unpack(">I", c.recv(4))[0]
    print(length)
    t = length
    pos = struct.unpack(f"{length}s", c.recv(t))[0]
    image = Image.open(io.BytesIO(pos))
    image.show()
    # print(pos)
    # data = struct.unpack(f">sI {image_length}s", "image", image_length, data)

    # c.close()  # 关闭连接
