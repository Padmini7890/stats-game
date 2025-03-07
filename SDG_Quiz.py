import streamlit as st
import json

# Sustainable Development Goals Data
sdg_goals = [
    {"id": 1, "title": "No Poverty", "description": "End poverty in all its forms everywhere."},
    {"id": 2, "title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition."},
    {"id": 3, "title": "Good Health and Well-being", "description": "Ensure healthy lives and promote well-being for all ages."},
    {"id": 4, "title": "Quality Education", "description": "Ensure inclusive and equitable quality education for all."},
    {"id": 5, "title": "Gender Equality", "description": "Achieve gender equality and empower all women and girls."},
    {"id": 6, "title": "Clean Water and Sanitation", "description": "Ensure availability and sustainable management of water and sanitation for all."},
    {"id": 7, "title": "Affordable and Clean Energy", "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all."},
    {"id": 8, "title": "Decent Work and Economic Growth", "description": "Promote sustained, inclusive, and sustainable economic growth."},
    {"id": 9, "title": "Industry, Innovation and Infrastructure", "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization."},
    {"id": 10, "title": "Reduced Inequalities", "description": "Reduce inequality within and among countries."},
    {"id": 11, "title": "Sustainable Cities and Communities", "description": "Make cities inclusive, safe, resilient, and sustainable."},
    {"id": 12, "title": "Responsible Consumption and Production", "description": "Ensure sustainable consumption and production patterns."},
    {"id": 13, "title": "Climate Action", "description": "Take urgent action to combat climate change and its impacts."},
    {"id": 14, "title": "Life Below Water", "description": "Conserve and sustainably use the oceans, seas, and marine resources."},
    {"id": 15, "title": "Life on Land", "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems."},
    {"id": 16, "title": "Peace, Justice and Strong Institutions", "description": "Promote peaceful and inclusive societies for sustainable development."},
    {"id": 17, "title": "Partnerships for the Goals", "description": "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development."}
]

# Quiz questions and answers for SDG 1 (No Poverty)
sdg_1_quiz = [
    {"question": "As of 2019, what percentage of the world’s population lived in extreme poverty (earning less than $1.90 per day)?",
     "options": ["A) 5.2%", "B) 9.2%", "C) 12.5%", "D) 15.1%"],
     "answer": "B) 9.2%"},
    {"question": "In 2021, due to the COVID-19 pandemic, the number of people living in extreme poverty increased for the first time in 20 years. Approximately how many million people fell into poverty?",
     "options": ["A) 50 million", "B) 75 million", "C) 90 million", "D) 120 million"],
     "answer": "D) 120 million"},
    {"question": "Which region had the highest extreme poverty rate in 2022?",
     "options": ["A) South Asia", "B) Sub-Saharan Africa", "C) Latin America", "D) East Asia"],
     "answer": "B) Sub-Saharan Africa"},
    {"question": "In 2015, what percentage of children under 5 in low-income countries were malnourished due to poverty?",
     "options": ["A) 10%", "B) 20%", "C) 30%", "D) 40%"],
     "answer": "C) 30%"},
    {"question": "According to the UN, what is the target year for eradicating extreme poverty for all people under SDG 1?",
     "options": ["A) 2030", "B) 2040", "C) 2050", "D) 2060"],
     "answer": "A) 2030"},
    {"question": "What percentage of people in low-income countries lack access to social protection programs (such as pensions, unemployment benefits, or food support)?",
     "options": ["A) 25%", "B) 50%", "C) 70%", "D) 90%"],
     "answer": "C) 70%"},
    {"question": "Between 2010 and 2019, the global poverty rate declined from 15.7% to what percentage?",
     "options": ["A) 12.3%", "B) 9.2%", "C) 7.8%", "D) 6.4%"],
     "answer": "B) 9.2%"},
    {"question": "In 2023, what percentage of the global population lacked access to basic drinking water services, affecting poverty levels?",
     "options": ["A) 10%", "B) 15%", "C) 25%", "D) 30%"],
     "answer": "C) 25%"},
    {"question": "Which country had the highest percentage reduction in poverty rates between 2000 and 2020?",
     "options": ["A) India", "B) China", "C) Brazil", "D) Nigeria"],
     "answer": "B) China"},
    {"question": "In rural areas of developing countries, what percentage of the population still lacks access to reliable electricity as of 2022?",
     "options": ["A) 5%", "B) 12%", "C) 18%", "D) 35%"],
     "answer": "C) 18%"},
    {"question": "According to the World Bank, how many people were lifted out of extreme poverty between 2000 and 2019?",
     "options": ["A) 500 million", "B) 700 million", "C) 900 million", "D) 1.2 billion"],
     "answer": "B) 700 million"},
    {"question": "What percentage of the world's poor work in agriculture as their primary source of income?",
     "options": ["A) 25%", "B) 40%", "C) 60%", "D) 75%"],
     "answer": "C) 60%"},
    {"question": "Which continent has the highest number of people living under the extreme poverty line as of 2023?",
     "options": ["A) Asia", "B) Africa", "C) South America", "D) Europe"],
     "answer": "B) Africa"},
    {"question": "By 2022, what percentage of the global poor were women, highlighting gender-based poverty disparities?",
     "options": ["A) 35%", "B) 45%", "C) 55%", "D) 70%"],
     "answer": "C) 55%"},
    {"question": "In 2021, what percentage of children in developing countries lacked access to proper education due to poverty-related barriers?",
     "options": ["A) 10%", "B) 15%", "C) 20%", "D) 30%"],
     "answer": "D) 30%"}
]

# Streamlit UI
st.set_page_config(layout="wide")
st.title("🌍 Sustainable Development Goals (SDGs) Dashboard")
st.write("Explore the 17 Sustainable Development Goals set by the United Nations.")

# Display SDG goals as a grid dashboard
cols = st.columns(3)  # Create a 3-column layout

for index, goal in enumerate(sdg_goals):
    with cols[index % 3]:
        with st.container():
            st.markdown(f"### {goal['title']}")
            st.write(goal["description"])
            if st.button(f"Let's Start the Quiz! 📝", key=goal["id"]):
                st.session_state["quiz_started"] = True
                st.session_state["selected_sdg"] = goal["title"]
                st.session_state["sdg_1_quiz"] = sdg_1_quiz
                st.experimental_rerun()

# Show Quiz Placeholder (You can replace this with actual quiz logic)
if "quiz_started" in st.session_state and st.session_state["quiz_started"]:
    selected_sdg = st.session_state["selected_sdg"]
    if selected_sdg == "No Poverty":
        st.subheader(f"Quiz for {selected_sdg}")
        
        score = 0
        for i, question in enumerate(st.session_state["sdg_1_quiz"]):
            st.write(f"**{i+1}. {question['question']}**")
            answer = st.radio(f"Choose an answer:", question["options"], key=f"question_{i}")
            
            if answer == question["answer"]:
                score += 1
            
        if st.button("Submit Answer"):
            st.write(f"Your Score: {score}/{len(st.session_state['sdg_1_quiz'])}")

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
