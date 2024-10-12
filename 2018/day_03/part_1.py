import re

conjs = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

pattern = r"#(\d+)\s*@\s*(\d+),(\d+):\s*(\d+)x(\d+)"

def extrair_numeros(s):
    match = re.findall(pattern, s)
    if match:
        return tuple(map(int, match[0])) 
    
def get_board(rows, columns):
    board = []
    for i in range(rows):
        line = '.' * columns
        board.append(line)
    for row in board:
        print(row)
        
conjs = [extrair_numeros(s) for s in conjs]
columns_len  = max(tupla[1] + tupla[3] for tupla in conjs)
rows_len = max(tupla[2] + tupla[4] for tupla in conjs)
get_board(rows_len, columns_len)
