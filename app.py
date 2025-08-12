import streamlit as st

# Page config
st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .stButton>button {
            height: 80px;
            width: 80px;
            font-size: 30px !important;
            font-weight: bold;
            border-radius: 15px;
            background-color: #f0f0f0;
            color: black;
        }
        .stButton>button:disabled {
            background-color: #d3d3d3 !important;
            color: black !important;
        }
        .game-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [[" " for _ in range(3)] for _ in range(3)]
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board, player):
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

# Title
st.markdown("<h1 style='text-align:center;'>🎮 Tic Tac Toe</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:gray;'>Play with a friend!</h4>", unsafe_allow_html=True)

# Display board
with st.container():
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            cell_value = st.session_state.board[i][j]
            display_symbol = "❌" if cell_value == "X" else ("⭕" if cell_value == "O" else " ")
            if cell_value == " ":
                cols[j].button(" ", key=f"{i}-{j}", on_click=make_move, args=(i, j))
            else:
                cols[j].button(display_symbol, key=f"{i}-{j}", disabled=True)

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.markdown("<h3 style='text-align:center; color:orange;'>🤝 It's a Draw!</h3>", unsafe_allow_html=True)
    else:
        winner_symbol = "❌" if st.session_state.winner == "X" else "⭕"
        st.markdown(f"<h3 style='text-align:center; color:green;'>🎉 Player {winner_symbol} Wins!</h3>", unsafe_allow_html=True)
else:
    turn_symbol = "❌" if st.session_state.current_player == "X" else "⭕"
    st.markdown(f"<h3 style='text-align:center; color:blue;'>Player {turn_symbol}'s Turn</h3>", unsafe_allow_html=True)

# Reset button
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.button("🔄 Restart Game", on_click=reset_game)
st.markdown("</div>", unsafe_allow_html=True)
