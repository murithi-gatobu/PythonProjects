from tkinter import *

# Dictionary of predefined responses
responses = {
    "hi": "hello",
    "hello": "hi",
    "how are you?": "I'm fine, and you?",
    "i'm fine too": "Nice to hear that.",
    "where is the library?": "It's next to the main administration block.",
    "who is the dean?": "The dean is Prof. Wanjiru.",
    "what's the wifi password?": "Check your student portal under 'IT Support'.",
    "where is the cafeteria?": "It's beside the student center.",
    "exam timetable": "You can find it on the notice board or the student portal."
}

# Function to handle user input and bot response
def send():
    user_message = e.get().strip().lower()
    if user_message == "":
        return  # ignore empty messages

    text.config(state=NORMAL)
    text.insert(END, "\nYou: " + user_message)

    # Get bot response
    bot_response = responses.get(user_message, "Sorry, I didn't get it.")
    text.insert(END, "\nBot: " + bot_response)
    text.config(state=DISABLED)
    text.see(END)  # Auto-scroll to bottom

    e.delete(0, END)  # Clear input field


# GUI setup
root = Tk()
root.title('Simple College Info Chatbot')
root.geometry('600x400')

# Chat display area with scrollbar
text_frame = Frame(root)
text_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(text_frame, bg='light blue', width=70, height=20, wrap=WORD, yscrollcommand=scrollbar.set, state=DISABLED)
text.pack()

scrollbar.config(command=text.yview)

# User input field
e = Entry(root, width=70)
e.grid(row=1, column=0, padx=10, pady=5)

# Send button
send_btn = Button(root, text='Send', bg='blue', fg='white', width=15, command=send)
send_btn.grid(row=1, column=1, padx=5, pady=5)

# Allow pressing Enter to send
root.bind('<Return>', lambda event: send())

# Start the GUI event loop
root.mainloop()
