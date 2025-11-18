# Aurora – Self-Learning AI Chatbot Using CSV Memory

Aurora is a simple Python-based chatbot that learns directly from the user.  
When Aurora encounters a question she doesn’t recognize, she asks the user to teach her.  
All learned responses are saved permanently in a CSV file and loaded again on the next run.

---

## Features
- Learns new responses from the user
- Stores memory in a CSV file
- Persistent knowledge across sessions
- Minimal Python code
- Works in Google Colab or any Python environment
- No external libraries needed except `csv`

---

## How It Works
1. User types a message  
2. Aurora checks the CSV memory  
3. If the message exists → responds  
4. If not → asks the user to teach the correct response  
5. Aurora saves the new answer to `aurora_memory.csv`  

---

## File Structure
```
|-- aurora.py
|-- aurora_memory.csv
|-- README.md
|-- LICENSE
```

---

## Running the Chatbot

### Step 1: Run the script
```
python aurora.py
```

### Step 2: Chat with Aurora
Example:
```
You: hello
Aurora: I don't know this. Teach me:
You: hi
Aurora: Learned.

You: hello
Aurora: hi
```

---

## Example Memory File
```csv
hello,hi
who are you,I am Aurora, a self-learning chatbot.
good morning,Good morning!
```

---

## Requirements
- Python 3.x
- Built-in `csv` module (no installation needed)

---

## Applications
- Educational demos
- Simple chat systems
- FAQ bots
- Introductory AI projects
- Beginner-level learning tool

---

## Limitations
- Exact text matching only
- No advanced NLP
- Learning depends on user input
- Incorrect teaching results in incorrect outputs

---

## License
This project is licensed under the MIT License.  
See the **LICENSE** file for details.

---

## Author
**K. Arun Tej**  
Roll No.: **NC.SC.U4CSE25218**

