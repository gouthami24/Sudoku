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
    st.write(prompt)
    response = llm.stream(prompt)
    st.write(response)
    return (response)
    
#sudoku = generate_sudoku(size,level)
# Define the HTML for the Sudoku puzzle
sudoku_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            border-collapse: collapse;
            width: 300px;
            height: 300px;
        }
        td {
            border: 1px solid black;
            width: 33px;
            height: 33px;
            text-align: center;
            font-size: 24px;
        }
        .bold-border {
            border-width: 2px;
        }
    </style>
</head>
<body>
    <h2>3x3 Sudoku Puzzle</h2>
    <table>
        <tr>
            <td class="bold-border"></td>
            <td class="bold-border">2</td>
            <td class="bold-border"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td class="bold-border">6</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class="bold-border">3</td>
        </tr>
        <tr>
            <td class="bold-border"></td>
            <td class="bold-border">7</td>
            <td class="bold-border">4</td>
            <td></td>
            <td class="bold-border">8</td>
            <td></td>
            <td class="bold-border">2</td>
            <td class="bold-border"></td>
            <td class="bold-border"></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class="bold-border">6</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class="bold-border">2</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class="bold-border">1</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </table>
</body>
</html>
"""

# Embed the HTML into the Streamlit app
#st.components.v1.html(sudoku_html, height=500)

# User input
size = st.selectbox('Select size:', ['2','3','4'])  
level = st.selectbox('Select level:', ['Easy','Medium','Hard'])  
st.write(size)
st.write(level)

#Calling the Sudoku
#generate_sudoku(size, level)
#st.write('The Sudoku Puzzle is', sudoku_puzzle)
if st.button('Generate'):
    #sudoku=generate_sudoku(size,level)
    st.markdown(sudoku_html, unsafe_allow_html=True)
    # st.components.v1.html(sudoku_html, height=600)
else:
    st.write("Sorry Cannot Generate")
st.write("Generated Sudoku puzzle:")
#print(sudoku)
    
