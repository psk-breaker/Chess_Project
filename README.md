# ♟️ Chess Web App

A full-stack chess application built from scratch, combining a custom Python chess engine with a Flask-based API and a lightweight JavaScript frontend for interactive play in the browser.

---

## 🚀 Overview

This project demonstrates the design and integration of:

- A domain-driven chess engine (Python)
- A REST-style API (Flask)
- A dynamic frontend (HTML, CSS, JavaScript)

The application allows users to play chess in the browser, with moves processed by the backend and reflected in real time on the UI.

---

## 🧠 Key Features

- Interactive chessboard rendered in the browser
- Click-to-move piece interaction
- Backend move validation via a custom chess engine
- JSON-based communication between frontend and backend
- Clean separation between domain logic and web layer

> Current implementation includes pawns and core game flow. Additional rules (e.g. en passant, promotion, castling, threat, gameover) are planned.

---

## 🏗️ Architecture

The project follows a layered design:


Frontend (HTML/CSS/JS)
↓ (HTTP / JSON)
Flask API (routes)
↓
Domain Logic (Game, Board, Piece)


### Project Structure


api/ # Flask routes (API layer)
domain/ # Core chess logic (engine)
static/ # Frontend assets (JS, CSS)
templates/ # HTML templates
tests/ # Unit tests (pytest)
app.py # Application entry point
requirements.txt


---

## 🔧 Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Testing:** pytest

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/psk-breaker/Chess_Project.git
cd Chess_Project
2. Install dependencies
pip install -r requirements.txt
3. Run the app
python app.py
4. Open in browser
http://127.0.0.1:5000
🧪 Running Tests
pytest
📌 Design Highlights
Domain-first design: Chess logic is fully decoupled from Flask
API-driven interaction: Frontend communicates exclusively via JSON endpoints
Testable core logic: Engine components validated with unit tests
🔮 Future Improvements
Implement full chess rules (threat detection, gameover detection, castling, promotion, en passant)
Improve UI (highlighting, animations, drag-and-drop)
Add game state persistence (database)
Multiplayer support (sessions or WebSockets)
Deploy to AWS with Docker
💡 Motivation

This project was built to explore full-stack development by integrating backend systems, API design, and frontend interaction, while applying software engineering principles such as modularity, testing, and clean architecture.
