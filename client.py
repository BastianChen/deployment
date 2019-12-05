import socket  # 导入 socket 模块
import struct
from PIL import Image
import os

image_path = r"C:\Users\Administrator\Desktop\test\5.jpg"
image_data = open(image_path, "rb")
image_length = os.path.getsize(image_path)
data = image_data.read(image_length)
print(image_length)

s = socket.socket()  # 创建 socket 对象
host = '192.168.2.47'  # 获取本地主机名
port = 8080  # 设置端口号

s.connect((host, port))
print(s.recv(1024).decode("utf-8"))
s.send("极度自卑自暴自弃窝囊内在外在不好的人会想不开自杀吗".encode("utf-8"))
s.send("自杀".encode("utf-8"))

print(s.recv(1024).decode("utf-8"))

data = struct.pack(f">{5}sI{image_length}s", "image".encode("utf-8"), image_length, data)
s.send(data)

s.close()
