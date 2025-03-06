import streamlit as st
import time

def main():
    st.title("🌍 Climate Crisis Escape Room 🏃‍♂️")
    st.subheader("Solve sustainability riddles to escape the crisis!")
    
    st.write("You are trapped in a world on the brink of climate disaster. Answer correctly to move forward. Wrong choices escalate the crisis!")
    
    questions = [
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
    ]
    
    crisis_level = 0
    for i, q in enumerate(questions):
        st.write(f"### Question {i+1}: {q['question']}")
        user_choice = st.radio("Choose an answer:", q["options"], key=i)
        
        if user_choice.startswith(q["answer"]):
            st.success("✅ Correct! " + q["fact"])
        else:
            st.error("❌ Wrong! " + q["fact"])
            crisis_level += 1
        
        time.sleep(1)  # Small delay for better UX
    
    st.write("\n---")
    if crisis_level == 0:
        st.success("🎉 You escaped the climate crisis! Your knowledge is impressive!")
    elif crisis_level < 2:
        st.warning("⚠️ You barely made it! The world needs better decision-making.")
    else:
        st.error("🌪️ The crisis is too severe. Try again and improve your sustainability knowledge!")
    
if __name__ == "__main__":
    main()
