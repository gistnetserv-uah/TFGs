import os

from flask import Flask

app = Flask(__name__)
# redis = Redis(host=os.environ['REDIS_HOST'], port=6379)
# #redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)
# bind_port = os.environ['BIND_PORT']

@app.route('/')
def get():
   return '<!DOCTYPE html><html><body><h1>TFG - Alberto Crego - Orquestacion de contenedores</h1><p>Node name: {}</p><p>Node IP: {}</p><br><br><p>Pod NAME: {}</p><p>Pod IP: {}</p><br><img src=" data:image/png;base64,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" alt="Red dot" /></body></html>'.format(os.environ['MY_NODE_NAME'], os.environ['MY_NODE_IP'], os.environ['MY_POD_NAME'], os.environ['MY_POD_IP'])

#    return 'asdasd {} sdf {} .'.format(os.environ['MY_NODE_IP'], os.environ['MY_POD_IP'])

# @app.route('/a')
# def get():
#     return 'El valor de la variables es {} .'.format(redis.get('value'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)