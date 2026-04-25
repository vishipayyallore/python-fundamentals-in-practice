---
learning_level: "Noob → Nerd"
level_number: 1
prerequisites: []
total_duration: "~5–6 hours"
format: "2 phases × (4 sessions + 1 mini project) = 10 sessions total"
outcome: "2 Mini Projects to cement your foundation"
transformation_focus: "Evolving mindset from complete beginner to someone genuinely curious about programming"
learning_objectives:
  - "Set up Python environment confidently"
  - "Write & run first Python scripts"
  - "Use built-in functions effectively"
  - "Work with variables, operators, and conditionals"
  - "Control program flow with loops"
  - "Debug errors using messages and print statements"
  - "Store/manipulate data using lists & dictionaries"
  - "Apply basic testing with asserts"
  - "Complete 2 mini projects showing your skills"
  - "Be ready for Level 2: Nerd → Novice"
related_topics:
  prerequisites: []
  builds_upon: []
  enables: []
  cross_refs: []
sessions:
  - session: 1
    topic: "Python Introduction, Environment & Built-in Functions"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L1/01_S1.md"
  - session: 2
    topic: "Variables & Data Types"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L1/02_S2.md"
  - session: 3
    topic: "Operators & Expressions"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L1/03_S3.md"
  - session: 4
    topic: "Conditionals, Indentation & Introduction to Modules"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L1/04_S4.md"
  - session: "MP1"
    topic: "Mini Project 1: Simple Calculator"
    duration: "30–45 min"
    type: "Project"
    status: "Ready"
    file: "docs/sessions/L1/05_MP1.md"
  - session: 5
    topic: "Loops & Iteration"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L1/06_S5.md"
  - session: 6
    topic: "Basic Debugging, Reading Errors & Built-in Functions"
    duration: "30 min"
    type: "Knowledge"
    status: "Planned"
    file: "docs/sessions/L1/07_S6.md"
  - session: 7
    topic: "Lists & Loops"
    duration: "30 min"
    type: "Knowledge"
    status: "Planned"
    file: "docs/sessions/L1/08_S7.md"
  - session: 8
    topic: "Dictionaries & Basic Testing"
    duration: "30 min"
    type: "Knowledge"
    status: "Planned"
    file: "docs/sessions/L1/09_S8.md"
  - session: "MP2"
    topic: "Mini Project 2: Personal Profile Generator"
    duration: "30–45 min"
    type: "Project"
    status: "Planned"
    file: "docs/sessions/L1/10_MP2.md"
---

# 🐍 Level 1: Noob → Nerd - Python Fundamentals

## From clueless to curious: Your first exposure to Python programming

> 1. **Level:** Noob → Nerd *(first exposure, installing Python, printing output)*
> 1. **Format:** 2 phases × (4 sessions + 1 mini project) = 10 sessions total
> 1. **Outcome:** 2 Mini Projects to cement your foundation  
> 1. **Total Duration:** ~5–6 hours (8 × 30 min + 2 × 30–45 min)

## Powered by ShyvnTech & Swamy's Tech Skills Academy

> **Transformation Focus**: This isn't just about learning Python syntax - it's about evolving your mindset from complete beginner to someone genuinely curious about programming. Each session builds confidence and practical skills.

---

## 🎯 **Level 1 Learning Path (Noob → Nerd)**

| Phase | Session | Topic                                                  | Duration  | Type         | Status     |
| ----- | ------- | ------------------------------------------------------ | --------- | ------------ | ---------- |
| A     | 1       | Python Introduction, Environment & Built-in Functions  | 30 min    | 📚 Knowledge | ✅ Ready   |
| A     | 2       | Variables & Data Types                                 | 30 min    | 📚 Knowledge | ✅ Ready   |
| A     | 3       | Operators & Expressions                                | 30 min    | 📚 Knowledge | ✅ Ready   |
| A     | 4       | Conditionals, Indentation & Introduction to Modules    | 30 min    | 📚 Knowledge | ✅ Ready   |
| A     | 🚀 MP1  | Mini Project 1: Simple Calculator *(after Session 4)*  | 30–45 min | 🛠️ Project   | ✅ Ready   |
| B     | 5       | Loops & Iteration                                      | 30 min    | 📚 Knowledge | ✅ Ready   |
| B     | 6       | Basic Debugging, Reading Errors & Built-in Functions   | 30 min    | 📚 Knowledge | 🔄 Planned |
| B     | 7       | Lists & Loops                                          | 30 min    | 📚 Knowledge | 🔄 Planned |
| B     | 8       | Dictionaries & Basic Testing                           | 30 min    | 📚 Knowledge | 🔄 Planned |
| B     | 🚀 MP2  | Mini Project 2: Personal Profile Generator *(after 8)* | 30–45 min | 🛠️ Project   | 🔄 Planned |

