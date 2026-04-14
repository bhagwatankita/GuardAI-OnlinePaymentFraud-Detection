# 🛡️ GuardAI: Online Payment Fraud Detection & AI Assistant

GuardAI is a hybrid financial security platform that combines traditional **Machine Learning** for high-precision fraud detection with **Generative AI** for intelligent user support. 

By utilizing the **CatBoost** algorithm and a custom **RAG (Retrieval-Augmented Generation)** pipeline, GuardAI provides both security and explainability for modern digital transactions.

---

## 🚀 Key Features

* **Real-time Fraud Prediction:** Analyzes transactions instantly using a CatBoost model optimized for high-precision ($Precision \approx 1.00$).
* **Intelligent Feature Engineering:** Calculates "Balance Inaccuracy" (mismatches between transaction amounts and balance changes) to identify fraudulent patterns.
* **Context-Aware AI Assistant:** A built-in chatbot powered by **Google Gemini 2.0 Flash** and **Agno (Phidata)** that answers user queries about transaction fields and security alerts.
* **Vector Search Knowledge Base:** Uses **PostgreSQL with pgvector** to store and retrieve application documentation for the chatbot.
* **Modern Web UI:** A clean, responsive dashboard built with **Flask** and **Bootstrap 5**.

---

## 📂 Project Structure

```text
├── app.py                      # Main Flask Backend & Routes
├── agent.py                    # AI Agent & RAG Pipeline Configuration
├── data_cleaning_training.py   # ML Model Training & Threshold Optimization
├── knowledgebase.txt           # Documentation for the AI Assistant
├── perfect_fraud_model.cbm     # Pre-trained CatBoost Model
├── best_threshold.txt          # Saved optimal decision threshold
├── templates/                  # HTML Frontend Files
│   ├── home.html
│   ├── predict.html
│   └── submit.html
└── requirements.txt            # Python Dependencies

🛠️ Technical Stack
Backend: Python (Flask)

Machine Learning: CatBoost, Scikit-learn, Pandas, NumPy

Generative AI: Google Gemini 2.0 Flash, Agno Framework (Phidata)

Database: PostgreSQL + pgvector (Vector Database)

Frontend: Bootstrap 5, Animate.css

📊 Dataset
The model is trained on the Online Payments Fraud Detection Dataset from Kaggle.

Source: Kaggle Dataset Link

Size: ~6.3 Million rows (Note: dataset.csv is excluded from this repo due to size; please download it manually for training).

⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/bhagwatankita/GuardAI-OnlinePaymentFraud-Detection.git](https://github.com/bhagwatankita/GuardAI-OnlinePaymentFraud-Detection.git)
cd GuardAI-OnlinePaymentFraud-Detection
2. Set Up Virtual Environment (Recommended)
Bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Database Setup
Ensure you have PostgreSQL installed with the pgvector extension.

Create a database named OnlinePaymentFraudAgentDB.

Update the db_url in agent.py with your credentials:

Python
db_url = "postgresql+psycopg://user:password@localhost:5432/OnlinePaymentFraudAgentDB"
5. Environment Variables
You need a Google AI API Key for the chatbot. Set it in your environment or directly in agent.py:

Python
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
🚀 Running the Application
Train the Model (Optional)
If you wish to re-train the model or optimize the threshold:

Bash
python data_cleaning_training.py
Start the Flask App
Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000.
