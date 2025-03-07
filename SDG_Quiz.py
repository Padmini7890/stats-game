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

# Streamlit UI
st.title("🌍 Sustainable Development Goals (SDGs)")
st.write("Explore the 17 Sustainable Development Goals set by the United Nations.")

# Display SDG goals as rectangles
for goal in sdg_goals:
    with st.container():
        st.markdown(f"### {goal['title']}")
        st.write(goal["description"])
        if st.button(f"Let's Start the Quiz! 📝", key=goal["id"]):
            st.session_state["quiz_started"] = True
            st.session_state["selected_sdg"] = goal["title"]
            st.experimental_rerun()

# Show Quiz Placeholder (You can replace this with actual quiz logic)
if "quiz_started" in st.session_state and st.session_state["quiz_started"]:
    st.subheader(f"Quiz for {st.session_state['selected_sdg']}")
    st.write("(Quiz questions related to this SDG will be shown here.)")
    
    # Example Question Placeholder
    st.write("Q1: What percentage of the world's population lives in poverty?")
    st.radio("Choose an answer:", ["10%", "20%", "30%", "40%"])
    
    if st.button("Submit Answer"):
        st.write("(Feedback on the answer will be displayed here.)")

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
