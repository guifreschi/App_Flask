from flask import Flask, render_template, request
from projeto.lista_filmes import resultado_filmes
from flask_sqlalchemy import SQLAlchemy
from livro import Livro as livro # to chamando de livro pq na aula ele fez tudo com a letra minuscula, dai pra evitar erro, decidir chamar 'livro'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'

db = SQLAlchemy()
db.init_app(app)

conteudos = []
@app.route('/', methods=['GET', 'POST']) # precisa sem em maiúsculo aqui
def principal():
  if request.method == 'POST': # precisa sem em maiúsculo aqui
    if request.form.get('conteudo'): # 'conteudo' é o nome que está no name do input
      conteudos.append(request.form.get('conteudo'))

  return render_template(
    "index.html",
    conteudos=conteudos
  ) 

registros = []
@app.route("/diario", methods=['GET', 'POST'])
def diario():
  if request.method == 'POST':
    if request.form.get('aluno') and request.form.get('nota'):
      aluno = request.form.get('aluno')
      nota = request.form.get('nota')
      registros.append(
        {
          "aluno": aluno,
          "nota": nota
        }
      )
  return render_template(
    'diario.html', 
    registros=registros
  )

@app.route("/filmes/<propriedade>")
def lista_filmes(propriedade):
  return render_template(
    'filmes.html',
    filmes=resultado_filmes(propriedade)
    )

@app.route('/livros')
def lista_livros():
  return render_template(
    'livros.html', 
    livros=livro.query.all() # para trazer TODAS as informações
    )
