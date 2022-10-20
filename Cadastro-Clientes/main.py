import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'acimpacta'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  email = request.form['email']
  nome = request.form['nome']
  sobrenome = request.form['sobrenome']
  senha = request.form['senha']
  confirmacao_senha = request.form['confirmacao_senha']
  if email and nome and sobrenome and senha and confirmacao_senha:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into login (email, nome, sobrenome, senha, confirmacao_senha) VALUES (%s, %s, %s, %s, %s)', (email, nome, sobrenome, senha, confirmacao_senha))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select email, nome, sobrenome, senha, confirmacao_senha from login')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)