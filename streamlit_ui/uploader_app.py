import streamlit as st
import os
import json

st.set_page_config(page_title="\U0001f9e0 Upload + Pretrain Engine", layout="wide")
st.title("\U0001f9e0 Flowly Codex Upload + AI Pretraining Module")

st.markdown("Upload your `conversations.json` (300–400MB supported). This will convert your ChatGPT history into a structured AI training module.")

# Upload UI
uploaded_file = st.file_uploader("\U0001f4e4 Upload your Data", type=["json"])

if uploaded_file:
    os.makedirs("flowly/memory", exist_ok=True)
    save_path = os.path.join("flowly/memory", "conversations.json")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("\u2705 File uploaded and saved.")

    # Load preview
    try:
        with open(save_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        st.subheader("\U0001f9e0 Memory Summary")
        st.write(f"Threads: {len(data)}")

        st.markdown("### \U0001fa84 Training Dataset Generation Ready")
        st.code("flowly_pretrain --file flowly/memory/conversations.json --format instruct --out train_set.jsonl")

    except Exception as e:
        st.error(f"\u274c Error parsing uploaded file: {e}")
else:
    st.info("Awaiting your `conversations.json` upload.")
