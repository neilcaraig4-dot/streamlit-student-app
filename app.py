import streamlit as st
from datetime import date, time

# Set page config
st.set_page_config(page_title="Student Productivity Tracker")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Tracker", "About"])

# --- HOME PAGE ---
if page == "Home":
    st.title("🎓 Student Productivity Tracker")
    st.header("Welcome!")
    st.subheader("Track your study habits and productivity")
    
    st.write("This app helps students monitor study hours, mood, and skills.")
    
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80")
    st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")
    st.balloons()

# --- TRACKER PAGE ---
elif page == "Tracker":
    st.title("📊 Study Tracker")
    
    # User inputs
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", 10, 100)
    
    study_hours = st.slider("Hours studied today", 0, 12)
    
    favorite_subject = st.selectbox(
        "Favorite Subject",
        ["Math", "Programming", "Science", "History"]
    )
    
    mood = st.radio(
        "Mood today",
        ["Happy", "Neutral", "Tired", "Stressed"]
    )
    
    skills = st.multiselect(
        "Skills you practiced today",
        ["Coding", "Writing", "Problem Solving", "Reading"]
    )
    
    reminder = st.checkbox("Enable study reminder")
    
    study_date = st.date_input("Select study date", date.today())
    study_time = st.time_input("Select study time", time(hour=9, minute=0))
    
    color_theme = st.color_picker("Pick your theme color", "#00f900")
    
    uploaded_file = st.file_uploader("Upload your study notes (optional)", type=["txt", "pdf"])
    
    if st.button("Calculate Productivity"):
        # Simple productivity calculation
        score = study_hours * 10 + len(skills)*5
        st.metric("Productivity Score", score)
        st.progress(min(score/100, 1.0))
        st.success(f"Great job, {name}!")
        
        st.snow()

# --- ABOUT PAGE ---
elif page == "About":
    st.title("ℹ️ About This App")
    
    st.header("Use Case")
    st.write("This app helps students track study time, mood, and skills to monitor productivity.")
    
    st.header("Target Users")
    st.write("College and high school students who want to track study habits.")
    
    st.header("Inputs")
    st.write("""
    - Name  
    - Age  
    - Study hours  
    - Mood  
    - Favorite subject  
    - Skills practiced  
    - Date and time of study  
    - Color preference  
    - File uploads (optional)  
    - Reminder toggle
    """)
    
    st.header("Outputs")
    st.write("""
    - Productivity score  
    - Progress bar  
    - Motivational messages and animations  
    - Summary metrics
    """)