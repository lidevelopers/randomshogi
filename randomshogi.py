import chess
import random
import sys

LOGFILE = "logs.txt"

def main():

    board = chess.Board()

    while True:
        msg = input()

        f = open(LOGFILE, "a")
        f.write(f"> {msg}\n")
        f.close()

        command(board, msg)

def sendResponse(msg: str):
    f = open(LOGFILE, "a")
    f.write(f"< {msg}\n")
    f.close()
    print(msg)

def command(board: chess.Board, msg: str):
    if msg == "quit":
        sys.exit(0)

    if msg == "uci":
        sendResponse("id name randomshogi")
        sendResponse("id author lidevelopers")
        sendResponse("uciok")
        return

    if msg == "isready":
        sendResponse("readyok")
        return

    if msg == "ucinewgame":
        return

    if msg[0:2] == "go":
        _move = random.choice(list(board.legal_moves)) 
        sendResponse(f"bestmove {_move}")
        return

main()
