import streamlit as st
import time
import random

def main():
    st.title("🌍 Climate Crisis Escape Room 🏃‍♂️")
    st.subheader("Solve sustainability riddles to escape the crisis!")
    
    st.write("You are trapped in a world on the brink of climate disaster. Answer correctly to move forward. Wrong choices escalate the crisis!")
    
    levels = {"Easy": (7, 10), "Medium": (5, 15), "Hard": (3, 20)}
    level = st.selectbox("Choose your difficulty level:", list(levels.keys()))
    num_questions, time_limit = levels[level]
    
    all_questions = [
        {"question": "Which sector contributes the most to global CO2 emissions?", 
         "options": ["A. Transportation", "B. Agriculture", "C. Energy Production", "D. Deforestation"],
         "answer": "C",
         "fact": "Energy production accounts for around 73% of global greenhouse gas emissions!"},
        {"question": "What is the main reason for rising sea levels?", 
         "options": ["A. Melting glaciers", "B. Underwater volcanoes", "C. More fish in the ocean", "D. Sun’s radiation"],
         "answer": "A",
         "fact": "Glaciers and ice sheets melting contribute the most to rising sea levels!"},
        {"question": "Which renewable energy source has grown the fastest in the past decade?", 
         "options": ["A. Solar power", "B. Hydroelectricity", "C. Wind energy", "D. Geothermal energy"],
         "answer": "A",
         "fact": "Solar energy has seen the fastest growth due to decreasing costs and increased efficiency!"},
        {"question": "What percentage of plastic waste has been recycled globally?", 
         "options": ["A. 9%", "B. 25%", "C. 40%", "D. 60%"],
         "answer": "A",
         "fact": "Only about 9% of all plastic waste ever produced has been recycled!"},
        {"question": "Which country leads in wind energy production?", 
         "options": ["A. USA", "B. China", "C. Germany", "D. India"],
         "answer": "B",
         "fact": "China is the world leader in wind energy capacity!"},
        {"question": "What is the primary gas responsible for global warming?", 
         "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
         "answer": "B",
         "fact": "Carbon dioxide (CO2) is the main greenhouse gas driving climate change!"},
        {"question": "How long does it take for a plastic bottle to decompose?", 
         "options": ["A. 10 years", "B. 50 years", "C. 450 years", "D. 1000 years"],
         "answer": "C",
         "fact": "A plastic bottle can take up to 450 years to decompose!"},
        {"question": "Which country generates the most plastic waste per capita?", 
         "options": ["A. USA", "B. China", "C. India", "D. Brazil"],
         "answer": "A",
         "fact": "The USA produces the most plastic waste per capita in the world!"},
        {"question": "Which ecosystem stores the most carbon?", 
         "options": ["A. Rainforests", "B. Mangroves", "C. Peatlands", "D. Coral reefs"],
         "answer": "C",
         "fact": "Peatlands store more carbon per unit area than any other ecosystem!"},
        {"question": "What percentage of Earth's freshwater is available for human use?", 
         "options": ["A. 1%", "B. 10%", "C. 25%", "D. 50%"],
         "answer": "A",
         "fact": "Only about 1% of Earth's freshwater is accessible for human use!"}
    ]
    
    selected_questions = random.sample(all_questions, num_questions)
    crisis_level = 0
    start_time = time.time()
    
    for i, q in enumerate(selected_questions):
        st.write(f"### Question {i+1}: {q['question']}")
        st.info("Hint: " + q["fact"])
        user_choice = st.radio("Choose an answer:", q["options"], key=f"q{i}", index=None)
        
        if user_choice and user_choice.startswith(q["answer"]):
            st.success("✅ Correct! " + q["fact"])
        elif user_choice:
            st.error("❌ Wrong! " + q["fact"])
            crisis_level += 1
        
        if time.time() - start_time > time_limit:
            st.error("⏳ Time’s up! The climate crisis worsened before you could escape!")
            return
        
        time.sleep(1)  # Small delay for better UX
    
    st.write("\n---")
    if crisis_level == 0:
        st.success("🎉 You escaped the climate crisis! Your knowledge is impressive!")
    elif crisis_level < num_questions // 2:
        st.warning("⚠️ You barely made it! The world needs better decision-making.")
    else:
        st.error("🌪️ The crisis is too severe. Try again and improve your sustainability knowledge!")
    
if __name__ == "__main__":
    main()
