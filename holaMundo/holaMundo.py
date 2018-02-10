from bottle import route,run

@route('/')
def index():
	return 'Hello world!!!'
run(debug=True,reloader=True)