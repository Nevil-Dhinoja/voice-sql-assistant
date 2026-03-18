import static_ffmpeg
static_ffmpeg.add_paths()

import streamlit as st
from app.voice import record_audio, transcribe, speak
from app.sql_agent import get_agent, query

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Voice SQL Assistant",
    page_icon="🎙️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e2e8f0;
}

/* Title */
.title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Chat bubbles */
.user-msg {
    background: #1e293b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.bot-msg {
    background: #020617;
    border: 1px solid #1e293b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
}

.stButton>button:hover {
    opacity: 0.9;
}

/* Input */
.stTextInput>div>div>input {
    border-radius: 10px;
    background: #020617;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🎙️ Voice SQL Assistant</div>', unsafe_allow_html=True)
st.caption("Ask with voice or text → AI writes SQL → results + voice reply")

# ---------------- SESSION ----------------
if "agent" not in st.session_state:
    with st.spinner("⚡ Booting AI agent..."):
        st.session_state.agent = get_agent()

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- INPUT BAR ----------------
col1, col2 = st.columns([6, 1])

with col1:
    text_q = st.text_input(
        "",
        placeholder="Ask something like: Show top 5 students by marks",
        label_visibility="collapsed"
    )

with col2:
    record = st.button("🎤")

# ---------------- INPUT LOGIC ----------------
question = ""

if record:
    with st.spinner("🎤 Listening..."):
        path = record_audio(duration=5)

    with st.spinner("🧠 Transcribing..."):
        question = transcribe(path)

    st.toast(f"You said: {question}")

elif text_q:
    question = text_q

# ---------------- PROCESS ----------------
if question:
    with st.spinner("⚡ Thinking..."):
        answer = query(st.session_state.agent, question)
        audio_path = speak(answer)

    st.session_state.history.append({
        "q": question,
        "a": answer,
        "audio": audio_path
    })

# ---------------- CHAT UI ----------------
st.markdown("### 💬 Conversation")

for item in reversed(st.session_state.history):
    st.markdown(f'<div class="user-msg">🧑 {item["q"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="bot-msg">🤖 {item["a"]}</div>', unsafe_allow_html=True)

    st.audio(item["audio"])

# ---------------- FOOTER ACTIONS ----------------
if st.session_state.history:
    col1, col2 = st.columns([1, 5])

    with col1:
        if st.button("🗑 Clear"):
            st.session_state.history = []
            st.rerun()

    with col2:
        st.caption("Built with Streamlit • Voice + SQL AI")