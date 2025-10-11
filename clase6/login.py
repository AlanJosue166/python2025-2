from flask import Blueprint, request, jsonify

login =Blueprint('login', __name__)

@login.route('/login',methods=['POST'])
def login_user():
    user = request.json.get('user')
    password = request.json.get('password')
    print("Headers:", request.headers)
    print(f"usuario: {user}, Password: {password}")
    
    codRes,menRes,accion= inicializarVariables(user, password) #llamada a la funmcion de login
    
    salida = {
        "codRes":codRes,
        "menRes": menRes,
        "user": user,
        "accion": accion
    }
    return jsonify(salida)
def inicializarVariables(user, password):
    userLocal = "derlisca"
    passLocal = "unida123"
    codRes= "Sin_Error"
    menRes= "OK"
    
    try: 
        print("Verificar login")
        if user == userLocal and password == passLocal:
            print("Login exitoso")
            accion= "Succes"
        else:
            print("usuario o contraseña incorrectas")
            codRes= "error_1"
            menRes= "usuario o password incorrecto"
            print("Login fallido")
            accion="No_succes"
    except Exception as e:
        print("Error",str(e))
        codRes= "Error"
        menRes= 'Msg: ' + str(e)
        accion= "Error interno"
    return codRes,menRes, accion
    