---

## 🗺️ **Visual Roadmap**

```mermaid
flowchart TB
    A[🎯 Noob] --> PhaseA
    PhaseA --> PhaseB
    PhaseB --> K[🎓 Nerd]

    subgraph PhaseA[📘 Phase A: Core Foundations]
        B1[📚 Session 1<br/>Intro & Environment]
        B2[📚 Session 2<br/>Variables & Data Types]
        B3[🔢 Session 3<br/>Operators & Expressions]
        B4[🤔 Session 4<br/>Conditionals & Modules]
        B5[🚀 MP1<br/>Mini Project 1: Calculator]
        B1 --> B2 --> B3 --> B4 --> B5
    end

    subgraph PhaseB[📘 Phase B: Expanding Skills]
        C1[🔄 Session 5<br/>Loops & Iteration]
        C2[🐛 Session 6<br/>Debugging & Built-ins]
        C3[📋 Session 7<br/>Lists & Loops]
        C4[📚 Session 8<br/>Dicts & Testing]
        C5[🚀 MP2<br/>Mini Project 2: Profile Generator]
        C1 --> C2 --> C3 --> C4 --> C5
    end

    classDef startEnd fill:#e1f5fe,stroke:#01579b,stroke-width:3px,color:#000
    classDef session fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#000
    classDef project fill:#e8f5e8,stroke:#1b5e20,stroke-width:3px,color:#000

    class A,K startEnd
    class B1,B2,B3,B4,C1,C2,C3,C4 session
    class B5,C5 project
```

ASCII fallback:

```text
[🎯 Noob]
    |
    v
[📘 Phase A: Core Foundations]
    ├─ [📚 Session 1: Intro & Environment]
    ├─ [📚 Session 2: Variables & Data Types]
    ├─ [🔢 Session 3: Operators & Expressions]
    ├─ [🤔 Session 4: Conditionals & Modules]
    └─ [🚀 MP1: Mini Project 1: Calculator]
    |
    v
[📘 Phase B: Expanding Skills]
    ├─ [🔄 Session 5: Loops & Iteration]
    ├─ [🐛 Session 6: Debugging & Built-ins]
    ├─ [📋 Session 7: Lists & Loops]
    ├─ [📚 Session 8: Dicts & Testing]
    └─ [🚀 MP2: Mini Project 2: Profile Generator]
    |
    v
[🎓 Nerd]
```

---

## 📅 **Phase A: Core Foundations + Mini Project 1**

### ✅ Session 1: Python Introduction & Environment Setup

* What is Python? History, usage, job market
* Installing Python 3.13+ and VS Code
* Understanding Python execution (PVM explanation)
* Python Interactive Shell (REPL) exploration
* Built-in functions: `print()`, `input()`, `type()`, `help()`, f-strings
* Your first scripts: From "Hello World" to interaction
* Introduction to comments

🧪 *Practice Files*:  
`src/L1/S1/01_hello.py`, `src/L1/S1/02_interactive_hello.py`, `src/L1/S1/bytecode_demo.py`

📖 *Documentation*: [01_S1.md](01_S1.md)

---

### ✅ Session 2: Variables & Data Types

* Variable naming conventions and assignment
* Data types: `int`, `float`, `str`, `bool`
* Dynamic typing, `type()`, `isinstance()`
* Type conversion and casting

🧪 *Practice Files*:  
`src/L1/S2/01_variables.py`, `src/L1/S2/02_data_types.py`, `src/L1/S2/03_type_conversion.py`

📖 *Documentation*: [02_S2.md](02_S2.md)

🧪 *Mini Practice*: Store and display personal details with different data types.  
📌 *Feeds into Mini Project 1*: User input and storage are core to the calculator.

---

### ✅ Session 3: Operators & Expressions

* Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
* Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
* Assignment operators: `=`, `+=`, `-=`, etc.
* Operator precedence and parentheses

🧪 *Practice Files*:  
`src/L1/S3/01_arithmetic.py`, `src/L1/S3/02_comparisons.py`, `src/L1/S3/03_mini_calculator.py`

📖 *Documentation*: [03_S3.md](03_S3.md)

🧪 *Mini Practice*: Build a basic calculator with different operations.  
📌 *Feeds into Mini Project 1*: Calculator logic.

---

### ✅ Session 4: Conditional Statements, Indentation & Modules

* Python indentation rules (why no braces)
* `if`, `elif`, `else` statements
* Boolean logic: `and`, `or`, `not`
* Built-in functions vs modules
* Importing modules (`import`, `from...import`)
* `random` module: random numbers, choices, shuffling

