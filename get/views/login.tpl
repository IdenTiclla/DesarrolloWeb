%include('base.tpl',title='login')
<h1>Ingrese sus datos</h1>

<form name="miformulario" id="miformulario" method="get">
	
Nombre: <input type="text" name="Texto" id ="Texto" autocomplete="off" required><br><br>
Email:	<input type="Email" name="Correo" id ="Correo" required> <br> <br>
Buscar: <input type="Search" name="search" id = "search"> <br> <br>
Edad: <input type="Number" name="number" min="1" max="100" required><br> <br>
Fecha: <input type="Date" name="Fecha">
Hora: <input type="Time" name="time">
<input type="submit" value="Enviar datos"><br> <br>
</form>