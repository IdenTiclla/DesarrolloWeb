from bottle import  run, route, template

@route('/')
def index():
	return 'hola soy el index'
@route('/login')
def login():
	return template('login.html')
run(port =8008,debug = True, reloader= True)