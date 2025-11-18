import csv
MEMORY_FILE="/content/aurora_memory.csv"
def load_memory():
    memory={}
    try:
        with open(MEMORY_FILE, "r") as f:
            for q,a in csv.reader(f):
                memory[q]=a
    except:
        pass
    return memory
def save_memory(q, a):
    with open(MEMORY_FILE,"a",newline="") as f:
        csv.writer(f).writerow([q,a])
memory=load_memory()
pending=None
print("Aurora online. Type 'exit' to stop.\n")
while True:
    msg=input("You: ").lower().strip()
    if msg=="exit":
        print("Aurora: Goodbye.")
        break
    if pending:
        memory[pending]=msg
        save_memory(pending,msg)
        print("Aurora: Learned.")
        pending = None
        continue
    if msg in memory:
        print("Aurora:",memory[msg])
    else:
        print("Aurora: I don’t know this. Teach me:")
        pending=msg