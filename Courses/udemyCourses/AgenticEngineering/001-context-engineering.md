# Context Engineering for AI Systems

## Overview

**Context engineering** is the practice of designing, selecting, structuring, and managing the information an AI model receives at each step so that it can reliably perform a task.

A useful distinction is:

> **Prompt engineering = what you tell the model.**  
> **Context engineering = everything you give the model to work with.**

For AI agents, context engineering is often more important than writing a clever prompt.

---

## Simple Example

A naive approach to an investigation assistant might look like:

```text
You are an investigator. Review this SF-86 and identify issues.

[entire SF-86]
```

A context-engineered approach dynamically builds a focused context:

```text
SYSTEM
You are an investigation support assistant.
Do not make investigative decisions. Cite evidence for every finding.

CASE
Case ID: 12345
Investigation type: Clearance Investigation
Status: Initial Review

SUBJECT
Name: John Doe
DOB: ...
Current residence: ...

RELEVANT SF-86 DATA
Section 11 - Where You Have Lived
- 123 Main St, 2021–Present

Section 20 - Foreign Activities
- Foreign contact: Jane Doe
- Relationship: Friend
- Country: ...

CASE HISTORY
- Investigator previously requested clarification regarding foreign contact.
- Subject responded on 2026-09-15.

EVIDENCE
[document excerpts]
[interview transcript]
[email]
[database records]

CURRENT TASK
Determine whether the available evidence contains unresolved
inconsistencies concerning the subject's foreign contacts.

RESPONSE REQUIREMENTS
- Identify relevant evidence.
- Distinguish facts from inference.
- Cite source and location.
- Identify missing information.
- Do not make a final adjudicative determination.
```

This is **context engineering**.

---

# Core Context Engineering Pipeline

A useful architecture looks like:

```text
                 ┌─────────────────┐
                 │   User Request  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Task / Intent   │
                 └────────┬────────┘
                          ↓
        ┌─────────────────┴──────────────────┐
        ↓                                    ↓
┌───────────────┐                    ┌────────────────┐
│ Relevant Data │                    │ Agent State   │
│ SF-86         │                    │ Previous steps│
│ Documents     │                    │ Decisions     │
│ Evidence      │                    │ Pending tasks │
└───────┬───────┘                    └───────┬────────┘
        └────────────────┬───────────────────┘
                         ↓
                ┌──────────────────┐
                │ Context Builder  │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ LLM / Agent      │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Tool Calls       │
                │ Search / DB / RAG│
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Updated Context  │
                └──────────────────┘
```

---

# Major Components

## 1. Context Selection

Determine what information the model actually needs.

Avoid sending an entire case or document when only a small portion is relevant.

```text
500 pages
   ↓
Retrieve relevant evidence
   ↓
12 relevant passages
   ↓
LLM
```

The goal is not to maximize the amount of context.

The goal is to maximize the **relevance and usefulness** of the context.

---

## 2. Context Retrieval

Retrieve relevant information from sources such as:

- Databases
- Vector stores
- Documents
- APIs
- Previous conversations
- Case-management systems
- Knowledge bases
- Search systems
- External tools

This is where **RAG (Retrieval-Augmented Generation)** commonly fits.

```text
User Question
      ↓
Query Construction
      ↓
Retriever
      ↓
Relevant Evidence
      ↓
Context Builder
      ↓
LLM
```

---

## 3. Context Compression

Long conversations and investigations can eventually exceed the useful context window.

Instead of continuously passing the entire history:

```text
100 messages
```

create a structured representation:

```text
Case Summary
+
Important Findings
+
Open Questions
+
Previous Investigator Actions
+
Relevant Evidence
```

Compression should preserve information that is necessary for future reasoning while removing duplication and irrelevant history.

---

## 4. Context Prioritization

Not all information has equal importance.

Example:

