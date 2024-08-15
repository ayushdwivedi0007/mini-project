import os
import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import speech_recognition as sr

class VoiceTextConverter:
    def __init__(self, root):

        self.root = root
        self.root.title("Voice to Text / Text to Voice")
        self.root.geometry("430x240")
        self.choice_var = tk.StringVar()
        self.text_input_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):

        self.label = ttk.Label( text="Enter the text:")
        self.label.place(x=50, y=10)


        self.entry = ttk.Entry( textvariable=self.text_input_var, width=30)
        self.entry.place(x=50, y=40)


        self.radiobutton1 = ttk.Radiobutton( text="Voice to Text", variable=self.choice_var, value='1')
        self.radiobutton1.place(x=50, y=80)


        self.radiobutton2 = ttk.Radiobutton( text="Text to Voice", variable=self.choice_var, value='2')
        self.radiobutton2.place(x=50, y=110)


        self.button = ttk.Button(text="Perform Action", command=self.perform_action)
        self.button.place(x=50, y=150)

        self.label = ttk.Label(text="Made by Ayush")
        self.label.place(x=300, y=200)

        self.message_label = ttk.Label( text="")
        self.message_label.place(x=50, y=180)


    def perform_action(self):
        choice = self.choice_var.get()
        text_input = self.text_input_var.get()

        if choice == '1':
            self.voice_to_text()
        elif choice == '2':
            self.text_to_voice(text_input)
        else:
            self.message_label.config(text="Please select an option.")




    def voice_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.message_label.config(text="Say something:")

            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            self.message_label.config(text=f"You said: {text}")
        except sr.UnknownValueError:
            self.message_label.config(text="Could not understand audio")




    def text_to_voice(self, text):
        if text:
            output_path = "output.mp3"
            tts = gTTS(text=text, slow=False)
            tts.save(output_path)
            os.system(f"start {output_path}")
            self.message_label.config(text="Voice saved and played.")
        else:
            self.message_label.config(text="No text provided for conversion.")


# Main function
root = tk.Tk()
ayush = VoiceTextConverter(root)
root.mainloop()
