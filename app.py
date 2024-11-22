from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Usuarios registrados
users = {
    "juan": "admin",
    "pepe": "user"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        cantidad_tarros = int(request.form.get('cantidad_tarros'))

        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        # Calcular descuento según edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        total_descuento = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - total_descuento

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_descuento=total_descuento, total_a_pagar=total_a_pagar)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        password = request.form.get('password')

        # Verificación de credenciales
        if nombre in users and users[nombre] == password:
            if nombre == "juan":
                mensaje = f"Bienvenido administrador {nombre}"
            else:
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrecta"

        return render_template('ejercicio2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)