import streamlit as st
import random
from datetime import datetime

# 1. Page Config
st.set_page_config(page_title="Mindset Master", page_icon="✨")

# 2. Add Background Image using Python
# You can replace this URL with any image link you prefer
bg_image_url = https://i.postimg.cc/brxP0Ydw/Pngtree-a-background-of-orange-blue-15791586.jpg

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_image_url}");
        background-attachment: fixed;
        background-size: cover;
    }}
    
    /* This part makes the text area readable by adding a semi-transparent overlay */
    .main-container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Rest of your logic ---
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
    "I alone hold the truth of who I am."
]

if 'current_affirmation' not in st.session_state:
    st.session_state.current_affirmation = ""
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# Using a container to make the content pop against the background
with st.container():
    st.title("🌟 Daily Affirmation")
    st.write(f"### {datetime.now().strftime('%A, %d %B')}")
    
    if st.button("Generate ✨"):
        st.session_state.current_affirmation = random.choice(affirmations)
        st.balloons()

    if st.session_state.current_affirmation:
        # Displaying the affirmation in a nice box
        st.info(f"**{st.session_state.current_affirmation}**")
        
        if st.button("Save ❤️"):
            if st.session_state.current_affirmation not in st.session_state.favorites:
                st.session_state.favorites.append(st.session_state.current_affirmation)
                st.toast("Saved!")

# Sidebar for favorites
with st.sidebar:
    st.header("My Favorites ❤️")
    for f in st.session_state.favorites:
        st.write(f"• {f}")
