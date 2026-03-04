# Zero‑Cost Automation Pipeline for Clara Answers Intern Assignment

## Project Overview

This repository demonstrates a fully offline, zero‑cost automation pipeline that ingests call transcripts and produces structured memos and agent specifications. Two pipelines are defined:

- **Pipeline A** – Process a demo call and create a v1 account memo and agent spec.
- **Pipeline B** – Process onboarding input to update the memo and generate v2 artifacts plus changelog.

All code leverages free tools: n8n for orchestration, local Python for processing, and plain JSON files for storage.

---

## Architecture Diagram 📊

```
[Demo Transcript] → n8n → extract_fields.py → memo.json (v1) → generate_prompt.py → agent_spec.json (v1)
                        ↘ task tracker

[Onboarding Transcript] → n8n → extract_fields.py → patch memo → v2 outputs → diff_generator.py → changelog
```

The system is intentionally simple, self‑contained, and idempotent.

---

## Automation Flow

1. **Ingest transcript** via webhook or manual upload.
2. **Normalize** text to remove noise.
3. **Assign** a unique `account_id` (e.g. slug of company name or UUID).
4. **Extract structured fields** with rule‑based Python (`extract_fields.py`).
5. **Generate account memo JSON** and write to `outputs/accounts/<id>/v1`.
6. **Create agent spec** using the memo (`generate_prompt.py`).
7. **Save artifacts** to the repository.
8. **Create task tracker entry** (could be a simple JSON or spreadsheet row).
9. **Onboarding** re‑runs extraction, compares, and patches previous memo.
10. **Regenerate agent spec** for `v2` and store alongside.
11. **Compute changelog** with `diff_generator.py` and save under `changelog/`.

The workflows are **idempotent**, meaning reprocessing the same input yields the same files. Partial failures can be retried without side effects.

---

## Tools Used (Zero Cost) 🛠️

- [n8n](https://n8n.io) – open‑source automation engine (running locally via Docker).
- Python 3 – for extraction and generation scripts.
- Whisper (optional) – local transcription if starting from audio.
- Git – version control; outputs live in the repo.
- SQLite or Google Sheets (optional) – for task tracking/dashboard.

---

## How to Run Locally

1. **Clone repo** and navigate to workspace.
2. **Install Python dependencies** (none external; core libs only).
3. **Start n8n**:
   ```bash
   docker run -it --rm \
     -p 5678:5678 \
     -v "${PWD}/workflows:/home/node/.n8n/" \
     n8nio/n8n
   ```
4. **Import** the JSON workflows via the n8n UI (`Import from File`).
5. **Trigger** demo pipeline by POSTing a transcript to the webhook URL or manually executing the node.
6. **Inspect outputs** under `outputs/accounts/<id>/v1`.

---

## How to Import n8n Workflows

Open n8n UI at `http://localhost:5678`, choose *Settings → Workflow* and import the JSON files located in `/workflows`.

---

## How to Process Dataset

Place raw transcript files into `dataset/demo_calls` or `dataset/onboarding_calls`. The workflows can be modified to read from those folders in batch mode.

---

## Where Outputs Are Stored

Outputs live under `outputs/accounts/<account_id>/vX`. Each version folder contains `memo.json` and `agent_spec.json`.

Changelogs appear in `changelog/<account_id>.md`.

---

## Limitations ⚠️

- Extraction is rule‑based and brittle; missing or ambiguous information ends up under `questions_or_unknowns`.
- No real LLM is used; system prompts are static.
- Task tracker and dashboard are placeholders.
- No authentication/security on webhooks.

---

## Future Improvements 🚀

- Plug in an open‑source LLM (e.g., LLaMA‑2) for smarter extraction and prompt generation.
- Add a simple web GUI for entering transcripts and viewing results.
- Implement diff viewer and batch metrics via Google Sheets or a lightweight web dashboard.
- Extend workflows for audio transcription with Whisper.
- Containerize the entire stack for easier deployment.

---

*This repository satisfies the Clara Answers Intern assignment by showcasing a zero‑cost, extendable automation pipeline.*