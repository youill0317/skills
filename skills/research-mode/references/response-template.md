# Response Template

Always respond in the user's original language.

## Required Structure

1. Direct answer:
   - 1-2 sentences only
   - include the main conclusion first

2. Research synthesis:
   - use `###` headers
   - use lists for evidence grouping
   - use tables for comparisons

3. Citations:
   - use inline citation markers like `[1]`, `[2]`, `[3]`
   - never output external URLs
   - map each citation marker to an internal source note

## Recommended Section Order

```markdown
직답 1-2문장 [1][2]

### 핵심 발견
- 사실 A [1]
- 사실 B [2]

### 언어권 교차검증
| 항목 | 사용자 언어 결과 | 영어 결과 | 판단 |
|---|---|---|---|
| claim X | ... [1] | ... [2] | 일치/불일치 |

### 불일치/한계
- 충돌 지점 ... [3]
- 남은 불확실성 ...
```

## Style Constraints

- Bold only critical terms.
- Avoid filler phrases.
- If uncertain, state uncertainty explicitly and show next verification target.
