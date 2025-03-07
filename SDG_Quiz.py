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
            st.markdown("---")  # Add a horizontal line for separation

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
