# Risks, Guardrails, Evals, and Traps

## Risks of Agent Frameworks

- Unpredictable path
- Unpredictable output
- Unpredictable costs

### Mitigation Strategies:

To mitigate risks associated with agent frameworks, consider the following strategies:

 - **Utilize Guardrails:** Implement guardrails to ensure that your agent operates within safe and predetermined boundaries. These guardrails help prevent unexpected behaviors that could arise from the agent's actions.

- **Monitoring and Observability:** Continuous monitoring of the agent's performance is crucial. Understanding what happens during both development and production helps you identify potential issues early on. Observability facilitates monitoring the system, allowing you to have insights into the agent's operations and outputs.

- **Understand Unpredictability:** One of the primary risks of working with agent frameworks is their unpredictable nature. Outputs can vary each time the system is run, so you must be prepared for these fluctuations in performance and potential costs.

- **Hybrid Approach to Design Patterns:** Consider combining elements of various design patterns. The risks associated with unpredictability may differ across patterns, making it necessary to evaluate and adjust your approach based on the specific implementation.

---
### Agent Trap

> NOTE: This section needs to be moved into its own page:

An agent trap is a situation where an AI agent gets stuck in an unproductive, incorrect, or potentially harmful behavior loop while attempting to complete a task.

This can happen when an AI agent repeatedly takes actions that don't lead to meaningful progress, misinterprets its objectives, or makes decisions based on flawed assumptions.

As AI agents become more autonomous, understanding and mitigating these traps is essential for building reliable AI applications.

#### Below are the two key traps:

1. Solution-Centric Focus: 

when stakeholders become overly focused on the idea of having an agent without clearly defining the specific business problem it’s intended to solve. 

Example: 

User:

> "Help me review an insurance claim form for potential issues."

The agent interprets this as:

> "Find as many potential issues as possible."

It begins flagging minor inconsistencies as serious concerns.

Why It Happens
- Vague objectives.
- Poorly defined success criteria.
- Overly aggressive system prompts.
- Lack of domain-specific constraints.

#### Mitigation

Define explicit objectives and boundaries.

Key principle: An agent should assist with decisions, not silently make decisions that belong to a human.

```
INVESTIGATION_OBJECTIVE = {
    "goal": "Identify discrepancies requiring investigator review",
    "constraints": [
        "Do not make final eligibility determinations",
        "Do not infer undisclosed facts",
        "Distinguish missing information from contradictory information",
        "Cite supporting evidence for every finding"
    ],
    "success_criteria": [
        "All relevant sections reviewed",
        "Potential discrepancies documented",
        "Evidence references included",
        "Uncertainty clearly stated"
    ]
}
```
2. Infinite Loops


Problem: An agent repeatedly performs the same action without making progress.

Example:

Imagine an AI agent responsible for investigating an SF-86 case.
```
Agent: Search for financial discrepancies.
   ↓
Tool: No relevant records found.
   ↓
Agent: Try searching for financial discrepancies again.
   ↓
Tool: No relevant records found.
   ↓
Agent: Try searching for financial discrepancies again.
   ↓
... continues indefinitely
```

Why It Happens
- The agent doesn't recognize that a search has failed.
- There is no limit on the number of attempts.
- The agent's goal is underspecified.
- The agent cannot distinguish between an empty result and a failed request.

