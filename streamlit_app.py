import streamlit as st
import openai
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Streamlit App
st.title('Sudoku Puzzle Generator')

#Generate Sudoku
def generate_sudoku(size, level):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature = 0.5)
    prompt=f"Generate {size} x {size} {level} sudoku in printable grid format"
    response = llm.stream(prompt)
    return (response)

sudoku = generate_sudoku(size)
print("Generated Sudoku puzzle:")
print_grid(sudoku)
# User input
size = st.selectbox('Select size:', ['2','3','4'])  
level = st.selectbox('Select level:', ['Easy','Medium','Hard'])  

#Calling the Sudoku
sudoku_puzzle = generate_sudoku(size, level)
st.write('The Sudoku Puzzle is', sudoku_puzzle)
    
