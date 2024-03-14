from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Привет, Мир из Flask на Minishift!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

