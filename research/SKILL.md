---
name: research
description: >-
  Maximum-saturation evidence research for explicit research-grade requests,
  including Korean-language research requests, deep research, literature
  review, evidence review, market/vendor/competitive scans,
  diligence, policy/regulatory/legal review, OSINT/source verification,
  scholarly search, and decision-support research. Always run the strongest
  available research protocol with no quick/deep/lightweight modes: exhaust
  authorized source families, inspect source bodies, expand leads,
  counter-search, verify claims, and produce one evidence-backed Markdown
  research record.
---

# Research

This skill has one behavior: maximum-saturation research. Do not offer, infer, or follow quick/deep/lightweight modes. Do not ask the user to choose depth. Once this skill is triggered, use the strongest authorized research protocol available and continue until the stop rule is satisfied or an external limit must be recorded as a gap.

## Product Contract

Produce exactly one Markdown research record as the durable deliverable. A concise final chat response may point to the record and summarize the outcome, but the record is the source of truth.

Maximum-saturation means:

- Search across every authorized source family that could materially change the answer.
- Inspect source bodies or connector records before using them as evidence.
- Treat search snippets, AI summaries, citations found in other summaries, and subagent conclusions as leads only.
- Expand useful leads through citations, references, named entities, datasets, authors, organizations, filings, standards, cases, archive captures, and contrary terms.
- Counter-search for disagreement, negative evidence, supersession, retractions, incentives, and currentness.
- Verify every important claim before final synthesis.

If the user's scope is ambiguous but a reasonable maximum-saturation scope is available, proceed and state the scope assumption in the record. Ask a narrow clarifying question only when materially different scopes would require different evidence families or produce incompatible records.

## Outcome First

Before broad search, write or establish the record header with:

- The exact research question and intended decision or use.
- Scope assumptions, exclusions, jurisdiction, language, entity disambiguation, and date/currentness requirements.
- Success criteria for what the record must settle.
- Evidence rules for the topic, including what counts as primary, authoritative, independent, or weak evidence.
- Tool and access boundaries.
- The planned record path, preferably `research/<NNN-topic>.md` or another workspace-local path that does not conflict with existing files.

Keep process notes inside the record. Do not create multiple Markdown research deliverables for one request.

## Research Execution

Drive the available tools hard, but let the evidence question control the sequence.

1. Frame the evidence needs and source families: primary sources, scholarly work, official records, standards, legal/regulatory materials, datasets, market or vendor materials, news, expert commentary, community signals, archives, local files, connectors, and prior records as appropriate.
2. Build a lane plan and query/source matrix. Lanes are evidence routes, not modes.
3. Batch independent searches and retrievals where the tools allow it. Parallelize independent lanes or subagents when available and useful; keep dependent verification steps sequential.
4. Run a scout pass to map terminology, entities, source families, and obvious conflicts.
5. Retrieve and inspect the strongest target sources directly.
6. Snowball from each useful source: references, citations, authors, organizations, datasets, cases, releases, standards, issues, and archives.
7. Run counter-searches for disagreement, failures, criticism, retractions, supersession, incentives, and source manipulation.
8. Revisit the lane plan as new leads appear. Close, block, downgrade, or follow every material lead.
9. Verify and synthesize only after the claim ledger has enough inspected evidence.

Use local repository files, PDFs, office documents, Google/Gmail/Calendar/Drive connectors, GitHub, browser state, archives, specialist search, finance/weather/sports/time tools, or other available sources when they are materially relevant and authorized. Prior research records may orient the search, but refresh their underlying sources before relying on them.

## Evidence Rules

An important claim is any factual, comparative, causal, quantitative, legal/regulatory, technical, current, high-stakes, or decision-relevant statement that the final answer depends on.

For important claims:

