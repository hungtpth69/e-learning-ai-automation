---
description: A unified workflow for the UI/UX Expert Agent to take a project from research and visual design straight through to frontend web development and artifact building.
---

# UI/UX to Code Workflow

This is the standard, end-to-end workflow for the **UI/UX Expert Agent**. It bridges the gap between conceptual design and tangible, production-ready frontend code. Whenever tasked with creating a new web interface, component, or full website, follow these phases strictly in order.

## Phase 1: UX Research & Strategy
*Trigger Skill: `ux-research-and-strategy`*

Before writing any code or styling any pixels, you must understand the foundation.
1. **Analyze the Request**: Identify the target audience and the primary goal of the interface.
2. **Define IA (Information Architecture)**: Outline the content structure and hierarchy.
3. **Draft Wireframes/Flows**: Use text or markdown to map out the core user journey (e.g., Hero section -> Features grid -> Call to Action -> Footer).
4. **Checkpoint**: Present this pure logical structure to the user to confirm the flow makes sense before proceeding to visuals.

## Phase 2: Brand Identity & Interaction Design Setup
*Trigger Skills: `brand-identity-design`, `interaction-design`, `brand-guidelines`*

Once the logic is confirmed, establish the visual rules.
1. **Define the Theme**: Establish HSL/Hex color palettes (Primary, Secondary, Background, Semantic) and select a typography scale (Headings vs. Body). *If dealing with corporate brand guidelines, strictly adhere to them here.*
2. **Define Interactions**: Document how elements will behave. What is the hover state for buttons? What is the focus state for inputs? Establish standard animation durations (e.g., `0.2s ease-in-out`).
3. **Generate Tokens**: Output these decisions as CSS Variables (`:root`) or a Tailwind config structure.
4. **Checkpoint**: Share the visual tokens and design choices with the user for aesthetic approval.

## Phase 3: Frontend Development & Execution
*Trigger Skills: `frontend-development`, `frontend-design`, `web-artifacts-builder`*

With the logic and visual rules approved, build the interface.
1. **Scaffold the App/Component**: Set up the fundamental HTML/React/Vue structure mirroring the wireframe from Phase 1.
2. **Apply the Design System**: Inject the CSS variables, layout systems, and typography rules established in Phase 2.
3. **Build the Artifact**: For complex UI (like interactive dashboards or multi-step forms), utilize the `web-artifacts-builder` skills to manage state and complex standard components (like shadcn/ui or specialized Tailwind layouts).
4. **Implement Micro-interactions**: Add the hover, focus, and active states defined previously. Ensure precise padding, margin, and visual hierarchy.

## Phase 4: Rigorous Quality Verification
*Trigger Agent Core Trait: Visually Driven & Pixel Perfect*

Before final delivery, perform a self-audit:
1. **Visual Pass**: Are the colors harmonious? Is the typography scale respected? Is there enough whitespace (padding/margins) to let elements breathe?
2. **Accessibility Pass**: Do buttons have clear states? Is the contrast ratio high enough?
3. **Responsiveness Pass**: Does the layout break gracefully on mobile/tablet widths?

**Final Output**: Deliver the completed code along with a brief explanation of the key design and architectural decisions made.
