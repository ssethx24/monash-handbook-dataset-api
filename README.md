# 📚 Monash Handbook Dataset API

This project provides a **REST API** that serves Monash University handbook unit data.  
The dataset was scraped from the official Monash Handbook and contains ~5124 units (2025 edition).  

The API is built with **Flask (Python)** and deployed on **Render**.

---

## 🚀 Live API Endpoint

Base URL:  
https://monash-handbook-dataset-api.onrender.com


You can make requests to this URL using your browser, `curl`, Postman, or any HTTP client.

---

## 📌 Endpoints

### 🔹 Health Check
GET /health

Returns a simple status message to confirm the API is running.

**Example:**  
(https://monash-handbook-dataset-api.onrender.com/health)

```json
{
  "status": "ok"
}
🔹 All Units
bash
Copy code
GET /units
Returns all units in JSON format.

Example:
https://monash-handbook-dataset-api.onrender.com/units

🔹 Search Units
bash
Copy code
GET /units?q=<keyword>
Filter units by keyword in code or title.

Example:
https://monash-handbook-dataset-api.onrender.com/units?q=fit

json
Copy code
[
  {
    "common": {
      "code": "FIT3175",
      "title": "Usability",
      "faculty": "Faculty of Information Technology",
      "link": "https://handbook.monash.edu/2025/units/FIT3175"
    },
    "synopsis": "This unit explores the underpinning theories, principles and practices of interface design..."
  }
]
🔹 Get Specific Unit
bash
Copy code
GET /units/<unit_code>
Retrieve details of a specific unit by its code.

Example:
https://monash-handbook-dataset-api.onrender.com/units/FIT3175

json
Copy code
{
  "common": {
    "code": "FIT3175",
    "title": "Usability",
    "faculty": "Faculty of Information Technology",
    "link": "https://handbook.monash.edu/2025/units/FIT3175"
  },
  "synopsis": "This unit explores the underpinning theories, principles and practices of interface design...",
  "unit_level": "Level 3",
  "credit_points": 6,
  "learning_outcomes": [
    {"code": "ULO1", "description": "Explain the theories and principles of usability..."},
    {"code": "ULO2", "description": "Apply usability principles to the design of interfaces..."}
  ]
}
🛠️ Local Development
Clone the repo:

bash
Copy code
git clone https://github.com/<your-username>/monash-handbook-dataset-api.git
cd monash-handbook-dataset-api
Create a virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run locally:

bash
Copy code
python app.py
Access at:
http://127.0.0.1:8080

📦 Deployment
The API is deployed on Render.
Any changes pushed to the main branch will auto-deploy to the live API.

✨ Use Case
This API can be used for:

Building a Unit Review App (students leave ratings/reviews for units).

Developing course planning tools.

Exploring academic datasets for research.

Demonstrating how to leverage REST APIs in assignments.

📜 License
This project is for educational purposes only and is not an official Monash University service.

yaml
Copy code

---

✅ This README:  
- Explains your project.  
- Shows the **live deployed link**.  
- Documents all endpoints with examples.  
- Includes **sample JSON outputs** (like the Google Books API you showed).  
- Makes it look professional for your assignment.  

Do you also want me to add **a “Tech Stack” section** (Flask, Python, Render, JSON) so it looks even more polished for submission?






You said:
can you give me this readme in a single window that i can copy


ChatGPT said:
Of course 👍 here’s the full README.md in one block so you can just copy–paste it directly:

markdown
Copy code
# 📚 Monash Handbook Dataset API

This project provides a **REST API** that serves Monash University handbook unit data.  
The dataset was scraped from the official Monash Handbook and contains ~5124 units (2025 edition).  

The API is built with **Flask (Python)** and deployed on **Render**.

---

## 🚀 Live API Endpoint

Base URL:  
https://monash-handbook-dataset-api.onrender.com

yaml
Copy code

You can make requests to this URL using your browser, `curl`, Postman, or any HTTP client.

---

## 📌 Endpoints

### 🔹 Health Check
GET /health

pgsql
Copy code
Returns a simple status message to confirm the API is running.

**Example:**  
[https://monash-handbook-dataset-api.onrender.com/health](https://monash-handbook-dataset-api.onrender.com/health)

```json
{
  "status": "ok"
}
🔹 All Units
bash
Copy code
GET /units
Returns all units in JSON format.

Example:
https://monash-handbook-dataset-api.onrender.com/units

🔹 Search Units
bash
Copy code
GET /units?q=<keyword>
Filter units by keyword in code or title.

Example:
https://monash-handbook-dataset-api.onrender.com/units?q=fit

json
Copy code
[
  {
    "common": {
      "code": "FIT3175",
      "title": "Usability",
      "faculty": "Faculty of Information Technology",
      "link": "https://handbook.monash.edu/2025/units/FIT3175"
    },
    "synopsis": "This unit explores the underpinning theories, principles and practices of interface design..."
  }
]
🔹 Get Specific Unit
bash
Copy code
GET /units/<unit_code>
Retrieve details of a specific unit by its code.

Example:
https://monash-handbook-dataset-api.onrender.com/units/FIT3175


🛠️ Local Development
Clone the repo:

bash
Copy code
git clone https://github.com/<your-username>/monash-handbook-dataset-api.git
cd monash-handbook-dataset-api
Create a virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run locally:


Access at:
http://127.0.0.1:8080

📦 Deployment
The API is deployed on Render.
Any changes pushed to the main branch will auto-deploy to the live API.

✨ Use Case
This API can be used for:

Building a Unit Review App (students leave ratings/reviews for units).

Developing course planning tools.

Exploring academic datasets for research.

Demonstrating how to leverage REST APIs in assignments.

📜 License
This project is for educational purposes only and is not an official Monash University service.



