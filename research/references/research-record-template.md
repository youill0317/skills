# Research Record Template

Use this optional scaffold when a research run needs a durable Markdown record.
The governing contract is still `../SKILL.md`: maximum-saturation research, no
quick/deep/lightweight modes, inspected evidence only, and exactly one Markdown
research record as the deliverable.

This template is deliberately compact. Add detail only when it improves
verification, traceability, or decision quality.

## File Shape

Prefer a workspace-local path such as:

```text
research/<NNN-topic>.md
```

Use one Markdown record for one research request. Do not create separate
Markdown notes such as `brief.md`, `sources.md`, `claims.md`, or per-lane
research deliverables. Temporary downloaded or extracted evidence artifacts are
allowed when tools require them; summarize their stable locators and relevance
inside the record.

## Template

```markdown
# Research: <Topic>

Date: YYYY-MM-DD
As of: YYYY-MM-DD HH:MM timezone, when currentness matters
User request: <verbatim or concise restatement>
Scope: <jurisdiction, population, version, language, timeframe, exclusions>
Status: saturated / saturated with blocked gaps / insufficient

## Answer

State the answer, recommendation, comparison, or evidence-backed synthesis.
Keep firm claims limited to what the claim ledger supports.

## Scope And Success Criteria

- Research question:
- Intended use or decision:
- Included:
- Excluded:
- Entity, term, jurisdiction, and language assumptions:
- Evidence rules:
- Success criteria:

## Search Plan And Coverage

Summarize the evidence routes actually used. Lanes are source or claim routes,
not modes.

| Lane | Evidence Need | Source Families / Tools | Search Or Retrieval Path | Status | Notes |
|---|---|---|---|---|---|
| L1 | authoritative record / empirical data / counterevidence / currentness / provenance / comparison | official, scholarly, dataset, legal, market, archive, local file, connector, repository, etc. | queries, domains, files, connectors, APIs, archives, or local paths | searched / blocked / not applicable | effect on confidence |

## Sources And Observations

Assign source IDs only after inspecting the source body or retrieved connector
record. Snippets, AI summaries, and subagent conclusions are leads, not
evidence.

| Source ID | Source / Locator | Type | Accessed Evidence Location | Why It Matters | Key Observations |
|---|---|---|---|---|---|
| S1 | title, URL, file path, connector record, dataset, docket, repo, or archive | primary / official / scholarly / dataset / expert / market / community / other | page, section, table, timestamp, line, record ID, commit, or version | supports / contradicts / scopes / updates / contextualizes | concise evidence notes |

## Lead And Gap Log

Track material leads raised by searches and inspected sources. A lead can close
only with a reason.

| Lead ID | Raised From | Lead Or Gap | Action Taken | Outcome | Confidence Effect |
|---|---|---|---|---|---|
| LD1 | S1 / query / connector / prior record | citation, dataset, author, organization, standard, case, release, archive, counterclaim, missing source family | followed / closed / blocked / downgraded | result or reason | none / caveat / downgrade / insufficient |

## Claim Ledger

Every important final claim belongs here before synthesis.

| Claim ID | Claim | Type | Supporting Evidence | Counterevidence / Limits | Currentness / Version | Confidence | Decision |
|---|---|---|---|---|---|---|---|
| C1 | independently checkable claim | factual / current / quantitative / causal / comparative / legal / technical / decision | S1, S2, observations | none found / conflict / method limit / access gap | checked date, version, effective date, or not applicable | high / medium / low / insufficient | use / downgrade / exclude / insufficient |

## Verification And Counterevidence

Record the checks that make the answer trustworthy.

- Primary or authoritative sources checked:
- Independent corroboration:
- Counter-search and disagreement:
- Currentness, version, supersession, or retraction checks:
- Provenance, incentives, funding, authorship, or manipulation risk:
- Quantitative method, denominator, unit, geography, and date checks:
- Comparison criteria, tradeoffs, and sensitivity:
- Absence-claim search boundary, if any:
- Inference boundaries and unsupported possibilities:

## Confidence And Limits

Explain confidence by claim, subquestion, or decision. Tie limits to specific
source gaps, blocked access, thin source families, unresolved leads, or
conflicting evidence.

| Item | Confidence | Why | What Would Change It |
|---|---|---|---|
| C1 / question / recommendation | high / medium / low / insufficient | evidence strength, independence, currentness, method quality, counterevidence, gaps | source, data, access, date, jurisdiction, assumption, or event |

## Refresh Triggers

List events that should cause the record to be revisited:

- New official update, filing, standard, release, advisory, law, regulation, dataset, correction, retraction, litigation, pricing, product change, or material counterevidence.
- Known source family that was blocked or unavailable becomes accessible.
- Date after which currentness-sensitive claims should be refreshed.
```

## Optional Additions

Add a compact decision matrix, comparison table, timeline, source-lineage map,
method appendix, quote-context table, or domain-specific table only when it
materially improves verification or the user's decision. Keep additions inside
the same Markdown record.

Helper scripts are seeds. Use this compact scaffold unless extra sections are
necessary to prove saturation, claim traceability, or decision quality for the
active topic. Validate completed records with:

```bash
python <skill-dir>/scripts/validate_research_record.py <record>
```