```text
HIGH PRIORITY
- Current investigator task
- Relevant evidence
- Recent subject response

MEDIUM PRIORITY
- Case history
- Related SF-86 fields

LOW PRIORITY
- Old conversation
- Unrelated documents
- General case metadata
```

A context builder can use these priorities when the available context is limited.

---

## 5. Context Isolation

Different tasks should receive different context.

For example:

```text
Agent A
Evidence Extraction
        ↓
Agent B
Inconsistency Detection
        ↓
Agent C
Investigator Question Generation
```

Agent C does not necessarily need every raw document Agent A received.

This reduces:

- Context size
- Irrelevant information
- Cognitive noise
- Accidental dependency on unrelated evidence

---

# Context Engineering vs. Related Concepts

| Concept | Main Question |
|---|---|
| Prompt Engineering | How should I instruct the model? |
| RAG | Where do I retrieve relevant information from? |
| Context Engineering | What information should the model receive, when, and in what form? |
| Agent Engineering | How should the system reason, use tools, and take actions? |

A simplified relationship:

```text
                         Agent
                           │
                 ┌─────────┴─────────┐
                 │                   │
              Prompt              Context
                 │                   │
          Instructions       ┌───────┴────────┐
                             │                │
                         Retrieval          State
                             │                │
                            RAG        Conversation / Case
```

---

# Why Context Engineering Matters for AI Agents

A poorly designed agent may repeatedly accumulate information:

```text
User
 ↓
LLM
 ↓
Tool
 ↓
LLM
 ↓
Tool
 ↓
LLM
```

Over time the context can become:

```text
CURRENT TASK
+
old reasoning
+
irrelevant tool results
+
duplicate documents
+
previous mistakes
+
old instructions
+
conversation history
```

More information does not necessarily produce better reasoning.

The effective context can actually become worse.

A better design continuously builds a controlled context:

```text
                    CASE
                      │
          ┌───────────┼────────────┐
          ↓           ↓            ↓
       Current      Relevant     State
        Task        Evidence     Summary
          │           │            │
          └───────────┼────────────┘
                      ↓
              Context Builder
                      ↓
                    LLM
                      ↓
                  Tool Call
                      ↓
             New Evidence
                      ↓
              Context Update
```

---

# Context Engineering for an SF-86 Investigation Platform

For an investigation platform, context engineering should be treated as a first-class architectural component.

```text
                    Investigation Case
                           │
             ┌─────────────┴─────────────┐
             │                           │
       Case Context                 Evidence Store
             │                           │
     ┌───────┼────────┐          ┌───────┼────────┐
     │       │        │          │       │        │
    SF-86  History  Tasks      Docs   Interviews Records
     │       │        │          │       │        │
     └───────┴────────┴──────────┴───────┴────────┘
                           │
                    Context Builder
                           │
                  ┌────────┴────────┐
                  │                 │
             Retrieval          Filtering
                  │                 │
                  └────────┬────────┘
                           ↓
                    LLM / Agent
                           ↓
                    Structured Output
                           ↓
                     Case Timeline
```

---

# Recommended Context Model

A useful context object can be organized into layers:

```json
{
  "task": {
    "type": "investigation_review",
    "instruction": "Identify unresolved inconsistencies"
  },
  "case": {
    "case_id": "12345",
    "status": "initial_review",
    "investigation_type": "clearance"
  },
  "subject": {
    "subject_id": "subject-123"
  },
  "form_context": {
    "sections": []
  },
  "case_state": {
    "open_questions": [],
    "completed_tasks": [],
    "pending_tasks": []
  },
  "evidence": [
    {
      "source_id": "document-123",
      "source_type": "sf86",
      "location": "section-20",
      "content": "...",
      "relevance": 0.94
    }
  ],
  "conversation_summary": {
    "summary": "...",
    "important_decisions": [],
    "unresolved_topics": []
  },
  "constraints": {
    "must_cite_evidence": true,
    "must_distinguish_fact_from_inference": true
  }
}
```

