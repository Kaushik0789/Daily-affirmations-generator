import streamlit as st
import random
from datetime import datetime

# Page Config
st.set_page_config(page_title="Daily Affirmations", page_icon="✨")

# Affirmations list
affirmations = [
    "I am confident and capable.",
    "I believe in myself.",
    "I can achieve my goals.",
    "I am improving every day.",
    "I deserve happiness and success.",
    "I am strong and resilient.",
    "Today will be a great day.",
    "Changing my mind is a strength, not a weakness.",
    "I am good and getting better.",
    "I alone hold the truth of who I am.",
]

# Initialize Session State (This replaces global variables in web apps)
if 'current_affirmation' not in st.session_state:
    st.session_state.current_affirmation = ""
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# Title and Date
st.title("🌟 Daily Affirmation Generator")
st.write(f"**{datetime.now().strftime('%A, %d %B %Y')}**")

# Layout
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate ✨"):
        st.session_state.current_affirmation = random.choice(affirmations)

# Display Affirmation
if st.session_state.current_affirmation:
    st.info(f"### {st.session_state.current_affirmation}")
    
    if st.button("Save to Favorites ❤️"):
        if st.session_state.current_affirmation not in st.session_state.favorites:
            st.session_state.favorites.append(st.session_state.current_affirmation)
            st.success("Added to favorites!")
        else:
            st.warning("Already in favorites!")
else:
    st.write("Click the button to start your day with positivity.")

# Favorites Sidebar
with st.sidebar:
    st.header("My Favorites ❤️")
    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.write(f"- {fav}")
    else:
        st.write("No favorites saved yet.")
