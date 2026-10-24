# Open-Source Incident Management System 🛡️

A lightweight and functional web portal built to log, track, and resolve infrastructure or application incidents with role-based tracking.

## 🚀 Features
* **Incident Logging:** Report new technical issues with custom titles, descriptions, priorities (Low, Medium, High), and assignee details.
* **Real-time Tracking:** Monitor active and closed incidents directly from an intuitive Bootstrap dashboard.
* **Status Management:** Seamlessly update incident statuses from `Open` to `Resolved`.
* **RESTful APIs:** Built-in backend endpoints to handle incident creation and lifecycle management.

## 🛠️ Tech Stack
* **Backend:** Python (Flask), Flask-SQLAlchemy (ORM)
* **Database:** SQLite
* **Frontend:** Bootstrap 5, HTML5, Jinja2 Templates
* **Containerization & Version Control:** Docker, Git

## 📂 Project Structure
```text
incident-management/
├── app.py                  # Main Flask application & database models
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── base.html           # Bootstrap layout base
│   └── index.html          # Dashboard & incident form
└── static/                 # Static assets (CSS, JS)

Installation & Setup Locally
Clone the Repository:

Bash
git clone [https://github.com/YOUR_USERNAME/incident-management-system.git](https://github.com/YOUR_USERNAME/incident-management-system.git)
cd incident-management-system
Install Dependencies:

Bash
pip install --default-timeout=1000 --no-cache-dir -r requirements.txt
Run the Application:

Bash
python3 app.py
Access the Portal:
Open your browser and navigate to: http://127.0.0.1:5000

🐳 Docker Support (Optional)
To run this application inside a Docker container:

Bash
docker build -t incident-portal .
docker run -p 5000:5000 incident-portal
