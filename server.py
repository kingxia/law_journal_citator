import flask, json, os
from flask import Flask, jsonify, Response, request, render_template
from lib.constants import *
from lib.journals import *
from lib.frontend.cites import *

app = Flask(__name__)

## Flip this flag for prod builds.
debug = True

## Static Resources ##

journal_data = [JOURNALS[j].__dict__ for j in JOURNALS]

@app.route('/journals/')
def static_journals():
    return json.dumps(journal_data)

## API ##

@app.route('/cites', methods=['POST'])
def api_cites():
    return jsonify(get_cites(DATABASE_PATH, build_options(json.loads(request.data))))

## Individual Pages ##

@app.route('/')
def home():
    return Response(render_template('home.html'))

if __name__ == '__main_':
    port = int(os.envion.get('PORT', Server.PORT))
    app.run(host=Server.HOST, port=port, debug=debug)

    
