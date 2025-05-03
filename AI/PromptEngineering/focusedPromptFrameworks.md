# Focused Prompt Frameworks for ChatGPT

This guide outlines several focused prompt frameworks you can use with ChatGPT to improve the clarity and usefulness of its responses. These frameworks are especially helpful for beginner engineers learning prompt engineering.

---

## 1. ACT: Agent, Context, Task

**Structure:**

* **Agent**: Define the role of ChatGPT.
* **Context**: Provide background info.
* **Task**: State what you want it to do.

**Example:**

```
Agent: You are a senior React developer.
Context: A junior dev is struggling with understanding useEffect.
Task: Explain useEffect with a simple example and when to use it.
```

---

## 2. RICE: Role, Input, Constraints, Expected Output

**Structure:**

* **Role**: Who the assistant is.
* **Input**: The information it should work with.
* **Constraints**: Any rules (e.g., length, format).
* **Expected Output**: The final result format.

**Example:**

```
Role: You are a technical writer.
Input: An explanation of promises in JavaScript.
Constraints: Keep it under 100 words.
Expected Output: A concise beginner-friendly explanation.
```

---

## 3. COTE: Context, Objective, Task, Examples

**Structure:**

* **Context**: Describe the situation.
* **Objective**: What is the goal?
* **Task**: What do you want the model to do?
* **Examples**: (Optional) Show ideal responses.

**Example:**

```
Context: You're building a prompt library for your engineering team.
Objective: Teach them to write better prompts.
Task: Create 2 example prompts for debugging React.
Examples:
1. "You're a React expert. Help me debug why my useState isn't updating."
2. "Act as a senior dev. Diagnose why my component doesn't re-render after a prop change."
```

---

## 4. ReACT: Reasoning and Acting

**Used in tool-using agents.** Useful when ChatGPT has access to tools like a calculator or search.

**Example:**

```
Task: Find Tesla's Q1 2025 earnings.
Thought: I should look this up.
Action: search["Tesla Q1 2025 earnings"]
Observation: Found on Tesla’s investor page...
```

---

## 5. TAP: Task, Audience, Purpose

**Structure:**

* **Task**: What needs to be done.
* **Audience**: Who it's for.
* **Purpose**: Why you're doing it.

**Example:**

```
Task: Write a project update.
Audience: Product stakeholders.
Purpose: To summarize progress and next steps.
```

---

## 6. Prompt Sandwich

**Structure:**

* **Instruction → Input → Reminder**

**Example:**

```
Instruction: Write a polite decline email.
Input: I got a freelance offer, but accepted a full-time job.
Reminder: Keep it appreciative and professional.
```

---

## Tips for Beginner Engineers

* Be **clear** and **explicit** about what you want.
* Start with a **role** and **task** to guide ChatGPT.
* Include **constraints** to control output length and style.
* Use **examples** when possible to show the format you want.
* Break down large tasks into **step-by-step** instructions.

---

By using these frameworks, you'll get more reliable and helpful results from ChatGPT. Practice by creating your own prompts using the structures above!
