from flask import Flask

app = Flask(__name__)

@app.route('/api/<timevalue>', methods=['GET', 'POST'])
def welcome(timevalue):
    print(timevalue)
    return "{}".format(timevalue)

if __name__ == '__main__':
    app.run()