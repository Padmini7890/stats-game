import streamlit as st
import json

# Sustainable Development Goals Data with images
sdg_goals = [
    {"id": 1, "title": "No Poverty", "description": "End poverty in all its forms everywhere.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/8/8b/SDG_logo_no_poverty.png"},
    {"id": 2, "title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/4/42/SDG_logo_zero_hunger.png"},
    {"id": 3, "title": "Good Health and Well-being", "description": "Ensure healthy lives and promote well-being for all ages.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/a/a0/SDG_logo_good_health.png"},
    {"id": 4, "title": "Quality Education", "description": "Ensure inclusive and equitable quality education for all.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/1/1f/SDG_logo_quality_education.png"},
    {"id": 5, "title": "Gender Equality", "description": "Achieve gender equality and empower all women and girls.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/SDG_logo_gender_equality.png"},
    {"id": 6, "title": "Clean Water and Sanitation", "description": "Ensure availability and sustainable management of water and sanitation for all.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/d/d6/SDG_logo_clean_water.png"},
    {"id": 7, "title": "Affordable and Clean Energy", "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/SDG_logo_affordable_energy.png"},
    {"id": 8, "title": "Decent Work and Economic Growth", "description": "Promote sustained, inclusive, and sustainable economic growth.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/0/09/SDG_logo_decent_work.png"},
    {"id": 9, "title": "Industry, Innovation and Infrastructure", "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/4/44/SDG_logo_industry_innovation.png"},
    {"id": 10, "title": "Reduced Inequalities", "description": "Reduce inequality within and among countries.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/SDG_logo_reduced_inequalities.png"},
    {"id": 11, "title": "Sustainable Cities and Communities", "description": "Make cities inclusive, safe, resilient, and sustainable.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/4/45/SDG_logo_sustainable_cities.png"},
    {"id": 12, "title": "Responsible Consumption and Production", "description": "Ensure sustainable consumption and production patterns.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/7/7a/SDG_logo_responsible_consumption.png"},
    {"id": 13, "title": "Climate Action", "description": "Take urgent action to combat climate change and its impacts.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/a/a4/SDG_logo_climate_action.png"},
    {"id": 14, "title": "Life Below Water", "description": "Conserve and sustainably use the oceans, seas, and marine resources.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/SDG_logo_life_below_water.png"},
    {"id": 15, "title": "Life on Land", "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/SDG_logo_life_on_land.png"},
    {"id": 16, "title": "Peace, Justice and Strong Institutions", "description": "Promote peaceful and inclusive societies for sustainable development.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/SDG_logo_peace_justice.png"},
    {"id": 17, "title": "Partnerships for the Goals", "description": "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development.",
     "image": "https://upload.wikimedia.org/wikipedia/commons/a/a4/SDG_logo_partnerships.png"}
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
            st.image(goal['image'], use_column_width=True)  # Display the image related to the SDG goal
            
            # Add a "Let's Start Quiz" button for each goal
            if st.button(f"Let's Start Quiz! 📝", key=f"quiz_{goal['id']}"):
                st.session_state["selected_sdg"] = goal["title"]
                st.session_state[f"quiz_started_{goal['id']}"] = True
            
            # Display quiz placeholder if the button is clicked
            if st.session_state.get(f"quiz_started_{goal['id']}", False):
                st.subheader(f"Quiz for {goal['title']}")
                st.write("(Quiz questions related to this SDG will be shown here.)")
                
                # Example Question Placeholder
                st.write("Q1: What percentage of the world's population lives in poverty?")
                answer = st.radio("Choose an answer:", ["10%", "20%", "30%", "40%"], key=f"quiz_question_{goal['id']}")
                
                if st.button("Submit Answer", key=f"submit_{goal['id']}"):
                    if answer == "10%":
                        st.success("Correct! 🎉")
                    else:
                        st.error("Incorrect. Try again! ❌")
            
            st.markdown("---")  # Add a horizontal line for separation

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
