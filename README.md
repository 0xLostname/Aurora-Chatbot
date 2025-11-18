![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-success.svg)

# 🌌 Aurora – Self-Learning AI Chatbot (CSV-Based Memory)

Aurora is a simple Python chatbot that **learns directly from the user**.  
When she doesn’t know an answer, she asks the user to teach her — and stores the response permanently in a CSV file.  
This project demonstrates foundational AI concepts using **pure Python** and is ideal for educational purposes, assignments, and beginner projects.

---

## 🚀 Features
- 🧠 **Learns new responses** from the user  
- 📁 **Stores memory** in a CSV file (`aurora_memory.csv`)  
- 🔁 **Retains knowledge** across sessions  
- 💡 **Very lightweight** – no heavy AI libraries  
- 🖥️ Works in **Google Colab or any Python environment**  
- 🧩 Only uses Python's built-in `csv` module  

---

## 📂 Project Structure
```
Aurora-Chatbot/
│
├── aurora.py              # Main chatbot code
├── aurora_memory.csv      # Persistent memory file
├── README.md              # Project documentation
└── LICENSE                # MIT License
```

---

## ▶️ How to Run

### 1. Clone the repository
```
git clone https://github.com/0xLostname/Aurora-Chatbot.git
cd Aurora-Chatbot
```

### 2. Run the chatbot
```
python aurora.py
```

### 3. Example interaction
```
You: hello
Aurora: I don't know this. Teach me:
You: hi
Aurora: Learned.

You: hello
Aurora: hi
```

---

## 🧠 How Aurora Learns
Aurora follows a simple loop:
1. User enters a question  
2. If question exists → reply from memory  
3. If unknown → Aurora asks for the correct response  
4. User teaches the answer  
5. Answer is **saved to CSV** and remembered forever  

---

## 📝 Example Memory File (`aurora_memory.csv`)
```csv
hello,hi!
who are you,I am Aurora, a self-learning chatbot.
good morning,Good morning!
```

---

## 🧪 Requirements
- Python 3.x  
- No external libraries needed  
- Works on:
  - Windows  
  - Linux  
  - macOS  
  - Google Colab  

---

## 🌍 Applications
- Educational chatbots  
- Simple FAQ assistants  
- Demonstration of AI learning concepts  
- Data persistence examples  
- Lightweight CLI assistants  

---

## ⚠️ Limitations
- No natural language understanding  
- Exact text matching  
- Learning depends entirely on user   input  
- Incorrect teaching = incorrect memory  

---

## 📄 License
This project is licensed under the **MIT License**.  
You are free to use, modify, distribute, and build upon this project.

---

## 👤 Author
**K. Arun Tej**  
Roll No: **NC.SC.U4CSE25218**

If you found this helpful, ⭐ star the repo!
