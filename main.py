"""
Vessel Operations Management System
-----------------------------------
A professional, modular Flask application for vessel operations, logistics, and sustainability management.
Features:
- Intelligent navigation, routing, and predictive maintenance
- AI-powered chatbot for shipping/logistics queries
- Dynamic dashboard and API endpoints
- Robust error handling and logging

Author: Your Company Name
"""

# Refactored Flask application for better modularity and error handling

# This is the main entry point for the application.
# Features to be implemented:
# - Intelligent navigation
# - Optimized routing
# - Predictive maintenance

# Import necessary libraries
import random
import time
import os
from flask import Flask, render_template, request, jsonify, redirect, flash
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import logging
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import requests
from apscheduler.schedulers.background import BackgroundScheduler

# Ensure the instance directory exists
instance_dir = os.path.join(os.getcwd(), 'instance')
if not os.path.exists(instance_dir):
    os.makedirs(instance_dir)
    print(f"Created missing directory: {instance_dir}")

# Check if the database file exists and is accessible
db_path = os.path.join(instance_dir, 'vessel_operations.db')
try:
    if not os.path.exists(db_path):
        print(f"Database file not found at {db_path}. It will be created automatically.")
        open(db_path, 'w').close()  # Create an empty database file
    else:
        # Test if the database file is accessible
        with open(db_path, 'r') as db_file:
            pass
except IOError as e:
    print(f"Error accessing database file: {e}. Recreating the database file.")
    open(db_path, 'w').close()  # Recreate the database file

