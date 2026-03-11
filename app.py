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
    
    # Intro header and subheader
    st.header("Welcome!")
    st.subheader("Track your study habits and productivity with ease")
    
    # Info box for beginners
    st.info(
        """
        This app helps you monitor your **study hours**, **mood**, and **skills practiced**.
        Use it daily to stay motivated and improve your productivity!
        """
    )
    
    st.write("Here’s what you can do on this app:")
    st.markdown("""
    - Log your study hours 🕒  
    - Track your mood and motivation 😊  
    - Record skills practiced 🎯  
    - Get feedback and see your progress 📊  
    - Enjoy fun animations 🎈
    """)
    
    # Add an image with a caption
    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
        caption="Stay focused and motivated!",
        use_column_width=True
    )
    
    # Add a beginner-friendly video
    st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")
    
    # Fun celebration animation
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

# --- ABOUT PAGE -- 
elif page == "About":
    st.title("ℹ️ About Student Productivity Tracker App")

    st.header("🎯 Use Case")
    st.write(
        "This app helps students **track study time, mood, and skills** to monitor productivity, "
        "receive feedback, and improve study habits over time."
    )
    
    st.header("👥 Target Users")
    st.write(
        "Designed for **college and high school students** who want to keep track of their study sessions, "
        "measure productivity, and stay motivated with interactive feedback."
    )
    
    st.header("📝 Inputs Collected")
    st.markdown("""
- **Name**  
- **Age**  
- **Study hours** (slider input)  
- **Mood** (radio buttons)  
- **Favorite subject** (dropdown)  
- **Skills practiced** (multi-select)  
- **Date and time of study** (date & time picker)  
- **Color preference** (color picker)  
- **File uploads** (optional)  
- **Reminder toggle** (checkbox)  
- **Additional notes** (text area)
    """)
    
    st.header("📊 Outputs Shown")
    st.markdown("""
- **Productivity score** (numeric metric)  
- **Progress bar** (visual representation of completion)  
- **Motivational messages & animations** (balloons/snow)  
- **Summary table** (with all user inputs for reference)
    """)
    
    # Optional info box
    st.info("💡 Tip: Use this app daily to track your study habits and improve productivity over time!")
    
    # Optional success box
    st.success("✅ Built with Streamlit using 20+ UI components for an interactive experience!")




