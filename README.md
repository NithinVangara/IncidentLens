# IncidentLens

IncidentLens is an AI-powered incident investigation system designed to help investigate software incidents using evidence retrieval, reasoning, and structured analysis.

## Goal

IncidentLens aims to:

- Retrieve relevant incident evidence
- Investigate incidents using multiple evidence sources
- Generate and compare possible hypotheses
- Identify supporting and contradicting evidence
- Abstain when available evidence is insufficient
- Produce structured investigation reports
- Evaluate retrieval and investigation quality

## Core Technologies

- Python
- PostgreSQL
- pgvector
- LLM APIs
- Embeddings
- RAG
- Tool Calling
- FastAPI
- Scikit-learn
- PyTorch

## Project Structure

```text
incidentlens/
├── app/            # Application code
├── data/           # Incident and evidence data
├── tests/          # Automated tests
├── scripts/        # Utility scripts
├── notebooks/      # Experiments and analysis
├── evaluation/     # Evaluation datasets and results
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

#3 Status

Under active development.

This project is being built as a 30-day practical AI engineering project covering retrieval, RAG, agentic investigation, evaluation, and production-oriented backend engineering.