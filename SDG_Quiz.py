import streamlit as st
import random

# Sustainable Development Goals Data
sdg_goals = [
    {"id": 1, "title": "No Poverty", "description": "End poverty in all its forms everywhere.", "questions": [
        {"question": "What percentage of the world's population lives in poverty?", "options": ["10%", "20%", "30%", "40%"], "correct": "10%"},
        {"question": "Which country has the highest percentage of people living in poverty?", "options": ["India", "USA", "Nigeria", "China"], "correct": "Nigeria"}
    ]},
    {"id": 2, "title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition.", "questions": [
        {"question": "What is the global hunger index score in 2023?", "options": ["25", "17", "32", "13"], "correct": "17"},
        {"question": "How much food is wasted annually worldwide?", "options": ["1 billion tons", "2 billion tons", "1.3 billion tons", "3 billion tons"], "correct": "1.3 billion tons"}
    ]},
    {"id": 3, "title": "Good Health and Well-being", "description": "Ensure healthy lives and promote well-being for all ages.", "questions": [
        {"question": "What percentage of people in the world lack access to basic healthcare?", "options": ["10%", "20%", "30%", "40%"], "correct": "20%"},
        {"question": "What is the leading cause of death globally?", "options": ["Cancer", "Heart Disease", "Respiratory Infections", "Diabetes"], "correct": "Heart Disease"}
    ]},
    {"id": 4, "title": "Quality Education", "description": "Ensure inclusive and equitable quality education for all.", "questions": [
        {"question": "How many children worldwide are out of school?", "options": ["50 million", "100 million", "150 million", "200 million"], "correct": "100 million"},
        {"question": "What is the global literacy rate?", "options": ["80%", "85%", "90%", "95%"], "correct": "90%"}
    ]},
    {"id": 5, "title": "Gender Equality", "description": "Achieve gender equality and empower all women and girls.", "questions": [
        {"question": "What percentage of women in the world experience physical or sexual violence?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "Which country has the highest gender pay gap?", "options": ["USA", "Iceland", "Saudi Arabia", "China"], "correct": "Saudi Arabia"}
    ]},
    {"id": 6, "title": "Clean Water and Sanitation", "description": "Ensure availability and sustainable management of water and sanitation for all.", "questions": [
        {"question": "How many people lack access to safe drinking water?", "options": ["700 million", "1 billion", "2 billion", "3 billion"], "correct": "2 billion"},
        {"question": "How much water is used per person daily worldwide?", "options": ["100 liters", "200 liters", "150 liters", "50 liters"], "correct": "150 liters"}
    ]},
    {"id": 7, "title": "Affordable and Clean Energy", "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all.", "questions": [
        {"question": "What percentage of the world's population lacks access to electricity?", "options": ["5%", "10%", "20%", "25%"], "correct": "10%"},
        {"question": "What is the primary source of renewable energy?", "options": ["Solar", "Wind", "Hydropower", "Geothermal"], "correct": "Hydropower"}
    ]},
    {"id": 8, "title": "Decent Work and Economic Growth", "description": "Promote sustained, inclusive, and sustainable economic growth.", "questions": [
        {"question": "What percentage of youth are unemployed globally?", "options": ["10%", "15%", "20%", "25%"], "correct": "20%"},
        {"question": "What is the global unemployment rate?", "options": ["3%", "5%", "7%", "9%"], "correct": "5%"}
    ]},
    {"id": 9, "title": "Industry, Innovation and Infrastructure", "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization.", "questions": [
        {"question": "How much has global industrial production grown in the last decade?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "Which sector contributes the most to global GDP?", "options": ["Agriculture", "Industry", "Technology", "Services"], "correct": "Services"}
    ]},
    {"id": 10, "title": "Reduced Inequalities", "description": "Reduce inequality within and among countries.", "questions": [
        {"question": "What percentage of global wealth is held by the top 1%?", "options": ["15%", "25%", "40%", "50%"], "correct": "40%"},
        {"question": "Which continent has the highest level of inequality?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Africa"}
    ]},
    {"id": 11, "title": "Sustainable Cities and Communities", "description": "Make cities inclusive, safe, resilient, and sustainable.", "questions": [
        {"question": "What percentage of the global population lives in urban areas?", "options": ["50%", "55%", "60%", "70%"], "correct": "55%"},
        {"question": "How much does urbanization contribute to global greenhouse gas emissions?", "options": ["30%", "40%", "50%", "60%"], "correct": "50%"}
    ]},
    {"id": 12, "title": "Responsible Consumption and Production", "description": "Ensure sustainable consumption and production patterns.", "questions": [
        {"question": "How much food is wasted annually in the world?", "options": ["1 billion tons", "1.3 billion tons", "1.5 billion tons", "2 billion tons"], "correct": "1.3 billion tons"},
        {"question": "What percentage of the world's energy is produced from renewable sources?", "options": ["10%", "15%", "20%", "30%"], "correct": "20%"}
    ]},
    {"id": 13, "title": "Climate Action", "description": "Take urgent action to combat climate change and its impacts.", "questions": [
        {"question": "How much has global temperature increased since pre-industrial times?", "options": ["0.5°C", "1°C", "1.5°C", "2°C"], "correct": "1°C"},
        {"question": "What is the primary cause of global warming?", "options": ["Deforestation", "Greenhouse gases", "Ocean pollution", "Waste"], "correct": "Greenhouse gases"}
    ]},
    {"id": 14, "title": "Life Below Water", "description": "Conserve and sustainably use the oceans, seas, and marine resources.", "questions": [
        {"question": "What percentage of marine species are at risk of extinction?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "How much plastic is dumped into the oceans annually?", "options": ["4 million tons", "6 million tons", "8 million tons", "12 million tons"], "correct": "8 million tons"}
    ]},
    {"id": 15, "title": "Life on Land", "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems.", "questions": [
        {"question": "How much of the world's land is degraded?", "options": ["15%", "25%", "30%", "40%"], "correct": "25%"},
        {"question": "What is the leading cause of deforestation?", "options": ["Agriculture", "Mining", "Logging", "Urbanization"], "correct": "Agriculture"}
    ]},
    {"id": 16, "title": "Peace, Justice and Strong Institutions", "description": "Promote peaceful and inclusive societies for sustainable development.", "questions": [
        {"question": "How many countries have experienced violent conflict in the last decade?", "options": ["20", "40", "60", "80"], "correct": "60"},
        {"question": "What is the global homicide rate?", "options": ["5 per 100,000", "7 per 100,000", "10 per 100,000", "12 per 100,000"], "correct": "7 per 100,000"}
    ]},
    {"id": 17, "title": "Partnerships for the Goals", "description": "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development.", "questions": [
        {"question": "How much funding is required annually to achieve the SDGs?", "options": ["$1 trillion", "$2 trillion", "$3 trillion", "$5 trillion"], "correct": "$3 trillion"},
        {"question": "What is the primary source of financing for SDGs?", "options": ["Foreign direct investment", "Public spending", "Private sector", "Development assistance"], "correct": "Private sector"}
    ]}
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
            
            # Add a "Let's Start Quiz" button for each goal
            if st.button(f"Let's Start Quiz! 📝", key=f"quiz_{goal['id']}"):
                st.session_state["selected_sdg"] = goal["title"]
                st.session_state[f"quiz_started_{goal['id']}"] = True
            
            # Display quiz questions if the quiz has started
            if st.session_state.get(f"quiz_started_{goal['id']}", False):
                st.subheader(f"Quiz for {goal['title']}")
                question = random.choice(goal["questions"])
                st.write(question["question"])
                
                # Display the multiple-choice options
                answer = st.radio("Choose an answer:", question["options"], key=f"quiz_question_{goal['id']}")
                
                if st.button("Submit Answer", key=f"submit_{goal['id']}"):
                    if answer == question["correct"]:
                        st.success("Correct! 🎉")
                    else:
                        st.error("Incorrect. Try again! ❌")
            
            st.markdown("---")  # Add a horizontal line for separation

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
