"""
	*Proyecto Final Sistemas Embebidos
	*Smart Home Servidor
	*Autores: Hernández Hernández Alonso de Jesús
	*					Alvarado García Manuel
	*Fecha: 23 de Mayo del 2022
"""
from flask import Flask, render_template, request, redirect, url_for #Librerias Importadas para el uso de Flask

app = Flask(__name__)#Inicialización de el .py como app


@app.route('/focos',methods=["GET","POST"])#Definimos la ruta para el template de focos y los metodos como GET y POST
def focos():#Se crea la función que va a procesar la plantilla de Focos en HTML
	return render_template('/Focos/Focos.html')#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/',methods=["GET","POST"])#Definimos la ruta raíz para el template html y los metodos como GET y POST
def index():#Se crea la función que va a procesar la plantilla raíz en HTML
  return render_template('/Menu/Menu.html')#Renderiza la plantilla html y la retorna al interfaz web
	

@app.route('/camaras',methods=["GET","POST"])#Definimos la ruta camaras para el template de menu y los metodos como GET y POST
def camaras():#Se crea la función que va a procesar la plantilla camaras en HTML
    return render_template('/Camaras/Camaras.html')#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/simulador',methods=["GET","POST"])#Definimos la ruta simulador para el template html y los metodos como GET y POST
def simulador():#Se crea la función que va a procesar la plantilla simulador en HTML
	return render_template('/Simulador/casa.html')#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/timbre',methods=["GET","POST"])#Definimos la ruta timbre para el template html y los metodos como GET y POST
def timbre():#Se crea la función que va a procesar la plantilla timbre en HTML
    return render_template('/Timbre/Timbre.html')#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/Open', methods=["GET","POST"])#Definimos la ruta Open del garage para el template html y los metodos como GET y POST
def Open():#Se crea la función que va a procesar la plantilla simulador en HTML
	lugar=request.form.get("GarageO")#Recibimos el parametro enviado por los botones de la plantilla Garage Open
	estado='Open'#Enviamos el estado como open para su interacción con el javascript
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/Close', methods=["GET","POST"])#Definimos la ruta Close del garage para el template html y los metodos como GET y POST
def Close():#Se crea la función que va a procesar la plantilla simulador en HTML 
	lugar=request.form.get("GarageC")#Recibimos el parametro enviado por los botones de la plantilla Garage close
	estado='Close'#Enviamos el estado como close para su interacción con el javascript
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/Encender', methods=["GET","POST"])#Definimos la ruta encender de Focos para el template html y los metodos como GET y POST
def Encender():#Se crea la función que va a procesar la plantilla simulador en HTML 
	lugar=request.form.get("Encender")#Recibimos el parametro enviado por los botones de la plantilla Focos, donde mandaré el encendido de el foco seleccionado
	estado='On'#Enviamos el estado de encedido para su procesamiento en javascript
	if(lugar=='Atenuacion1'):#Si el valor recibido por Focos es atenuación1
		estado='Atenuacion1'#Enviamos el estado de atenuación1 para su procesamiento en javascript
	if(lugar=='Atenuacion2'):#Si el valor recibido por Focos es atenuación2
		estado='Atenuacion2'#Enviamos el estado de atenuación2 para su procesamiento en javascript
	if(lugar=='Atenuacion3'):#Si el valor recibido por Focos es atenuación3
		estado='Atenuacion3'#Enviamos el estado de atenuación3 para su procesamiento en javascript
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/Apagar', methods=["GET","POST"])#Definimos la ruta apagar de Focos de el template html y los metodos como GET y POST
def Apagar():#Se crea la función que va a procesar la plantilla simulador en HTML 
	lugar=request.form.get("Apagar")#Recibimos el parametro enviado por los botones de la plantilla Focos, donde mandaré el apagado de el foco seleccionado
	estado='Off'#Enviamos el estado de encedido para su procesamiento en javascript
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/Camara1', methods=["GET","POST"])#Definimos la ruta camara1 de template html y los metodos como GET y POST
def Camara1():#Se crea la función que va a procesar la plantilla simulador en HTML 
	lugar=request.form.get("Camara1")#Recibimos el parametro enviado por los botones de la plantilla Camara1
	estado='Camara1'#Enviamos el estado de encedido para su procesamiento en javascript
	return redirect('http://192.168.1.232:4747')#Redirecciona hacia la página admin de la camara 1

@app.route('/Camara2', methods=["GET","POST"])#Definimos la ruta camara2 de template html y los metodos como GET y POST
def Camara2():#Se crea la función que va a procesar la plantilla simulador en HTML 
	lugar=request.form.get("Camara2")#Recibimos el parametro enviado por los botones de la plantilla Camara2
	estado='Camara2'#Enviamos el estado de encedido para su procesamiento en javascript
	return redirect('http://192.168.1.156:4747')#Redirecciona hacia la pagina admina de la camara 2

@app.route('/Clock', methods=["GET","POST"])#Definimos la ruta clock de template html y los metodos como GET y POST
def Clock():#Se crea la función que va a procesar la plantilla simulador en HTML 
	return render_template('/Clock/Clock.html')#Renderiza la plantilla html y la retorna al interfaz web

@app.route('/Temporizador', methods=["GET","POST"])
def Temporizador():#Se crea la función que va a procesar la plantilla simulador en HTML 
	hora=request.form.get("Hora")#Recibimos el parametro enviado por los botones de la plantilla Temporizador
	minutos=request.form.get("Minutos")#Recibimos el parametro enviado por los botones de la plantilla Temporizador
	segundos=request.form.get("Segundos")#Recibimos el parametro enviado por los botones de la plantilla Temporizador
	estado=request.form.get("Enviar")#Recibimos el parametro enviado por los botones de la plantilla Temporizador
	return render_template('/Temporizador/Temporizador.html',hora=hora,minutos=minutos,segundos=segundos,estado=estado)#Renderiza la plantilla html y la retorna al interfaz web

