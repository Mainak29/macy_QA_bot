from flask import Flask, render_template, request, session
from qa_bot import ask_question

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session usage

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_question = request.form["question"]
        answer = ask_question(user_question)
        # Append new Q&A to the session history
        session["chat_history"].append({"question": user_question, "answer": answer})
        session.modified = True  # Mark session as changed

    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/clear", methods=["POST"])
def clear():
    session.pop("chat_history", None)
    return render_template("index.html", chat_history=[])


if __name__ == "__main__":
    app.run(debug=True)
