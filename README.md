# 🤖 Assignment: Reflex Vacuum Agent (Figure 2.8)

In this assignment, you will implement the **Reflex-Vacuum-Agent** algorithm described in the textbook (*Artificial Intelligence: A Modern Approach, 4th Edition*).

## 📖 Reference Material
You can view the logic for this agent here:
*   **[AIMA Figure 2.8 Pseudocode (PDF)](https://aima.cs.berkeley.edu/figures.pdf)**
    *   *Note: Open the PDF and scroll to **page 7** to find the Reflex-Vacuum-Agent logic.*

---

## 📋 Your Task
1. **Open** `agent.py`.
2. **Implement** the logic for `ReflexVacuumAgent(percept)` based on the rules in Figure 2.8:
   - If status is **Dirty**, return **'Suck'**.
   - If location is **A**, return **'Right'**.
   - If location is **B**, return **'Left'**.

---

## 🛠 Command Line Workflow

### 1. Clone & Navigate
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Test Locally
Run the provided test script to check your logic:
```bash
python3 test_agent.py
```

### 3. Submit
```bash
git add agent.py
git commit -m "Completed Figure 2.8"
git push origin ch2-agent
```

---

## ✅ Submission Checklist
- [ ] `test_agent.py` passes with a green checkmark.
- [ ] Changes are pushed to the `ch2-agent` branch.
- [ ] The `agent.py` file on GitHub contains your implementation.
