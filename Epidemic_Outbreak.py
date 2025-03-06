import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# Load real-world epidemic data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    data = pd.read_csv(url, usecols=["date", "location", "new_cases", "new_deaths", "icu_patients", "hosp_patients"])
    data = data[data["location"] == "World"]  # Using global data
    data["date"] = pd.to_datetime(data["date"])
    return data

data = load_data()

# Game variables
infection_rate = 1.0  # Starts at 1.0x, higher means more infections
public_trust = 100  # 100% trust level
healthcare_capacity = 100  # 100% means hospitals can handle all cases

def plot_trends():
    fig, ax = plt.subplots()
    ax.plot(data["date"], data["new_cases"], label="New Cases", color='blue')
    ax.plot(data["date"], data["new_deaths"], label="New Deaths", color='red')
    ax.set_title("Global Pandemic Trends")
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

def make_decision(decision):
    global infection_rate, public_trust, healthcare_capacity
    if decision == "Lockdown":
        infection_rate *= 0.7  # Reduce infections
        public_trust -= 10  # People don't like lockdowns
    elif decision == "Mass Vaccination":
        infection_rate *= 0.5  # Strong reduction
        public_trust += 10  # Public approves
        healthcare_capacity += 10  # Less burden on hospitals
    elif decision == "No Restrictions":
        infection_rate *= 1.5  # Infections rise
        public_trust += 5  # Public enjoys freedom
        healthcare_capacity -= 20  # Hospitals get overwhelmed
    elif decision == "Travel Ban":
        infection_rate *= 0.8  # Some effect
        public_trust -= 5  # Some people dislike it
    elif decision == "Misinformation Campaign":
        infection_rate *= 2.0  # Disaster!
        public_trust += 20  # People believe false info
        healthcare_capacity -= 30  # Hospitals collapse
    
    # Ensure values remain within limits
    public_trust = max(0, min(100, public_trust))
    healthcare_capacity = max(0, min(100, healthcare_capacity))

def game_status():
    st.write(f"### Infection Rate: {infection_rate:.2f}x")
    st.progress(infection_rate / 3.0)
    st.write(f"### Public Trust: {public_trust}%")
    st.progress(public_trust / 100)
    st.write(f"### Healthcare Capacity: {healthcare_capacity}%")
    st.progress(healthcare_capacity / 100)

def main():
    st.title("Epidemic Outbreak: Data-Driven Response")
    st.write("Use real-world data to control a pandemic. Make strategic decisions to save lives!")
    plot_trends()
    
    global infection_rate, public_trust, healthcare_capacity
    game_over = False
    
    for turn in range(5):
        st.write(f"## Turn {turn + 1}")
        
        # Decision options
        decision = st.radio("Choose your action:", [
            "Lockdown",
            "Mass Vaccination",
            "No Restrictions",
            "Travel Ban",
            "Misinformation Campaign"
        ], key=f"decision_{turn}")
        
        # Apply decision
        if st.button("Confirm Decision", key=f"confirm_{turn}"):
            make_decision(decision)
            st.write(f"You chose: {decision}")
            game_status()
            time.sleep(1)
        
        # Check for win/loss conditions
        if infection_rate >= 3.0 or healthcare_capacity <= 0:
            st.error("The outbreak is out of control! You lost!")
            game_over = True
            break
        if infection_rate <= 0.5 and public_trust >= 70:
            st.success("You successfully controlled the outbreak! You win!")
            game_over = True
            break
        
    if not game_over:
        st.warning("The pandemic is ongoing. You managed to delay it, but challenges remain.")

if __name__ == "__main__":
    main()
