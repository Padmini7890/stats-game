import streamlit as st
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_riddle_tasks(level):
    """Generates a structured set of tasks with durations and dependencies in an educational format."""
    task_names = [chr(i) for i in range(65, 91)]  # Task names A-Z
    random.shuffle(task_names)
    
    level_settings = {
        1: (4, 5, 1),   # Easy: Fewer tasks, minimal dependencies
        2: (4, 6, 2),   # Moderate: More dependencies
        3: (6, 8, 2),   # Hard: Complex task interlinks
        4: (6, 8, 3)    # Extremely Hard: High interdependencies
    }
    
    num_tasks, max_tasks, max_dependencies = level_settings[level]
    num_tasks = random.randint(num_tasks, max_tasks)
    
    tasks = {}
    dependencies = {task_names[i]: [] for i in range(num_tasks)}
    
    for i in range(num_tasks):
        task = task_names[i]
        description = f"Task {task} involves a crucial step in project completion. Estimate wisely!"
        duration = random.randint(3 + level, 6 + level * 2)
        tasks[task] = (description, duration)
        
        if i > 0:
            num_dependencies = random.randint(1, min(i, max_dependencies))
            dependencies[task] = random.sample(task_names[:i], num_dependencies)
    
    return tasks, dependencies

def calculate_critical_path(tasks, dependencies):
    """Uses CPM to determine the minimum project completion time."""
    G = nx.DiGraph()
    for task, (_, duration) in tasks.items():
        G.add_node(task, duration=duration)
    for task, deps in dependencies.items():
        for dep in deps:
            G.add_edge(dep, task)
    
    longest_path = nx.dag_longest_path(G)
    total_time = sum(tasks[task][1] for task in longest_path)
    
    return total_time, longest_path

def show_graph(tasks, dependencies):
    """Displays a task dependency network graph."""
    G = nx.DiGraph()
    for task, (_, duration) in tasks.items():
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

if "name" not in st.session_state:
    st.session_state.name = ""

st.session_state.name = st.text_input("Enter your name:", value=st.session_state.name)

if "level_selected" not in st.session_state:
    st.session_state.level_selected = False

if not st.session_state.level_selected:
    level = st.radio("Select Level:", ["🔵 Easy", "🟠 Moderate", "🔴 Hard", "⚫ Extremely Hard"])
    if st.button("Confirm Level"):
        st.session_state.level = ["🔵 Easy", "🟠 Moderate", "🔴 Hard", "⚫ Extremely Hard"].index(level) + 1
        st.session_state.level_selected = True
        st.rerun()
else:
    level = st.session_state.level

    if "tasks" not in st.session_state or st.session_state.level != level:
        st.session_state.tasks, st.session_state.dependencies = generate_riddle_tasks(level)
        st.session_state.correct_time, st.session_state.critical_path = calculate_critical_path(
            st.session_state.tasks, st.session_state.dependencies
        )
        st.session_state.game_over = False

    st.write("### Task Descriptions")
    for task, (desc, duration) in st.session_state.tasks.items():
        st.write(f"{task}:** {desc} (Duration: {duration} days)")
    
    st.write("### Project Dependency Graph")
    show_graph(st.session_state.tasks, st.session_state.dependencies)
    
    guess = st.number_input("Guess the minimum project completion time (in days):", min_value=1, step=1)
    if st.button("Submit Guess"):
        correct_time = st.session_state.correct_time
        st.session_state.game_over = True
        
        st.write(f"### Correct Time: {correct_time} days")
        st.write(f"Critical Path: {' → '.join(st.session_state.critical_path)}")
        
        if abs(guess - correct_time) == 0:
            st.success(f"🎉 Perfect guess, {st.session_state.name}! Well done! 🎊")
        elif abs(guess - correct_time) <= 2:
            st.success(f"👏 Great job, {st.session_state.name}! You were very close!")
        else:
            st.warning(f"Not quite, {st.session_state.name}. Keep practicing and try again!")
        
        if "leaderboard" not in st.session_state:
            st.session_state.leaderboard = []
        st.session_state.leaderboard.append((st.session_state.name, guess, correct_time))
        
    if "leaderboard" in st.session_state:
        st.write("### Leaderboard")
        for idx, (name, g, c) in enumerate(sorted(st.session_state.leaderboard, key=lambda x: abs(x[1] - x[2]))):
            st.write(f"{idx+1}. {name} - Guessed: {g} days | Correct: {c} days")

    if st.button("Reset Game"):
        st.session_state.level_selected = False
        st.rerun()
