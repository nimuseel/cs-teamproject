class Utils:
  def flatted_board(board):
    result = [];
    for i in range(11):
      for j in range(11):
        if board[i][j].get("name") != "":
          result.append(board[i][j])
    
    return result
