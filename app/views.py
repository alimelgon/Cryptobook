from flask import render_template, redirect
from flask import request
from app import app
import csv

ficherotransacciones='data/transacciones.dat'
#Tengo los campos de cada registro en un array
fields=['fecha','hora','descripcion','monedaComprada','cantidadComprada','monedaPagada','cantidadPagada']
@app.route('/') #por defecto  es un get
def index():
    transacciones=open(ficherotransacciones,'r') #la primera vez será vacío pero cuando rellene nuevacompra ya me retornará la info
    csvreader=csv.reader(transacciones, delimiter=',', quotechar="")
    #registro=transacciones.readline() #leo la primera linea
    movimientos=[]
    #while registro!="":
    for campos in csvreader:
        '''campos=registro.split(',') #me lo transformas en una list
        #inicializo el diccionario'''
        camposdict={}
        #el indice de los valores del diccionario empieza en 0 hasta que termine field
        #ix=0 Cuando uso enumerate me olvido de inicializar
        for ix,field in enumerate(fields): #con la funcion enumerate lleva el control del indice ix
            camposdict[field]=campos[ix]
            #ix=+1  Cuando pongo el enumerate me olvido de actualizar contador
        movimientos.append(campos) #una lista de listas
        resgistro=transacciones.readline()
        '''
        camposdic={
            'fecha':campos[0],
            'hora': campos[1],
            'descripcion':campos[2],
            'monedaComprada':campos[3],
            'cantidadComprada':campos[4],
            'monedaPagada':campos[5],
            'cantidadPagada':campos[6]
        }''' #meto las claves en el array fields y hago un for y asi me ahorro esto
    return render_template('index.html', campos=movimientos)

@app.route ('/nuevacompra', methods=['GET','POST'])
def nuevacompra():
    if request.method=='GET':  
        if request.values['btnselected']  == 'Nueva':
            return render_template('nuevacompra.html') #No puedo poner index.html porque me vuelve a la misma ventana, otro vacio
    else:
        ix=int(request.values['ix'])
        transacciones= open(ficherotransacciones, "r")
        csvreader=csv.reader(transacciones, delimiter=',', quotechar="")
        for registro in csvreader:
            for numreg, registro in enumerate[csvreader]:
                if numreg==ix:
                    camposdict={}
                    for ix, field in enumerate(fields):
                        camposdict(field)=registro(ix)

                    return render_template ('modificacompra.html', registro=camposdict)
            return "Movimiento no encontrado"

        #Aqui debo recuperr el registro ix y devolverlo para editar
        pass
    else:
        datos=request.form
        transacciones=open(ficherotransacciones,"a+")
        registro='{},{},"{}",{},{},{},{}'.format(request.form['fecha'], request.form['hora'],request.form['descripcion'],str(request.form['monedaComprada']), str(request.form['cantidadComprada']), request.form['monedaPagada'], request.form['cantidadPagada'])
       
        transacciones.write(registro)
        transacciones.close()
        return redirect(url_for('index'))
