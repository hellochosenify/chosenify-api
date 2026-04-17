# Chosenify – Codex Agent Rules

## System Overview
- Backend: FastAPI
- Endpoint: /submit-test
- Input: answers (List[int])
- Output:
  {
    "scores": {...},
    "top_trait": "...",
    "personality_type": "...",
    "report": "<html>"
  }

---

## Critical Rules (MUST FOLLOW)

- Never break API response format
- Never remove existing fields
- Always return:
  scores, top_trait, personality_type, report

- Always convert answers to int before scoring
- Never add early return statements
- Never leave unreachable code

---

## Scoring Logic Rules

- Scores are calculated from answers
- top_trait = highest score
- personality_type = based on top 2 traits

---

## Report Rules

- Output must be clean HTML (NOT markdown)
- Must include:
  - Overview
  - Top Trait Explanation
  - Strengths
  - Weaknesses
  - Career Matches
  - Growth Plan

---

## Frontend Safety

- Do not modify frontend unless explicitly asked
- Do not assume HTML structure exists
- Do not introduce UI-breaking changes

---

## Coding Rules

- Keep functions simple
- No duplicate return statements
- No unnecessary refactoring
- Preserve existing working logic

---

## Behavior Rules

- If unsure → do NOT guess
- Prefer safe modifications
- Maintain backward compatibility

## Frontend Rules (CRITICAL - WordPress + Elementor Environment)

### Environment Constraints
- Frontend runs inside WordPress (Elementor + Astra theme)
- HTML structure is NOT guaranteed
- IDs and classes may NOT exist
- JavaScript is injected via Custom JS plugin

---

### DOM Handling Rules (MANDATORY)

- NEVER assume element IDs exist (e.g., getElementById without fallback)
- ALWAYS use safe selectors:
  - document.querySelector(...) with fallback
  - fallback to document.body if container not found

Example:
const container = document.querySelector("#quiz-container") || document.body;

---

### Rendering Rules

- ALWAYS render content dynamically inside JS
- NEVER rely on pre-existing HTML from Elementor
- ALWAYS overwrite container.innerHTML safely
- Ensure all text is visible (no theme override issues)

---

### Visibility Fix (ASTRA ISSUE)

- ALWAYS enforce readable text:
  - color: #000 for text
  - background: #fff where needed

- NEVER rely on theme styles for visibility

---

### Data Safety Rules

- NEVER assume API response fields exist
- ALWAYS use fallback values

Example:
scores.Social ?? 0

- Prevent "undefined" in UI at all costs

---

### Event Handling Rules

- DO NOT rely on specific button IDs
- Use generic selectors:

Example:
const startBtn = document.querySelector("button");

- ALWAYS attach event listeners after rendering

---

### API Handling Rules

- Always validate API response before rendering
- Log response for debugging:
  console.log(data)

- If response missing → show safe fallback UI

---

### Forbidden Actions

- Do NOT modify frontend structure unless explicitly asked
- Do NOT introduce complex frameworks (React, Vue)
- Do NOT assume stable DOM
- Do NOT break report rendering

---

### Coding Style (Frontend)

- Use defensive programming ONLY
- Prefer simple JS (no advanced patterns)
- Keep logic inside single script
- Avoid global errors (no undefined variables)

---

### Goal

Frontend must:
- ALWAYS render questions
- NEVER show undefined values
- NEVER break on missing elements
- ALWAYS display report correctly