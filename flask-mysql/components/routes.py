import pandas as pd
import random
from flask import render_template, request, redirect, jsonify
from components import app
from components.functions import * 
from components.chess_model import *

# chess_data = pd.read_pickle('components/kaggle_chess_data.pkl', compression = 'zip')



@app.route("/")
def index():
    return {"DC Trinity": ["Superman", "Batman", "Wonderwoman"]}

@app.route("/startgame")
def startgame():
    player = PlayerHands()
    global controller
    controller = StartGame(player)
    # controller = PlayerHands(board)
    # controller.start_game(board)
    # legal_moves = controller.boardState.load_legal_moves_list()
    legal_moves = load_legal_moves_list(controller.board)
    # player_turn = controller.play.playerTurnMessage()
    return {
            "legal_moves": legal_moves,
            # "player_turn": player_turn,
            "gameStarted": True,
            "best_move": random.choice(legal_moves),
            "ascii": str(controller.board)
            }

@app.route("/endgame")
def endgame():
    return {"legal_moves": [],
            "player_turn": "Players has ended the game early",
            "gameStarted": False,
            "ascii": str(controller.board)
            }

@app.route("/getmoves")
def getmoves():
    legal_moves = load_legal_moves_list(controller.board)
    # player_turn = controller.play.playerTurnMessage()
    return {"legal_moves": legal_moves,
            # "player_turn": player_turn,
            "best_move": random.choice(legal_moves),
            "ascii": str(controller.board)
            }

@app.route("/movewhite", methods=['GET','POST'])
def movewhite():
    if request.method == 'POST':
        move = request.json
        # controller.playerInput(move)
        controller.board.push_san(move)
        print(move)
        print(controller.board)
        return "Success"

@app.route("/moveblack", methods=['GET','POST'])
def moveblack():
    if request.method == 'POST':
        move = request.json
        # controller.playerInput(move)
        controller.board.push_san(move)
        print(move)
        print(controller.board)
        return "Success"

# @app.route("/movewhite", methods=['GET','POST'])
# def movewhite():
#     if request.method == 'POST':
#         move = request.json
#         # controller.playerInput(move)
#         controller.board.push_san(move)
#         print(move)
#         print(controller.board)
#         return "Success"

@app.route("/board")
def board():
    return {"DC_Trinity": ["Superman", "Batman", "Wonderwoman"]}



# import pandas as pd
# from flask import render_template, request, redirect
# from dash_package.dashboard import app
# from dash_package.functions import *

# from dash_package.database import conn

# @app.server.route('/dash')
# def dashboard():
#         return app.index()

# @app.server.route('/')
# def index():
#         #query = 'SELECT * FROM test_data LIMIT 5;'
#         df = pd.DataFrame()
#         #df = pd.read_sql(query, conn)
#         return render_template('index.html', dataSaved=False, dataFound=False, data=df, next_w='e4', next_b='')

# @app.server.route('/test', methods=['GET', 'POST'])
# def test():
#         if request.method == 'POST':
#                 move = request.form['test']
#                 query = 'SELECT * FROM test_data WHERE B1= \'' + move + '\' LIMIT 1;'
#                 df = pd.read_sql(query, conn)
#                 return render_template('index.html', dataSaved=False, dataFound=False, data=df, next_w=df.iloc[0]['W2'], next_b='')

# @app.server.route('/returning', methods=['GET', 'POST'])
# def returning():
#         if request.method == 'POST':
#                 move = request.form['returning']
#                 query = 'SELECT * FROM test_data WHERE W1= \'' + move + '\' LIMIT 1;'
#                 df = pd.read_sql(query, conn)
#                 return render_template('index.html', dataSaved=False, dataFound=False, data=df, next_w='', next_b=df.iloc[0]['B1'])

# @app.server.route('/save', methods=['GET', 'POST'])
# def save():
#         if request.method == 'POST':
#                 game = request.form['save']
#                 data = [game]
#                 df = pd.DataFrame(data, columns=['Games'])
#                 df.to_sql('test_data', conn,if_exists='append',index=False)
#                 return render_template('index.html', dataSaved=True, dataFound=False, data=df, next_w='e4', next_b=df['B1'])

# @app.server.route('/search', methods=['GET', 'POST'])
# def search():
#         if request.method == 'POST':
#                 game = request.form['search']
#                 print(game)
#                 query = 'SELECT * FROM test_data WHERE Games = \'' + game + '\'' 
#                 #query = 'SELECT * FROM test_data LIMIT 5;'
#                 print(query)
#                 df = pd.read_sql(query, conn)
#                 return render_template('index.html', dataSaved=False, dataFound=True, data=df, next_w='e4', next_b='')