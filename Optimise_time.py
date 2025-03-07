import streamlit as st
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_project(level):
    """Generates a random project with tasks, durations, and dependencies."""
    task_count = {"Easy": 5, "Medium": 7, "Hard": 10}[level]
    tasks = [chr(65 + i) for i in range(task_count)]
    durations = {task: random.randint(2, 10) for task in tasks}
    dependencies = {}
    
    for i in range(1, task_count):
        dependencies[tasks[i]] = random.sample(tasks[:i], k=random.randint(1, min(i, 3)))
    
    return tasks, durations, dependencies

def calculate_critical_path(tasks, durations, dependencies):
    """Computes the project completion time using CPM."""
    G = nx.DiGraph()
    for task in tasks:
        G.add_node(task, duration=durations[task])
    
    for task, preds in dependencies.items():
        for pred in preds:
            G.add_edge(pred, task, weight=durations[pred])
    
    longest_path_length = nx.dag_longest_path_length(G, weight='weight')
    return longest_path_length, G

def draw_graph(G):
    """Draws the dependency graph."""
    pos = nx.spring_layout(G)
    labels = {node: f"{node}\n{G.nodes[node]['duration']}d" for node in G.nodes}
    nx.draw(G, pos, with_labels=True, labels=labels, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
    st.pyplot(plt)

def main():
    st.title("Project Time Estimation Game")
    level = st.selectbox("Select Difficulty Level:", ["Easy", "Medium", "Hard"])
    
    if st.button("Generate New Project"):
        tasks, durations, dependencies = generate_project(level)
        correct_time, G = calculate_critical_path(tasks, durations, dependencies)
        st.session_state["project"] = (tasks, durations, dependencies, correct_time, G)
        st.session_state["game_started"] = True
    
    if "game_started" in st.session_state:
        tasks, durations, dependencies, correct_time, G = st.session_state["project"]
        
        st.subheader("Project Details:")
        for task in tasks:
            dep_str = ", ".join(dependencies.get(task, ["Start"]))
            st.write(f"Task {task}: {durations[task]} days (Starts after: {dep_str})")
        
        user_guess = st.number_input("Guess the minimum project completion time (in days):", min_value=1, step=1)
        
        if st.button("Submit Guess"):
            st.write(f"Correct Time: {correct_time} days")
            diff = abs(user_guess - correct_time)
            if diff == 0:
                st.success("🎉 Perfect! You nailed it!")
            elif diff <= 2:
                st.info("👌 Close guess! Well done.")
            else:
                st.warning("❌ Not quite right. Try again!")
        
        if st.button("Show Dependency Graph"):
            draw_graph(G)
        
        if st.button("Restart Game"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()
