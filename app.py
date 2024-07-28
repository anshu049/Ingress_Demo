from flask import Flask

app = Flask(__name__)

@app.route('/service1')
def service1():
    return "Welcome to Service 1"

@app.route('/service2')
def service2():
    return "Welcome to Service 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

