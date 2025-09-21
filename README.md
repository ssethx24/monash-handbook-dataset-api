
````markdown
# 📚 Monash Handbook Dataset API

This project provides a **REST API** that serves Monash University handbook unit data.  
The dataset was scraped from the official Monash Handbook and contains ~5124 units (2025 edition).

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
````

---

### 🔹 List All Units (with Pagination)

**GET /units**
Returns units in JSON format, paginated by default.

Query Parameters:

* `page` → page number (default = 1)
* `limit` → number of results per page (default = 50)

**Example:**
[https://monash-handbook-dataset-api.onrender.com/units?page=1\&limit=2](https://monash-handbook-dataset-api.onrender.com/units?page=1&limit=2)

```json
{
  "totalItems": 5124,
  "page": 1,
  "limit": 2,
  "nextPage": "https://monash-handbook-dataset-api.onrender.com/units?page=2&limit=2",
  "prevPage": null,
  "items": [
    {
      "common": {
        "code": "FIT1045",
        "title": "Algorithms and Programming",
        "link": "https://handbook.monash.edu/2025/units/FIT1045"
      }
    },
    {
      "common": {
        "code": "FIT2004",
        "title": "Databases",
        "link": "https://handbook.monash.edu/2025/units/FIT2004"
      }
    }
  ]
}
```

✅ The API includes `nextPage` and `prevPage` links so your app can fetch more results like Google APIs.

---

### 🔹 Search Units

**GET /units?q=<keyword>**
Filter units by keyword in code or title. Works with pagination.

NOTE: there are 5152 units so they dataset will load in 104 pages if the limit is set to 50. 

**Example:**
[https://monash-handbook-dataset-api.onrender.com/units?q=fit\&page=1\&limit=50](https://monash-handbook-dataset-api.onrender.com/units?q=fit&page=1&limit=50)

```json
{
  "totalItems": 120,
  "page": 1,
  "limit": 3,
  "nextPage": "https://monash-handbook-dataset-api.onrender.com/units?q=fit&page=2&limit=3",
  "prevPage": null,
  "items": [
    {
      "common": {
        "code": "FIT3175",
        "title": "Usability",
        "faculty": "Faculty of IT"
      }
    },
    {
      "common": {
        "code": "FIT2004",
        "title": "Databases",
        "faculty": "Faculty of IT"
      }
    },
    {
      "common": {
        "code": "FIT1045",
        "title": "Algorithms and Programming",
        "faculty": "Faculty of IT"
      }
    }
  ]
}
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

The API is deployed on **Render**.
Any changes pushed to the **main** branch will auto-deploy to the live API.

---

## ✨ Use Case

This API is used for:

* Building a **Unit Review App** (students leave ratings/reviews for units).
* Developing **course planning tools**.
* Exploring **academic datasets** for research.
* Demonstrating how to **leverage REST APIs** in ios applications.

---

## 📜 License

This project is for **educational purposes only** and is not an official Monash University service.

```
```



