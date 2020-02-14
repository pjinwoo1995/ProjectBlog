from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbCtrlCV

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('post_show.html')

@app.route('/view')
def view():
    return render_template('post_single_show.html')


@app.route('/animal_count', methods=['GET'])
def test_get():
    animal = request.args.get('animal')
    doc = db.animals.find_one({'animal':animal}, {'_id':False})

    if doc is not None:
        return jsonify({'result': 'success', 'count': doc['count']})
    else:
        return jsonify({'result': 'fail', 'msg': '해당 동물이 없습니다.'})

@app.route('/animal', methods=['POST'])
def test_post():
    animal = request.form['animal']
    count = request.form['count']

    doc = {
        'animal': animal,
        'count': count
    }

    db.animals.insert_one(doc)

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)