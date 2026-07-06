# Subagent Orchestration

Use this only when subagents or sequential lane prompts would materially improve
coverage. The main agent owns the single Markdown record.

## Rules

- Subagents return message text only: inspected sources, observations, leads,
  claim checks, and gaps.
- Subagents do not create, edit, move, or delete research records.
- Give each lane concrete ownership: source family, claim set, jurisdiction,
  product/version, dataset, counterevidence path, or provenance path.
- Ask every lane to return leads and confidence limits, not just conclusions.
- Treat subagent summaries as leads until the main agent inspects or verifies
  the underlying sources.

## Lane Prompt Shape

```text
Research lane: <lane ownership>
Question: <research question>
Scope: <scope assumptions>
Find and inspect the strongest sources you can access for this lane.
Return:
- sources inspected with locators
- key observations
- leads to follow
- counterevidence or gaps
- claim-level confidence and limits
Do not write files.
```

If subagents are unavailable, run the same lanes sequentially and record the
fallback in the research record.
