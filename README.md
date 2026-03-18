<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=F55036&height=200&section=header&text=VoiceSQL&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Talk%20to%20your%20database.%20No%20SQL%20needed.&descAlignY=60&descSize=18&descColor=ffffff" width="100%"/>

[![Made by Nevil Dhinoja](https://img.shields.io/badge/Made%20by-Nevil%20Dhinoja-F55036?style=for-the-badge)](https://github.com/Nevil-Dhinoja)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com/)
[![Groq](https://img.shields.io/badge/Groq%20Llama%203.3-F55036?style=for-the-badge)](https://groq.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![API Cost](https://img.shields.io/badge/API%20Cost-%240%20%2F%20%E2%82%B90-brightgreen?style=for-the-badge)](https://console.groq.com)

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=3000&pause=1000&color=F55036&center=true&vCenter=true&width=700&lines=Speak+Naturally+%E2%86%92+AI+Writes+SQL+%E2%86%92+Answer+Read+Aloud;100%25+Free+Stack+%E2%80%94+Zero+API+Cost;Whisper+%2B+Groq+Llama+3.3+%2B+LangChain+%2B+gTTS;Built+by+Nevil+Dhinoja+%E2%80%94+Gujarat%2C+India" alt="Typing SVG" />
</p>

</div>

---
<img src="assets/architecture.html" width="100%"/>
---

## What Is This?

**VoiceSQL** is a project I built to explore what happens when you wire a local speech-to-text model directly to a SQL agent. You speak a plain-English question. Whisper transcribes it on your machine — no cloud, no API call. LangChain passes it to Groq's Llama 3.3 70b which inspects the database schema, writes a SQL query, verifies it, runs it, and returns a structured result. gTTS reads the answer back out loud.

The entire pipeline — from microphone to spoken answer — runs at zero cost.

### Key Stats

| Metric | Value |
|--------|-------|
| STR Engine | OpenAI Whisper Base — local, CPU-only |
| LLM | Groq Llama 3.3 70b — free tier, 14,400 req/day |
| TTS | gTTS — no rate limits, free |
| Database | SQLite via SQLAlchemy |
| API Cost | $0 / Rs.0 |
| End-to-end latency | ~3–5 seconds |

---

## How It Works

```
You speak
   |
   v
Whisper (local, CPU)  -->  transcribed text
                                |
                                v
                     LangChain SQL Agent
                     + Groq Llama 3.3 70b
                     (reads schema, writes SQL,
                      verifies, then executes)
                                |
                                v
                          SQLite via SQLAlchemy
                                |
                                v
                     gTTS converts answer to MP3
                                |
                                v
                     Streamlit plays audio inline
```

**Step 1 — Voice Input.** `sounddevice` records 5 seconds of audio from your mic and writes it to a local `.wav` file.

**Step 2 — Transcription.** `openai-whisper` base model transcribes the audio entirely on your CPU. No API key. No latency from a network call.

**Step 3 — SQL Generation.** LangChain's `create_sql_agent` sends the question plus the live database schema to Groq Llama 3.3 70b. The model uses `sql_db_query_checker` to verify the query before running it — reducing hallucinated SQL.

**Step 4 — Execution.** SQLAlchemy executes the verified query against the SQLite database and returns rows.

**Step 5 — Voice Output.** `gTTS` converts the answer string to an MP3. Streamlit's `st.audio` component plays it inline — no external player needed.

---

## Features

| Feature | Detail |
|---------|--------|
| Voice Input | Mic recording via sounddevice + Whisper base (local) |
| Schema-Aware Agent | LangChain reads your DB schema before generating any SQL |
| Query Verification | Agent runs `sql_db_query_checker` before execution — catches bad queries |
| Voice Output | gTTS reads the answer aloud, MP3 plays inline in the browser |
| Text Mode | Type questions directly if preferred — same pipeline |
| Chat History | Every Q&A stored in session with audio playback |
| Zero Cost | No paid APIs anywhere in the stack |

---

## Tech Stack

<div align="center">

### AI / ML

![Whisper](https://img.shields.io/badge/OpenAI%20Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq%20Llama%203.3%2070b-F55036?style=for-the-badge)

### Data

![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Voice

![gTTS](https://img.shields.io/badge/gTTS-4285F4?style=for-the-badge&logo=google&logoColor=white)
![sounddevice](https://img.shields.io/badge/sounddevice-FF6B35?style=for-the-badge)
![ffmpeg](https://img.shields.io/badge/static--ffmpeg-007808?style=for-the-badge)

### Interface

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## Project Structure

```
voice-sql-assistant/
├── app/
│   ├── main.py          <-- Streamlit UI
│   ├── voice.py         <-- Whisper + gTTS
│   └── sql_agent.py     <-- LangChain + Groq
├── data/
│   └── seed.py          <-- Builds demo SQLite DB
├── .env                 <-- Your Groq key (never push this)
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### Prerequisites

| Software | Version | Purpose |
|----------|---------|---------|
| Python | 3.10+ | Runtime |
| pip | Latest | Packages |
| Groq API Key | Free | LLM |
| Microphone | Any | Voice input |

### Clone

```bash
git clone https://github.com/Nevil-Dhinoja/voice-sql-assistant
cd voice-sql-assistant
```

### Install

```bash
pip install -r requirements.txt
```

> Windows — if PyAudio fails: `pip install pipwin` then `pipwin install pyaudio`

### Get Groq key (free)

Go to [console.groq.com](https://console.groq.com), sign up, create an API key. It starts with `gsk_`.

### Configure

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=gsk_your_key_here
```

### Seed the database

```bash
python data/seed.py
```

Creates `school.db` — 50 students, 5 subjects, 200 score records across Surat, Ahmedabad, Baroda, Rajkot, Mumbai.

### Run

```bash
streamlit run app/main.py
```

---

## Demo Questions

```
"How many students are there?"
"Show the top 5 students by marks"
"Count students by city"
"Which class has the highest average marks?"
"List students from Surat who scored above 80"
"Which subject has the highest average score?"
"How many students are in class 10A?"
"What is the average age of all students?"
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `AuthenticationError 401` | Key in `.env` must start with `gsk_`, not `xai-` |
| `FileNotFoundError` in Whisper | Add `import static_ffmpeg; static_ffmpeg.add_paths()` at top of `voice.py` |
| PyAudio fails on Windows | `pip install pipwin` then `pipwin install pyaudio` |
| Agent loops infinitely | Switch model to `llama-3.3-70b-versatile` — the 8b is too small for agent reasoning |
| `.env` key returns None | File must be in root, not inside `app/` folder |

---

## Roadmap

- [x] Local Whisper STR — no API call
- [x] LangChain SQL Agent with schema inspection
- [x] Groq Llama 3.3 70b — free tier
- [x] gTTS voice output, plays in browser
- [x] Streamlit chat UI with history
- [ ] Coqui TTS — better voice quality, still free
- [ ] MySQL and PostgreSQL support
- [ ] Upload any CSV and query it live
- [ ] PDF export of query history
- [ ] Streamlit Cloud deployment

---

## License

MIT — free to use, fork, and build on.

---


<div align="center">


<br/>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="180" align="center" valign="top">

<img src="https://github.com/Nevil-Dhinoja.png" width="120" style="border-radius:50%"/>

</td>
<td width="30"></td>
<td valign="middle">

<h2 align="left">Nevil Dhinoja</h2>
<p align="left"><i>AI / ML Engineer &nbsp;·&nbsp; Full-Stack Developer &nbsp;·&nbsp; Gujarat, India</i></p>
<p align="left">
I build AI systems that are practical, deployable, and free to run.<br/>
This project is part of a larger series of open-source AI tools — each one<br/>
designed to teach a real concept through a working, shippable product.
</p>

</td>
</tr>
</table>

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nevil%20Dhinoja-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/nevil-dhinoja)
[![GitHub](https://img.shields.io/badge/GitHub-Nevil--Dhinoja-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nevil-Dhinoja)
[![Gmail](https://img.shields.io/badge/Email-nevil%40email.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nevil@email.com)

<br/>

If this project helped you or saved you time, a star on the repo goes a long way.

<br/>

[![Star this repo](https://img.shields.io/github/stars/Nevil-Dhinoja/voice-sql-assistant?style=for-the-badge&color=F55036)](https://github.com/Nevil-Dhinoja/voice-sql-assistant)
&nbsp;
[![Fork](https://img.shields.io/github/forks/Nevil-Dhinoja/voice-sql-assistant?style=for-the-badge&color=gray)](https://github.com/Nevil-Dhinoja/voice-sql-assistant/fork)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=F55036&height=120&section=footer" width="100%"/>

</div>