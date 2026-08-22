# Distributed 5-Agent NLP Orchestration System

A production-grade, fully decoupled Multi-Agent Generative AI orchestration platform engineered with Python, Streamlit, and the Groq Inference Engine. The framework bypasses monolithic single-prompt bottlenecks by implementing a strict **Directed Acyclic Graph (DAG)** architecture across 5 isolated, specialized LLM node environments.

---

## 📸 System Interface & Execution Visuals

### 1. Ingestion Control & Asynchronous Telemetry
The core interactive dashboard showing custom keyword ingestion and live status tracking as each distributed agent node finishes execution.
![System Control Interface](interface.png)

### 2. Multi-Lingual Generation & Title Synthesis
The parallel fan-out stage displaying simultaneous English source generation, French mapping, Hindi Devanagari translation, and synthesized title headers for any user input.
![Poetic and Translation Output](output_cup_of_tea_word.png)

### 3. Visual Prompt Concept Synthesis
The downstream visual rendering node generating detailed watercolor artwork descriptions from the literary payload.
![Artist Concept Output](output_cup_of_tea_word2.png)

---

## 🏗️ System Architecture & Data Flow

This architecture enforces absolute **Context Isolation** and **Data Encapsulation**. The system state progresses linearly down the execution graph where downstream nodes operate purely on localized upstream payloads, completely eliminating prompt-bleed:

1. **User Ingestion Point:** Raw user-provided keywords act as the primary ignition parameters.
2. 🤖 **PoetAgent (Node 1 - Root):** Compiles a structured, high-variance 12-line core text payload.
3. **Downstream Parallel Fan-Out:** The core text payload branches simultaneously into 4 independent sub-tracks:
    * 🌐 **French Translator (Node 2):** Rigid structural mapping into European French.
    * 🧡 **Hindi Translator (Node 3):** Transmutes stylistic themes into native Devanagari poetic meters.
    * 🏷️ **TitleAgent (Node 4):** Evaluates semantic layers to extract an abstract metaphorical title.
    * 🎨 **ArtistAgent (Node 5):** Synthesizes structural prose into explicit descriptive brushstrokes, colors, and lighting properties.

---

## 🔬 Node Environments & Hyperparameter Heterogeneity

To maximize processing throughput and minimize hallucination vectors, every micro-agent is bound to precise execution parameters matching its task specialization:

* **PoetAgent (Root)**
  * *Responsibility:* High-variance creative text generation
  * *Model:* `openai/gpt-oss-120b` | *Temperature:* `0.75` (Creative)
* **French Translator Node**
  * *Responsibility:* Literal, deterministic literary mapping
  * *Model:* `openai/gpt-oss-120b` | *Temperature:* `0.25` (Deterministic)
* **Hindi Translator Node**
  * *Responsibility:* Lyrical Devanagari rhythm matching
  * *Model:* `openai/gpt-oss-120b` | *Temperature:* `0.30` (Balanced)
* **TitleAgent Node**
  * *Responsibility:* Concentrated semantic compression
  * *Model:* `openai/gpt-oss-120b` | *Temperature:* `0.45` (Focused)
* **ArtistAgent Node**
  * *Responsibility:* Visual/Sensory prompt compilation
  * *Model:* `openai/gpt-oss-120b` | *Temperature:* `0.65` (Imaginative)

---

## 🛠️ Core Technical Highlights

- **Absolute Context Isolation:** Downstream extraction blocks (Translators, Title, Artist) possess zero visibility of the initial raw user keywords. This safeguards instruction boundaries against reverse-engineering prompts.
- **Asynchronous Telemetry:** Integrates Streamlit's `st.status` engine to track and print live asynchronous runtime footprints as each distributed node completes execution.
- **Unified Style Architecture:** Overrides the Streamlit layout engine with embedded low-level CSS sheets to enforce a persistent enterprise workspace canvas container (`#FEFBF0`).

---

## 🚀 System Setup & Run Instructions

### 1. Verification
Ensure your environment runs Python 3.10+ before setting up dependencies.

### 2. Environment Initialization
Clone the repository and install the application dependencies:
```bash
git clone [https://github.com/dhanshree17/Distributed-5-Agent-NLP-Orchestration-System.git](https://github.com/dhanshree17/Distributed-5-Agent-NLP-Orchestration-System.git)
cd Distributed-5-Agent-NLP-Orchestration-System
pip install streamlit groq
