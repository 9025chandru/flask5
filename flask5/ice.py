from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1> hiiiiiii  </h1>"
@app.route('/ice')
def icee():
    return "<h1>ice venum </h1>"

if __name__=='__main__':
    app.run(debug=True)












