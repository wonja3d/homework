from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():

    name = request.form.get('name_give')
    num = request.form.get('num_give')
    address = request.form.get('address_give')
    phone = request.form.get('phone_give')

    orders = {
        'name' : name,
        'num' : num,
        'address' : address,
        'phone' : phone
    }

    db.orders.insert_one(orders)

    return jsonify({'result': 'success', 'msg':'DB에 주문정보를 저장하였습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({},{'_id':False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