The exact schema should evolve with the application's requirements.

---

# Context Layers

A practical agent can divide context into several layers.

## Layer 1: System Instructions

Stable instructions describing the agent's role and boundaries.

```text
You are an investigation support assistant.

You must:
- Ground findings in evidence.
- Cite sources.
- Distinguish facts from inference.
- Identify uncertainty.
```

## Layer 2: Task Context

Information about what the agent needs to do now.

```text
Current task:
Review foreign-contact information for inconsistencies.
```

## Layer 3: Case Context

Information that defines the current case.

```text
Case:
- Case ID
- Investigation status
- Relevant SF-86 sections
- Open questions
- Previous actions
```

## Layer 4: Evidence Context

The actual evidence relevant to the task.

```text
Evidence:
- SF-86 field
- Interview transcript
- Document
- Email
- Database record
```

## Layer 5: Agent State

Information accumulated during the current workflow.

```text
Completed:
- Reviewed Section 20

Pending:
- Verify date of foreign contact

Open Questions:
- Was the relationship disclosed elsewhere?
```

## Layer 6: Conversation Context

Only the conversation history that is relevant to the current task.

---

# Context Builder

The **Context Builder** is one of the most important components of an agent architecture.

Its job is to transform raw application state into a model-ready context.

```text
                    ┌─────────────────┐
                    │ User Request    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Task Classifier  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Context Builder  │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            ↓                ↓                ↓
       Case Database      RAG/Search      Agent State
            │                │                │
            └────────────────┼────────────────┘
                             ↓
                    ┌─────────────────┐
                    │ Context Filter   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Context Ranker   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Context Compiler │
                    └────────┬────────┘
                             ↓
                           LLM
```

The Context Builder should ideally be deterministic and testable.

---

# Evidence Provenance

For systems that support investigations, context should preserve provenance.

Every important piece of evidence should answer:

- Where did this information come from?
- What document or record contains it?
- What section/page/field contains it?
- When was it retrieved?
- Has the evidence been modified?
- Which agent or user supplied it?
- Which model response relied on it?

Example:

```json
{
  "evidence_id": "ev-123",
  "source_id": "doc-456",
  "source_type": "sf86",
  "location": {
    "section": "20",
    "field": "foreign_contact"
  },
  "content": "Example evidence",
  "retrieved_at": "2026-09-23T14:00:00Z",
  "version": 3
}
```

This enables an important relationship:

```text
LLM Finding
     │
     ├── Evidence A
     │     └── SF-86 Section 20
     │
     ├── Evidence B
     │     └── Interview Transcript, Page 4
     │
     └── Evidence C
           └── Case Document 123
```

The model output can therefore be traced back to the context that supported it.

---

# Context Window Management

Context engineering is not simply about fitting everything into the model's context window.

Consider:

```text
Available Context
        │
        ├── Required
        │
        ├── Relevant
        │
        ├── Optional
        │
        └── Irrelevant
```

A useful strategy is:

```text
1. Identify task
2. Retrieve relevant information
3. Remove duplicates
4. Rank evidence
5. Compress where appropriate
6. Build structured context
7. Send to model
8. Validate output
```

---

# Context Quality

Useful metrics for evaluating context include:

### Relevance

Does the context contain information related to the current task?

### Completeness

Does the model have the information necessary to perform the task?

### Groundedness

Are generated conclusions supported by supplied evidence?

### Freshness

Is the information current?

### Provenance

Can each important claim be traced to its source?

### Noise

How much irrelevant information is included?

### Consistency

Does the context contain conflicting or contradictory information?

### Token Efficiency

How much useful information is delivered per token?

---

# Context Engineering and Agent Traps

Poor context design can contribute to agent traps.

Examples include:

### Context Drift

The agent gradually moves away from the original task.

```text
Original Task
     ↓
Tool Result
     ↓
New Topic
     ↓
Another Tool
     ↓
Context Drift
```

