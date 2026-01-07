import streamlit as st
import re
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# -----------------------------
# LLM SETUP (Groq - Free)
# -----------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key="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"
)


# -----------------------------
# External bounded memory
# -----------------------------
if "user_memory" not in st.session_state:
    st.session_state.user_memory = {}

def remember(user_id, text):
    text_l = text.lower()

    if user_id not in st.session_state.user_memory:
        st.session_state.user_memory[user_id] = {}

    # Name extraction
    name_match = re.search(r"my name is ([a-zA-Z ]+)", text_l)
    if name_match:
        st.session_state.user_memory[user_id]["name"] = name_match.group(1).strip().title()

    # Weakness extraction
    weakness_patterns = [
        r"weak in ([a-zA-Z ]+)",
        r"struggle with ([a-zA-Z ]+)",
        r"find ([a-zA-Z ]+) difficult",
        r"([a-zA-Z ]+) is hard",
        r"([a-zA-Z ]+) is challenging"
    ]

    for pattern in weakness_patterns:
        match = re.search(pattern, text_l)
        if match:
            st.session_state.user_memory[user_id]["weakness"] = match.group(1).strip()
            break
def multiply(a: int, b: int) -> int:
    return a * b
import re

def extract_multiplication(text):
    match = re.search(r"(\d+)\s*\*\s*(\d+)", text)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None

def chat(user_id, message):
    remember(user_id, message)

    mem = st.session_state.user_memory.get(user_id, {})
    memory_text = f"""
User profile:
- Name: {mem.get("name", "unknown")}
- Weak topic: {mem.get("weakness", "unknown")}
"""

    mul = extract_multiplication(message)

    if mul:
        a, b = mul
        result = multiply(a, b)

        return f"""
Let's solve this step by step 😊

We are multiplying {a} × {b}.

This means adding {b}, {a} times:
{b} + {b} + {b} = {result}

✅ Final Answer: {a} × {b} = {result}
"""

    prompt = memory_text + """
You are a friendly math tutor.

User: """ + message

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def chat(user_id, message):
    remember(user_id, message)

    mem = st.session_state.user_memory.get(user_id, {})
    memory_text = f"""
User profile:
- Name: {mem.get("name", "unknown")}
- Weak topic: {mem.get("weakness", "unknown")}
"""

    mul = extract_multiplication(message)

    if mul:
        a, b = mul
        result = multiply(a, b)

        return f"""
Let's solve this step by step 😊

We are multiplying {a} × {b}.

This means adding {b}, {a} times:
{b} + {b} + {b} = {result}

✅ Final Answer: {a} × {b} = {result}
"""

    prompt = memory_text + """
You are a friendly math tutor.

User: """ + message

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Personalized Math Tutor", page_icon="🧮")

st.title("🧮 Personalized Math Tutor Agent")
st.write("A LangChain + Groq powered AI tutor with memory")

# User ID (session-based)
user_id = st.text_input("Enter your user ID", value="student1")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input.strip():
        response = chat(user_id, user_input)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Tutor", response))

# Display chat
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Tutor:** {msg}")

