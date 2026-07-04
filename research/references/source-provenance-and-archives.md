# Source Provenance And Archives

Use this for widely repeated claims, statistics, quotations, benchmarks, viral
screenshots, clips, rumors, inaccessible originals, deleted sources, web
archives, cached pages, mutable internal sources, connector-backed records, and
historical timelines.

## Claim Provenance Audits

For widely repeated claims, statistics, quotations, or benchmarks:

1. Capture the claim exactly as stated.
2. Find the earliest accessible appearance.
3. Trace cited sources backward until reaching original evidence or a dead end.
4. Compare original wording with later wording.
5. Check denominator, population, date, geography, method, scope, and
   uncertainty.
6. Identify duplicated citation lineages.
7. Label provenance or scope as `direct`, `narrow`, `drifted`, `unsupported`,
   or `untraceable`. These are not confidence labels; final claim confidence
   still uses `high`, `medium`, `low`, or `insufficient`.

Use `direct` for ordinary source rows when the candidate directly supports the
claim and no special provenance drift is being evaluated. Use `narrow` when the
source supports only a narrower version of the claim, `unsupported` when it does
not support the claim, and `untraceable` when the upstream source cannot be
found. If a row is merely contextual, mark `Status` as `lead only` or `limited`
and keep `Direct Support?` as `no` or `partial` rather than inventing support.

For viral quotes, screenshots, clips, and rumors, also check:

- full original context: transcript, audio/video, full post/thread, article,
  press conference, meeting record, or document
- cropped or edited boundaries: what happened before/after the quoted segment
- account/entity identity, impersonation risk, deletion history, and archive
  timestamp
- whether a screenshot, clipped video, repost, or translation is the only
  available evidence
- whether the wording is exact quote, paraphrase, headline framing, translation,
  satire, allegation, or interpretation

For repeated statistics, benchmarks, or rankings that may be derived from a real
source, reconstruct the number before treating it as directly supported:

- numerator, denominator, formula, unit, geography, population, date, and data
  vintage
- rounding, unit conversion, currency, exchange-rate, inflation, per-capita,
  percent vs. percentage-point, or index-base transformations
- benchmark formula, weighting, inclusion rules, category definitions, and later
  methodology changes
- whether a secondary source copied the final number without preserving the
  original calculation

Common drift patterns include paraphrase drift, changed denominator, changed
population, correlation stated as causation, narrow sample generalized broadly,
outdated source treated as current, and a source citing another source as if it
were original.

## Unavailable Sources

When an important original source is inaccessible, paywalled, deleted, or
unavailable:

- check canonical URLs, archived pages, metadata pages, report PDFs, cited
  snapshots, and publisher records
- search by title, exact phrase, statistic, author, institution, and date
- mark provenance as unresolved rather than inferring support from repeated
  secondary citations

## Archive Capture Reliability

When using web archives, cached pages, or captured documents for historical
timelines:

- distinguish capture timestamp from publication time, modification time, and
  event time
- check whether the capture is complete, partial, dynamically rendered, blocked
  by robots, paywalled, redirected, or missing assets/scripts
- do not treat missing archive captures as evidence that content did not exist
- compare canonical URLs, redirects, mirrors, language versions, and multiple
  archive services when the timing matters
- corroborate archive-based sequence claims with metadata, filings, changelogs,
  release notes, citations, or other dated records when possible

## Mutable Internal Sources

For internal docs, tickets, chats, meeting notes, dashboards, CRM/support
records, code repositories, or connector-backed records that may change after
inspection, record chain-of-custody metadata where available:

- source system and object ID or path
- document or record owner/team
- revision ID, version, commit SHA, ticket state, dashboard version, message
  timestamp, meeting date, or export timestamp
- retrieved/accessed timestamp and timezone
- whether the inspected material was original, export, cached view, excerpt,
  generated summary, or screenshot
- evidence location such as heading, page, comment ID, ticket ID, commit line,
  API field, dashboard tile, case field, or message timestamp
- access basis, sensitivity, and redistribution limits
- whether the source has been superseded, archived, deleted, edited, resolved,
  reopened, merged, released, or rolled back

Do not treat a mutable source as stable unless its version, status, and as-of
context are recorded. If only an export, excerpt, screenshot, or generated
summary is available, mark URL/source role and provenance accordingly and avoid
firm claims unless corroborated by stronger evidence.
