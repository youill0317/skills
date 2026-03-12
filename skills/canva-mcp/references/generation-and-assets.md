# Generation And Assets

Load this reference when the task involves `generate-design`, brand kits, uploaded assets, or conversion from candidate output to a real design.

## Brand Kit Rule

- Before `generate-design`, ask whether the user wants an on-brand result.
- If the user says yes, call `list-brand-kits`, show the available kits, and let the user choose one.
- Only pass `brand_kit_id` after the user confirms the selected kit.
- If the connector reports missing brand-kit scopes, tell the user to reconnect the Canva connector with the required permissions.

## Asset Upload Rule

- `generate-design` accepts `asset_ids`, not raw external URLs.
- Upload each user-provided asset first with `upload-asset-from-url`.
- Keep asset order intentional because Canva inserts assets in the order provided.
- For presentations or multi-page outputs, order assets to match the intended slide or page sequence.

## Candidate Lifecycle

1. Call `generate-design` with a detailed brief.
2. Review the returned candidates with the user.
3. Call `create-design-from-candidate` using both `job_id` and `candidate_id`.
4. Use the returned `design_id` for export, comments, folder moves, page operations, or metadata reads.

## Query Writing Standard

- Include all relevant context from prior user messages in every `generate-design` call.
- Prefer explicit audience, goal, tone, style, constraints, and deliverable type over short prompts.
- Ask for more specifics if Canva rejects the query as too generic.

## Presentation Rule

For presentation generation, structure the brief with these sections in order:

1. `Presentation Brief`
2. `Narrative Arc`
3. `Slide Plan`

Inside `Slide Plan`, keep exact slide titles, goals, bullets, visuals, data inputs, speaker notes, optional asset hints, and transitions explicit. This reduces weak, generic slide generation and improves downstream export quality.

## Representative Input Shapes

### Generate A Presentation

```json
{
  "design_type": "presentation",
  "query": "Presentation Brief\n- Title: Q2 Product Review\n- Topic / Scope: Adoption, churn, roadmap\n- Key Messages: Enterprise growth leads; onboarding remains the main friction; roadmap shifts toward admin controls\n- Constraints & Assumptions: 12 slides, executive audience, English\n- Style Guide: Clean editorial layout, restrained brand palette, light background\n\nNarrative Arc\nHook -> performance snapshot -> friction -> root causes -> response plan -> next-quarter asks\n\nSlide Plan\nSlide 1 - \"Q2 In One View\"\nGoal: Summarize the quarter.\nBullets (3-6): Revenue +12%; logo churn flat; enterprise seats +28%.\nVisuals: KPI strip and trend line.\nData/Inputs: Example values allowed.\nSpeaker Notes (2-4 sentences): Explain why enterprise growth matters.\nTransition: Move into the segment mix.",
  "user_intent": "Generate an executive review presentation"
}
```

### Convert Candidate To Design

```json
{
  "job_id": "job_123",
  "candidate_id": "cand_456",
  "user_intent": "Turn the selected generated concept into a real Canva design"
}
```