- Cite only sources whose body or connector record was inspected.
- Prefer primary and authoritative sources, then independent corroboration, then expert synthesis. Label weaker evidence.
- For current-dependent claims, check latest status, effective dates, version history, supersession, and recently conflicting sources.
- For quantitative claims, record numerator/denominator, unit, method, date range, geography, source vintage, and comparability limits where available.
- For causal or evaluative claims, separate direct evidence from inference and explain the inference boundary.
- For comparisons and recommendations, define criteria, options, evidence by option, missing data, tradeoffs, and sensitivity to assumptions.
- For absence claims, state the searched boundary: source families, terms, languages, dates, jurisdictions, and access limits.
- For provenance-sensitive claims, examine incentives, authorship, funding, publication venue, source lineage, manipulation risk, and independent corroboration.

The final synthesis must make it clear which claims are well-supported, contested, uncertain, outdated, or unsupported.

## Record Shape

Use a compact structure unless the topic demands more:

- `Answer`
- `Scope And Success Criteria`
- `Search Plan And Coverage`
- `Sources And Observations`
- `Lead And Gap Log`
- `Claim Ledger`
- `Verification And Counterevidence`
- `Confidence And Limits`
- `Refresh Triggers`

Add domain-specific sections only when they materially improve verification or decision quality. Do not let formatting, tables, or boilerplate displace source inspection, lead expansion, or claim verification.

Temporary extraction files, downloaded source artifacts, or non-Markdown evidence files are allowed when tools require them, but they are not separate research deliverables. Summarize their evidence and stable locators in the single Markdown record.

## Stop Rule

Stop only when all of these are true:

- Every important claim is represented in the claim ledger with inspected supporting evidence or is explicitly marked insufficient.
- The strongest reachable source families for the question have been searched.
- Material leads from useful sources are followed, closed, blocked by access, or downgraded with a reason.
- Counterevidence, disagreement, currentness, provenance, and source incentives have been checked where material.
- Remaining uncertainty is stated as a limit rather than hidden in confident prose.
- Further authorized search is unlikely to change the main answer, confidence, or decision.

Continue researching when primary sources are missing, source-family coverage is thin, material leads remain open, currentness is unresolved, conflicting evidence is unexplained, or the final answer would depend on unverified claims.

Tool, time, access, or context limits do not authorize a weaker research mode. If a limit prevents saturation, record the limit, identify what remains unresolved, and calibrate confidence.

## Verification Loop

Before finalizing the record, audit it against these checks:

- Does it answer the user's exact research question and stated use?
- Are scope assumptions and exclusions visible?
- Are all important claims traceable to inspected sources or marked insufficient?
- Did the search include primary/authoritative sources, independent corroboration, and counterevidence where available?
- Are currentness, version, jurisdiction, and entity disambiguation handled?
- Are quantitative and comparative claims normalized enough to compare?
- Are source incentives, provenance, and manipulation risks addressed where material?
- Are unresolved gaps explicit and tied to confidence?
- Is there exactly one Markdown research record?

Fix the record before final response if any check fails.

## References

Load extra references only when they materially help the active research task. The instructions in this `SKILL.md` govern if a reference or helper script is stale, narrower, or more format-heavy.

- `references/evidence-needs-core.md`: evidence-family selection and topic framing.
- `references/research-process.md`: extra process detail when the compact contract is not enough.
- `references/query-and-source-patterns.md`: query construction, source discovery, and snowballing patterns.
- `references/source-verification.md`: high-stakes, current, conflicting, provenance-sensitive, translated, or manipulated-source checks.
- `references/subagent-orchestration.md`: parallel lane prompts and synthesis handoff when subagents are useful.
- `references/web-search-harness-maximization.md`: web/search/browser/archive/source-open maximization.
- `references/research-record-template.md`: optional scaffold for complex records; adapt it to the compact record shape above.

Helper scripts may seed a record, query plan, or audit, but their output is not the contract. When validating a record, prefer `scripts/validate_research_record.py <record>` because it runs both the shape validator and the consistency audit.
