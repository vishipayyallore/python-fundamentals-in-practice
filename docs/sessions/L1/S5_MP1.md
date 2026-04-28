---
learning_level: "Noob → Nerd"
prerequisites:
  - "docs/sessions/L1/S1.md"
  - "docs/sessions/L1/S2.md"
  - "docs/sessions/L1/S3.md"
  - "docs/sessions/L1/S4.md"
estimated_time: "30–45 minutes"
session_type: "Project"
learning_objectives:
  - "Build a working CLI calculator that performs basic arithmetic operations"
  - "Validate and convert user input before calculation to avoid type-related failures"
  - "Use if/elif/else branching to select operations and handle divide-by-zero safely"
  - "Run the calculator in a loop until the user chooses to quit"
related_topics:
  prerequisites:
    - "docs/sessions/L1/S1.md"
    - "docs/sessions/L1/S2.md"
    - "docs/sessions/L1/S3.md"
    - "docs/sessions/L1/S4.md"
  builds_upon: []
  enables:
    - "docs/sessions/L1/S6.md"
  cross_refs: []
---

# Mini Project 1: Simple Calculator

**Duration:** 30–45 minutes  
**Type:** 🛠️ Project  
**Level:** Noob → Nerd  
**Session:** MP1

---

## 🎯 Project mission

Build a calculator that does more than print fixed lines: it asks for input, validates it, chooses the correct operation, and handles edge cases safely.

This project is the first "full-flow" integration point for Sessions 1–4:

- **Session 1** gives input/output and script flow
- **Session 2** gives data types and conversion
- **Session 3** gives arithmetic operators
- **Session 4** gives branching with `if/elif/else`

---

## ✅ Outcomes

By the end of this mini project, you should be able to:

- Build a CLI calculator that supports `+`, `-`, `*`, `/`
- Validate number input before conversion
- Use branching to route operations
- Guard against divide-by-zero
- Explain why validation and branching make the program safer

---

## 📋 Prerequisites / builds-on

Complete these first:

- [S1.md](S1.md)
- [S2.md](S2.md)
- [S3.md](S3.md)
- [S4.md](S4.md)

This project then builds toward:

- [S6.md](S6.md) for loop fluency and control flow extension

---

## 🧪 Practice file mapping

**Project practice folder:** `src/L1/MP1/`

| File | Purpose |
| --- | --- |
| `src/L1/MP1/01_simple_calculator.py` | One-run calculator with operation choice, numeric validation, and divide-by-zero handling |
| `src/L1/MP1/02_simple_calculator_loop.py` | Loop-enabled calculator that repeats until user quits |

---

## 🛠️ Build path

### Step 1: Core one-run calculator

Start with `01_simple_calculator.py`:

1. Ask for operation (`+`, `-`, `*`, `/`)
2. Ask for two numbers
3. Validate that both inputs are numeric text
4. Convert to `float`
5. Use `if/elif/else` to choose operation
6. Handle divide-by-zero explicitly

### Step 2: Loop-enabled calculator

Move to `02_simple_calculator_loop.py`:

1. Wrap calculator logic in a `while` loop
2. Add `q` option to exit cleanly
3. Keep the same validation + operation logic every round
4. Print a clear goodbye message on exit

---

## 🔍 Project acceptance checklist

Use this to verify your implementation:

- [ ] Program supports `+`, `-`, `*`, `/`
- [ ] Invalid operation input is handled clearly
- [ ] Non-numeric input is rejected before conversion
- [ ] Division by zero does not crash the program
- [ ] Loop version exits only when user types `q`
- [ ] Output is readable and beginner-friendly

---

## 🔧 Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `ValueError` on conversion | Input text was not numeric | Validate first, then convert |
| Wrong branch runs | Condition order/logic issue | Re-check `if/elif` flow |
| Crash on division | Denominator is `0` | Add explicit divide-by-zero guard |
| Loop never ends | No `q` check or break path | Add quit condition in loop |

---

## 🧠 Why this project matters

This project is your first full program with clear input → validation → decision → output flow.  
It sets up the same pattern you will reuse in every bigger project.

---

## 📌 Wrap-up

After this project, you can say:

- "I can build a calculator that handles normal and edge cases."
- "I know why input validation matters before doing arithmetic."
- "I can combine operators and conditionals in one complete script."

Next: strengthen loop thinking in [S6.md](S6.md), then apply the same pattern to future mini projects.
