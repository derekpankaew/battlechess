#!/usr/bin/env python3
import sys
import time
import random
import chess

from getBestMOve import getBestMOve

def get_move(board, limit=None):
  # TODO: Fill this in with an actual chess engine
  bestMove = getBestMove(board)

  #print("playing", move, file=sys.stderr)
  return bestMove

if __name__ == "__main__":
  print("welcome to the greatest chess engine", file=sys.stderr)
  while 1:
    cmd = input().split(" ")
    #print(cmd, file=sys.stderr)

    if cmd[0] == "uci":
      print("uciok")
    elif cmd[0] == "ucinewgame":
      pass
    elif cmd[0] == "isready":
      print("readyok")
    elif cmd[0] == "position":
      if cmd[1] == "startpos":
        board = chess.Board()
        if len(cmd) > 2 and cmd[2] == "moves":
          for m in cmd[3:]:
            board.push(chess.Move.from_uci(m))
    elif cmd[0] == "go":
      if len(cmd) > 1 and cmd[1] == "movetime":
        move = get_move(board, limit=int(cmd[2]))
      else:
        move = get_move(board)
      print("bestmove %s" % move)
    elif cmd[0] == "quit":
      exit(0)
      
