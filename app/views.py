from app import app
from flask import render_template
import csv

ficheromovimientos='data/movimientos.txt'

@app.route('/')
def index():
    #leer movimientos
    fMovimientos= open(ficheromovimientos,'r')
    csvreader=csv.reader(fMovimientos, delimiter=',' , quotechar='"')

    movimientos =[]
    for movimiento in csvreader:
        movimientos.append(movimiento) 

        
    #enviar movimientos
    return render_template('index.html',movimientos=movimientos)
   

@app.route('/nuevacompra')
def compra():
    return render_template('adios.html')