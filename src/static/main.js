function Foco1()
{
	estado=localStorage.getItem('Foco1');
	var imagen= document.getElementById('Foco1');
	if(estado=='On')
	{
    imagen.src="static/foco.png";
	}
	else
	{
    imagen.src="static/focoapagado.png";	
	}
}

function Foco2()
{
	estado=localStorage.getItem('Foco2');
	var imagen= document.getElementById('Foco2');
	if(estado=='On')
	{
    imagen.src="static/foco.png";
	}
	else
	{
    imagen.src="static/focoapagado.png";	
	}
}

function Foco3()
{
	estado=localStorage.getItem('Foco3');
	var imagen= document.getElementById('Foco3');
	if(estado=='On')
	{
    imagen.src="static/foco.png";
	}
	else
	{
    imagen.src="static/focoapagado.png";	
	}
}

function Foco4()
{
	estado=localStorage.getItem('Foco4');
	var imagen= document.getElementById('Foco4');
	if(estado=='On')
	{
    imagen.src="static/foco.png";
	}
	else
	{
    imagen.src="static/focoapagado.png";	
	}
}

function Foco5()
{
	estado=localStorage.getItem('Foco5');
	var imagen= document.getElementById('Foco5');
	if(estado=='On')
	{
    imagen.src="static/foco.png";
	}
	else
	{
    imagen.src="static/focoapagado.png";	
	}
}

function Foco6()
{
	estado=localStorage.getItem('Foco6');
	var imagen= document.getElementById('Foco6');
	if(estado=='On')
	{
    imagen.src="static/foco.png";
	}

	if(estado=='Atenuacion1')
	{
    imagen.src="static/A1.png";
	}

	if(estado=='Atenuacion2')
	{
    imagen.src="static/A2.png";
	}
	if(estado=='Atenuacion3')
	{
    imagen.src="static/A3.png";
	}
	if(estado=='Off')
	{
    imagen.src="static/focoapagado.png";	
	}
}

function Garage()
{
	estado = localStorage.getItem('garage');
	var imagen= document.getElementById('Carro');
	if(estado=='Open')
	{
    imagen.src="static/carro.png";
	}
	else
	{
    imagen.src="";
	}
}

function Camara1()
{
  window.open("http://0.0.0.0:8081/Camara1.mp4", "Camara1", "width=300, height=200")
}

function Camara2()
{
  window.open("http://0.0.0.0:8081/Camara1.mp4", "Camara2", "width=300, height=200")  
}

function Camara3()
{
  window.open("http://192.168.1.232:4747/", "Camara3", "width=800, height=800")  
}


function Timbre()
{
  const audio = new Audio("static/Timbre1.mp3");
  alert("Tocan la puerta!!!!!!");
  audio.play();
}

function main(action,value)
{
	if(action=='Foco1')
	{
		localStorage.setItem('Foco1',value);
		if(value=='Off')
		{
			Foco1();
			Foco2();
			Foco3();
			Foco4();
			Foco5();
			Foco6();
		}
		else{
			Foco1();
		}
	}
	if(action=='Foco2')
	{
		localStorage.setItem('Foco2',value);
		if(value=='Off')
		{
			Foco1();
			Foco2();
			Foco3();
			Foco4();
			Foco5();
			Foco6();
		}
		else{
			Foco2();
		}
	}
	if(action=='Foco3')
	{
		localStorage.setItem('Foco3',value);
		if(value=='Off')
		{
			Foco1();
			Foco2();
			Foco3();
			Foco4();
			Foco5();
			Foco6();
		}
		else{
			Foco3();
		}
	}
	if(action=='Foco4')
	{
		localStorage.setItem('Foco4',value);
		if(value=='Off')
		{
			Foco1();
			Foco2();
			Foco3();
			Foco4();
			Foco5();
			Foco6();
		}
		else{
			Foco4();
		}
	}
	if(action=='Foco5')
	{
		localStorage.setItem('Foco5',value);
		if(value=='Off')
		{
			Foco1();
			Foco2();
			Foco3();
			Foco4();
			Foco5();
			Foco6();
		}
		else{
			Foco5();
		}
	}
	if(action=='Foco6')
	{
		localStorage.setItem('Foco6',value);
		if(value=='Off')
		{
			Foco1();
			Foco2();
			Foco3();
			Foco4();
			Foco5();
			Foco6();
		}
		else{
			Foco6();
		}
	}
	if(action=='Atenuacion1')
	{
		localStorage.setItem('Foco6',value);
		Foco6();		
	}
	if(action=='Atenuacion2')
	{
		localStorage.setItem('Foco6',value);
		Foco6();		
	}
	if(action=='Atenuacion3')
	{
		localStorage.setItem('Foco6',value);
		Foco6();		
	}


	if(action=='Garage')
	{
		localStorage.setItem('garage',value);
		Garage();
	}

}