🧪 *Mini Practice*: Build a number guessing game using conditionals + `random`.  
📌 *Feeds into Mini Project 1*: Conditional checks & input handling.

---

### 🚀 Mini Project 1: Simple Calculator *(Ready)*

**Goal:** Build a command-line calculator for basic arithmetic.

**Features:**

* Addition, subtraction, multiplication, division
* User-friendly input handling
* Input validation
* Runs until user quits
* Clean, structured code

🧪 *Practice Pack*: `src/L1/MP1/01_simple_calculator.py`, `src/L1/MP1/02_simple_calculator_loop.py`  
📖 *Project Guide*: [05_MP1.md](05_MP1.md)

🎯 *Stretch Goals*:

* Add power (`**`) and square root
* Add a memory function to store last result

---

## 📅 **Phase B: Expanding Skills + Mini Project 2**

### ✅ Session 5: Loops & Iteration

* `for` loops with `range()` and iterables
* `while` loops and loop conditions
* Loop controls: `break`, `continue`, `pass`
* Nested loops and performance considerations

🧪 *Practice Files*:  
`src/L1/S5/01_for_loops.py`, `src/L1/S5/02_while_loops.py`, `src/L1/S5/03_loop_controls_fizzbuzz.py`

📖 *Documentation*: [06_S5.md](06_S5.md)

🧪 *Mini Practice*: FizzBuzz challenge, countdown timer, pattern printing.  
📌 *Feeds into Mini Project 2*: Looping over profiles.

---

### 🔄 Session 6: Basic Debugging & Built-in Functions *(Planned)*

* Error types: syntax vs runtime
* Reading error messages
* Common beginner mistakes
* Debugging with `print()`
* Built-in functions: `len()`, `max()`, `min()`, `sum()`, `type()`

🧪 *Mini Practice*: Debug broken code samples.  
📌 *Feeds into Mini Project 2*: Debugging profile input.

---

### 🔄 Session 7: Lists & Loops *(Planned)*

* List creation, indexing, slicing, basic methods
* Operations: `append()`, `remove()`, `len()`, accessing elements
* Iteration with lists
* Practical list usage: filtering, modifying, building from user input

🧪 *Mini Practice*: Task list manager with lists + loops.  
📌 *Feeds into Mini Project 2*: Storing multiple hobbies or goals.

---

### 🔄 Session 8: Dictionaries & Basic Testing *(Planned)*

* Dictionaries: creation, update, deletion
* Methods: `.keys()`, `.values()`, `.items()`, `.get()`
* Iterating over dictionaries
* Why testing matters
* Manual testing vs using `assert`

🧪 *Mini Practice*: Student gradebook with dictionaries + asserts.  
📌 *Feeds into Mini Project 2*: User profiles as dictionaries + validation.

---

### 🚀 Mini Project 2: Personal Profile Generator *(Planned)*

**Goal:** Create an interactive profile generator and display system.

**Features:**

* Collect user info (name, age, hobbies, goals)
* Store in dictionaries + lists
* Display formatted profile
* Handle multiple profiles
* Basic input validation

🧪 *Deliverable*: `profile_generator.py`

🎯 *Stretch Goals*:

* Export profile to JSON file
* Allow search/filter by name
* Add “edit profile” option

---

## 🎓 **Level 1 Learning Outcomes**

By completing Level 1, you will:

* ✅ Set up Python environment confidently
* ✅ Write & run first Python scripts
* ✅ Use built-in functions effectively
* ✅ Work with variables, operators, and conditionals
* ✅ Control program flow with loops
* ✅ Debug errors using messages and print statements
* ✅ Store/manipulate data using lists & dictionaries
* ✅ Apply basic testing with asserts
* ✅ Complete 2 mini projects showing your skills
* ✅ Be ready for **Level 2: Nerd → Novice**

---

## 📊 **Assessment Criteria**

* **Phase A**: Can install Python, work with variables, operators, and conditionals → Complete Calculator Project
* **Phase B**: Can debug, work with loops, lists, and dictionaries → Complete Profile Generator Project

**Mini Project Success Indicators:**

* Calculator works with all four operations, validates input, runs continuously.
* Profile generator collects + displays user data, supports multiple profiles, validates inputs.

---

## 🎓 **Next Steps & Resources**

After Level 1, you’re ready to explore:

* Functions & modular programming
* File handling
* Error handling (exceptions)
* Advanced data structures

**Tools Recommended:**

* Python 3.13+
* VS Code with Python extension
* Git for version control
* (Optional) Jupyter Notebook, PyCharm, Replit

---

✨ Happy Coding! 🐍
