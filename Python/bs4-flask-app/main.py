import os
from flask import Flask, render_template, jsonify, request, redirect, url_for
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import crawler

print(crawler.hello())

load_dotenv()
app = Flask(__name__)

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'todo-items-app',
})

db = firestore.client()

PORT = os.getenv('PORT')

# Send templates
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Params with converter
@app.route('/<int:id>')
def get_id(id):
    print(type(id))
    return f'<h1>{id}</h1>'

# Get data from firebase
@app.route('/firebase-get')
def get_fb_data():
    data = db.collection(u'todo-items')
    docs = data.stream()
    res = []
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
        res.append(doc.to_dict())

    return jsonify(res)

# HTTP methods
@app.route('/ipost', methods=['POST'])
def handle_post():
    name = request.args.get('name', 'Not found')
    return {'method': request.method, 'path': request.path, 'name': name}

# Redirect and errors
@app.route('/redirect')
def redirectme():
    return redirect(url_for('hello_world'))

# Customize error page
@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return render_template('error.html'), 404


if __name__ == '__main__':
    # Do not use run() in production
    app.run(debug=True, port=PORT)
