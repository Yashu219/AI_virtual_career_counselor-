import streamlit as st
import requests

st.set_page_config(page_title="Career Counsellor Bot", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .stApp {
        background: linear-gradient(to bottom right, #ffe4ec, #fceaff);
        padding: 2rem;
        border-radius: 20px;
    }
    .bot-msg {
        background-color: #fff;
        padding: 0.9rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        border-left: 5px solid #ff69b4;
    }
    .user-msg {
        background-color: #f9f3f3;
        padding: 0.9rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        border-left: 5px solid #a29bfe;
    }
    </style>
""", unsafe_allow_html=True)

st.title("AI Career Counsellor")
st.write("Talk to your personal guide to find the perfect career path💬")

# Store chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to fetch bot reply
def get_bot_response(message):
    payload = {"sender": "user", "message": message}
    response = requests.post("http://localhost:5005/webhooks/rest/webhook", json=payload)
    bot_messages = [r.get("text") for r in response.json()]
    return bot_messages

# Show chat messages in proper order (top to bottom)
chat_html = ""
for role, msg in st.session_state.messages:
    if role == "user":
        chat_html += f"<div class='user-msg'><strong>👩 You:</strong> {msg}</div>"
    else:
        chat_html += f"<div class='bot-msg'><strong>🤖 Bot:</strong> {msg}</div>"

# Wrap in a scrollable box
st.markdown(f"""
    <div style='height: 400px; overflow-y: auto; padding-right:10px'>
        {chat_html}
    </div>
""", unsafe_allow_html=True)

# Input bar (appears below chat now)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You: ", "")
    submit = st.form_submit_button("Send")

if submit and user_input:
    st.session_state.messages.append(("user", user_input))
    bot_replies = get_bot_response(user_input)
    for reply in bot_replies:
        st.session_state.messages.append(("bot", reply))