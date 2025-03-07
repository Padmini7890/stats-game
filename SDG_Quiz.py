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
        {"question": "What percentage of women have access to reproductive health services?", "options": ["50%", "60%", "70%", "80%"], "correct": "60%"
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
     {"id": 9, "title": "Industry, Innovation and Infrastructure", "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization.", "questions": [
        {"question": "What percentage of global infrastructure is in developing countries?", "options": ["50%", "60%", "70%", "80%"], "correct": "70%"},
        {"question": "What is the fastest-growing sector globally?", "options": ["Technology", "Healthcare", "Manufacturing", "Agriculture"], "correct": "Technology"},
        {"question": "What is the most commonly used material in infrastructure?", "options": ["Steel", "Wood", "Concrete", "Glass"], "correct": "Concrete"},
        {"question": "How many people live in slums worldwide?", "options": ["500 million", "700 million", "900 million", "1 billion"], "correct": "900 million"},
        {"question": "Which country has the most advanced infrastructure?", "options": ["Japan", "USA", "Germany", "China"], "correct": "Japan"}
    ]},
     {"id": 10, "title": "Reduced Inequalities", "description": "Reduce inequality within and among countries.", "questions": [
        {"question": "What is the global income inequality index?", "options": ["0.30", "0.40", "0.50", "0.60"], "correct": "0.50"},
        {"question": "Which region has the highest income inequality?", "options": ["Latin America", "Africa", "Europe", "Asia"], "correct": "Latin America"},
        {"question": "What is the wealth gap between the top 1% and the rest of the population?", "options": ["10 times", "20 times", "50 times", "100 times"], "correct": "50 times"},
        {"question": "Which country has the lowest inequality?", "options": ["Norway", "Sweden", "Finland", "Denmark"], "correct": "Norway"},
        {"question": "What is the unemployment rate among minorities?", "options": ["4%", "8%", "12%", "16%"], "correct": "12%"}
    ]},
     {"id": 11, "title": "Sustainable Cities and Communities", "description": "Make cities inclusive, safe, resilient, and sustainable.", "questions": [
        {"question": "What percentage of the world’s population lives in cities?", "options": ["40%", "50%", "60%", "70%"], "correct": "60%"},
        {"question": "What is the most sustainable city in the world?", "options": ["Copenhagen", "Amsterdam", "Paris", "New York"], "correct": "Copenhagen"},
        {"question": "How many people live in informal settlements?", "options": ["800 million", "1 billion", "1.5 billion", "2 billion"], "correct": "1 billion"},
        {"question": "Which is the fastest-growing city in the world?", "options": ["Beijing", "New Delhi", "Lagos", "Tokyo"], "correct": "Lagos"},
        {"question": "What percentage of urban areas suffer from air pollution?", "options": ["20%", "40%", "60%", "80%"], "correct": "80%"}
    ]},
     {"id": 12, "title": "Responsible Consumption and Production", "description": "Ensure sustainable consumption and production patterns.", "questions": [
        {"question": "How much of global waste is recycled?", "options": ["10%", "15%", "20%", "25%"], "correct": "20%"},
        {"question": "What percentage of global carbon emissions come from production?", "options": ["40%", "50%", "60%", "70%"], "correct": "60%"},
        {"question": "Which industry produces the most waste?", "options": ["Fashion", "Food", "Technology", "Construction"], "correct": "Construction"},
        {"question": "What percentage of food produced globally is wasted?", "options": ["25%", "30%", "35%", "40%"], "correct": "30%"},
        {"question": "Which country uses the most plastic per capita?", "options": ["USA", "China", "India", "Japan"], "correct": "USA"}
    ]},
     {"id": 13, "title": "Climate Action", "description": "Take urgent action to combat climate change and its impacts.", "questions": [
        {"question": "What is the main greenhouse gas responsible for global warming?", "options": ["Carbon dioxide", "Methane", "Nitrous oxide", "Water vapor"], "correct": "Carbon dioxide"},
        {"question": "What percentage of global carbon emissions come from fossil fuels?", "options": ["70%", "80%", "90%", "95%"], "correct": "80%"},
        {"question": "How many tons of CO2 are released annually worldwide?", "options": ["20 billion", "30 billion", "40 billion", "50 billion"], "correct": "40 billion"},
        {"question": "Which country produces the most CO2 emissions?", "options": ["USA", "China", "India", "Russia"], "correct": "China"},
        {"question": "How much has the global temperature increased since 1900?", "options": ["0.5°C", "1°C", "1.5°C", "2°C"], "correct": "1°C"}
    ]},
     {"id": 14, "title": "Life Below Water", "description": "Conserve and sustainably use the oceans, seas, and marine resources.", "questions": [
        {"question": "How much of the ocean is protected?", "options": ["10%", "15%", "20%", "25%"], "correct": "15%"},
        {"question": "What is the biggest threat to marine biodiversity?", "options": ["Overfishing", "Pollution", "Climate change", "Habitat destruction"], "correct": "Overfishing"},
        {"question": "What percentage of plastic in the ocean comes from land-based sources?", "options": ["60%", "70%", "80%", "90%"], "correct": "80%"},
        {"question": "How many species of marine animals are at risk of extinction?", "options": ["200", "300", "400", "500"], "correct": "400"},
        {"question": "Which ocean has the highest level of plastic pollution?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "correct": "Pacific"}
    ]},
     {"id": 15, "title": "Life on Land", "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems.", "questions": [
        {"question": "What percentage of land is protected worldwide?", "options": ["10%", "15%", "20%", "25%"], "correct": "15%"},
        {"question": "What is the leading cause of deforestation?", "options": ["Agriculture", "Logging", "Urbanization", "Mining"], "correct": "Agriculture"},
        {"question": "Which country has the most forest area?", "options": ["Russia", "Canada", "Brazil", "USA"], "correct": "Russia"},
        {"question": "How much of the Earth's land area is desert?", "options": ["15%", "20%", "25%", "30%"], "correct": "25%"},
        {"question": "What is the most endangered animal on land?", "options": ["Tiger", "Elephant", "Panda", "Rhinoceros"], "correct": "Rhinoceros"}
    ]},
     {"id": 16, "title": "Peace, Justice and Strong Institutions", "description": "Promote peaceful and inclusive societies for sustainable development.", "questions": [
        {"question": "What is the global homicide rate?", "options": ["5 per 100,000", "7 per 100,000", "9 per 100,000", "11 per 100,000"], "correct": "7 per 100,000"},
        {"question": "What percentage of countries have free elections?", "options": ["50%", "60%", "70%", "80%"], "correct": "70%"},
        {"question": "What is the most common cause of conflict?", "options": ["Political", "Religious", "Ethnic", "Economic"], "correct": "Ethnic"},
        {"question": "Which country has the highest incarceration rate?", "options": ["USA", "China", "Russia", "Brazil"], "correct": "USA"},
        {"question": "How many people are affected by violence globally?", "options": ["1 billion", "2 billion", "3 billion", "4 billion"], "correct": "2 billion"}
    ]},
     {"id": 17, "title": "Partnerships for the Goals", "description": "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development.", "questions": [
        {"question": "How much is global official development assistance?", "options": ["$100 billion", "$150 billion", "$200 billion", "$250 billion"], "correct": "$200 billion"},
        {"question": "What percentage of global trade is sustainable?", "options": ["10%", "15%", "20%", "25%"], "correct": "20%"},
        {"question": "Which region contributes the most to development aid?", "options": ["Europe", "North America", "Asia", "Africa"], "correct": "North America"},
        {"question": "What is the primary goal of the Paris Agreement?", "options": ["Reduce poverty", "Fight climate change", "Promote education", "Ensure food security"], "correct": "Fight climate change"},
        {"question": "Which international organization promotes the SDGs?", "options": ["World Bank", "IMF", "UN", "WHO"], "correct": "UN"}
    ]},
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
            if st.button(f"Start Quiz for {goal['title']} 📝", key=f"quiz_{goal['id']}"):
                st.session_state["selected_sdg"] = goal["title"]
                st.session_state[f"quiz_started_{goal['id']}"] = True

# Show quiz questions if a quiz is started
sdg_choice = st.session_state.get("selected_sdg")
if sdg_choice:
    selected_sdg = next(goal for goal in sdg_goals if goal["title"] == sdg_choice)
    
    # Select 2 random questions
    selected_questions = random.sample(selected_sdg['questions'], 2)

    for idx, question in enumerate(selected_questions):
        # Display the question
        st.write(f"Question {idx + 1}: {question['question']}")
        answer = st.radio(f"Choose an answer for Question {idx + 1}:", question['options'], key=f"quiz_question_{selected_sdg['id']}_{idx}")
        
        if st.button(f"Submit Answer for Question {idx + 1}", key=f"submit_{selected_sdg['id']}_{idx}"):
            if answer == question['correct']:
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect. Try again! ❌")
