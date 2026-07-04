# Source Verification

## Source Priority

Prefer the most authoritative source for the exact question:

1. primary, official, original, governing, or source-of-truth material
2. high-quality secondary synthesis that points to primary sources
3. useful but weaker interpretation
4. low-authority, mirrored, unverified, promotional, or provenance-poor material

Prefer scope fit over generic authority. Use recency as a tie-breaker only when the topic is time-sensitive; older primary records can remain authoritative.

AI summaries, search result snippets, and generated overviews are not evidence
for factual claims. Use them only as leads unless the research question is
about what that AI/search surface says.

## High-Stakes Claim Protocol

Use this protocol for medical, legal, financial, safety, clinical, regulatory,
or other claims where a wrong answer could cause material harm.

1. Apply the maximal investigation standard and do not rely on single-source
   shortcuts.
2. Require primary or governing sources before giving a firm answer:
   - medical/clinical: current regulator guidance, drug/device labels, clinical
     guidelines, trial registry records, and full study text when method details
     matter; use systematic reviews as high-quality synthesis to compare,
     contextualize, or find primary evidence, not as a primary/governing source
   - legal/regulatory: current statutes, regulations, agency guidance, court
     orders, docket entries, contracts, or official enforcement materials for the
     relevant jurisdiction
   - financial: official filings, audited reports, regulator materials,
     prospectuses, fee schedules, market data methodology, or original datasets
   - safety/technical: standards, official incident reports, manufacturer
     notices, recalls, engineering analyses, test protocols, regulator alerts,
     vendor security advisories, CVE/NVD records, GitHub Security Advisories,
     OSV records, package registry advisories, and maintainer security pages
3. Use secondary sources only to find, explain, or compare primary sources; do
   not let a secondary summary override governing text or original evidence.
4. State the non-advice boundary when the answer could be mistaken for medical,
   legal, financial, or safety advice. Frame the output as evidence summary or
   research support, and direct decisions to qualified professionals or governing
   authorities when appropriate.
5. Check recency explicitly: publication date, effective date, amendment date,
   last-updated date, superseding guidance, recalls, warnings, retractions,
   docket activity, and rule changes.
   If live/current access is unavailable for a claim whose truth depends on
   current status, label the claim `insufficient` unless the answer is
   explicitly historical.
6. Check jurisdiction and applicability: country, state/province, regulator,
   court, product/version, population, dosage/exposure, account type, entity
   status, and effective date.
   - For legal/regulatory landscape work, record authority hierarchy and status
     for each source: statute vs. regulation vs. guidance vs. enforcement action
     vs. court order; binding vs. nonbinding; proposed vs. final; effective and
     compliance dates; amendment/repeal/sunset dates; stays, injunctions,
     vacatur, preemption, and supersession; covered entities, thresholds,
     exemptions, and territorial scope.
7. Check method quality when evidence is empirical: study design, comparator,
   sample, denominator, uncertainty interval, endpoint, confounding, missing
   data, validation, sponsor/funder, and whether the method supports the exact
   claim.
8. Preserve residual uncertainty. Report unresolved conflicts, missing primary
   sources, stale or superseded material, jurisdiction limits, method limits, and
   practical conditions that could change the conclusion.

For enterprise decisions, escalate or mark `requires owner review` before firm
operational use when a claim affects legal obligations, compliance posture,
security controls, customer commitments, revenue recognition, regulated data,
employment decisions, financial exposure, material procurement, public
statements, or contractual obligations. Use `not decision-ready` when required
owner review, governing sources, or current verification are missing for a
material claim.

## Verification Labels

Use compact working labels while evaluating sources:

- `original-document`: law, filing, dataset, paper, transcript, archived page, or original release
- `source-of-claim`: earliest or clearest source making the claim
- `independent-confirmation`: materially independent corroboration
- `official-response`: official confirmation, denial, clarification, or statement
- `dataset`: source provides data used for the claim
- `methodology`: source explains methods, definitions, sampling, or measurement
- `correction`: correction, update, erratum, retraction, or denial
- `stale`: source may be outdated for the question
- `current`: current source for a time-sensitive question
- `superseded`: older source replaced by a newer version
- `conflicting`: source conflicts with another candidate
- `single-source`: claim appears to rely on one source family only
- `provenance-unclear`: unclear author, origin, date, version, or chain of custody
- `not-evidence`: useful context but not support for the target claim
- `requires-owner-review`: evidence may support research synthesis but needs a
  responsible business, legal, security, finance, data, or compliance owner
  before operational use
