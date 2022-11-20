# import chess

# board = chess.Board()

# board.is_game_over()

# def load_legal_moves_list(board):
#     legal_moves = []
#     for i in board.legal_moves:
#         legal_moves.append(i)
    
#     i = 0
#     num_legal_moves = board.legal_moves.count()
#     legal_moves_str = []
#     while num_legal_moves > 0:
#         legal_moves_str.append(board.san(legal_moves[i]))
#         i += 1
#         num_legal_moves -= 1
        
#     return legal_moves_str

# def start_game(board):    
#     W_turn = True # initialize to white since they go first.
#     while not board.is_game_over():
#         if W_turn:
#             player_turn = 'White'
#         else:
#             player_turn = 'Black'

#         print(f'It is {player_turn}\'s turn to move\n')
#         print(f'available moves for {player_turn} are:\n')
#         print(load_legal_moves_list(board))
#         chess_move = str(input('\nenter chess mov str, or enter q to quit'))
#         if chess_move == 'q': break
        
#         try:
#             board.push_san(chess_move)
#         except ValueError:
#             print('wrong move, try again')
#             continue

#         W_turn = not W_turn

#         print(f'{player_turn} played {chess_move}')

#         # print(board.move_stack)
#         # print(board)

# start_game(board)