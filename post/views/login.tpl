%include('base.tpl',title='bienvenido')
<h1>Complete el siguiente formulario</h1>
<form action="/login" name="formulario" id="formulario" method="post">
Nombre:	<input type="Text" name="nombre"> <br> <br>
Apellido:	<input type="tex" name="apellido"> <br> <br>
	<input type="Submit" value="Enviar formulario">
</form>