- `not-decision-ready`: evidence is too weak, inaccessible, stale, conflicting,
  sensitive, or unverified for the scoped decision

## Independence Rule

Multiple sources count as corroboration only when they are materially independent. Repeated wire stories, press-release rewrites, mirrored PDFs, syndicated articles, and articles citing the same unnamed source are duplicate lineage, not independent confirmation.

## Provenance Checks

For important sources, check:

- canonical publisher or domain
- publication date, event date, and last-updated date
- document version, amendment, release, or archive timestamp
- author, institution, funder, or issuing body
- whether the URL is original, mirror, archive, excerpt, or commentary
- whether the source directly supports the target claim or only gives background
- lineage and claim provenance label for the source row
- access method and whether the body or retrieved record was inspected
- evidence location such as section, page, table, API field, commit, line, or
  timestamp
- accessed/as-of date for current, mutable, or connector-backed sources
- access basis, sensitivity, minimum-necessary status, and redistribution limits
  for internal or connected sources
- source quality status such as current, stale, superseded, conflicting,
  provenance-unclear, or not-evidence

## Variant Trace

For quotes, screenshots, clips, translated claims, viral claims, or repeated
media summaries, build a chronological variant map before deciding whether the
claim changed:

- record each version's URL or archive capture, publisher/platform/account,
  publication or capture time, exact wording or screenshot OCR/transcription,
  language and translator/source, and cited upstream source
- mark observed transformations such as crop, ellipsis, paraphrase, headline
  framing, translation drift, media-summary compression, repost attribution, or
  image/video edit
- assign confidence per variant, separating direct original evidence from
  inferred lineage or missing-source gaps

## Person And Organization Conflict-Of-Interest Pass

When evaluating a person or organization profile, expert statement, institutional
position, market claim, policy position, or research output, check relevant
interest signals before relying on apparent independence:

- board seats, advisory roles, employment, consulting, speaking, grants,
  ownership, equity, related-party transactions, sponsors, funders, lobbying,
  political donations, procurement relationships, partnerships, and reseller or
  affiliate arrangements
- litigation, enforcement actions, sanctions, regulatory findings, complaints,
  settlements, disciplinary actions, and public corrections tied to the person,
  organization, funder, or closely related entity
- whether the affiliation is disclosed, historical, current, denied, disputed,
  or only alleged; do not infer undisclosed conflict without evidence, but keep
  unresolved affiliation risk visible when independence matters

## Cross-Language Verification

For multilingual or non-English evidence, check:

- original-language wording, translated wording, and any official translation
- native-script name, romanized variants, aliases, and entity disambiguation
- translator/source of translation: official, publisher, reporter, machine, or
  agent-generated working translation
- whether local legal, administrative, cultural, or institutional terms have no
  exact English equivalent
- whether later-language coverage changes denominator, modality, certainty,
  actor, date, scope, or allegation/resolution status

Label claim support as `translation-equivalent`, `translation-narrower`,
`translation-broader`, `translation-drifted`, or `translation-unverified` when
language affects interpretation.

## Conflict Protocol

When sources conflict:

1. Identify the exact disputed claim.
2. Group sources by lineage and independence.
3. Prefer primary or original sources over commentary.
4. Check whether dates, scope, definitions, methods, jurisdictions, or versions explain the conflict.
5. Keep unresolved conflicts explicit instead of flattening them into a stronger conclusion.
6. Treat official or party denials as evidence of that party's position unless
   they directly resolve the claim with records, documents, or verifiable detail.
   Compare the denial's exact scope with the disputed claim, and do not let a
   broad denial override narrower documentary evidence.

## Confidence Calibration

Calibrate confidence per important claim:

- `high`: direct primary or original evidence, adequate method quality,
  independent corroboration where needed, current enough for the question,
  transferability checked where relevant, and no material unresolved conflict.
- `medium`: strong but incomplete support, partial primary evidence, credible
  secondary synthesis, acceptable proxy evidence, or minor unresolved
  limitations.
- `low`: indirect evidence, weak source fit, single-source lineage, unclear
  provenance, stale sources, opaque methods, weak transferability, or
  substantial unresolved alternatives.
- `insufficient`: no direct evidence for the claim, evidence does not address
  the actual question, or a current-dependent claim lacks a latest-update or
  supersession check.

Confidence should follow evidence strength, not the number of search results.

## Claim Boundary

Describe why a source matters without overstating what it proves. Do not treat
a claim as stronger than the inspected source supports.
