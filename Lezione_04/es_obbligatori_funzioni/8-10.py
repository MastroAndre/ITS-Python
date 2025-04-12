messages:list[str] = ["Ciao bello", "Tutto bene?", "Wow"]

sent_messages:list = []

def send_messages(mess:list) -> list:
    for m in range(len(mess)):
        sent_messages.append(messages.pop())

    print(f"messages = {messages}")
    print(f"sent messages = {sent_messages}")

send_messages(messages)