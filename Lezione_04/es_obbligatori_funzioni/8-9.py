messages:list[str] = ["Ciao bello", "Tutto bene?", "Wow"]

def show_messages(mess:list):
    for m in mess:
        print(m)

show_messages(messages)