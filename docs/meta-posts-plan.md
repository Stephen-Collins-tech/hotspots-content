# Meta Posts Plan

Posts synthesising patterns across the analysis corpus, rather than analysing a single repo.

**Corpus as of 2026-04-17:** 53 analysis posts — 28 TypeScript, 9 JavaScript, 4 each of Rust / Python / Java / Go.

---

## Proposed Posts

### 1. Overview: "5 patterns in 96% of TypeScript OSS repos"
**Status:** Published — `blog/typescript-structural-patterns.mdx`  
**Angle:** The big-5 patterns (`long_function`, `god_function`, `exit_heavy`, `complex_branching`, `deeply_nested`) appear in nearly every TS repo we've analysed. This is the anchor/overview post — it can link forward to posts 2 and 4.  
**Data:** All 28 TS repos; prevalence 86–100% per pattern.  
**SEO hook:** "what causes technical debt in TypeScript"  
**Write when:** Now.

---

### 2. Deep dive: "Why TypeScript's top complexity pattern is branching, not exit_heavy"
**Status:** Published — `blog/typescript-branching-complexity.mdx`  
**Angle:** In non-TS repos, `exit_heavy` leads (avg 5.3); in TS repos, `complex_branching` leads (avg 4.0, highest max-5 hit rate at 13/28). The likely cause: TypeScript encourages discriminated unions and type-narrowing conditionals, which create structural branching even in well-written code. Actionable: use exhaustive-switch helpers or strategy objects to flatten union dispatch.  
**Data:** TS avg 4.0 vs non-TS avg 4.6 for `complex_branching`; TS avg 4.5 vs non-TS avg 5.3 for `exit_heavy`.  
**Write when:** Now. Strongest standalone piece; most surprising finding.

---

### 3. Deep dive: "Hub functions are a frontend/UI framework problem"
**Status:** Published — `blog/typescript-hub-functions.mdx`  
**Angle:** `hub_function` is almost exclusive to TS UI/framework repos in our corpus — xyflow, tldraw, umami, react-hook-form, ink all show it. Clear structural reason: event buses, render trees, and centralised state naturally produce a single orchestrator with very high fan-in. Actionable: identify hub functions early and split by event category or concern.  
**Data:** 5 TS repos with `hub_function`; 0 notable hits in non-TS corpus.  
**Write when:** Now.

---

### 4. "AI-tooling repos are consistently more complex"
**Status:** Needs more data — hold  
**Angle:** All 4 fully-saturated repos (every pattern at max count) are AI-tooling apps: Flowise, chatbox, context7, paperclip. The hypothesis is that AI-tooling code is inherently harder to decompose (streaming, multi-step pipelines, mixed sync/async). But 4 repos is too thin to publish a confident claim.  
**Data needed:** ~10 AI-tooling repos total; also check if non-TS corpus has AI-tooling repos that fail to show the same saturation.  
**Write when:** Corpus reaches ~10 AI-tooling analyses.

---

### 5. "What fully-saturated repos have in common"
**Status:** Needs more data — hold  
**Angle:** Some repos max out on all 5 structural patterns simultaneously. What do they share? (Size? Domain? Age? Contributor count?)  
**Data needed:** Same as post 4 — 4 examples is not enough to draw conclusions.  
**Write when:** Corpus reaches 10+ saturated repos, or a clear non-AI-tooling saturated repo appears to test the hypothesis.

---

## Recommended Write Order

1. Post 2 (branching vs exit_heavy flip) — sharpest hook, most explainable
2. Post 1 (overview) — links to 2 and 3; good for internal linking
3. Post 3 (hub functions) — clear audience (frontend framework authors)
4. Posts 4 & 5 — revisit when corpus grows

---

## Corpus Tracking

| Language | Count (2026-04-17) | Needed for blocked posts |
|---|---|---|
| TypeScript | 28 | — |
| JavaScript | 9 | — |
| Rust | 4 | — |
| Python | 4 | — |
| Java | 4 | — |
| Go | 4 | — |
| AI-tooling repos (any language) | 4 | 10 to unblock posts 4 & 5 |
