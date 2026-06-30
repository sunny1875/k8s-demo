# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker + K8s! 服务已经成功跑起来了'

if __name__ == '__main__':
    # 监听0.0.0.0，允许外部访问，端口8080
    app.run(host='0.0.0.0', port=8080)
