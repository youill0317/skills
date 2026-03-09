# Quick Search Mode

This reference defines the optimal approach for handling "quick," simple, or high-level cross-engine queries (e.g., "What is machine learning?"). It is the counterpart to deep-research-mode, prioritizing speed, breadth, and synthesized summaries over exhaustive depth.

## Trigger Conditions

Use Quick Search Mode when the user:
1. Asks a general knowledge or definition question without demanding exhaustive research.
2. Explicitly asks for a "quick search," "overview," or "simple search."
3. Wants to compare high-level results across multiple engines quickly.

## Execution Strategy

1. **Parallel Execution is Mandatory**: Do not run searches sequentially. You must call multiple search tools concurrently in a single turn.
2. **Engine Selection**: Combine 2 or 3 distinct types of engines to get a well-rounded answer.
   - Example mix: `tavily_search` (general web) + `exa_search` (semantic/high-quality) + `scholar_search` (academic, if the topic is academic).
3. **Query Formulation**: Use the exact same core keyword or question across all selected tools to highlight differences in coverage.
4. **Depth Constraints**: 
   - Set low result limits (e.g., `max_results: 3` or `limit: 3`).
   - Do NOT use heavy extraction tools like `tavily_extract` or `exa_get_contents` unless a specific result is highly relevant but its summary is insufficient. Rely on the snippets provided by the initial search results.
5. **Synthesis**: Synthesize the results from all engines into a single, concise answer. Do not just list the raw engine outputs; blend them into a coherent summary.

## Example Tools Array (Conceptual)
```json
// Executed in a single tool call payload
[
  {
    "name": "tavily_search",
    "arguments": { "query": "What is machine learning?", "max_results": 3 }
  },
  {
    "name": "exa_search",
    "arguments": { "query": "What is machine learning?", "num_results": 3 }
  }
]
```

## Anti-Patterns
- **Sequential Calling**: Running Tavily, waiting for the response, and then running Exa. (Always parallelize).
- **Over-extraction**: Scraping the full text of 5 websites for a simple definition query.
- **Single Engine Dependency**: Relying on only one engine when the user requested a cross-engine summary.
