---
name: brand-identity-design
description: Instructions for establishing a cohesive brand vision, including color theory, typography scales, layout systems, and visual consistency. Use this skill when asked to define a brand's look and feel, create a design system, select color palettes, or set up global styling tokens.
---

# Brand Identity Design

A skill dedicated to crafting a cohesive, memorable, and visually stunning brand identity system.

## 1. Color Theory and Application
Do not use generic colors (e.g., "blue" or "red"). Define precise, harmonious palettes using HSL or Hex values.
- **Primary Color**: The core brand color. Use it for primary actions (buttons, active states).
- **Secondary/Accent**: For highlights, badges, or secondary actions. Must contrast well with the primary.
- **Semantic Colors**: Success (Green), Warning (Yellow/Orange), Error (Red), Info (Blue) - tuned to match the brand's aesthetic.
- **Backgrounds & Surfaces**: Define shades for elevated surfaces (cards, modals) to create depth without relying solely on heavy shadows.

## 2. Typography
Typography is 90% of web design.
- **Font Pairing**: Suggest 1-2 font families maximum (e.g., a Sans-Serif like Inter for UI, and a Serif/Display font for headers).
- **Type Scale**: Establish a clear hierarchy (e.g., h1: 3rem, h2: 2rem, body: 1rem, small/meta: 0.875rem).
- Always specify font weights (e.g., 400 for body, 600/700 for headings) and generous line heights (1.5 - 1.6 for readability).

## 3. Spacing and Layout Systems
- Use a consistent spacing scale, usually based on an 8px or 4px grid (e.g., 8px, 16px, 24px, 32px, 48px).
- Apply whitespace generously to group related elements and separate distinct sections.

## Output Structure
When presenting a brand identity system, output CSS variables or a structured token list:
```css
/* Example Token System */
:root {
  /* Colors */
  --brand-primary: #4F46E5;
  --bg-surface: #FAFAFA;
  
  /* Typography */
  --font-display: 'Outfit', sans-serif;
  --font-body: 'Inter', sans-serif;
  
  /* Scale */
  --text-base: 16px;
  --spacing-md: 1.5rem;
}
```
**Goal**: The brand system should feel premium, deliberate, and highly curated.
