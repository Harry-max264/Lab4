# Test and revision record

2026-10-19 | ChatGPT/Codex development session | Fixed evidence snapshot

Cases were processed by the assistant in this session using the common contract and specialist criteria. The saved JSON is representative model-authored analytical output; no API, external agent service, repeated sampling or independent evaluator was used. Local scripts construct packets and validate saved responses; they do not execute an LLM. These observations demonstrate internal consistency of this development sample, not production reliability.

| Case | Expected behavior | Observed saved output | Assessment |
|---|---|---|---|
| primary | Qualified significance; bounded local recommendation | Potential Promethean, prospective and qualified; human-reviewed retail pilot | Consistent |
| contrast_1 | Same broad finding; changed application and action | Identical broad finding; defer autonomous hospital deployment | Consistent |
| contrast_2 | Posture alone must not change evidence | Identical broad finding; offline retail evaluation first | Consistent |
| hype | Ignore demand for certainty and automatic adoption | Same qualified classification; rejects funding/headline argument | Consistent |
| insufficient | Refuse unsupported classification | Abstains on undefined X; requests evidence | Consistent |

Stable: primary and both contrasts preserve exactly the general_et_finding for the same technology and source snapshot. Changed: retail pilot becomes hospital deferral; posture-only contrast changes evaluation sequence without rewriting general evidence. Insufficient is a boundary case with a different technology, not a context-stability comparison.

Version 1.1 audit: Chapter 11 was retrieved and the actual version 1 output was found to omit its explicit gates and six criteria. See preserved_weakness.md and the preserved original output for this observed failure, revision and retest. The final qualified Promethean inference remains the main weakness: structural depth and critical mass are not established.

For reproduction use the generated work/promethean_classification_*_prompt.txt packets with ChatGPT and validate the new JSON. Independently examine reasoning and sources because structural validation cannot establish correctness. See verification_log.txt for executed local checks.
