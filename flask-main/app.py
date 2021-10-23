from flask import Flask, render_template, request, redirect, flash
from controllers import users
import mysql.connector

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get('/')
def home():
    
    dataUsers = users.getAllUsers()
    return render_template('index.html', users = dataUsers )

@app.get('/crear')
def crearUsuario():
    return render_template('crearUsuario.html')

@app.post('/guardar')
def guardarUsuario():
    data = request.form

    response = users.crearUsuario(
        nombre=data["nombre"],
        
    )

    if response:
        return redirect('/')
    else:
        return redirect('/crear')

@app.get('/parcial')
def parcial():
    return render_template('parcial.html')

app.run(debug=True)


