import streamlit as st
import openai
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Streamlit App
st.title('Sudoku Puzzle Generator')

#Generate Sudoku
def generate_sudoku(grid, level):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature = 0.5)
    prompt=f"Generate {grid} {level} sudoku"
    response = llm.stream(prompt)
    return (response)

# User input
grid = st.selectbox('Select grid:', ['2x2','3x3','4x4'])  
level = st.selectbox('Select level:', ['Easy','Medium','Hard'])  

#Calling the Sudoku
 sudoku_puzzle = generate_sudoku(grid, level)
        st.write('The Sudoku Puzzle is', sudoku_puzzle)
    
