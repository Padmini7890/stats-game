import streamlit as st
import json
import random

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

# Quiz questions for specific SDGs
quiz_questions = {
    1: [
        ("As of 2019, what percentage of the world’s population lived in extreme poverty (earning less than $1.90 per day)?", ["5.2%", "9.2%", "12.5%", "15.1%"], "9.2%"),
        ("In 2021, due to the COVID-19 pandemic, how many million people fell into poverty?", ["50 million", "75 million", "90 million", "120 million"], "120 million"),
        ("Which region had the highest extreme poverty rate in 2022?", ["South Asia", "Sub-Saharan Africa", "Latin America", "East Asia"], "Sub-Saharan Africa"),
        ("In 2015, what percentage of children under 5 in low-income countries were malnourished due to poverty?", ["10%", "20%", "30%", "40%"], "30%"),
        ("According to the UN, what is the target year for eradicating extreme poverty for all people under SDG 1?", ["2030", "2040", "2050", "2060"], "2030")
    ],
    2: [
        ("As of 2022, approximately how many people worldwide suffered from hunger?", ["500 million", "670 million", "735 million", "900 million"], "735 million"),
        ("What percentage of children under 5 globally were affected by stunting in 2021?", ["10%", "15%", "22%", "30%"], "22%"),
        ("Which region had the highest prevalence of undernourishment in 2022?", ["Sub-Saharan Africa", "South Asia", "Latin America", "Middle East"], "Sub-Saharan Africa"),
        ("How many people globally were affected by food insecurity in 2021?", ["1.2 billion", "2.3 billion", "3 billion", "3.5 billion"], "2.3 billion"),
        ("By what year does SDG 2 aim to end all forms of hunger and malnutrition?", ["2025", "2030", "2040", "2050"], "2030")
    ],
    4: [
        ("As of 2022, approximately how many children worldwide were out of school?", ["120 million", "244 million", "350 million", "500 million"], "244 million"),
        ("What percentage of children in low-income countries complete primary school?", ["45%", "60%", "75%", "90%"], "75%"),
        ("By what year does SDG 4 aim to ensure that all children complete free, equitable, and quality education?", ["2025", "2030", "2040", "2050"], "2030"),
        ("As of 2021, what percentage of young people worldwide lack basic literacy skills?", ["5%", "10%", "15%", "20%"], "15%"),
        ("Which region has the highest percentage of children out of school?", ["Latin America", "South Asia", "Sub-Saharan Africa", "Middle East"], "Sub-Saharan Africa")
    ]
}

# Streamlit UI
st.set_page_config(layout="wide")
st.title("🌍 Sustainable Development Goals (SDGs) Dashboard")
st.write("Explore the 17 Sustainable Development Goals set by the United Nations.")

cols = st.columns(3)
for index, goal in enumerate(sdg_goals):
    with cols[index % 3]:
        st.markdown(f"### {goal['title']}")
        st.write(goal["description"])
        
        if st.button(f"Let's Start Quiz! 📝", key=f"quiz_{goal['id']}"):
            st.session_state[f"quiz_started_{goal['id']}"] = True
            st.session_state[f"selected_sdg_{goal['id']}"] = goal['id']

        if st.session_state.get(f"quiz_started_{goal['id']}", False):
            st.subheader(f"Quiz for {goal['title']}")
            questions = random.sample(quiz_questions.get(goal['id'], []), min(5, len(quiz_questions.get(goal['id'], []))))
            for q, options, correct in questions:
                answer = st.radio(q, options, key=q)
                if st.button("Submit", key=f"submit_{q}"):
                    if answer == correct:
                        st.success("Correct! 🎉")
                    else:
                        st.error("Incorrect. Try again! ❌")
