import streamlit as st
import random

# Full list of SDGs and their questions
sdg_goals = [
    {"id": 1, "title": "No Poverty", "description": "End poverty in all its forms everywhere.", "questions": [
        {"question": "What percentage of the world's population lives in poverty?", "options": ["10%", "20%", "30%", "40%"], "correct": "10%"},
        {"question": "What is the leading cause of poverty?", "options": ["Lack of education", "Natural disasters", "Political instability", "Unemployment"], "correct": "Unemployment"},
        {"question": "What region has the highest poverty rate?", "options": ["Africa", "Asia", "Latin America", "Europe"], "correct": "Africa"},
        {"question": "How many people live on less than $1.90 a day?", "options": ["1 billion", "1.5 billion", "2 billion", "3 billion"], "correct": "1.5 billion"},
        {"question": "Which country has the highest poverty rate?", "options": ["India", "Nigeria", "USA", "Brazil"], "correct": "India"}
    ]},
    {"id": 2, "title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition.", "questions": [
        {"question": "How many people are undernourished globally?", "options": ["500 million", "700 million", "900 million", "1 billion"], "correct": "700 million"},
        {"question": "Which region has the highest levels of hunger?", "options": ["Asia", "Africa", "Europe", "North America"], "correct": "Africa"},
        {"question": "What percentage of food is wasted globally?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "Which crop is the most widely consumed in the world?", "options": ["Rice", "Wheat", "Corn", "Barley"], "correct": "Rice"},
        {"question": "What is the main cause of food insecurity?", "options": ["Climate change", "Conflict", "Poverty", "All of the above"], "correct": "All of the above"}
    ]},
    {"id": 3, "title": "Good Health and Well-being", "description": "Ensure healthy lives and promote well-being for all at all ages.", "questions": [
        {"question": "What is the leading cause of death globally?", "options": ["Cancer", "Cardiovascular diseases", "Respiratory diseases", "Diabetes"], "correct": "Cardiovascular diseases"},
        {"question": "What percentage of the global population has access to basic health services?", "options": ["50%", "60%", "70%", "80%"], "correct": "70%"},
        {"question": "Which region has the highest life expectancy?", "options": ["Europe", "Asia", "North America", "Africa"], "correct": "North America"},
        {"question": "What is the most common mental health disorder?", "options": ["Anxiety", "Depression", "Schizophrenia", "Bipolar disorder"], "correct": "Anxiety"},
        {"question": "What is the global vaccination coverage rate?", "options": ["70%", "75%", "80%", "90%"], "correct": "80%"}
    ]},
    {"id": 4, "title": "Quality Education", "description": "Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.", "questions": [
        {"question": "How many children are out of school globally?", "options": ["50 million", "70 million", "100 million", "130 million"], "correct": "100 million"},
        {"question": "What is the global literacy rate?", "options": ["80%", "85%", "90%", "95%"], "correct": "90%"},
        {"question": "Which region has the highest dropout rate in education?", "options": ["Africa", "Asia", "Latin America", "Europe"], "correct": "Africa"},
        {"question": "What percentage of students have access to quality education worldwide?", "options": ["50%", "60%", "70%", "80%"], "correct": "70%"},
        {"question": "Which country has the highest education spending?", "options": ["USA", "China", "Germany", "Finland"], "correct": "USA"}
    ]},
    {"id": 5, "title": "Gender Equality", "description": "Achieve gender equality and empower all women and girls.", "questions": [
        {"question": "What is the gender pay gap worldwide?", "options": ["10%", "20%", "30%", "40%"], "correct": "20%"},
        {"question": "Which region has the lowest female labor force participation?", "options": ["Asia", "Africa", "Europe", "Latin America"], "correct": "Asia"},
        {"question": "How many women globally experience gender-based violence?", "options": ["100 million", "200 million", "300 million", "400 million"], "correct": "300 million"},
        {"question": "Which country has the highest number of women in parliament?", "options": ["Rwanda", "Sweden", "Norway", "Finland"], "correct": "Rwanda"},
        {"question": "What percentage of women have access to reproductive health services?", "options": ["50%", "60%", "70%", "80%"], "correct": "60%"}
    ]},
    {"id": 6, "title": "Clean Water and Sanitation", "description": "Ensure availability and sustainable management of water and sanitation for all.", "questions": [
        {"question": "How many people lack access to clean drinking water?", "options": ["700 million", "1 billion", "1.5 billion", "2 billion"], "correct": "1 billion"},
        {"question": "What is the global sanitation coverage?", "options": ["50%", "60%", "70%", "80%"], "correct": "60%"},
        {"question": "Which region faces the greatest water scarcity?", "options": ["Africa", "Asia", "Europe", "Latin America"], "correct": "Africa"},
        {"question": "What percentage of wastewater is treated globally?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "Which country uses the most water per capita?", "options": ["USA", "Australia", "China", "India"], "correct": "USA"}
    ]},
    {"id": 7, "title": "Affordable and Clean Energy", "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all.", "questions": [
        {"question": "What percentage of global energy comes from renewable sources?", "options": ["20%", "30%", "40%", "50%"], "correct": "30%"},
        {"question": "Which country leads the world in solar power generation?", "options": ["China", "USA", "Germany", "India"], "correct": "China"},
        {"question": "What is the global electrification rate?", "options": ["80%", "85%", "90%", "95%"], "correct": "90%"},
        {"question": "How many people lack access to electricity?", "options": ["500 million", "700 million", "1 billion", "1.5 billion"], "correct": "1 billion"},
        {"question": "Which energy source is the most used worldwide?", "options": ["Coal", "Natural Gas", "Solar", "Wind"], "correct": "Coal"}
    ]},
    {"id": 8, "title": "Decent Work and Economic Growth", "description": "Promote sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all.", "questions": [
        {"question": "What is the global unemployment rate?", "options": ["3%", "4%", "5%", "6%"], "correct": "5%"},
        {"question": "Which sector contributes the most to global employment?", "options": ["Agriculture", "Industry", "Services", "Technology"], "correct": "Services"},
        {"question": "What is the global poverty rate?", "options": ["10%", "15%", "20%", "25%"], "correct": "20%"},
        {"question": "Which region has the highest youth unemployment rate?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Africa"},
        {"question": "What is the global GDP growth rate?", "options": ["1%", "2%", "3%", "4%"], "correct": "3%"}
    ]},
    # Repeat for all remaining SDGs (9 to 17)
]

def show_question(sdg, question_idx):
    question = sdg['questions'][question_idx]
    st.subheader(f"Question: {question['question']}")
    options = question['options']
    selected_option = st.radio("Choose your answer:", options, key=question_idx)

    if st.button("Submit Answer", key=f"submit_{question_idx}"):
        if selected_option == question['correct']:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is {question['correct']}.")

def display_sdg_dashboard():
    st.title("Sustainable Development Goals (SDGs) Dashboard")
    st.write("Explore the 17 Sustainable Development Goals (SDGs). Click on a goal to start the quiz.")

    # Create a 3-column grid layout for SDG cards
    cols = st.columns(3)
    
    # Iterate through SDGs and create clickable sections
    for index, goal in enumerate(sdg_goals):
        with cols[index % 3]:
            st.markdown(f"### {goal['title']}")
            st.write(f"{goal['description']}")
            if st.button(f"Start Quiz for {goal['title']} 📝", key=f"quiz_{goal['id']}"):
                st.session_state["selected_sdg"] = goal["title"]
                st.session_state[f"quiz_started_{goal['id']}"] = True

    # Show quiz questions if a quiz is started
    sdg_choice = st.session_state.get("selected_sdg")
    if sdg_choice:
        selected_sdg = next(goal for goal in sdg_goals if goal["title"] == sdg_choice)
        question_idx = random.randint(0, len(selected_sdg['questions']) - 1)  # Random question from the goal
        show_question(selected_sdg, question_idx)

def play_quiz():
    display_sdg_dashboard()

play_quiz()
