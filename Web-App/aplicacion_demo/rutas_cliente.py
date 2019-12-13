from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Cliente
import tkinter
from tkinter import messagebox    
from logging import FileHandler, WARNING
            
@app.route('/cliente/')
def cliente():
    
    clientes = Cliente.get_all()
    return render_template("cliente/index.html",
                           clientes=clientes,
                           titulo='clientes')


@app.route("/cliente/crear", methods=["GET"])
def cliente_crear():
    return render_template("cliente/crear.html")

@app.route("/cliente/crear", methods=["POST"])
def cliente_agregar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
    if nombre and apellido:
        cliente1 = Cliente(nombre=nombre, apellido=apellido,
                        creado=dt.now(), activo=True)
        db.session.add(cliente1)
        db.session.commit()
        cliente_id = cliente1.id
        root = tkinter.Tk()
        root.withdraw()
        
        messagebox.showinfo("Estado","Se creo el Cliente:\n\n " + cliente1.nombre + " " + cliente1.apellido + "\n\n  Code: 200")
        f = open("systemlog.txt", "a")
        f.write("\nSe Creo el Cliente numero : " + str(cliente_id) +  " Exitosamente | Tiempo:" + str(dt.now()) + "\n\n")
        f.close()
        root.destroy()
        
        return redirect(url_for('cliente'))
    
    else:
        root2 = tkinter.Tk()
        root2.withdraw()
        messagebox.showerror("Estado","El Cliente NO fue Creado.\n\n      Code: 403")
        f = open("systemlog.txt", "a")
        f.write("\nCliento NO Creado Correctamente | Tiempo:" + str(dt.now()) + "\n\n")
        f.close()
        root2.destroy()
        return redirect(url_for('cliente'))

@app.route("/cliente/crear", methods=["POST"])
def cliente_agregar_post():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
    if nombre and apellido:
        cliente1 = Cliente(nombre=nombre, apellido=apellido,
                        creado=dt.now(), activo=True)
        db.session.add(cliente1)
        db.session.commit()
    return redirect(url_for('cliente'))

@app.route("/cliente/detalle", methods=['GET'])
def cliente_detalles():
    cliente_id = int(request.args['id'])
    cliente = Cliente.find_by_id(cliente_id)
    return render_template("cliente/detalle.html", cliente=cliente)

@app.route("/cliente/delete", methods=['GET', 'POST'])
def cliente_delete():
    cliente_id = int(request.args['id'])
    cliente = Cliente.find_by_id(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect("/cliente")

@app.route("/cliente/update", methods=['GET'])
def cliente_updating():
    print('request.args')
    print(request.args)
    print('request.base_url')
    print(request.base_url)
    print('request.data')
    print(request.data)
    print('request.form')
    print(request.form)
    print('request.get_json()')
    print(request.get_json())
    print('request.get_data()')
    print(request.get_data())
    print('request.full_path')
    print(request.full_path)
    print('request.headers')
    print(request.headers)
    print('request.method')
    print(request.method)
    print('request.query_string')
    print(request.query_string)
    print('request.referrer')
    print(request.referrer)
    print('request.user_agent')
    print(request.user_agent)
    cliente_id = int(request.args['id'])
    cliente = Cliente.find_by_id(cliente_id)
    return render_template("cliente/update.html", cliente=cliente)

@app.route("/cliente/update", methods=['GET', 'POST'])
def cliente_updated():
    if request.method == 'POST':
        id = request.form.get("id")
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
    if id and nombre and apellido:
        cliente = Cliente.find_by_id(id)
        cliente.apellido = apellido
        cliente.nombre = nombre
        cliente.update()
    return redirect("/")
        

        