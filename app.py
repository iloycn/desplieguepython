from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, JugadorSchema
from jugador import Jugador

jugadores_schema = JugadorSchema()
jugadores_schema = JugadorSchema(many=True)

@app.route('/')
def home():
    jugadores = Jugador.query.all()
    jugadoresLeidos = jugadores_schema.dump(jugadores)
    return render_template('index.html', jugadores = jugadoresLeidos)

    # return jsonify(estudiantesLeidos)

#Method Post
@app.route('/jugadores', methods=['POST'])
def addEstudiante():
    nombre = request.form['Nombre']
    equipo = request.form['Equipo']
    altura = request.form['Altura']
    posicion = request.form['Posicion']

    if nombre and equipo and altura and posicion:
        nuevo_jugador = Jugador(nombre, equipo, altura, posicion)
        db.session.add(nuevo_jugador)
        db.session.commit()
        response = jsonify({
            'nombre' : nombre,
            'equipo' : equipo,
            'altura' : altura, 
            'posicion' : posicion,
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<id>')
def deleteJugador(id):
    estudiante = Jugador.query.get(id)
    db.session.delete(jugador)
    db.session.commit()
    
    flash('Jugador ' + id + ' eliminado correctamente')
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<id>', methods=['POST'])
def editJugador(id):    
    
    nombre = request.form['Nombre']
    equipo = request.form['Equipo']
    altura = request.form['Altura']
    posicion = request.form['Posicion']
    
    if nombre and equipo and altura and posicion:
        jugador = Jugador.query.get(id)
  # return student_schema.jsonify(student)
        jugador.nombre = nombre
        jugador.equipo = equipo
        jugador.altura = altura
        jugador.posicion = posicion
        
        db.session.commit()
        
        response = jsonify({'message' : 'Jugador ' + id + ' actualizado correctamente'})
        flash('Jugador ' + id + ' modificado correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)