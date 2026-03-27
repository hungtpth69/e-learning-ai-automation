---
name: Agentic AI Architecture & Orchestration
description: Guidelines and frameworks for designing, implementing, and managing Agentic AI systems, LLM orchestration, and multi-agent workflows.
version: 1.0.0
---

# IDENTITY & PURPOSE
This skill provides advanced knowledge and theoretical foundations in **Agentic AI Architecture**. It enables the evaluation and design of systems where Large Language Models (LLMs) operate autonomously or semi-autonomously using tools, memories, and multi-agent coordination.

# CORE DIRECTIVES
1. **Agentic Autonomy Verification:** ALWAYS ensure that any agentic system has strict guardrails, capability boundaries, and fallback mechanisms when API tools fail.
2. **Deterministic over Probabilistic Outputs:** MUST prefer deterministic execution (code, strict schema validation) when managing critical workflows, rather than relying solely on LLM text generation.
3. **Context Window Management:** ALWAYS design architectures that optimize context length (using RAG, summarization, or vector databases) to reduce costs and hallucinations.
4. **Tool Use Paradigm:** MUST enforce the principle of least privilege for the tools exposed to the agent.

# EXECUTION WORKFLOW
Whenever asked to design or review an Agentic AI feature, you MUST follow these steps:
1. **Capability Assessment:** Determine if a traditional rule-based system is sufficient before opting for an Agentic AI solution.
2. **LLM Orchestration Strategy:** Decide between a single-agent with multiple tools vs. multi-agent orchestration (e.g., CrewAI, LangGraph, AutoGen paradigms).
3. **Memory & State Design:** Architect how the agent maintains short-term (conversation) and long-term (vector DB) state.
4. **Guardrail Implementation:** Define explicit evaluation and validation paths for LLM output before executing actions.

# CONSTRAINTS
- **NEVER** expose destructive APIs (like database drops or uncontrolled cloud resource creation) directly to an autonomous agent without a "Human-in-the-loop" approval step.
- **ALWAYS** decouple the core business logic from the LLM prompts.

# RESOURCES
When needed, use the `view_file` tool to reference the template:
- `../../skills/agentic_ai/resources/agentic_design_template.md`: Template for designing a new Agentic feature.
