from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Medical chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to MedCare Center. How can I assist you today?"
    elif "hours" in user_input or "open" in user_input:
        return "We're open Monday to Friday, 8 AM to 6 PM. Closed on weekends."
    elif "appointment" in user_input:
        return "You can book an appointment by calling (123) 456-7890 or visiting our website."
    elif "emergency" in user_input:
        return "For emergencies, please call 911 or visit the nearest emergency room."
    elif "departments" in user_input:
        return "We offer Pediatrics, Cardiology, Dermatology, General Medicine, and more."
    elif "location" in user_input or "where" in user_input:
        return "We are located at 123 Health St., Wellness City."
    elif "thank" in user_input:
        return "You're welcome! Stay healthy!"
    elif "bye" in user_input:
        return "Goodbye! Take care and feel free to chat anytime."
    else:
        return "Sorry, I didn't understand that. Please ask about hours, appointments, departments, or emergencies."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
