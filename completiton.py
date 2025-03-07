import streamlit as st
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_riddle_tasks():
    """Generates a random set of tasks with durations and dependencies in riddle format."""
    tasks = {
        "A": ("The start of the journey, setting up the base.", random.randint(2, 6)),
        "B": ("This task can only begin once A is done, crafting the framework.", random.randint(3, 7)),
        "C": ("After B, we refine the details.", random.randint(2, 5)),
        "D": ("When A is completed, this runs in parallel to B, creating support.", random.randint(4, 8)),
        "E": ("C and D must be complete before we finalize everything.", random.randint(5, 9)),
    }
    dependencies = {"A": [], "B": ["A"], "C": ["B"], "D": ["A"], "E": ["C", "D"]}
    return tasks, dependencies

def calculate_critical_path(tasks, dependencies):
    """Uses CPM to determine the least time required to complete the project."""
    G = nx.DiGraph()
    for task, (desc, duration) in tasks.items():
        G.add_node(task, duration=duration)
    for task, deps in dependencies.items():
        for dep in deps:
            G.add_edge(dep, task)
    
    longest_path = nx.dag_longest_path(G)
    total_time = sum(tasks[task][1] for task in longest_path)
    return total_time, longest_path

def show_graph(tasks, dependencies):
    """Displays a simple network graph of the project."""
    G = nx.DiGraph()
    for task, (desc, duration) in tasks.items():
        G.add_node(task, label=f"{task}\n({duration} days)")
    for task, deps in dependencies.items():
        for dep in deps:
            G.add_edge(dep, task)
    
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G)
    labels = {node: G.nodes[node]['label'] for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color='lightblue', edge_color='gray')
    st.pyplot(plt)

st.title("Project Time Estimation Challenge")

# Generate a new set of tasks and dependencies
if "tasks" not in st.session_state:
    st.session_state.tasks, st.session_state.dependencies = generate_riddle_tasks()
    st.session_state.correct_time, st.session_state.critical_path = calculate_critical_path(
        st.session_state.tasks, st.session_state.dependencies
    )
    st.session_state.game_over = False
    st.session_state.show_graph = False

st.write("### Task Descriptions (Solve the Riddles!)")
for task, (desc, duration) in st.session_state.tasks.items():
    st.write(f"**{task}:** {desc}")

# User input for estimated time
guess = st.number_input("Guess the least time needed to complete the project (in days):", min_value=1, step=1)
if st.button("Submit Guess"):
    correct_time = st.session_state.correct_time
    st.session_state.game_over = True
    st.session_state.show_graph = True
    
    st.write(f"### Correct Time: {correct_time} days")
    st.write(f"Critical Path: {' → '.join(st.session_state.critical_path)}")
    
    if abs(guess - correct_time) == 0:
        st.success("🎉 Perfect guess! Congratulations! 🎊")
        st.image("https://media.giphy.com/media/3o7TKsQYAVjXyG3hXa/giphy.gif")
    elif abs(guess - correct_time) <= 2:
        st.success("👏 Great guess! You were very close!")
    else:
        st.warning("Not quite! Try again next time.")
    
    # Store scores in leaderboard
    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = []
    st.session_state.leaderboard.append((guess, correct_time))
    
if "leaderboard" in st.session_state:
    st.write("### Leaderboard")
    for idx, (g, c) in enumerate(sorted(st.session_state.leaderboard, key=lambda x: abs(x[0] - x[1]))):
        st.write(f"{idx+1}. Guessed: {g} days | Correct: {c} days")

# Reset Button
if st.button("Reset Game"):
    st.session_state.tasks, st.session_state.dependencies = generate_riddle_tasks()
    st.session_state.correct_time, st.session_state.critical_path = calculate_critical_path(
        st.session_state.tasks, st.session_state.dependencies
    )
    st.session_state.game_over = False
    st.session_state.show_graph = False
    st.experimental_rerun()

# Show network graph of dependencies only after restart
if st.session_state.show_graph:
    st.write("### Project Dependency Graph")
    show_graph(st.session_state.tasks, st.session_state.dependencies)
