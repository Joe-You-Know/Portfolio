# CausalGPT / Eligens — a provenance-gated learning prototype

**Domains:** C++20, Python, durable learning state, AI agents, constrained advisory feedback, research provenance, test-oriented system design.

**Separate work:** This project is not the GPT-OSS-20B inference/cache customization discussed in the [CausalCodex/GPT case study](../case-studies/causalcodex-gpt.md). They address different components and use different evidence.

## 1. What problem did I address?

A model can produce fluent explanations or gather new text without establishing causal truth. Autonomous collection can also lose source ancestry, silently treat text as approved evidence, or repeatedly retry questions without a meaningful audit record. I sought a prototype that records unresolved WHY questions and conditions any knowledge promotion on explicit review rather than on fluency alone.

## 2. What did I implement?

The private CausalGPT repository contains a C++20 core with structured instructional patterns, WHY-directed investigation, and Python/GitHub Actions orchestration. Components include:

- Persistent causal-question and acquisition ledgers, source ancestry and retry counts.
- Query selection driven by unresolved WHY questions instead of static rotating topics.
- Source and relevance reporting, role-completeness checks and review statuses.
- A separate **external advisory teacher** that can propose a validated search-query change for an existing question.
- Contract-enforced separation between teacher recommendations, retrieved reports, reviewed evidence and approved changes. The teacher cannot automatically edit the reasoning kernel or elevate a retrieved claim to verified truth.

The learner core does not depend on pretrained neural weights. The optional external teacher is a separate API-based component; it should not be confused with the core's learning mechanism.

## 3. What did I actually verify?

A preserved private `learning-state` report generated **November 7, 2026** recorded:

| Recorded state | Count |
| --- | ---: |
| Acquired documents | 50 |
| WHY questions / unresolved questions | 7 / 7 |
| Claim candidates | 124 |
| Human-reviewed sources | **0** |
| Questions with complete causal roles | **0** |
| Verified mechanisms | **0** |

The repository includes C++ and Python test modules for question investigation, prose handling, source review, relevance, feedback contracts and other components. These artifacts support that the workflow and review architecture exist; **the public portfolio does not reproduce a full CausalGPT run**. A successful scheduled run or search-query adoption is not proof of successful learning or scientific verification.

## 4. What remains unresolved?

Reviewed and permission-cleared source acquisition; end-to-end demonstration of a correct, complete causal mechanism; robust negative controls; meaningful generalization to unfamiliar domains; external replication of the agent's performance; and a safe minimal public release of its test harness.

**Access:** The full CausalGPT code and durable research-state branch are **private**. No source records, third-party acquired texts or secrets are being published in this portfolio. This page is a bounded engineering case study, not a claim of general intelligence or independently verified causation.

[All featured projects](README.md) · [Portfolio home](../README.md)
