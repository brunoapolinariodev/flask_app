from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)


app.debug = True

@app.route('/inicio')
def ola():
    jogo1= Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2= Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3= Jogo('Motal Kombat', 'Luta', 'PS2')

    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)    

if __name__ == "__main__":
    app.run()