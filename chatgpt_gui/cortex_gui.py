import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QColor

import openai

openai.api_key = "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"

messages = [{"role": "system", "content": "You are the smartest AI on earth"}]

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CORTEX: Chat with an AI Assistant")
        self.initUI()

    def initUI(self):
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setPlaceholderText("Chat history will be displayed here.")
        self.chat_display.setStyleSheet("background-color: white; color: black;")

        self.user_entry = QTextEdit()
        self.user_entry.setPlaceholderText("Type your message here and press Enter to send.")
        self.user_entry.setStyleSheet("background-color: white; color: black;")

        send_button = QPushButton("Send")
        send_button.setStyleSheet("background-color: #4CAF50; color: white;")
        send_button.clicked.connect(self.send_message)

        vbox = QVBoxLayout()
        vbox.addWidget(self.chat_display)
        vbox.addWidget(self.user_entry)

        hbox = QHBoxLayout()
        hbox.addWidget(send_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # Increase the size of the window
        self.resize(600, 400)

    def send_message(self):
        user_input = self.user_entry.toPlainText().strip()
        if user_input:
            # Clear the chat history before appending new messages
            self.chat_display.clear()

            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            self.chat_display.append("You: " + user_input)
            self.chat_display.append("AI Assistant: " + ChatGPT_reply)
            self.chat_display.append("-----------------------------------------")
            self.user_entry.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
