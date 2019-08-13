from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title> Mi primera pagina</title>
    </head>
    <body>
        <h1> Título de mi página </h1>
        <p>Hola, mundo </p>
        
    </body>
    </html>
    '''

@app.route('/adios')
def bye():
    return '''
    {"success":false,"error":{"code":101,"type":"missing_access_key","info":"You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"}}
    '''
    
if __name__ == '__main__':
    app.run()