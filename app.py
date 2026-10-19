import streamlit as st

st.set_page_config(
    page_title="Programming Help Bot",
    page_icon="💻",
    layout="wide"
)

st.title("Programming Help Bot")
st.write("Your AI assistant for learning programming.")

st.sidebar.title("Choose a Feature")

feature = st.sidebar.selectbox(
    "What do you want to do?",
    [
        "Ask a Programming Question",
        "Debug My Code",
        "Explain My Code",
        "Coding Practice"
    ]
)

language = st.selectbox(
    "Select Programming Language",
    ["Python", "C", "C++", "Java"]
)

if feature == "Debug My Code":
    st.subheader("Code Debugging")
    code = st.text_area("Paste your code here")
    error = st.text_area("Paste your error message here")

    if st.button("Debug Code"):
        if code.strip():
            st.write("Your code has been submitted.")
            st.info("AI debugging will be added in the next step.")
        else:
            st.warning("Please enter your code.")

elif feature == "Explain My Code":
    st.subheader("Code Explanation")
    code = st.text_area("Paste code to explain")

    if st.button("Explain Code"):
        if code.strip():
            st.code(code, language=language.lower())
            st.info("AI code explanation will be added in the next step.")
        else:
            st.warning("Please enter your code.")

elif feature == "Coding Practice":
    st.subheader("Coding Practice")
    difficulty = st.selectbox(
        "Choose Difficulty",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Generate Question"):
        st.write("Write a program to check whether a number is even or odd.")
        st.write("Difficulty:", difficulty)

else:
    st.subheader("Ask a Programming Question")
    question = st.text_input("Enter your programming question")

    if st.button("Submit Question"):
        if question.strip():
            st.write("Your question:", question)
            st.info("AI question-answering will be added in the next step.")
        else:
            st.warning("Please enter a question.")
