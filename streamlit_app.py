import streamlit as st
import openai
import pandas as pd
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Streamlit App
st.title('Sudoku Puzzle Generator')

#Generate Sudoku
def generate_sudoku(size, level):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature = 0.5)
    prompt=f"Generate {size} x {size} {level} sudoku in printable grid format. Give me back only the HTML. Do not add any text before as context"
    response = llm.stream(prompt)
    st.write(response)
    
    # Read the HTML tables into a list of DataFrames
    dfs = pd.read_html(response)

    # Display each DataFrame
    for i, df in enumerate(dfs):
        print(f"Table {i+1}:\n", df, "\n")


    # Initialize an empty string to hold the response
    #response_text = ""
    # Iterate over the generator and accumulate the response text
    #for chunk in response:
     #   response_text += chunk["choices"][0]["text"]  # Adjust based on the actual structure of the response

    #return (response_text)
    #st.write(response_text)
# sudoku = generate_sudoku(size,level)
# Define the HTML for the Sudoku puzzle
# sudoku_html = generate_sudoku(size, level)

# Embed the HTML into the Streamlit app
# st.components.v1.html(sudoku_html, height=500)

# User input
size = st.selectbox('Select size:', ['2','3','4'])  
level = st.selectbox('Select level:', ['Easy','Medium','Hard'])  

#Calling the Sudoku
#generate_sudoku(size, level)
#st.write('The Sudoku Puzzle is', sudoku_puzzle)
if st.button('Generate'):
    sudoku = generate_sudoku(size, level)
    st.markdown(sudoku, unsafe_allow_html=False)
    # st.components.v1.html(sudoku, height=600)
else:
    st.write("Please Press Generate Button to see the puzzle")
#st.write("Generated Sudoku puzzle:")
# print(sudoku)
    
