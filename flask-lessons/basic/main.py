from flask import Flask

app = Flask(__name__)
message = 'Hello, world!'\

@app.route('/')
def index():
    return f'<h3>{message}</h3>'

@app.route('/spam')
def spam():
    person = { 'name': 'John', 'age' : 21}
    return person, 201

@app.route('/hello')
def hello():
    name = request.args.get('name')
    # name = 'Jack'
    return { 'message' : f'Hello, {name}!'}

@app.route('/add')
def add():
   num1 = int(request.arg.get('num1'))
   num2 = int(request.arg.get('num2'))
   return { 'result' : num1 + num2}


@app.errorhandler(404)
def not_found(error):
    return {'error' : f'{error}'}, 404 # Remember to send back the 404 code

if __name__ == '__main__':
    app.run(debug=True)