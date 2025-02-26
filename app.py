import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Get the current date and timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Set up the page layout and title
st.set_page_config(page_title="FizzBuzz Fun & Attendance", page_icon="🎉", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        background: linear-gradient(135deg, #72EDF2 10%, #5151E5 100%);
        color: white;
    }
    .header {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #FF6F61;
        text-shadow: 2px 2px 4px #000000;
    }
    .subheader {
        font-size: 1.5em;
        text-align: center;
        color: #FFE156;
    }
    .fizzbuzz {
        font-size: 2em;
        color: #34ebba;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Header
st.markdown("<div class='header'>FizzBuzz Fun & Attendance Data</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>A fun way to keep track of numbers and attendance!</div>", unsafe_allow_html=True)

# Create a dynamic counter with a fun twist
count = st.number_input("Enter a number:", min_value=0, value=0, step=1)

if count % 3 == 0 and count % 5 == 0:
    st.balloons()  # Celebrate FizzBuzz milestones with balloons!
    st.markdown("<div class='fizzbuzz'>🎉 FizzBuzz! 🎉</div>", unsafe_allow_html=True)
elif count % 3 == 0:
    st.markdown("<div class='fizzbuzz'>🔵 Fizz</div>", unsafe_allow_html=True)
elif count % 5 == 0:
    st.markdown("<div class='fizzbuzz'>🟢 Buzz</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='fizzbuzz'>Count: {count}</div>", unsafe_allow_html=True)

# Load and display attendance data
try:
    df = pd.read_csv(f"Attendance/Attendance_{date}.csv")
    st.subheader("Today's Attendance Data")
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.error(f"Attendance file for {date} not found.")

# Footer
st.markdown("<div class='subheader'>Powered by Streamlit | Have a great day! 😊</div>", unsafe_allow_html=True)
