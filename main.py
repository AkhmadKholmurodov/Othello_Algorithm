import numpy as np # linear algebra
import pandas as pd 


othello_games_file = './othello_dataset.csv'
initial_board = '000000000000000000000000000-+000000+-000000000000000000000000000'



who = ('Draw', 'Black', 'White')
marker = {'0': 0, '+': 1, '-': -1,
          0: '0', 1: '+', -1: '-',
         }
training_value = {'+': 1.0, '-': 0.0, '0': 0.5}
letter_conv = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7,
               'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7,
              }
increments = ((-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1),
              )



def a1_num(pos):
    return (int(pos[1]) - 1) * 8 + letter_conv[pos[0]]

def a1_rc(pos):
    return int(pos[1]) - 1, letter_conv[pos[0]]



def txt_training(brd):
    result = []
    for b in brd:
        result.append(training_value[b])
    return result


def chk(brd, r, c):
    if 0 <= r < 8 and 0 <= c < 8:
        return marker[brd[r * 8 + c]]
    else:
        return 99



def upd(brd, r, c, player):
    return brd[:r * 8 + c] + marker[player] + brd[r * 8 + c + 1:]






def mv(brd, pos, player):
    r, c = pos
    if chk(brd, r, c) != 0:
        return brd
    
    for inc in increments:
        inc_r, inc_c = inc
        i = 1
        while chk(brd, r + inc_r * i, c + inc_c * i) == -player:
            i += 1
        if i > 1 and chk(brd, r + inc_r * i, c + inc_c * i) == player:
            i -= 1
            while i >= 0:
                brd = upd(brd, r + inc_r * i, c + inc_c * i, player)
                i -= 1
    
    return brd




def conv_winner(x):
    return who[int(x)]



def conv_log(log):
    player = 1
    b0 = initial_board
    result = []
    for i in range(0, len(log), 2):
        b1 = mv(b0, a1_rc(log[i:i+2]), player)
        if b1 == b0:
            player *= -1
            b1 = mv(b0, a1_rc(log[i:i+2]), player)
        result.append((who[player], b0, log[i:i+2], b1))
        b0 = b1
        player *= -1
        
    return tuple(result)



historic_game_data = pd.read_csv(othello_games_file,
                                 header=0,
                                 names=['eOthello Game ID',
                                        'Winner',
                                        'Log',
                                       ],
                                 converters={'Winner': conv_winner,
                                             'Log': conv_log,
                                            },
                                 index_col=['eOthello Game ID'],
                                )



winning_moves_list = []
for game in list(historic_game_data[historic_game_data['Winner']=='Black'].Log):
    for game_move in game:
        if game_move[0] == 'Black':
            winning_moves_list.append(('Black', game_move[1], a1_num(game_move[2])))
for game in list(historic_game_data[historic_game_data['Winner']=='White'].Log):
    for game_move in game:
        if game_move[0] == 'White':
            winning_moves_list.append(('White', game_move[1], a1_num(game_move[2])))
            

training_df = pd.DataFrame(winning_moves_list, columns=['Player', 'Feature - Board', 'Label - Move'])
training_df['Feature - Board'] = training_df['Feature - Board'].apply(txt_training)

# Separate data for 'Black' player
black_feature_board = np.vstack(training_df[training_df.Player == 'Black']['Feature - Board'])
black_label_move = np.array(training_df[training_df.Player == 'Black']['Label - Move'])

# Separate data for 'White' player
white_feature_board = np.vstack(training_df[training_df.Player == 'White']['Feature - Board'])
white_label_move = np.array(training_df[training_df.Player == 'White']['Label - Move'])

# Print or inspect the results
print("Black Player Feature Board:")
print(black_feature_board)

print("Black Player Label Move:")
print(black_label_move)

print("White Player Feature Board:")
print(white_feature_board)

print("White Player Label Move:")
print(white_label_move)
