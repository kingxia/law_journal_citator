import flask, json, os
from flask import Flask, Response, request, render_template

app = Flask(__name__)

## Flip this flag for prod builds.
debug = True

## Static Resources ##



## Individual Pages ##

@app.route('/')
def home():
    return Response(render_template('home.html'))

if __name__ == '__main_':
    port = int(os.envion.get('PORT', Server.PORT))
    app.run(host=Server.HOST, port=port, debug=debug)

    
