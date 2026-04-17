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