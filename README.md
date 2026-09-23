# CAG-RAG JARVIS Model

A **JARVIS-style voice assistant that combines Cache-Augmented Generation (CAG) with Retrieval-Augmented Generation (RAG)** — FAISS semantic retrieval over a document store, Sarvam AI as the LLM, and full voice input/output.

## Components

| File | Description |
|---|---|
| `cag.py` | Cache-Augmented generation over a fixed context |
| `retriever.py` | FAISS + sentence-transformers semantic retrieval from `data/docs.txt` |
| `sarvam_llm.py` | LLM calls via the Sarvam AI API |
| `voice.py` | Speech-to-text (SpeechRecognition) and text-to-speech (pyttsx3) |
| `app.py` | Streamlit UI wiring everything together |

## Quick start

```bash
pip install -r requirements.txt
streamlit run app.py
```

Set your Sarvam API key, then ask questions by text or voice.

## Stack

FAISS · sentence-transformers · Sarvam AI · Streamlit · SpeechRecognition · pyttsx3

## License

No license specified — for learning/reference use.