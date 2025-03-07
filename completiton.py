import streamlit as st
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_riddle_tasks(level):
    """Generates a random set of tasks with durations and dependencies in riddle format based on level."""
    task_names = [chr(i) for i in range(65, 91)]  # Generate task names dynamically (A-Z)
    random.shuffle(task_names)
    
    if level == 1:
        num_tasks = random.randint(4, 5)
        max_dependencies = 1
    elif level == 2:
        num_tasks = random.randint(4, 6)
        max_dependencies = random.randint(2, 3)
    elif level == 3:
        num_tasks = random.randint(6, 8)
        max_dependencies = random.randint(1, 2)
    else:
        num_tasks = random.randint(6, 8)
        max_dependencies = random.randint(3, num_tasks - 1)
    
    tasks = {}
    dependencies = {task_names[i]: [] for i in range(num_tasks)}
    riddle_statements = []
    
    for i in range(num_tasks):
        task = task_names[i]
        duration = random.randint(3 + level, 6 + level * 2)
        tasks[task] = (duration, [])
        
        if i > 0:
            num_dependencies = random.randint(1, min(i, max_dependencies))
            dependencies[task] = random.sample(task_names[:i], num_dependencies)
            
            for dep in dependencies[task]:
                riddle_statements.append(f"Before you start **Task {task}**, make sure **Task {dep}** is finished!")
    
    return tasks, dependencies, riddle_statements

def calculate_critical_path(tasks, dependencies):
    G = nx.DiGraph()
    for task, (duration, _) in tasks.items():
        G.add_node(task, duration=duration)
    for task, deps in dependencies.items():
        for dep in deps:
            G.add_edge(dep, task)
    
    longest_path = nx.dag_longest_path(G)
    total_time = sum(tasks[task][0] for task in longest_path)
    return total_time, longest_path

def show_graph(tasks, dependencies):
    G = nx.DiGraph()
    for task, (duration, _) in tasks.items():
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
        st.session_state.tasks, st.session_state.dependencies, st.session_state.riddle_statements = generate_riddle_tasks(level)
        st.session_state.correct_time, st.session_state.critical_path = calculate_critical_path(
            st.session_state.tasks, st.session_state.dependencies
        )
        st.session_state.game_over = False
        st.session_state.show_graph = True
    
    st.write("### Task Dependency Riddles")
    for riddle in st.session_state.riddle_statements:
        st.write(f"🔹 {riddle}")
    
    if st.session_state.show_graph:
        st.write("### Project Dependency Graph")
        show_graph(st.session_state.tasks, st.session_state.dependencies)
    
    guess = st.number_input("Guess the least time needed to complete the project (in days):", min_value=1, step=1)
    if st.button("Submit Guess"):
        correct_time = st.session_state.correct_time
        st.session_state.game_over = True
        
        st.write(f"### Correct Time: {correct_time} days")
        st.write(f"Critical Path: {' → '.join(st.session_state.critical_path)}")
        
        if abs(guess - correct_time) == 0:
            st.success(f"🎉 Perfect guess, {st.session_state.name}! Congratulations! 🎊")
            st.image("https://media.giphy.com/media/3o7TKsQYAVjXyG3hXa/giphy.gif")
        elif abs(guess - correct_time) <= 2:
            st.success(f"👏 Great guess, {st.session_state.name}! You were very close!")
        else:
            st.warning(f"Not quite, {st.session_state.name}! Try again next time.")
        
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
