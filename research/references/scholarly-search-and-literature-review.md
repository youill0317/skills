# Scholarly Search And Literature Review

Use this reference when research depends on academic papers, scholarly
databases, citation trails, study appraisal, or publication metadata.

## Source Families

- Discovery indexes: PubMed, Semantic Scholar, OpenAlex, Crossref, arXiv,
  bioRxiv, medRxiv, CORE, Unpaywall, and Google Scholar when accessible.
- Full text and extraction sources: PubMed Central, publisher pages, open PDFs,
  institutional repositories, and structured full-text extraction tools.
- Citation and metadata sources: DOI landing pages, Crossref records, PubMed
  records, ORCID, journal pages, Zotero/BibTeX metadata, and retraction
  databases when available.
- Domain databases: use specialized databases only when the question needs
  data beyond papers, such as clinical trials, compounds, proteins, patents,
  grants, regulatory records, or benchmark datasets.

## Database Selection

Choose databases by discipline before searching:

- Biomedical/clinical: PubMed/MEDLINE, Cochrane Library, Embase when available,
  ClinicalTrials.gov, WHO ICTRP, and specialty registries.
- Psychology/behavioral science: PsycINFO, PubMed, ERIC when educational, and
  multidisciplinary citation indexes.
- Education: ERIC, Education Source, PsycINFO, and domain journals or policy
  repositories.
- Social science/policy: Scopus, Web of Science, SSRN, EconLit, Sociological
  Abstracts, PAIS, think-tank or government repositories as appropriate.
- Computer science/engineering: ACM Digital Library, IEEE Xplore, arXiv, DBLP,
  Semantic Scholar, and benchmark/dataset repositories.
- Law/regulation: legal databases, official dockets, agency guidance, statutes,
  and law reviews.
- Multidisciplinary coverage: OpenAlex, Semantic Scholar, Crossref, Scopus/Web
  of Science when available, and Google Scholar only as a supplementary
  discovery source.

## Search Process

1. Convert the user question into researchable concepts. Use PICO/PECO for
   clinical, behavioral, public-health, or intervention questions; otherwise
   use entity, mechanism, method, population, outcome, and context concepts.
2. Build seed terms from synonyms, abbreviations, controlled vocabulary,
   spelling variants, method names, datasets, instruments, key authors,
   jurisdictions, and date constraints.
3. Create concept blocks rather than one long query: population/context,
   phenomenon/intervention/exposure, outcome, method/design, and exclusions.
4. Validate the query against a small gold set of known relevant papers from
   reviews, seminal works, or expert-recognized sources. If the query misses
   them, revise terms, field tags, controlled vocabulary, and exclusions before
   continuing.
5. Translate concepts into database-specific syntax such as MeSH, Emtree,
   PsycINFO thesaurus terms, title/abstract fields, proximity operators, and
   citation-index filters when available.
6. Scout broad indexes to identify vocabulary, seminal papers, recent reviews,
   and active research clusters.
7. Run targeted searches in the source families that best match the evidence
   need.
8. Snowball backward from references and forward through citing papers.
9. Extract details from full text when abstracts are insufficient or when the
   claim depends on methods, sample, measures, statistical model, or limitations.
10. Verify publication metadata before citing: title, authors, year, venue, DOI,
   version, preprint status, and retraction or expression-of-concern status.

## Evidence Extraction

Track evidence in a compact map rather than a paper dump.

| Subquestion or claim | Paper | Study type | Sample or data | Method | Result | Limitation | Quality note |
|---|---|---|---|---|---|---|---|

Separate primary studies, reviews, meta-analyses, methods papers, datasets, and
commentary. Do not treat a review as independent confirmation of the primary
studies it summarizes.

## Quality Appraisal

Check the quality dimensions that fit the field:

- study design, controls, comparator, sample size, statistical power, and
  representativeness
- measurement validity, construct validity, confounding, selection bias, and
  missing-data handling
- statistical appropriateness, preregistration, multiple-comparison handling,
  sensitivity analyses, replication, and robustness checks
- data/code availability, benchmark leakage, reproducibility, and external
  validity
- funding, conflicts of interest, publication venue, peer-review status,
  preprint status, and recency

Select appraisal checks by study design:

- Systematic reviews/meta-analyses: search completeness, inclusion criteria,
  duplicate screening, risk-of-bias handling, heterogeneity, publication bias,
  and whether conclusions exceed included studies.
- Randomized or quasi-experimental studies: allocation, comparator, blinding
  where relevant, attrition, preregistration, outcome switching, effect sizes,
  confidence intervals, and causal identification.
- Observational studies: sampling, confounding control, selection bias,
  measurement validity, missing data, model specification, sensitivity analyses,
  and plausible alternative explanations.
- Qualitative studies: sampling rationale, data collection transparency, coding
  procedure, reflexivity, triangulation, and whether claims are grounded in
  excerpts or observations.
- Computational/benchmark studies: dataset leakage, baseline choice, evaluation
  metrics, reproducibility, code/data availability, external validity, and
  benchmark saturation.

Do not use journal prestige, citation count, or peer-review status as a
substitute for method appraisal.

Use stronger language only when independent, high-quality evidence converges.
Flag disagreement, weak evidence, and domain transfer limits explicitly.

## Citation Handling

- Prefer DOI, PubMed ID, arXiv ID, or stable publisher URLs over search-result
  links.
- Generate BibTeX or formatted references only after metadata verification.
- For preprints, state that the work is a preprint and check whether a later
  peer-reviewed version exists.
- For medical, legal, clinical, financial, or safety-relevant claims, verify
  current sources and avoid relying on a single abstract or secondary summary.

## Synthesis Pattern

For literature reviews, synthesize by concepts, mechanisms, methods, evidence
quality, and disagreements. Use paper-by-paper summaries only when the user
asks for an annotated bibliography or source inventory.

State the search scope: databases checked, key query families, language/date
limits, inclusion/exclusion logic, and the date of search when recency matters.

## Literature Review Stop Rule

Stop the academic search when:

- the discipline-appropriate databases have been searched with documented query
  families;
- backward and forward citation chasing from the strongest seed papers, recent
  reviews, and contradictory studies no longer finds new eligible concepts,
  methods, populations, or result clusters;
- major disagreements have been traced to differences in design, sample,
  measures, definitions, analysis, timing, or publication status, or are
  explicitly unresolved;
- metadata and retraction/preprint status are verified for cited papers;
- remaining gaps are unlikely to be closed by more search and are reported as
  evidence gaps rather than inferred conclusions.

When discipline-appropriate databases are unavailable, include a database
coverage table and avoid calling the result a systematic review unless the
methods actually meet that standard:

```markdown
## Database Coverage

| Database | Needed? | Access Status | Query Run | Result Count / Summary | Gap Impact |
|---|---|---|---|---|---|
| ... | yes / no | searched / unavailable / not applicable | ... | ... | ... |
```