### Context Poisoning

Incorrect or untrusted information gets incorporated into future context.

```text
Bad Data
   ↓
Agent
   ↓
Summary
   ↓
Persistent State
   ↓
Future Agent Calls
```

### Context Bloat

Too much information causes important information to become difficult to identify.

### Instruction Collision

Different pieces of context contain conflicting instructions.

### Stale Context

Previously correct information becomes outdated but remains in the context.

### Recursive Summarization Loss

Repeated summarization gradually removes important details.

A strong context architecture should explicitly mitigate these risks.

---

# Practical Design Principles

## 1. Context should be task-specific

Do not create one enormous context object for every agent action.

Instead:

```text
Task A → Context A
Task B → Context B
Task C → Context C
```

## 2. Separate facts from interpretations

For example:

```text
FACT
The SF-86 lists residence X from 2021–2023.

SOURCE
SF-86 Section 11.

INTERPRETATION
The date range may conflict with another record.

STATUS
Requires investigator review.
```

## 3. Preserve provenance

Never lose the source of important information during summarization or transformation.

## 4. Prefer structured data where possible

Instead of:

```text
"The subject lived in Virginia sometime around 2021..."
```

prefer:

```json
{
  "address": "...",
  "start_date": "2021-01-01",
  "end_date": "2023-05-01",
  "source": "sf86.section11"
}
```

## 5. Treat summaries as derived data

A summary should not silently replace the original evidence.

Maintain:

```text
Original Evidence
       ↓
Derived Summary
       ↓
Agent Context
```

rather than:

```text
Original Evidence
       ↓
Summary
       ↓
Original Evidence deleted
```

## 6. Make context inspectable

For important agent actions, developers should be able to determine:

```text
What did the model receive?
Why did it receive it?
Which retrieval results were selected?
Which information was omitted?
Which tools were called?
```

---

# A Context Engineering Checklist

Before deploying an agent, ask:

### Task

- What exactly is the agent trying to accomplish?
- What information is required?
- What information is optional?

### Retrieval

- Where does relevant information live?
- How is it retrieved?
- How is relevance determined?

### Filtering

- What information should be excluded?
- Are duplicate records removed?
- Is stale information detected?

### State

- What does the agent need to remember?
- What should not persist?
- How is state updated?

### Provenance

- Can every important fact be traced to a source?
- Can the exact context used for an output be reconstructed?

### Safety

- Can untrusted data modify instructions?
- Can retrieved documents contain prompt injection?
- Are tool outputs validated?

### Performance

- How large is the context?
- How many tokens are being used?
- Can context be compressed?
- Is retrieval latency acceptable?

### Evaluation

- Are you measuring retrieval quality?
- Are you testing context completeness?
- Are you testing for irrelevant context?
- Are you testing for stale or conflicting context?

---

# Mental Model

A concise mental model is:

```text
        RIGHT INFORMATION
               +
          RIGHT TIME
               +
         RIGHT STRUCTURE
               +
          RIGHT SOURCE
               +
         RIGHT STATE
               ↓
        USEFUL CONTEXT
               ↓
        BETTER AI OUTPUT
```

The goal is **not** to give the model everything.

The goal is:

> **Give the model the right information, in the right structure, at the right time, with enough provenance to understand and verify it.**

---

# Key Takeaway

Context engineering is the discipline of building the **information environment around an AI model**.

For an agent-based system, it encompasses:

```text
Retrieval
   +
Filtering
   +
Ranking
   +
Compression
   +
Memory
   +
State
   +
Provenance
   +
Task-specific context
   +
Tool results
   +
Validation
```

For an investigation platform, this becomes especially important because the system should be able to explain not only **what the AI generated**, but also **what information the AI was given and which evidence supported the result**.

That makes context engineering a foundational part of building reliable, auditable AI agents—not merely an optimization for prompts.
