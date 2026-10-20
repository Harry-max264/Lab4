# Promethean Technology Classification Agent

Assignment 4 | Shenghao Ma | 2026-10-19 | Version 1.1

Start with `records/agent_record.md`. Criteria are in `classification_criteria.md`; verified sources in `records/source_register.md`; comparisons and revision in `records/test_record.md`.

From repository root:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/promethean_classification --case agents/promethean_classification/cases/primary.json
python tools/validate_response.py agents/promethean_classification/responses/primary_response.json
```

Paste the generated packet into ChatGPT and save the returned JSON; repeat for contrast_1, contrast_2, hype and insufficient. This is a prompt-based specialist using ChatGPT as its runtime, not an API service. No API key is needed. Saved outputs are representative analyses authored by the ChatGPT/Codex assistant in the development session, not independent model calls or production performance measurements. New runs can differ.

Audit: see records/compliance_audit.md, records/course_alignment.md and records/preserved_weakness.md. Run `python agents/promethean_classification/verify_package.py` for the standard-library checks.
