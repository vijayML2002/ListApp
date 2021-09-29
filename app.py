from flask import Flask

app = Flask(__name__)

#@app.route('/api/<timevalue>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def welcome():
    #print(timevalue)
    #return "{}".format(timevalue)
    return "hello world"

if __name__ == '__main__':
    app.run()