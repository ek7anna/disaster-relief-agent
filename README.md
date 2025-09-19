

# Disaster-Relief Resource Routing Agent

During disasters like floods, bridge collapses, or landslides, emergency teams often struggle to quickly match limited resources such as ambulances, relief boats, or shelters to the right locations.
This project automates that process by analysing incoming alerts and instantly generating an optimal dispatch plan of available resources.

## Demo

Watch the demo video on YouTube: https://www.youtube.com/watch?v=haAKP9x3zYw

## Project Architecture

The system consists of three main parts:

* TiDB database stores alerts and resource data.
* Python backend (agent.py) fetches alerts and available resources, computes nearest resources, and builds a dispatch plan.
* Streamlit frontend (app.py) displays live alerts and lets users generate a customized response plan with one click.

## How It Works

1. An alert (location, type, severity) is recorded in the database.
2. The backend retrieves available resources.
3. A geographic distance algorithm selects the closest resources.
4. A dispatch plan is generated and sent to the UI.
5. The Streamlit dashboard displays metrics, alerts, the dispatch plan, and a collapsible table of allocated resources.



## Getting Started

### Prerequisites

* Python 3.9+
* TiDB or MySQL instance
* pipenv or virtualenv recommended

### Installation

git clone [https://github.com/yourusername/disaster-relief-agent.git](https://github.com/yourusername/disaster-relief-agent.git)
cd disaster-relief-agent
pip install -r requirements.txt

Configure your database credentials in .env or config.py.

### Running the App

streamlit run app.py

## Repository Structure

agent.py – Backend logic to compute dispatch plans
app.py – Streamlit frontend
requirements.txt
README.md

## Tech Stack

* Database: TiDB (MySQL-compatible)
* Backend: Python
* Frontend: Streamlit
* Version Control: Git/GitHub

## Future Improvements

* Real-time GPS tracking of resources
* AI predictions of resource needs based on historical disasters
* Automated SMS/WhatsApp notifications to field teams

## Team

Built collaboratively by our hackathon team.

## License

MIT License 
