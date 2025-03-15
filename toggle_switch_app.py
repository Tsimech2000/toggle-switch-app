import streamlit as st
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the toggle switch model
def toggle_switch(y, t, alpha1, alpha2, beta, gamma):
    u, v = y
    du_dt = alpha1 / (1 + v**beta) - u
    dv_dt = alpha2 / (1 + u**gamma) - v
    return [du_dt, dv_dt]

# Streamlit App
st.title("Synthetic Genetic Toggle Switch Simulator")

# Sidebar for user inputs
st.sidebar.header("Set Parameters")
alpha1 = st.sidebar.slider("Alpha 1 (Gene A)", 0.1, 20.0, 10.0)
alpha2 = st.sidebar.slider("Alpha 2 (Gene B)", 0.1, 20.0, 10.0)
beta = st.sidebar.slider("Beta (β)", 1, 5, 2)
gamma = st.sidebar.slider("Gamma (γ)", 1, 5, 2)
initial_u = st.sidebar.slider("Initial Protein U", 0.0, 5.0, 0.1)
initial_v = st.sidebar.slider("Initial Protein V", 0.0, 5.0, 0.1)
t_max = st.sidebar.slider("Simulation Time", 10, 100, 50)

# Time points for the simulation
t = np.linspace(0, t_max, 500)

# Solve ODE
solution = odeint(toggle_switch, [initial_u, initial_v], t, args=(alpha1, alpha2, beta, gamma))
u, v = solution[:, 0], solution[:, 1]

# Plotting results
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, u, label='Protein U (Gene A)', linewidth=2)
ax.plot(t, v, label='Protein V (Gene B)', linewidth=2)
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Protein Concentration', fontsize=14)
ax.set_title('Dynamics of Synthetic Genetic Toggle Switch', fontsize=16)
ax.legend()
ax.grid(True)

st.pyplot(fig)

