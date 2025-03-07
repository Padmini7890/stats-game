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
        max_dependencies = 1  # Ensuring at least one interlink or two-way task
    elif level == 2:
        num_tasks = random.randint(4, 6)
        max_dependencies = random.randint(2, 3)  # More interlinks
    elif level == 3:
        num_tasks = random.randint(6, 8)
        max_dependencies = random.randint(1, 2)  # Some interlinks
    else:  # Extremely Hard Level
        num_tasks = random.randint(6, 8)
        max_dependencies = random.randint(3, num_tasks - 1)  # Higher interlinks
    
    tasks = {}
    dependencies = {task_names[i]: [] for i in range(num_tasks)}
    
    for i in range(num_tasks):
        task = task_names[i]
        description = f"Task {task} must be completed under certain conditions."
        duration = random.randint(3 + level, 6 + level * 2)
        tasks[task] = (description, duration)
        
        if i > 0:
            num_dependencies = random.randint(1, min(i, max_dependencies))
            dependencies[task] = random.sample(task_names[:i], num_dependencies)
    
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
    
    # Compute Earliest Start and Latest Finish Times
    earliest_start = {node: 0 for node in G.nodes()}
    for node in nx.topological_sort(G):
        for successor in G.successors(node):
            earliest_start[successor] = max(earliest_start[successor], earliest_start[node] + tasks[node][1])
    
    latest_finish = {node: total_time for node in G.nodes()}
    for node in reversed(list(nx.topological_sort(G))):
        for predecessor in G.predecessors(node):
            latest_finish[predecessor] = min(latest_finish[predecessor], latest_finish[node] - tasks[predecessor][1])
    
    return total_time, longest_path, earliest_start, latest_finish

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

# Select level
if "level_selected" not in st.session_state:
    st.session_state.level_selected = False

if not st.session_state.level_selected:
    level = st.radio("Select Level:", [1, 2, 3, 4])
    if st.button("Confirm Level"):
        st.session_state.level = level
        st.session_state.level_selected = True
        st.rerun()
else:
    level = st.session_state.level

    if "tasks" not in st.session_state or st.session_state.level != level:
        st.session_state.tasks, st.session_state.dependencies = generate_riddle_tasks(level)
        st.session_state.correct_time, st.session_state.critical_path, st.session_state.earliest_start, st.session_state.latest_finish = calculate_critical_path(
            st.session_state.tasks, st.session_state.dependencies
        )
        st.session_state.game_over = False
        st.session_state.show_graph = True

    st.write("### Task Descriptions (Solve the Riddles!)")
    for task, (desc, duration) in st.session_state.tasks.items():
        st.write(f"**{task}:** {desc}")

    if st.session_state.show_graph:
        st.write("### Project Dependency Graph")
        show_graph(st.session_state.tasks, st.session_state.dependencies)

    guess = st.number_input("Guess the least time needed to complete the project (in days):", min_value=1, step=1)
    if st.button("Submit Guess"):
        correct_time = st.session_state.correct_time
        st.session_state.game_over = True
        
        st.write(f"### Correct Time: {correct_time} days")
        st.write(f"Critical Path: {' → '.join(st.session_state.critical_path)}")
        
        st.write("### Solution Explanation")
        for task in st.session_state.critical_path:
            st.write(f"**Task {task}:** Duration = {st.session_state.tasks[task][1]} days, Earliest Start = {st.session_state.earliest_start[task]} days, Latest Finish = {st.session_state.latest_finish[task]} days")
        
        if abs(guess - correct_time) == 0:
            st.success("🎉 Perfect guess! Congratulations! 🎊")
            st.image("https://media.giphy.com/media/3o7TKsQYAVjXyG3hXa/giphy.gif")
        elif abs(guess - correct_time) <= 2:
            st.success("👏 Great guess! You were very close!")
        else:
            st.warning("Not quite! Try again next time.")
        
        if "leaderboard" not in st.session_state:
            st.session_state.leaderboard = []
        st.session_state.leaderboard.append((guess, correct_time))
        
    if "leaderboard" in st.session_state:
        st.write("### Leaderboard")
        for idx, (g, c) in enumerate(sorted(st.session_state.leaderboard, key=lambda x: abs(x[0] - x[1]))):
            st.write(f"{idx+1}. Guessed: {g} days | Correct: {c} days")

    if st.button("Reset Game"):
        st.session_state.level_selected = False
        st.session_state.tasks, st.session_state.dependencies = generate_riddle_tasks(st.session_state.level)
        st.session_state.correct_time, st.session_state.critical_path, st.session_state.earliest_start, st.session_state.latest_finish = calculate_critical_path(
            st.session_state.tasks, st.session_state.dependencies
        )
        st.session_state.game_over = False
        st.session_state.show_graph = True
        st.rerun()
