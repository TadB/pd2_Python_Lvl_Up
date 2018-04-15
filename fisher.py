from flask import Flask, session, request, render_template, make_response

users = { 'Akwarysta69': 'J3si07r'}

app = Flask(__name__)
#secret key for flask session
app.secret_key = 'tajneHaslo nie poznasz'

@app.route("/")
def hello():
    return 'hello my dear user'

@app.route("/login", methods=['GET', 'POST'])
def login():
    user=request.authorization['username']
    if user in users and request.authorization['password']==users[user]:
        return 'loged in, welcome'
    else:
        return 'not loged in sory bro'



if __name__ == '__main__':
    app.run(debug=True)
