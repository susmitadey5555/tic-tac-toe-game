import streamlit as st

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [[" " for _ in range(3)] for _ in range(3)]
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None


def check_winner(board, player):
    """Check rows, columns, and diagonals"""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def make_move(row, col):
    if st.session_state.board[row][col] == " " and st.session_state.winner is None:
        st.session_state.board[row][col] = st.session_state.current_player
        if check_winner(st.session_state.board, st.session_state.current_player):
            st.session_state.winner = st.session_state.current_player
        elif is_full(st.session_state.board):
            st.session_state.winner = "Draw"
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"


def reset_game():
    st.session_state.board = [[" " for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.winner = None


st.title("🎮 Tic Tac Toe - Streamlit")
st.write("Play Tic Tac Toe directly in your browser!")

# Display board with buttons
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        if cell_value == " ":
            cols[j].button(" ", key=f"{i}-{j}", on_click=make_move, args=(i, j))
        else:
            cols[j].button(cell_value, key=f"{i}-{j}", disabled=True)

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("🤝 It's a draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"Player {st.session_state.current_player}'s turn")

# Reset button
st.button("🔄 Restart Game", on_click=reset_game)
