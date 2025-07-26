# 🎓 AI Career Counsellor Chatbot

An intelligent career guidance chatbot that suggests career paths based on a user's education level and interests. Built using Rasa and optionally powered by GPT-3.5.

## 🔧 Technologies Used
- Python
- Rasa Open Source
- Streamlit (for UI)
- GPT-3.5 (OpenAI, fallback supported)
- YAML

## 🚀 Features
- Natural language input
- Slot extraction for education & interest
- Rule-based + GPT-based suggestions
- Extendable for quizzes, resume tips

## 💡 Sample Conversation

🧑‍💻 You: hi 

🤖 Bot: Hi! I'm your Career Counsellor Bot 🤖. What is your current education level? (10th, 11th, PUC, UG, PG)

🧑‍💻 You: 10th

🤖 Bot: Nice! What are your favorite subjects or interests?

🧑‍💻 You: science

🤖 Bot: 🤔 Based on your input, here are some suggestions:

🤖 Bot: 🔬 You're at the school level and interested in science. You can choose **PCMB or PCMC** in PUC. Later, explore **MBBS, Engineering, B.Sc (Physics/Chemistry/Biology)**, or even **Research & Teaching** roles.

🧑‍💻 You: i like coding

🤖 Bot: 🤔 Based on your input, here are some suggestions:

🤖 Bot: 💻 You seem interested in tech! Opt for **PCMC in PUC**, then pursue **BCA, BSc CS, or BE in CSE/AI**. You’ll have great scope in software and AI careers


## 🔍 Folder Structure
- `actions/`: Custom career suggestion logic
- `data/`: Intents, training stories, rules
- `domain.yml`: Slot/intent definitions
- `config.yml`: Rasa pipeline
- `requirements.txt`: Dependencies

## 📦 Setup

```bash
pip install -r requirements.txt
rasa train
rasa run actions
rasa shell
