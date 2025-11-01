
from flask import Flask
from login import login 

app=Flask(__name__)
app.register_blueprint(login) #registramos el blueprint
@app.route('/')
def home():
    return ""
if __name__ == '__main__':
    app.run(debug=True,port=5003,host='localhost')