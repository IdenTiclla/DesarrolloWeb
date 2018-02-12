from bottle import run,route,template,redirect

minimo = 0
mitad = 0
maximo = 100

def modificarMitad(numero):
	global mitad
	mitad = int(numero)
def modificarMaximo(numero):
	global maximo
	maximo = int(numero)
def modificarMinimo(numero):
	global minimo
	minimo = int(numero)
@route('/')
def inicio():
	return template('index.tpl')
@route('/jugar')
def jugar():
	modificarMitad((minimo + maximo) / 2)
	#mitad = round((minimo + maximo) / 2)
	return template('jugar.tpl',mitad = mitad)
@route('/si')
def si():
	return template('si.tpl')
@route('/no')
def no():
	return template('no.tpl',mitad = mitad)


@route('/mayor')
def mayor():
    #maximo = mitad
    modificarMinimo(mitad)
    return redirect('/jugar')
 
@route('/menor')
def menor():
    modificarMaximo(mitad)
    #minimo = mitad
    return redirect('/jugar')


if __name__ == '__main__':
	run(debug=True,reloader=True)