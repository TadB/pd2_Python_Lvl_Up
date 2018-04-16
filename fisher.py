from flask import Flask, redirect, session, request, render_template, make_response, flash

users = { 'Akwarysta69': 'J3si07r'}

app = Flask(__name__)
#secret key for flask session
app.secret_key = 'tajneHaslo nie poznasz'

@app.route("/")
def welcome():
    return 'hello my dear user'

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        user=request.authorization['username']
        if 'user' in session:
            return redirect('/hello')
        elif user in users and request.authorization['password']==users[user]:
            session['user']=user
            return 'loged in, welcome'
        else:
            return 'not loged in sory bro'
    else:
        return 'jestes niezalogowany'

@app.route("/hello", methods=['GET'])
def hello():
    if 'user' in session:
        return render_template(
        'hello_tmpl.html',
        user=session['user'],
        my_id='greetings'
        )
    else:
        return redirect('/login')

@app.route("/logout", methods=['POST']) 
def logout(): 
    if 'user' in session:
        session.pop('user', None)
        flash('zostales wylogowany')
        return redirect('/')
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
