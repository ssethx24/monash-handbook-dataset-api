# 📚 Monash Handbook Dataset API

This project provides a **REST API** that serves Monash University handbook unit data.
The dataset was scraped from the official Monash Handbook and contains \~5124 units (2025 edition).

The API is built with **Flask (Python)** and deployed on **Render**.

---

## 🚀 Live API Endpoint

Base URL:
**[https://monash-handbook-dataset-api.onrender.com](https://monash-handbook-dataset-api.onrender.com)**

You can make requests to this URL using your browser, `curl`, Postman, or any HTTP client.

---

## 📌 Endpoints

### 🔹 Health Check

**GET /health**
Returns a simple status message to confirm the API is running.

**Example:**
[https://monash-handbook-dataset-api.onrender.com/health](https://monash-handbook-dataset-api.onrender.com/health)

```json
{
  "status": "ok"
}
```

---

### 🔹 All Units

**GET /units**
Returns all units in JSON format.

**Example:**
[https://monash-handbook-dataset-api.onrender.com/units](https://monash-handbook-dataset-api.onrender.com/units)

---

### 🔹 Search Units

**GET /units?q=<keyword>**
Filter units by keyword in code or title.

**Example:**
[https://monash-handbook-dataset-api.onrender.com/units?q=fit](https://monash-handbook-dataset-api.onrender.com/units?q=fit)

```json
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
```

---

### 🔹 Get Specific Unit

**GET /units/\<unit\_code>**
Retrieve details of a specific unit by its code.

**Example:**
[https://monash-handbook-dataset-api.onrender.com/units/FIT3175](https://monash-handbook-dataset-api.onrender.com/units/FIT3175)

```json
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
```

---

## 🛠️ Local Development

Clone the repo:

```bash
git clone https://github.com/<your-username>/monash-handbook-dataset-api.git
cd monash-handbook-dataset-api
```

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run locally:

```bash
python app.py
```

Access at:
[http://127.0.0.1:8080](http://127.0.0.1:8080)

---

## 📦 Deployment

The API is deployed on Render.
Any changes pushed to the **main** branch will auto-deploy to the live API.

---

## ✨ Use Case

This API can be used for:

* Building a **Unit Review App** (students leave ratings/reviews for units).
* Developing **course planning tools**.
* Exploring **academic datasets** for research.
* Demonstrating how to **leverage REST APIs** in assignments.

---

## 📜 License

This project is for **educational purposes only** and is not an official Monash University service.

---



