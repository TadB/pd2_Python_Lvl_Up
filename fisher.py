from flask import Flask, redirect, session, request, render_template, make_response, jsonify, json

users = { 'Akwarysta69': 'J3si07r'}
rybki ={
    "id_1": {
        "who": "Znajomy",
        "where": {
            "lat": 0.001,
            "long": 0.002
        },
        "mass": 34.56,
        "length": 23.67,
        "kind": "szczupak"
    },
    "id_2": {
        "who": "Kolega kolegi",
        "where": {
            "lat": 34.001,
            "long": 52.002
        },
        "mass": 300.12,
        "length": 234.56,
        "kind": "sum olimpijczyk"
    }
}
id_number=3

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
        return redirect('/')
    else:
        return redirect('/login')


@app.route("/fishes", methods=['POST', 'GET'])
def fishes():
#    ret_format=request.args.get('format', None)
    if request.method=='GET':
        return jsonify(rybki)
    elif request.method=='POST':
        return post_fish_info()
   # elif request.method=='POST':
    return 'cso poszlo nei tak'

def post_fish_info(fish_id=None):
    data=request.get_json()
    new_fish={
        'who':data['who'],
        'where':{ 
            'lat':data['where']['lat'],
            'long':data['where']['long']
            },
        'mass' : data['mass'],
        'length':data['length'],
        'kind':data['kind']
        }
    global rybki
    if fish_id is None:
        global id_number
        rybki['id_'+str(id_number)]=new_fish
        id_number+=1
        return 'OK'
    else:
        rybki[fish_id]=new_fish
        return 'podmioniono rybke ;)'

def patch_fish(fish_id):
    data=request.get_json()
    global rybki
    for i in data:
        rybki[fish_id][i]=data[i]
    return "podmiana ok"


@app.route("/fishes/<id>", methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def modify(id):
    if request.method=='GET':
#    ret_format=request.args.get('format', None)
        return jsonify(rybki[id])        
    elif request.method=='DELETE':
        del rybki[id]
        return "ryba zostala usunieta"
    elif request.method=="PUT":
        return post_fish_info(id)
    elif request.method=="PATCH":
        return patch_fish(id)


    return "cos poszlo nie tak"

if __name__ == '__main__':
    app.run(debug=True)
