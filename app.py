# QURRATUL AINI
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def connect_database():
    con = mysql.connector.connect(user='root', password='', host='localhost', database='python')
    return con


@app.route('/')
def index():
    con = connect_database()
    cursor = con.cursor()

    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    con.close()

    return render_template('index.html', products=products)


@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    description = request.form['description']

    con = connect_database()
    cursor = con.cursor()

    query = 'INSERT INTO products(name, description) VALUES (%s,%s)'
    values = (name, description)
    cursor.execute(query, values)

    con.commit()
    cursor.close()
    con.close()

    return redirect('/')


@app.route('/update_product/<int:product_id>', methods=['POST'])
def update_product(product_id):
    name = request.form['name']
    description = request.form['description']

    con = connect_database()
    cursor = con.cursor()

    query = 'UPDATE products SET name = %s, description = %s WHERE id = %s'
    values = (name, description, product_id)
    cursor.execute(query, values)

    con.commit()
    cursor.close()
    con.close()

    return redirect('/')


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    con = connect_database()
    cursor = con.cursor()

    query = 'DELETE FROM products WHERE id = %s'
    values = (product_id,)
    cursor.execute(query, values)

    con.commit()
    cursor.close()
    con.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
