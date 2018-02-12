from bottle import run,route,template,request

@route('/')
def index():
	return template('index.tpl')

@route('/login')
def login():
	return template('login.tpl')

@route('/login',method = 'POST')
def do_login():
	nombre = request.forms.get('nombre')
	apellido = request.forms.get('apellido')
	return template('bienvenido.tpl',nombre = nombre,apellido = apellido)
if __name__ =='__main__':
	run(debug=True, reloader= True)