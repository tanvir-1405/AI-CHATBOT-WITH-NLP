# 📦 Importing required libraries
import re  # For checking user messages using patterns
import tkinter as tk  # For making the GUI window
from tkinter import scrolledtext  # For adding a scrollable chat area
from PIL import Image, ImageTk, ImageSequence  # For showing the animated GIF

# 💬 Handling user messages and giving chatbot replies
def get_response(user_input):
    user_input = user_input.lower()
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hi there! I'm Pari 💖"
    elif "how are you" in user_input:
        return "I'm sparkly and happy! ✨ How about you?"
    elif "your name" in user_input:
        return "I'm Pari, your pastel chatbot 🌸"
    elif "who made you" in user_input:
        return "A kind human who loves pastel pinks! 🌷"
    elif "what can you do" in user_input:
        return "I can chat, cheer you up, and be your soft bestie 💬"
    elif "sad" in user_input or "upset" in user_input:
        return "Aww, sending you big virtual hugs 🤗"
    elif "joke" in user_input:
        return "Why was the computer cold? It left its Windows open! 😂"
    elif "love me" in user_input:
        return "Of course! 💖 You're my favorite human!"
    elif "weather" in user_input:
        return "I live in cyberspace, but I hope it’s sunny in your heart ☀️"
    elif "cute" in user_input:
        return "Aww! You're making me blush 💞"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Bye bye! Come back soon! 💫"
    else:
        return "Hmm, I'm not sure about that yet 💭 Can you ask me something else?"

# 📨 Sending the user message and getting a reply from Pari
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_area.insert(tk.END, f"You: {user_input}\n", "user")  # Showing user's message
    response = get_response(user_input)  # Getting Pari's response
    chat_area.insert(tk.END, f"Pari: {response}\n\n", "bot")  # Showing Pari's reply
    user_entry.delete(0, tk.END)  # Clearing input box after sending

# 🪟 Creating the main window
root = tk.Tk()
root.title("Chat with Pari 🌸")
root.configure(bg="black")

# 🧸 Left frame for showing animated teddy GIF
left_frame = tk.Frame(root, bg="black")
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

gif_path = "pari_teddy.gif"
try:
    # Loading and resizing GIF frames
    im = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame.copy().convert('RGBA').resize((150,150), Image.Resampling.LANCZOS))
              for frame in ImageSequence.Iterator(im)]
except Exception as e:
    print("Error loading GIF:", e)
    frames = None

gif_label = tk.Label(left_frame, bg="black")
gif_label.pack()

# 🎞️ Playing the animated teddy GIF
def animate(index=0):
    if frames:
        frame = frames[index]
        gif_label.configure(image=frame)
        index = (index + 1) % len(frames)
        root.after(100, animate, index)  # Updating frame every 100 ms
    else:
        gif_label.config(text="🐻", font=("Comic Sans MS", 72), fg="#ffc0cb")  # Fallback emoji

animate()

# 💬 Right frame for chatting area and input
right_frame = tk.Frame(root, bg="black")
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 📜 Adding the chat display area
chat_area = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, bg="black", fg="#ffc0cb", font=("Comic Sans MS", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground="#ffb6c1")
chat_area.tag_config("bot", foreground="#ffc0cb")
chat_area.insert(tk.END, "🌟 Welcome! I'm Pari — your pastel pink chatbot!\nLet's chat 💕\n\n", "bot")

# 🧾 Entry box for typing messages
user_entry = tk.Entry(right_frame, bg="#2b2b2b", fg="#ffc0cb", font=("Comic Sans MS", 12))
user_entry.pack(padx=10, pady=5, fill=tk.X)
user_entry.bind("<Return>", lambda event=None: send_message())  # Sending message on Enter key

# 📤 Send button
send_btn = tk.Button(right_frame, text="Send", command=send_message, bg="#ffc0cb", fg="black",
                     font=("Comic Sans MS", 10, "bold"), activebackground="#ff99cc")
send_btn.pack(pady=5)

# 🚀 Running the app
root.mainloop()
