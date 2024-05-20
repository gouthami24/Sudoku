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
    prompt=f"Generate {size} x {size} {level} sudoku in printable grid format. Give me back only the HTML. Do not add any text before as context"
    st.write(prompt)
    response = llm.stream(prompt)
    # st.write(response)
    return (response)
    
# sudoku = generate_sudoku(size,level)
# Define the HTML for the Sudoku puzzle
# sudoku_html = generate_sudoku(size, level)

# Embed the HTML into the Streamlit app
# st.components.v1.html(sudoku_html, height=500)

# User input
size = st.selectbox('Select size:', ['2','3','4'])  
level = st.selectbox('Select level:', ['Easy','Medium','Hard'])  
st.write(size)
st.write(level)

#Calling the Sudoku
#generate_sudoku(size, level)
#st.write('The Sudoku Puzzle is', sudoku_puzzle)
if st.button('Generate'):
    sudoku=generate_sudoku(size, level)
    st.markdown(sudoku, unsafe_allow_html=False)
    # st.components.v1.html(sudoku, height=600)
else:
    st.write("Sorry Cannot Generate")
st.write("Generated Sudoku puzzle:")
# print(sudoku)
    
