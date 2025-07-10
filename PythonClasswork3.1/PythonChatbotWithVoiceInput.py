from tkinter import *
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

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

# Bot response function
def get_response(message):
    return responses.get(message, "Sorry, I didn't get it.")

# Speak a message aloud
import threading

def speak_text(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

# Handle text input
def send():
    user_message = e.get().strip().lower()
    if user_message == "":
        return
    text.config(state=NORMAL)
    text.insert(END, "\nYou: " + user_message)
    bot_reply = get_response(user_message)
    text.insert(END, "\nBot: " + bot_reply)
    speak_text(bot_reply)  # Speak the reply
    text.config(state=DISABLED)
    text.see(END)
    e.delete(0, END)

# Handle voice input
def speak():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text.config(state=NORMAL)
        text.insert(END, "\n[Listening...]")
        text.config(state=DISABLED)
        root.update()

        try:
            audio = recognizer.listen(source, timeout=5)
            voice_input = recognizer.recognize_google(audio)
            e.delete(0, END)
            e.insert(0, voice_input)
            send()  # Automatically send the recognized speech
        except sr.UnknownValueError:
            bot_msg = "Sorry, I couldn't understand you."
            text.config(state=NORMAL)
            text.insert(END, "\nBot: " + bot_msg)
            speak_text(bot_msg)
            text.config(state=DISABLED)
        except sr.RequestError:
            bot_msg = "Speech service is down."
            text.config(state=NORMAL)
            text.insert(END, "\nBot: " + bot_msg)
            speak_text(bot_msg)
            text.config(state=DISABLED)
        except sr.WaitTimeoutError:
            bot_msg = "Listening timed out."
            text.config(state=NORMAL)
            text.insert(END, "\nBot: " + bot_msg)
            speak_text(bot_msg)
            text.config(state=DISABLED)
        text.see(END)

# GUI setup
root = Tk()
root.title('College Info Chatbot with Voice')
root.geometry('650x400')

# Chat display area
text_frame = Frame(root)
text_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(text_frame, bg='light blue', width=80, height=20, wrap=WORD, yscrollcommand=scrollbar.set, state=DISABLED)
text.pack()
scrollbar.config(command=text.yview)

# Input field
e = Entry(root, width=70)
e.grid(row=1, column=0, padx=10, pady=5)

# Send button
send_btn = Button(root, text='Send', bg='blue', fg='white', width=15, command=send)
send_btn.grid(row=1, column=1)

# Voice input button
voice_btn = Button(root, text='🎤 Speak', bg='green', fg='white', width=10, command=speak)
voice_btn.grid(row=1, column=2)

# Allow Enter key to send
root.bind('<Return>', lambda event: send())

# Start GUI loop
root.mainloop()
