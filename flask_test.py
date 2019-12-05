from flask import Flask
# import json
import torch
from flask import request, json, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    x = torch.randn(3, 784)
    # y = net(x)
    # _y = y.detach().numpy()
    return json.dumps({'test': x.tolist(), 'data': 's'})


@app.route('/test', methods=["GET", "POST"])
def post_test():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
        print(title)
        print(desc)
        return jsonify({'title': title, 'desc': desc})
    else:
        title = request.values.get('title')
        desc = request.values.get('desc')
        print(title)
        print(desc)
    return jsonify({'title': title, 'desc': desc})

    # # 假设有如下 JSON 数据
    # # {"obj": [{"name":"John","age":"20"}] }
    #
    # # 方法一
    # data = request.get_json()  # 获取 JSON 数据
    # print(data)
    # # data = pd.DataFrame(data["obj"])  # 获取参数并转变为 DataFrame 结构
    #
    # # 方法二
    # # data = request.json        # 获取 JOSN 数据
    # # data = data.get('obj')     #  以字典形式获取参数
    #
    # # 经过处理之后得到要传回的数据
    # # res = some_function(data)
    #
    # # 将 DataFrame  数据再次打包为 JSON 并传回
    # # 方法一
    # # res = '{{"obj": {} }}'.format(res.to_json(orient="records", force_ascii=False))
    # # 方法二
    # # res = jsonify({"obj":res.to_json(orient = "records", force_ascii = False)})
    #
    # return res


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=8080)
    # app.run()
