from flask import Flask
servidor =Flask (__name__)
@servidor.route('/')
def hola():
    return "HOLAAAAA BIENVENIDO XD"
if __name__ == '__main__':
    servidor.run(host='0.0.0.0')