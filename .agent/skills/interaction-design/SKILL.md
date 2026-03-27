---
name: interaction-design
description: Focuses on micro-interactions, state changes, accessibility (WCAG), motion principles, and responsive behavior. Trigger when refining how a UI feels to use, adding animations, handling device breakpoints, or ensuring the interface is usable for all states (hover, focus, error, disabled).
---

# Interaction Design

A skill focused on how a user interface *feels* and behaves, rather than just how it looks statically. Excellent interaction design closes the gap between the user and the digital product.

## 1. Micro-interactions and Motion
Animations should have a purpose: to guide attention, confirm action, or establish spatial relationships.
- Use CSS transitions for state changes (hover, focus, active). A standard duration is `0.2s ease-in-out` for UI elements.
- Avoid motion sickness; keep animations subtle (e.g., slight scaling `transform: scale(1.02)`, subtle opacity changes, or smooth background color transitions).
- Provide feedback for every action (e.g., button click ripple, loading spinner, success toast).

## 2. State Management
A button is never just a button. Always design for the following states:
- **Default (Resting)**
- **Hover** (Visual clue that the element is interactive)
- **Focus** (CRITICAL for keyboard accessibility. Provide a clear `outline: 2px solid var(--focus-color)`).
- **Active / Pressed** (Feedback that the action is occurring)
- **Disabled** (Low opacity, `cursor: not-allowed`)

## 3. Responsive Behavior
- Design fluidly. Use relative units (`rem`, `%`, `vw/vh`, or `clamp()`) instead of fixed pixel widths.
- Ensure touch targets on mobile devices are at least 44x44px.
- Re-architect layouts for mobile rather than just scaling them down (e.g., convert horizontal tabs to a dropdown or accordion on narrow screens).

## 4. Accessibility (A11y) Core Rules
- Ensure High Contrast ratios (at least 4.5:1 for normal text).
- Include `aria-label` or visually hidden text for icon-only buttons.
- Never rely on color alone to convey meaning (e.g., an error input needs a red border AND an error icon or text message).

**Objective**: Make the interface dynamic, robust to edge cases, and a joy to interact with physically.
