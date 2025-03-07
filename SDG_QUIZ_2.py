import streamlit as st
import random

# Sustainable Development Goals Data
sdg_goals = [
    {"id": 1, "title": "No Poverty", "emoji": "🚫💵", "description": "End poverty in all its forms everywhere.", "questions": [
        {"question": "What percentage of the world's population lives in poverty?", "options": ["10%", "20%", "30%", "40%"], "correct": "10%"},
        {"question": "Which country has the highest percentage of people living in poverty?", "options": ["India", "USA", "Nigeria", "China"], "correct": "Nigeria"},
        {"question": "What is the international poverty line according to the World Bank?", "options": ["$1.90/day", "$2.50/day", "$3.00/day", "$5.00/day"], "correct": "$1.90/day"},
        {"question": "How many people live in extreme poverty globally?", "options": ["700 million", "1 billion", "1.3 billion", "2 billion"], "correct": "700 million"},
        {"question": "Which region has the highest number of people living in extreme poverty?", "options": ["Sub-Saharan Africa", "Asia", "Latin America", "Europe"], "correct": "Sub-Saharan Africa"}
    ]},
    {"id": 2, "title": "Zero Hunger", "emoji": "🍽️🌍", "description": "End hunger, achieve food security and improved nutrition.", "questions": [
        {"question": "What is the global hunger index score in 2023?", "options": ["25", "17", "32", "13"], "correct": "17"},
        {"question": "How much food is wasted annually worldwide?", "options": ["1 billion tons", "2 billion tons", "1.3 billion tons", "3 billion tons"], "correct": "1.3 billion tons"},
        {"question": "How many people suffer from chronic hunger globally?", "options": ["500 million", "750 million", "800 million", "1 billion"], "correct": "800 million"},
        {"question": "What is the most common micronutrient deficiency in the world?", "options": ["Iron", "Vitamin D", "Iodine", "Vitamin A"], "correct": "Iron"},
        {"question": "Which region has the highest rate of food insecurity?", "options": ["South Asia", "Sub-Saharan Africa", "Middle East", "Europe"], "correct": "Sub-Saharan Africa"}
    ]},
    {"id": 3, "title": "Good Health and Well-being", "emoji": "🩺💪", "description": "Ensure healthy lives and promote well-being for all ages.", "questions": [
        {"question": "What percentage of people in the world lack access to basic healthcare?", "options": ["10%", "20%", "30%", "40%"], "correct": "20%"},
        {"question": "What is the leading cause of death globally?", "options": ["Cancer", "Heart Disease", "Respiratory Infections", "Diabetes"], "correct": "Heart Disease"},
        {"question": "What is the life expectancy globally?", "options": ["70 years", "72 years", "74 years", "76 years"], "correct": "72 years"},
        {"question": "What is the global maternal mortality ratio?", "options": ["200 per 100,000 live births", "150 per 100,000 live births", "300 per 100,000 live births", "400 per 100,000 live births"], "correct": "200 per 100,000 live births"},
        {"question": "How many people globally are living with HIV/AIDS?", "options": ["10 million", "20 million", "36 million", "50 million"], "correct": "36 million"}
    ]},
    {"id": 4, "title": "Quality Education", "emoji": "📚🎓", "description": "Ensure inclusive and equitable quality education for all.", "questions": [
        {"question": "How many children worldwide are out of school?", "options": ["50 million", "100 million", "150 million", "200 million"], "correct": "100 million"},
        {"question": "What is the global literacy rate?", "options": ["80%", "85%", "90%", "95%"], "correct": "90%"},
        {"question": "What percentage of youth are enrolled in secondary education globally?", "options": ["50%", "60%", "70%", "80%"], "correct": "70%"},
        {"question": "How many teachers are needed worldwide to achieve quality education for all?", "options": ["10 million", "25 million", "35 million", "50 million"], "correct": "25 million"},
        {"question": "Which continent has the lowest enrollment in primary education?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Africa"}
    ]},
    {"id": 5, "title": "Gender Equality", "emoji": "♀️♂️", "description": "Achieve gender equality and empower all women and girls.", "questions": [
        {"question": "What percentage of women in the world experience physical or sexual violence?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "Which country has the highest gender pay gap?", "options": ["USA", "Iceland", "Saudi Arabia", "China"], "correct": "Saudi Arabia"},
         {"question": "What is the global gender parity in primary education?", "options": ["80%", "90%", "95%", "98%"], "correct": "90%"},
        {"question": "What percentage of women hold positions in national parliaments globally?", "options": ["10%", "25%", "30%", "40%"], "correct": "25%"},
        {"question": "Which country ranks first for gender equality?", "options": ["Norway", "Sweden", "Finland", "Denmark"], "correct": "Norway"}
    ]},
    {"id": 6, "title": "Clean Water and Sanitation", "emoji": "💧🚽", "description": "Ensure availability and sustainable management of water and sanitation for all.", "questions": [
        {"question": "How many people lack access to safe drinking water?", "options": ["700 million", "1 billion", "2 billion", "3 billion"], "correct": "2 billion"},
        {"question": "How much water is used per person daily worldwide?", "options": ["100 liters", "200 liters", "150 liters", "50 liters"], "correct": "150 liters"},
        {"question": "What percentage of wastewater is treated globally?", "options": ["10%", "20%", "30%", "40%"], "correct": "20%"},
        {"question": "How many people globally lack access to sanitation facilities?", "options": ["1 billion", "1.5 billion", "2 billion", "2.5 billion"], "correct": "2 billion"},
        {"question": "What is the leading cause of waterborne diseases?", "options": ["Pollution", "Lack of sanitation", "Poor water quality", "Water scarcity"], "correct": "Poor water quality"}
    ]},
    {"id": 7, "title": "Affordable and Clean Energy", "emoji": "⚡🌱", "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all.", "questions": [
        {"question": "What percentage of the world's population lacks access to electricity?", "options": ["5%", "10%", "20%", "25%"], "correct": "10%"},
        {"question": "What is the primary source of renewable energy?", "options": ["Solar", "Wind", "Hydropower", "Geothermal"], "correct": "Hydropower"},
        {"question": "Which country produces the most wind energy?", "options": ["China", "USA", "Germany", "India"], "correct": "China"},
        {"question": "How much of the world’s electricity is generated from renewable sources?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "What is the global average energy consumption per person?", "options": ["2000 kWh", "5000 kWh", "7000 kWh", "10000 kWh"], "correct": "5000 kWh"}
    ]},
    {"id": 8, "title": "Decent Work and Economic Growth", "emoji": "💼📈", "description": "Promote sustained, inclusive, and sustainable economic growth.", "questions": [
        {"question": "What percentage of youth are unemployed globally?", "options": ["10%", "15%", "20%", "25%"], "correct": "20%"},
        {"question": "What is the global unemployment rate?", "options": ["3%", "5%", "7%", "9%"], "correct": "5%"},
        {"question": "Which sector contributes the most to global GDP?", "options": ["Agriculture", "Industry", "Technology", "Services"], "correct": "Services"},
        {"question": "What is the global average income inequality?", "options": ["0.3", "0.4", "0.5", "0.6"], "correct": "0.5"},
        {"question": "Which region has the highest levels of economic growth?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Asia"}
    ]},
    {"id": 9, "title": "Industry, Innovation and Infrastructure", "emoji": "🏭💡", "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization.", "questions": [
        {"question": "How much has global industrial production grown in the last decade?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "Which sector contributes the most to global GDP?", "options": ["Agriculture", "Industry", "Technology", "Services"], "correct": "Services"},
        {"question": "Which country has the most advanced infrastructure?", "options": ["Japan", "USA", "China", "Germany"], "correct": "Japan"},
        {"question": "How much of global infrastructure is considered sustainable?", "options": ["10%", "20%", "30%", "40%"], "correct": "20%"},
        {"question": "What is the primary challenge to global infrastructure development?", "options": ["Funding", "Technology", "Resources", "Regulations"], "correct": "Funding"}
    ]},
    {"id": 10, "title": "Reduced Inequalities", "emoji": "↔️🌍", "description": "Reduce inequality within and among countries.", "questions": [
        {"question": "What percentage of global wealth is held by the top 1%?", "options": ["15%", "25%", "40%", "50%"], "correct": "40%"},
        {"question": "Which continent has the highest level of inequality?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Africa"},
        {"question": "What is the global Gini coefficient for income inequality?", "options": ["0.3", "0.4", "0.5", "0.6"], "correct": "0.5"},
        {"question": "What is the richest country in terms of income per capita?", "options": ["USA", "Luxembourg", "Germany", "Switzerland"], "correct": "Luxembourg"},
        {"question": "Which region has the highest levels of wealth inequality?", "options": ["Latin America", "Asia", "Africa", "Europe"], "correct": "Latin America"}
    ]},
    {"id": 11, "title": "Sustainable Cities and Communities", "emoji": "🏙️🌳", "description": "Make cities inclusive, safe, resilient, and sustainable.", "questions": [
        {"question": "What percentage of the global population lives in urban areas?", "options": ["50%", "55%", "60%", "70%"], "correct": "55%"},
        {"question": "How much does urbanization contribute to global greenhouse gas emissions?", "options": ["30%", "40%", "50%", "60%"], "correct": "50%"},
        {"question": "Which city is considered the most sustainable city in the world?", "options": ["Copenhagen", "New York", "Tokyo", "London"], "correct": "Copenhagen"},
        {"question": "What is the primary challenge for urban sustainability?", "options": ["Pollution", "Overpopulation", "Water scarcity", "Waste management"], "correct": "Overpopulation"},
        {"question": "Which country has the most urbanized population?", "options": ["USA", "China", "Japan", "Germany"], "correct": "Japan"}
    ]},
    {"id": 12, "title": "Responsible Consumption and Production", "emoji": "♻️🌱", "description": "Ensure sustainable consumption and production patterns.", "questions": [
        {"question": "How much food is wasted annually in the world?", "options": ["1 billion tons", "1.3 billion tons", "1.5 billion tons", "2 billion tons"], "correct": "1.3 billion tons"},
        {"question": "What percentage of the world's energy is produced from renewable sources?", "options": ["10%", "15%", "20%", "30%"], "correct": "20%"},
        {"question": "What is the primary material causing plastic waste?", "options": ["Plastic bags", "Plastic bottles", "Plastic packaging", "Plastic straws"], "correct": "Plastic packaging"},
        {"question": "What percentage of global production is sustainable?", "options": ["30%", "40%", "50%", "60%"], "correct": "50%"},
        {"question": "Which country has the highest recycling rate?", "options": ["Germany", "Japan", "Sweden", "USA"], "correct": "Germany"}
    ]},
    {"id": 13, "title": "Climate Action", "emoji": "🌍🔥", "description": "Take urgent action to combat climate change and its impacts.", "questions": [
        {"question": "How much has global temperature increased since pre-industrial times?", "options": ["0.5°C", "1°C", "1.5°C", "2°C"], "correct": "1°C"},
        {"question": "What is the primary cause of global warming?", "options": ["Deforestation", "Greenhouse gases", "Ocean pollution", "Waste"], "correct": "Greenhouse gases"},
        {"question": "Which country is the largest emitter of CO2?", "options": ["USA", "China", "India", "Russia"], "correct": "China"},
        {"question": "What percentage of global CO2 emissions come from agriculture?", "options": ["10%", "15%", "25%", "30%"], "correct": "25%"},
        {"question": "Which country has made the largest investments in renewable energy?", "options": ["China", "USA", "Germany", "India"], "correct": "China"}
    ]},
    {"id": 14, "title": "Life Below Water", "emoji": "🌊🐠", "description": "Conserve and sustainably use the oceans, seas, and marine resources.", "questions": [
        {"question": "What percentage of marine species are at risk of extinction?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "How much plastic is dumped into the oceans annually?", "options": ["4 million tons", "6 million tons", "8 million tons", "12 million tons"], "correct": "8 million tons"},
        {"question": "What percentage of marine species are at risk due to human activities?", "options": ["10%", "20%", "30%", "40%"], "correct": "30%"},
        {"question": "What is the largest dead zone in the ocean?", "options": ["Gulf of Mexico", "Indian Ocean", "Pacific Ocean", "Baltic Sea"], "correct": "Gulf of Mexico"},
        {"question": "Which ocean is the most polluted?", "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"], "correct": "Pacific Ocean"}
    ]},
    {"id": 15, "title": "Life on Land", "emoji": "🌳🐅", "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems.", "questions": [
        {"question": "How much of the world's land is degraded?", "options": ["15%", "25%", "30%", "40%"], "correct": "25%"},
        {"question": "What is the leading cause of deforestation?", "options": ["Agriculture", "Mining", "Logging", "Urbanization"], "correct": "Agriculture"},
         {"question": "What is the leading cause of deforestation?", "options": ["Agriculture", "Logging", "Urbanization", "Mining"], "correct": "Agriculture"},
        {"question": "How many species are at risk of extinction?", "options": ["20%", "30%", "40%", "50%"], "correct": "30%"},
        {"question": "Which country has the largest protected area of land?", "options": ["USA", "Brazil", "China", "Australia"], "correct": "USA"}
    ]},
    {"id": 16, "title": "Peace, Justice and Strong Institutions", "emoji": "✌️⚖️", "description": "Promote peaceful and inclusive societies for sustainable development.", "questions": [
        {"question": "How many countries have experienced violent conflict in the last decade?", "options": ["20", "40", "60", "80"], "correct": "60"},
        {"question": "What is the global homicide rate?", "options": ["5 per 100,000", "7 per 100,000", "10 per 100,000", "12 per 100,000"], "correct": "7 per 100,000"},
        {"question": "Which region has the highest number of conflict zones?", "options": ["Africa", "Asia", "Europe", "Middle East"], "correct": "Middle East"},
        {"question": "What is the global homicide rate?", "options": ["3%", "5%", "7%", "10%"], "correct": "7%"},
        {"question": "Which country is known for its strong judicial system?", "options": ["USA", "Switzerland", "Norway", "Finland"], "correct": "Switzerland"}
    ]},
    {"id": 17, "title": "Partnerships for the Goals", "emoji": "🤝🌍", "description": "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development.", "questions": [
        {"question": "How much funding is required annually to achieve the SDGs?", "options": ["$1 trillion", "$2 trillion", "$3 trillion", "$5 trillion"], "correct": "$3 trillion"},
        {"question": "What is the primary source of financing for SDGs?", "options": ["Foreign direct investment", "Public spending", "Private sector", "Development assistance"], "correct": "Private sector"},
        {"question": "Which is the primary goal of international partnerships?", "options": ["Reducing poverty", "Climate action", "Access to education", "Global health"], "correct": "Reducing poverty"},
        {"question": "What is the budget for achieving SDGs globally?", "options": ["$3 trillion", "$5 trillion", "$10 trillion", "$15 trillion"], "correct": "$5 trillion"},
        {"question": "How many UN organizations are working on SDGs?", "options": ["15", "20", "30", "50"], "correct": "30"}
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
            st.markdown(f"### {goal['emoji']} {goal['title']}")
            st.write(goal["description"])
            
            # Add a "Let's Start Quiz" button for each goal
            if st.button(f"Let's Start Quiz! 📝", key=f"quiz_{goal['id']}"):
                st.session_state["selected_sdg"] = goal["title"]
                st.session_state[f"quiz_started_{goal['id']}"] = True
                # Select the first question when the quiz starts
                st.session_state[f"quiz_question_{goal['id']}"] = random.choice(goal["questions"])

            # Display quiz questions if the quiz has started
            if st.session_state.get(f"quiz_started_{goal['id']}", False):
                st.subheader(f"Quiz for {goal['title']}")
                
                # Retrieve the selected question from session state
                question = st.session_state.get(f"quiz_question_{goal['id']}")
                st.write(question["question"])
                
                # Display the multiple-choice options
                answer = st.radio("Choose an answer:", question["options"], key=f"quiz_answer_{goal['id']}")
                
                if st.button("Submit Answer", key=f"submit_{goal['id']}"):
                    if answer == question["correct"]:
                        st.success("Correct! 🎉")
                        # Select a new question for the next round
                        st.session_state[f"quiz_question_{goal['id']}"] = random.choice(goal["questions"])
                    else:
                        st.error(f"Incorrect. The correct answer is: {question['correct']} ❌")
                # Reset button
                if st.button("Reset Quiz", key=f"reset_{goal['id']}"):
                    # Reset quiz state
                    st.session_state[f"quiz_started_{goal['id']}"] = False  # Reset quiz state
                    st.session_state[f"quiz_question_{goal['id']}"] = None  # Clear the current question
                    st.session_state[f"quiz_answer_{goal['id']}"] = None  # Clear the answer selection

            st.markdown("---")  # Add a horizontal line for separation

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
