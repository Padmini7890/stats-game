import streamlit as st
import random

# Initialize session state if not already done
if 'secret_number_p1' not in st.session_state:
    st.session_state.secret_number_p1 = random.randint(1, 50)
    st.session_state.secret_number_p2 = random.randint(1, 50)
    st.session_state.car1_x = 0
    st.session_state.car2_x = 0
    st.session_state.current_player = 1
    st.session_state.winner = None
    st.session_state.hint_p1 = ""
    st.session_state.hint_p2 = ""

st.title("🏎️ Turbo Guess Race")

st.write(f"**Player {st.session_state.current_player}'s turn** - Enter a guess (1-50)")

# Input from the user
guess = st.text_input("Your guess:", key="guess_input")

# Function to process the guess
def process_guess():
    if guess.isdigit():
        guess_num = int(guess)
        if 1 <= guess_num <= 50:
            if st.session_state.current_player == 1:
                st.session_state.hint_p1 = (
                    "Too Low! 🔽" if guess_num < st.session_state.secret_number_p1 else
                    "Too High! 🔼" if guess_num > st.session_state.secret_number_p1 else "Correct! 🎉"
                )
                if guess_num == st.session_state.secret_number_p1:
                    st.session_state.car1_x = 100
                    st.session_state.winner = "Player 1 Wins!"
                else:
                    move = max(10, 50 - abs(st.session_state.secret_number_p1 - guess_num))
                    st.session_state.car1_x = min(st.session_state.car1_x + move, 99)  # Prevent reaching 100% early
            else:
                st.session_state.hint_p2 = (
                    "Too Low! 🔽" if guess_num < st.session_state.secret_number_p2 else
                    "Too High! 🔼" if guess_num > st.session_state.secret_number_p2 else "Correct! 🎉"
                )
                if guess_num == st.session_state.secret_number_p2:
                    st.session_state.car2_x = 100
                    st.session_state.winner = "Player 2 Wins!"
                else:
                    move = max(10, 50 - abs(st.session_state.secret_number_p2 - guess_num))
                    st.session_state.car2_x = min(st.session_state.car2_x + move, 99)  # Prevent reaching 100% early
            
            # Switch player
            st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1
            
if st.button("Submit Guess"):
    process_guess()

# Display race progress
if st.session_state.car1_x > 0:
    st.progress(st.session_state.car1_x)
    st.write(f"🚗 Player 1's Car Position: {st.session_state.car1_x}%")
    st.write(f"Hint: {st.session_state.hint_p1}")

if st.session_state.car2_x > 0:
    st.progress(st.session_state.car2_x)
    st.write(f"🚙 Player 2's Car Position: {st.session_state.car2_x}%")
    st.write(f"Hint: {st.session_state.hint_p2}")

# Show winner
if st.session_state.winner:
    st.success(st.session_state.winner)
    st.write(f"Player 1's Secret Number: {st.session_state.secret_number_p1}")
    st.write(f"Player 2's Secret Number: {st.session_state.secret_number_p2}")
    
    if st.button("Restart Game"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
