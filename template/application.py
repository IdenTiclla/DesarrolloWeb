from bottle import route, run, template

@route('/')
def index():
	return 'welcome to index'
@route('/template')
def render():
	name = 'iden ticlla choque'
	return template('layout.html',name=name)

if __name__ == '__main__':
	run(debug=True, reloader=True)