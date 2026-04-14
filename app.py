from flask import Flask, render_template, request
import pandas as pd
from catboost import CatBoostClassifier
from agent import agent

app = Flask(__name__)

# 1. Load the saved CatBoost model
model = CatBoostClassifier()
model.load_model("perfect_fraud_model.cbm")

# The threshold we calculated for "perfection"
BEST_THRESHOLD = 0.9526

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')


from flask import jsonify # Add this to your imports

# ... (keep your existing model and routes) ...

@app.route('/ask_chatbot', methods=['POST'])
def ask_chatbot():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"status": "error", "response": "No message provided"}), 400

    # Call your Agno agent from agent.py
    # We use .run() to get the response object
    response = agent.run(user_message)
    
    # Extract the text content from the agent's response
    bot_text = response.content 
    
    return jsonify({"status": "success", "response": bot_text})

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # 2. Retrieve values from UI
        data = {
            'type': request.form['type'],
            'amount': float(request.form['amount']),
            'oldbalanceOrg': float(request.form['oldbalanceOrg']),
            'newbalanceOrig': float(request.form['newbalanceOrig']),
            'oldbalanceDest': float(request.form['oldbalanceDest']),
            'newbalanceDest': float(request.form['newbalanceDest'])
        }
        
        # 3. Apply the same Feature Engineering used in training
        data['errorBalanceOrig'] = data['newbalanceOrig'] + data['amount'] - data['oldbalanceOrg']
        data['errorBalanceDest'] = data['oldbalanceDest'] + data['amount'] - data['newbalanceDest']
        
        # Convert to DataFrame for the model
        query_df = pd.DataFrame([data])
        
        # 4. Get Prediction Probability
        prob = model.predict_proba(query_df)[0][1]
        
        # 5. Determine result based on optimal threshold
        if prob >= BEST_THRESHOLD:
            prediction = "FRAUD DETECTED"
            res_class = "fraud"
        else:
            prediction = "TRANSACTION IS LEGITIMATE"
            res_class = "legit"
            
        return render_template('submit.html', 
                               prediction_text=prediction, 
                               result_class=res_class)

if __name__ == "__main__":
    app.run(debug=True)