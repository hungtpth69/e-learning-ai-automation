# Agentic System Design Template

Use this template to formalize the architecture of a new Agentic AI Workflow or System.

## 1. Objective & Scope
- **Goal:** What autonomous or semi-autonomous task is the agent performing?
- **LLM Independence:** Does it require continuous prompts, or can it run in the background?

## 2. Orchestration Pattern
- [ ] Single Agent with Tools
- [ ] Multi-Agent Sequential Workflow
- [ ] Multi-Agent Hierarchical Workflow
- [ ] Evaluator-Optimizer Pattern

## 3. Tooling & Capabilities
- What tools (APIs, Functions, CLI) will be exposed to the Agent?
- What are the authorization boundaries for these tools?

## 4. Memory & Context
- **Short-Term Context:** How is the chat/action history managed (sliding window, summarization)?
- **Long-Term Memory:** Is RAG or a Vector DB required? If so, what is the embedding strategy?

## 5. Security & Guardrails
- **Human-in-the-loop (HITL):** Which actions require explicit user approval?
- **Output Validation:** How are hallucinations or malformed JSON responses handled?
- **Cost Controls:** What are the token limits or budget constraints per execution?
