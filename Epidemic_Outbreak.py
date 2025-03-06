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

# Initialize session state variables
def reset_game():
    st.session_state.infection_rate = 1.0
    st.session_state.public_trust = 100
    st.session_state.healthcare_capacity = 100

if "infection_rate" not in st.session_state:
    reset_game()

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
    if decision == "Lockdown":
        st.session_state.infection_rate *= 0.7  # Reduce infections
        st.session_state.public_trust -= 10  # People don't like lockdowns
    elif decision == "Mass Vaccination":
        st.session_state.infection_rate *= 0.5  # Strong reduction
        st.session_state.public_trust += 10  # Public approves
        st.session_state.healthcare_capacity += 10  # Less burden on hospitals
    elif decision == "No Restrictions":
        st.session_state.infection_rate *= 1.5  # Infections rise
        st.session_state.public_trust += 5  # Public enjoys freedom
        st.session_state.healthcare_capacity -= 20  # Hospitals get overwhelmed
    elif decision == "Travel Ban":
        st.session_state.infection_rate *= 0.8  # Some effect
        st.session_state.public_trust -= 5  # Some people dislike it
    elif decision == "Misinformation Campaign":
        st.session_state.infection_rate *= 2.0  # Disaster!
        st.session_state.public_trust += 20  # People believe false info
        st.session_state.healthcare_capacity -= 30  # Hospitals collapse
    
    # Ensure values remain within limits
    st.session_state.public_trust = max(0, min(100, st.session_state.public_trust))
    st.session_state.healthcare_capacity = max(0, min(100, st.session_state.healthcare_capacity))

def game_status():
    st.write(f"### Infection Rate: {st.session_state.infection_rate:.2f}x")
    st.progress(st.session_state.infection_rate / 3.0)
    st.write(f"### Public Trust: {st.session_state.public_trust}%")
    st.progress(st.session_state.public_trust / 100)
    st.write(f"### Healthcare Capacity: {st.session_state.healthcare_capacity}%")
    st.progress(st.session_state.healthcare_capacity / 100)

def main():
    st.title("Epidemic Outbreak: Data-Driven Response")
    st.write("Use real-world data to control a pandemic. Make strategic decisions to save lives!")
    plot_trends()
    
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
        if st.session_state.infection_rate >= 3.0 or st.session_state.healthcare_capacity <= 0:
            st.error("The outbreak is out of control! You lost!")
            game_over = True
            break
        if st.session_state.infection_rate <= 0.5 and st.session_state.public_trust >= 70:
            st.success("You successfully controlled the outbreak! You win!")
            game_over = True
            break
        
    if not game_over:
        st.warning("The pandemic is ongoing. You managed to delay it, but challenges remain.")
    
    if st.button("New Game"):
        reset_game()
        st.experimental_rerun()

if __name__ == "__main__":
    main()
