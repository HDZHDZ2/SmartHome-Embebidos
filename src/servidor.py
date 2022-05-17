from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/focos',methods=["GET","POST"])
def focos():
	return render_template('/Focos/Focos.html')

@app.route('/',methods=['GET'])
def index():
	
	return render_template('/Simulador/casa.html')

@app.route('/camaras')
def camaras():
    return render_template('/Camaras/Camaras.html')

@app.route('/timbre')
def timbre():
    return render_template('/Timbre/Timbre.html')

@app.route('/Open', methods=["GET","POST"])
def Open():
	lugar=request.form.get("GarageO")
	estado='Open'
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)

@app.route('/Close', methods=["GET","POST"])
def Close():
	lugar=request.form.get("GarageC")
	estado='Close'
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)

@app.route('/Encender', methods=["GET","POST"])
def Encender():
	lugar=request.form.get("Encender")
	estado='On'
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)

@app.route('/Apagar', methods=["GET","POST"])
def Apagar():
	lugar=request.form.get("Apagar")
	estado='Off'
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)

@app.route('/Camara1', methods=["GET","POST"])
def Camara1():
	lugar=request.form.get("Camara1")
	estado='Camara1'
	return redirect('http://192.168.1.156:4747/video')

@app.route('/Camara2', methods=["GET","POST"])
def Camara2():
	lugar=request.form.get("Camara2")
	estado='Camara2'
	return render_template('/Simulador/casa.html', lugar=lugar,estado=estado)

