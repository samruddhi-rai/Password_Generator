import random
import string
import streamlit as st

# ---------------- Password Generator ----------------
def generate_password(n_letters, n_symbols, n_numbers):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    password = ""
    
    # Add letters
    for i in range(n_letters):
        char = random.choice(letters)
        password += char
    
    # Add symbols
    for i in range(n_symbols):
        char = random.choice(symbols)
        password += char
    
    # Add numbers
    for i in range(n_numbers):
        char = random.choice(numbers)
        password += char
    
    # Shuffle the password
    password_list = list(password)
    random.shuffle(password_list)
    final_password = "".join(password_list)
    
    return final_password


# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# Custom CSS for professional look
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            color: #2e7d32; /* Dark green */
            text-align: center;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #2e7d32;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1b5e20;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔑 Password Generator")

st.write("Generate a secure password by choosing how many letters, symbols, and numbers you want.")

# Inputs
n_letters = st.number_input("How many letters?", min_value=0, value=0)
n_symbols = st.number_input("How many symbols?", min_value=0, value=0)
n_numbers = st.number_input("How many numbers?", min_value=0, value=0)

# Generate button
if st.button("Generate Password"):
    final_password = generate_password(n_letters, n_symbols, n_numbers)
    st.success(f" Your generated password is: **{final_password}**")
