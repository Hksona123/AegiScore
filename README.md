# AegisCore — Enterprise-Grade Cybersecurity Intelligence Platform

AegisCore (formerly Sentinal AI) is a robust, production-ready cybersecurity platform designed for real-time threat detection, log analysis, and AI-powered security auditing. It utilizes LSTM deep learning models to detect potential threats and provides a sophisticated multi-agent chat interface for investigative security work.

## 📺 Usage Demo
[![image](https://github.com/user-attachments/assets/b811d5e2-e398-4118-9964-e743da0cb004)](https://www.youtube.com/watch?v=OAhx3_3ObBQ)

---

## 📂 Project Structure

The project is divided into a decoupled Client-Server architecture:

```text
Sentinal_Ai/
├── Server/                 # Backend (Flask + Python)
│   ├── app/                # Core application package
│   │   ├── blueprints/     # Route handlers (Auth, Logs, Threat, Chat)
│   │   ├── models/         # Database schemas
│   │   ├── services/       # Core engines (SOAR, Correlation, Baselines)
│   │   └── utils/          # AI Agents and utility scripts
│   ├── resources/          # Static ML weights and datasets
│   ├── data/               # Persistent log storage and audit reports
│   └── run.py              # Backend Entry Point
├── Frontend/               # Frontend (React + Vite)
│   ├── src/
│   │   ├── api/            # API communication layer
│   │   ├── pages/          # UI Dashboards and SOC views
│   │   └── styles/         # Global CSS and themes
│   └── index.html
├── Sample/                 # Demo files for testing/auditing
└── README.md               # You are here
```

---

## 🛠️ Complete Local Setup Guide (VS Code)

If you have just cloned this repository and want to run it locally in **Visual Studio Code**, follow these exact steps:

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **Google Gemini API Key** (for AI features)

### Step 1: Open in VS Code
1. Clone the repository to your machine.
2. Open **VS Code**.
3. Go to `File > Open Folder...` and select the cloned repository folder (`Sentinal_Ai`).
4. Open the Integrated Terminal in VS Code by pressing `` Ctrl + ` `` (or going to `Terminal > New Terminal`).
5. **Open a second terminal panel** using the `+` icon or split screen icon in the terminal window. You will need two terminals: one for the Backend, one for the Frontend.

### Step 2: Backend Setup (Terminal 1)
In your first terminal panel, run the following commands to set up the Python backend:

```bash
# 1. Navigate to the Server directory
cd Server

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows (Command Prompt / PowerShell):
.\venv\Scripts\activate
# On Mac / Linux:
source venv/bin/activate

# 4. Install required dependencies
pip install -r requirements.txt

# 5. Create environment variables file
cp .env.example .env
# (Open the new .env file in VS Code and add your GOOGLE_API_KEY)

# 6. Start the backend server
python run.py
```
*The backend should now be running on `http://localhost:5000`.*

### Step 3: Frontend Setup (Terminal 2)
In your second terminal panel, run the following commands to set up the React frontend:

```bash
# 1. Navigate to the Frontend directory
cd Frontend

# 2. Install Node modules
npm install

# 3. Start the Vite development server
npm run dev
```
*The frontend should now be running. Open the Local URL provided in the terminal (usually `http://localhost:5173`).*

### Step 4: Login & Demo Data
When the web app opens, you can log in using the default administrative credentials:
- **Username**: `admin`
- **Password**: `AegisCore@2025!`

To test the system immediately, navigate to the **Logs** page and upload the pre-made realistic demo files located in the `/Sample` folder (`demo_network_attacks.csv` or `demo_host_telemetry.csv`).

---

## 🔋 Key Features

- **🚀 Real-Time SOC Monitoring**: Live feeds for system logs, network alerts, and flagged AI chat interactions.
- **🧠 ML Threat Detection**: Uses an LSTM model trained on the UNSW-NB15 dataset to detect Reconnaissance, DoS, Backdoors, Worms, and more.
- **🤖 Multi-Agent AI**: A "Master Agent" powered by Google Gemini that can autonomously create logs, analyze threats, and generate detailed audit reports.
- **📄 AI-Powered Auditing**: Generates human-readable cybersecurity audit reports in Markdown format based on live system telemetry.
- **🛡️ NLP Chat Guard**: Analyzes every chat message for potential prompt injections or social engineering attempts before processing.
- **📊 Interactive Visualization**: Force-directed network topology graphs and dynamic threat distribution charts.

---

## 📖 Component Documentation

### 1. Security Operations Center (SOC)
The tactical command center where analysts monitor live threat feeds. It features real-time WebSocket updates and an NLP Testing Console to verify message security scores.

### 2. Network Topology
A force-directed graph visualization of your network's security posture. It maps connections between the Master Node (AegisCore), detected threat categories, and individual source IPs.

### 3. Log Management
Allows for manual ingestion of CSV/LOG files and provides a "Live Snapshot" feature that captures real-time server telemetry including CPU, Memory, and Network Connections.

### 4. AI Audit Hub
Synthesizes massive amounts of log data into professional Markdown reports. These reports include executive summaries, detailed incident breakdowns, and prioritized security recommendations.

---

## 🛠️ Technical Specifications
- **Backend**: Flask, Socket.IO, SQLAlchemy, APScheduler, Keras/TensorFlow, LlamaIndex.
- **Frontend**: React 18, Vite, Tailwind CSS, Framer Motion, Recharts, D3-Force.
- **Database**: SQLite (Development) / PostgreSQL (Production).
- **AI Models**: LSTM (Threat Detection), Google Gemini 1.5 Flash (Reporting & Interaction).

---

## 📜 Credits
Developed as an enterprise-grade solution for advanced cybersecurity monitoring and AI-driven automation.
