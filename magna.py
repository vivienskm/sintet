import streamlit as st

# Define the leave button
leave_button = st.button("Leave")

# Add a click event to the button
if leave_button:
    # Display a farewell message when the button is clicked
    st.write("Goodbye! Have a great day!")
