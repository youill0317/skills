# Evidence Needs Core

Use this compact map before opening heavier query references.

## Question Types

| Type | Use When | Search Implication |
| --- | --- | --- |
| `factual` | The task asks whether a claim is true. | Prioritize direct evidence and independent corroboration. |
| `temporal` | The task asks when something happened or what changed recently. | Track event date, publication date, and later updates separately. |
| `comparative` | The task compares entities, cases, periods, policies, products, methods, or claims. | Build parallel evidence requirements for each side. |
| `causal` | The task asks why something happened or what effects it had. | Separate evidence of correlation, mechanism, causal identification, and alternatives. |
| `definitional` | The task asks what something means, includes, excludes, or is called. | Search authoritative definitions, boundary cases, and competing terminology. |
| `evaluative` | The task asks whether something is good, risky, effective, feasible, or important. | Define criteria first, then map evidence to each criterion. |
| `landscape` | The task asks for an overview of actors, positions, debates, options, or structure. | Start broad, identify major dimensions, then target strong source families. |

## Evidence Needs

| Evidence Need | What It Answers | Strong Source Families |
| --- | --- | --- |
| `authoritative-record` | What is officially true or binding? | Laws, regulations, official documents, filings, standards, contracts, records, transcripts, meeting minutes, original releases. |
| `empirical-data` | What is observed, measured, counted, or estimated? | Datasets, statistics, surveys, experiments, logs, measurements, benchmarks, data dictionaries, methodology notes. |
| `method-quality` | How reliable are the data, method, measurement, or analysis? | Methodology notes, sampling descriptions, validation studies, audit records, replication materials, limitations, data dictionaries. |
| `expert-interpretation` | How do qualified experts interpret the issue? | Peer-reviewed papers, literature reviews, expert reports, technical explainers, interviews, professional guidance. |
| `stakeholder-position` | What do affected parties claim, support, oppose, or disclose? | Official statements, press releases, public comments, testimony, interviews, consultation submissions, investor materials. |
| `claim-provenance` | Where did a claim originate, and how did it spread? | Original statements, earliest reports, archives, citations, syndication chains, reposts, mirrored documents, correction histories. |
| `lead-expansion` | Which discovered leads could change the answer or close a coverage gap? | Citations, footnotes, linked documents, authors, institutions, datasets, methods, repositories, issues, dockets, standards, successors, corrections, co-citations. |
| `source-retrieval` | How can blocked or inaccessible source-of-truth material be recovered through authorized alternates? | Archives, mirrors, PDFs, APIs, transcripts, appendices, repository history, package registries, cached copies, official mirrors, cited excerpts. |
| `observed-behavior` | What are people, organizations, or markets actually doing? | Reviews, forums, social media, app stores, transaction traces, pricing changes, hiring posts, product changes, support threads. |
| `historical-timeline` | What changed, when, and in what sequence? | Archives, changelogs, court dockets, news records, filings, version histories, web captures, update notices. |
| `comparative-benchmark` | Compared with what baseline, peer, prior period, or standard? | Peer groups, competitor materials, benchmarks, standards, previous measurements, official comparisons, industry datasets. |
| `evaluation-criteria` | What standard should be used to judge quality, risk, importance, feasibility, or success? | Benchmarks, standards, requirements, expert frameworks, prior evaluations, client criteria, decision thresholds. |
| `transferability` | Can evidence from one setting apply to another? | Baseline comparisons, context variables, local constraints, boundary conditions, implementation differences, subgroup data. |
| `forecast-indicator` | What signals support or weaken a future-looking judgment? | Baseline trends, leading indicators, adoption signals, scenarios, trigger events, forecasts, disconfirming indicators. |
| `causal-mechanism` | Why might this happen, and what alternatives could explain it? | Causal studies, methods papers, natural experiments, mechanism descriptions, process records, counterfactual evidence. |
| `implementation-detail` | How does it actually work in practice? | Official docs, specs, source code, issue trackers, examples, manuals, operating procedures, migration guides. |
| `counterevidence` | What would weaken, reverse, or qualify the claim? | Negative findings, failed replications, corrections, retractions, rebuttals, dissenting expert views, contradictory records. |
| `profile-identity` | Who or what is this entity, and which records belong to the same person or organization? | Official profiles, registry records, ORCID/author IDs, CIK/LEI/company IDs, institutional pages, archived profiles, publication or affiliation records. |

For each important subquestion, search the strongest source family implied by
its evidence need before relying on weaker contextual sources.

## Source Strength

1. Primary sources: official documents, original papers, laws, regulations,
   court records, filings, datasets, changelogs, standards, transcripts, and
   direct statements.
2. High-quality secondary sources: expert reviews, reputable journalism,
   institutional reports, analyst reports, literature reviews, and technical
   explainers that point back to primary sources.
3. Contextual sources: blogs, forums, social media, aggregators, newsletters,
   summaries, and wikis. Use these for leads, terminology, and sentiment, not as
   evidence unless the topic is specifically about those sources.

When a secondary or contextual source makes an important claim, trace it back to
the primary source before treating it as strong evidence.

## Query Construction

Build queries after identifying the claim, evidence need, and likely source
family. Extract:

- keywords and synonyms
- entities, jurisdictions, datasets, products, methods, laws, and acronyms
- status, comparison, timeline, cause, definition, dispute, update, or
  verification intent
- date, location, language, source type, author, institution, and domain
  constraints
- overloaded meanings, unrelated entities, and other false positives to exclude

## Broadening And Narrowing

If searches return too few useful results, broaden by relaxing filters, replacing
exact phrases with core terms, adding synonyms or local-language variants, and
following citations or linked documents.

If searches return too many weak results, narrow with exact claim/title terms,
source-family terms, authoritative domains, file types, date ranges where
freshness matters, and exclusions for unrelated meanings.

## Core Checks

- Keep source lineages separate; repeated copies of one source do not count as
  independent support.
- Define counterevidence before synthesis for every central claim.
- Turn every material citation, author, dataset, repository, issue, docket,
  correction, local term, and blocked primary source into a lead-expansion or
  source-retrieval decision before synthesis.
- Check source authority, freshness, independence, completeness, and relevance.
- Mark a source as used only after inspecting its body or retrieved record
  through an authorized source path; search snippets, AI summaries, and
  generated overviews are leads only.
- Record missing source families and failed searches in `## Search Craft Log`,
  `## Wave Log`, or `## Dead Ends` in the single research record.

## Confidence Labels

Use these final confidence labels per important claim:

- `high`: direct primary or original evidence, adequate method quality,
  independent corroboration where needed, current enough for the question, and
  no material unresolved conflict.
- `medium`: strong but incomplete support, partial primary evidence, credible
  secondary synthesis, acceptable proxy evidence, or minor unresolved
  limitations.
- `low`: indirect evidence, weak source fit, single-source lineage, unclear
  provenance, stale sources, opaque methods, weak transferability, or
  substantial unresolved alternatives.
- `insufficient`: no direct evidence for the claim, evidence does not address
  the actual question, or a current-dependent claim cannot be current-verified.

Confidence follows evidence strength, not the number of search results.
