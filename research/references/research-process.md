# Research Process

## Principle

Start from the evidence needed for each claim, search the strongest likely
source families, expand through promising leads, and stop only after the
maximal investigation standard is met.

## Search Ladder

1. `Scout`: run broad searches to learn vocabulary, aliases, official names, origin-language terms, key institutions, and likely source families.
2. `Target`: search high-value source families directly.
3. `Snowball`: from strong seeds, chase references, footnotes, cited reports, cited laws, standards, datasets, methodology documents, successors, updates, and corrections.
4. `Gap Pass`: check missing source families, unresolved conflicts, freshness gaps, and claims that still lack original support.

Use `evidence-needs-core.md` for evidence needs, source family selection, and
compact query construction. Load `query-and-source-patterns.md` only when the
framing or discovered claims require specialized query patterns.

## Maximal Investigation Standard

Every research task uses the full Search Ladder. Split broad investigations
into independent lanes when subtopics or source families can be searched
separately.

Treat each strong source as a seed for lead expansion. Extract cited sources,
named institutions, datasets, methods, laws, standards, authors, corrections,
counterclaims, and terminology shifts, then pursue leads that can change an
important claim or close a source-family gap.

Before synthesis, complete these checks or record why they were unavailable:

- a claim inventory classifies every factual claim used in the final answer,
  every decision-relevant claim, every current/high-stakes/comparative claim,
  and every cited claim as important or `background/not decision-relevant`
- scout queries identified vocabulary, aliases, timelines, source families, and
  local or original-language terms where relevant
- target searches covered each high-value source family implied by the evidence
  needs
- snowball searches followed citations, source links, datasets, methodology
  notes, updates, corrections, successors, and credible counterclaims from
  strong seeds
- high-value recursive leads were tracked in the record's notes and either
  followed, rejected with a reason, blocked by access
  constraints, or used to downgrade affected claims
- gap-pass searches checked missing source families, unresolved conflicts,
  freshness gaps, weak provenance, and claims without original support
- important claims were tested against counterevidence and limitations
- source independence and lineage were checked
- dates, versions, jurisdictions, methods, and transferability were checked
  where they could affect the answer
- current-dependent claims received a latest-update or supersession check, or
  were labeled `insufficient`
- used sources were opened/read or retrieved through an authorized connector,
  with evidence location recorded
- the search path records scout, target, snowball, and gap-pass work at the
  level needed to reconstruct the investigation
- source-family coverage is summarized in `## What I Checked`,
  `## What I Did Not Check`, `## Search Path`, and `## Coverage Gates`
- important claims discovered during source discovery or synthesis are added to
  the claim list before the completeness gate

## Stop Rule

This is the canonical general stop rule for the research skill. Domain
references may add extra stop gates; those gates are cumulative, not
substitutes.

Stop per claim only after the maximal investigation standard has been met, the
evidence need is satisfied, key source families have been checked, and new
searches mostly repeat existing source lineages or drift away from the target.
When an evidence gap remains, stop only after documented scout, target,
snowball, and gap-pass attempts show the gap is unavailable or unlikely to be
closed with authorized sources.

For important claims, do not stop until direct evidence, method quality,
counterevidence, source independence, and transferability have been checked or
explicitly marked unavailable or low value.

For quantitative claims based on statistics, datasets, dashboards, benchmarks,
or surveys, do not stop until the relevant methodology, data dictionary or
codebook, denominator/universe definition, release vintage, revision status,
uncertainty, and cross-period or cross-source comparability limits have been
checked or explicitly marked unavailable.

For policy/regulatory/legal landscape research, do not stop until each requested
jurisdiction has a current governing-source check, pending-rule/docket check,
enforcement/guidance check, effective-date and supersession check, and explicit
applicability note, or those gaps are marked unavailable.

For technical/product implementation research, do not stop until the relevant
official docs/API reference, source or release tag, release notes/changelog,
migration/deprecation notes, supported version matrix, relevant issues, security
advisories, and reproducibility inputs such as package/runtime versions or
lockfiles have been checked or explicitly marked unavailable.

For product/tool recommendation or purchase research, do not stop until current
availability, discontinuation risk, regional SKU/model variants, shipping lead
time, seller/retailer reliability, return policy, warranty terms, refurbished or
used condition caveats, compatibility, and total-cost drivers have been checked
or explicitly marked unavailable.

Continue when primary sources are missing, provenance is unclear, claims
conflict, source-family coverage is thin, decision-relevant snowball leads
remain pending, or freshness remains unresolved.

Write the stop-rule result into the single research record. The record must
state which scout, target, snowball, gap-pass, verification, and coverage gates
passed, failed, were blocked, or were not applicable, and which unresolved gaps
could still change the conclusion.