# Update the database URI to use an absolute path
absolute_db_path = os.path.abspath(db_path)

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{absolute_db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set the secret key for session management
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define database models
class Vessel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

class Logistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shipment_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    delay = db.Column(db.Integer, nullable=False)

class Sustainability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vessel_name = db.Column(db.String(100), nullable=False)
    fuel_consumption = db.Column(db.Float, nullable=False)
    emissions = db.Column(db.Float, nullable=False)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize the database
with app.app_context():
    db.create_all()

# Function to automate vessel scheduling
def automate_scheduling():
    print("Automating vessel scheduling...")
    # Example: Randomly assign berths to vessels
    vessels = ["Vessel A", "Vessel B", "Vessel C"]
    berths = ["Berth 1", "Berth 2", "Berth 3"]
    schedule = {vessel: random.choice(berths) for vessel in vessels}
    print("Schedule:", schedule)

# Function to optimize resource allocation
def optimize_resources():
    print("Optimizing resource allocation...")
    # Example: Allocate cranes based on cargo weight
    cargo_weights = {"Vessel A": 100, "Vessel B": 200, "Vessel C": 150}
    cranes = ["Crane 1", "Crane 2", "Crane 3"]
    allocation = {vessel: cranes[i % len(cranes)] for i, vessel in enumerate(cargo_weights)}
    print("Resource Allocation:", allocation)

# Function for intelligent operations
def intelligent_operations():
    print("Running intelligent operations...")
    # Example: Predict delays based on weather conditions
    weather_conditions = ["Clear", "Rainy", "Stormy"]
    delays = {condition: random.randint(0, 5) for condition in weather_conditions}
    print("Predicted Delays (hours):", delays)

# Initialize the Hugging Face text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Load GPT-2 model and tokenizer
gpt2_model_name = "gpt2"
gpt2_tokenizer = AutoTokenizer.from_pretrained(gpt2_model_name)
gpt2_model = AutoModelForCausalLM.from_pretrained(gpt2_model_name)

# Switch to GPT-Neo model and tokenizer
gpt_neo_model_name = "EleutherAI/gpt-neo-1.3B"
gpt_neo_tokenizer = AutoTokenizer.from_pretrained(gpt_neo_model_name)
gpt_neo_model = AutoModelForCausalLM.from_pretrained(gpt_neo_model_name)

# Function for AI-powered communication
def ai_chatbot(prompt):
    try:
        # Add detailed context and examples to the prompt
        contextual_prompt = (
            "You are a helpful assistant specializing in shipping and logistics. "
            "Answer the following query with detailed and accurate information. "
            "Examples: \n"
            "1. Query: What is shipping?\n"
            "   Answer: Shipping is the process of transporting goods from one location to another, typically using ships, trucks, or planes.\n"
            "2. Query: What is a shipping label?\n"
            "   Answer: A shipping label is a document attached to a package that contains information about the sender, recipient, and delivery details.\n"
            f"Query: {prompt}\n"
        )
        inputs = gpt_neo_tokenizer(contextual_prompt, return_tensors="pt")
        outputs = gpt_neo_model.generate(inputs.input_ids, max_length=150, num_return_sequences=1)
        response = gpt_neo_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        logging.error(f"GPT-Neo Model Error: {e}")
        return f"Error: {str(e)}"

# Function for intelligent monitoring
def intelligent_monitoring():
    print("Monitoring vessel operations for sustainability...")
    # Example: Monitor fuel consumption and emissions
    vessels = ["Vessel A", "Vessel B", "Vessel C"]
    fuel_consumption = {vessel: random.uniform(50, 100) for vessel in vessels}  # in liters/hour
    emissions = {vessel: fuel * 2.68 for vessel, fuel in fuel_consumption.items()}  # CO2 emissions in kg
    print("Fuel Consumption (liters/hour):", fuel_consumption)
    print("Emissions (kg CO2):", emissions)
    return {"fuel_consumption": fuel_consumption, "emissions": emissions}

# Function for optimized resource management
def optimized_resource_management():
    print("Optimizing resources for sustainability...")
    # Example: Allocate resources to minimize emissions
    vessels = ["Vessel A", "Vessel B", "Vessel C"]
    cranes = ["Crane 1", "Crane 2", "Crane 3"]
    allocation = {vessel: cranes[i % len(cranes)] for i, vessel in enumerate(vessels)}
    print("Optimized Resource Allocation:", allocation)
    return allocation

# Function for data-driven reporting
def sustainability_report():
    print("Generating sustainability report...")
    monitoring_data = intelligent_monitoring()
    resource_data = optimized_resource_management()
    report = {
        "monitoring_data": monitoring_data,
        "resource_data": resource_data,
        "summary": "Sustainability metrics calculated successfully."
    }
    print("Sustainability Report:", report)
    return report

# Function for real-time tracking
def real_time_tracking():
    print("Tracking shipments in real-time...")
    # Example: Simulate tracking data
    shipments = ["Shipment A", "Shipment B", "Shipment C"]
    locations = {shipment: f"Location {random.randint(1, 100)}" for shipment in shipments}
    print("Real-time Locations:", locations)
    return locations

# Function for predictive forecasting
def predictive_forecasting():
    print("Performing predictive forecasting...")
    # Example: Predict delays based on historical data
    shipments = ["Shipment A", "Shipment B", "Shipment C"]
    delays = {shipment: random.randint(0, 5) for shipment in shipments}  # Delays in hours
    print("Predicted Delays (hours):", delays)
    return delays

# Function for automated processing
def automated_processing():
    print("Automating logistics processing...")
    # Example: Automate scheduling
    shipments = ["Shipment A", "Shipment B", "Shipment C"]
    schedules = {shipment: f"Scheduled at {random.randint(1, 24)}:00" for shipment in shipments}
    print("Automated Schedules:", schedules)
    return schedules

# Function for intelligent navigation
def intelligent_navigation(vessel_name, destination):
    print(f"Calculating navigation for {vessel_name} to {destination}...")
    # Example: Simulate route suggestions
    route = f"Route for {vessel_name} to {destination} via optimal path."
    return route

# Function for optimized routing
def optimized_routing(vessel_name):
    print(f"Optimizing route for {vessel_name}...")
    # Example: Simulate optimized route based on fuel efficiency
    optimized_route = f"Optimized route for {vessel_name} with minimal fuel consumption."
    return optimized_route

# Function for predictive maintenance
def predictive_maintenance(vessel_name):
    print(f"Predicting maintenance schedule for {vessel_name}...")
    # Example: Simulate maintenance prediction
    maintenance_schedule = f"Maintenance for {vessel_name} is due in 30 days."
    return maintenance_schedule

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/logistics')
def logistics():
    return render_template('logistics.html')

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')

@app.route('/vessel_operations', methods=['GET', 'POST'])
def vessel_operations():
    if request.method == 'POST':
        vessel_name = request.form.get('vessel_name')
        destination = request.form.get('destination')

        navigation = intelligent_navigation(vessel_name, destination)
        routing = optimized_routing(vessel_name)
        maintenance = predictive_maintenance(vessel_name)

        return render_template('vessel_operations.html', 
                               vessel_name=vessel_name, 
                               destination=destination, 
                               navigation=navigation, 
                               routing=routing, 
                               maintenance=maintenance)
    else:
        # Fetch all vessels from the database
        vessels = Vessel.query.all()
        return render_template('vessel_operations.html', vessels=vessels)

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    """
    Renders the AI Assistant page and handles chat requests.
    Passes navigation context for integration with navigation bar.
    """
    if request.method == 'POST':
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({"response": "Please enter a message."}), 400
        bot_response = ai_chatbot(user_message)
        return jsonify({"response": bot_response})
    # Pass navigation context for integration with navigation bar
    return render_template('chat.html', active_page='chatbot')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form.get('user_input')
    if not user_input:
        return render_template('index.html', result="Please provide input.")

    # Example processing logic
    result = f"Processed input: {user_input}"
    return render_template('index.html', result=result)

# Utility: Get SQLite connection (for raw SQL operations)
def get_db_connection():
    return sqlite3.connect('instance/vessel_operations.db')

# Health check endpoint for monitoring
@app.route('/api/health', methods=['GET'])
def health_check():
    try:
        conn = get_db_connection()
        conn.execute("SELECT 1")
        conn.close()
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return jsonify({"status": "error", "details": str(e)}), 500

# Route to handle feedback submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.get('feedback')
    comments = request.form.get('comments')

    if not feedback:
        flash('Feedback is required!', 'danger')
        return redirect('/vessel_operations')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            feedback TEXT NOT NULL,
                            comments TEXT,
                            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )''')
        cursor.execute('INSERT INTO feedback (feedback, comments) VALUES (?, ?)', (feedback, comments))
        conn.commit()
        conn.close()
        flash('Thank you for your feedback!', 'success')
        logging.info("Feedback submitted successfully.")
    except Exception as e:
        flash(f'An error occurred: {e}', 'danger')
        logging.error(f"Feedback submission failed: {e}")

    return redirect('/vessel_operations')

# API endpoint for chatbot integration (uses ai_chatbot)
@app.route('/api/chat', methods=['POST'])
def chat():
    """
    AI-powered chatbot endpoint.
    Expects JSON: { "message": "your question" }
    Returns: { "response": "AI answer" }
    """
    user_message = request.json.get('message', '')
    if not user_message:
        logging.warning("No message provided to chatbot endpoint.")
        return jsonify({'error': 'No message provided'}), 400
    response = ai_chatbot(user_message)
    logging.info("Chatbot response generated.")
    return jsonify({'response': response})

# API documentation endpoint
@app.route('/api/docs', methods=['GET'])
def api_docs():
    """
    Returns API documentation for available endpoints.
    """
    docs = {
        "endpoints": [
            {"path": "/api/chat", "method": "POST", "description": "AI-powered chatbot"},
            {"path": "/api/export", "method": "GET", "description": "Export vessel operation data as CSV"},
            {"path": "/dashboard", "method": "GET", "description": "Dashboard with key metrics"},
            {"path": "/api/health", "method": "GET", "description": "Health check for API"},
            # ...add more as needed...
        ]
    }
    return jsonify(docs)

# Dashboard route to showcase dynamic metrics
@app.route('/dashboard')
def dashboard():
    """
    Dashboard displaying dynamic vessel, logistics, and sustainability metrics.
    """
    try:
        vessels = Vessel.query.all()
        logistics = Logistics.query.all()
        sustainability = Sustainability.query.all()
        vessel_count = Vessel.query.count()
        shipment_count = Logistics.query.count()
        avg_fuel = db.session.query(db.func.avg(Sustainability.fuel_consumption)).scalar() or 0
        avg_emissions = db.session.query(db.func.avg(Sustainability.emissions)).scalar() or 0
        return render_template(
            'dashboard.html',
            vessels=vessels or [],
            logistics=logistics or [],
            sustainability=sustainability or [],
            vessel_count=vessel_count,
            shipment_count=shipment_count,
            avg_fuel=round(avg_fuel, 2),
            avg_emissions=round(avg_emissions, 2),
            active_page='dashboard'
        )
    except Exception as e:
        logging.error(f"Dashboard data fetch failed: {e}")
        return render_template('dashboard.html', vessels=[], logistics=[], sustainability=[], vessel_count=0, shipment_count=0, avg_fuel=0, avg_emissions=0, error=str(e), active_page='dashboard')

# API endpoint to export vessel operation data as CSV (robust and dynamic)
@app.route('/api/export', methods=['GET'])
def export_data():
    """
    Export vessel operation data as CSV.
    Returns CSV or JSON error.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='operations'")
        if not cursor.fetchone():
            logging.warning("No operations data found for export.")
            return jsonify({"error": "No operations data found."}), 404
        cursor.execute("SELECT * FROM operations")
        rows = cursor.fetchall()
        col_names = [description[0] for description in cursor.description]
        csv_data = ",".join(col_names) + "\n"
        for row in rows:
            csv_data += ",".join(map(str, row)) + "\n"
        conn.close()
        logging.info("Operations data exported as CSV.")
        return csv_data, 200, {'Content-Type': 'text/csv'}
    except Exception as e:
        logging.error(f"Export failed: {e}")
        return jsonify({"error": str(e)}), 500

# Function to populate the database with sample data
def populate_database():
    # Add sample vessels
    vessels = [
        Vessel(name="Vessel A", destination="Port X", status="In Transit"),
        Vessel(name="Vessel B", destination="Port Y", status="Docked"),
        Vessel(name="Vessel C", destination="Port Z", status="Maintenance")
    ]
    db.session.bulk_save_objects(vessels)

    # Add sample logistics data
    logistics = [
        Logistics(shipment_name="Shipment A", location="Location 45", delay=2),
        Logistics(shipment_name="Shipment B", location="Location 78", delay=4),
        Logistics(shipment_name="Shipment C", location="Location 12", delay=1)
    ]
    db.session.bulk_save_objects(logistics)

    # Add sample sustainability data
    sustainability = [
        Sustainability(vessel_name="Vessel A", fuel_consumption=54.56, emissions=146.23),
        Sustainability(vessel_name="Vessel B", fuel_consumption=67.46, emissions=180.80),
        Sustainability(vessel_name="Vessel C", fuel_consumption=77.18, emissions=206.84)
    ]
    db.session.bulk_save_objects(sustainability)

    db.session.commit()
    print("Sample data added to the database.")

# Wrap database population in an application context
with app.app_context():
    populate_database()

def fetch_live_vessel_data():
    """
    Fetch live vessel data from a public API (replace with a real API endpoint and key).
    Returns a list of vessel dicts: [{name, destination, status}, ...]
    """
    try:
        # Example: Replace with a real vessel tracking API
        # response = requests.get('https://api.example.com/vessels?apikey=YOUR_KEY')
        # data = response.json()
        # For demo, return mock data
        data = [
            {"name": "Vessel A", "destination": "Port X", "status": "In Transit"},
            {"name": "Vessel B", "destination": "Port Y", "status": "Docked"},
            {"name": "Vessel C", "destination": "Port Z", "status": "Maintenance"}
        ]
        return data
    except Exception as e:
        logging.error(f"Failed to fetch vessel data: {e}")
        return []

def update_vessel_table():
    """
    Fetch live vessel data and update the Vessel table in the database.
    """
    with app.app_context():
        vessels = fetch_live_vessel_data()
        if vessels:
            Vessel.query.delete()  # Clear old data
            for v in vessels:
                vessel = Vessel(name=v["name"], destination=v["destination"], status=v["status"])
                db.session.add(vessel)
            db.session.commit()
            logging.info("Vessel table updated with live data.")
        else:
            logging.warning("No vessel data to update.")

# Set up APScheduler to update vessel data every 10 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(update_vessel_table, 'interval', minutes=10)
scheduler.start()

@app.route('/api/vessels')
def api_vessels():
    vessels = Vessel.query.all()
    data = [{"name": v.name, "destination": v.destination, "status": v.status} for v in vessels]
    return jsonify(data)

@app.route('/api/sustainability')
def api_sustainability():
    data = Sustainability.query.all()
    return jsonify([
        {
            'vessel_name': s.vessel_name,
            'fuel_consumption': s.fuel_consumption,
            'emissions': s.emissions
        } for s in data
    ])

@app.route('/api/logistics')
def api_logistics():
    data = Logistics.query.all()
    return jsonify([
        {
            'shipment_name': l.shipment_name,
            'delay': l.delay
        } for l in data
    ])

if __name__ == '__main__':
    # Ensure database tables exist and sample data is loaded
    with app.app_context():
        db.create_all()
        # Only populate if tables are empty to avoid duplicate data
        if Vessel.query.count() == 0 and Logistics.query.count() == 0 and Sustainability.query.count() == 0:
            populate_database()
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("Welcome to the Vessel Operations Application!")
    automate_scheduling()
    optimize_resources()
    intelligent_operations()