# RegistrarQueue

RegistrarQueue is a web-based queue management system for the Registrar's Office at MSU-IIT. It lets students join the queue for a registrar service (such as a transcript request, enrollment certification, or ID validation) from their phone or laptop, check their ticket number and position in line, and lets registrar staff call, serve, or mark tickets as no-show from a dashboard. It is built with Flask, Jinja and Bootstrap for CCC181, and currently keeps its data in memory (a Python list), so tickets reset whenever the app restarts.

## How to run

1. Create and activate a virtual environment:

   ```
   python -m venv .venv
   # Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
   ```

2. Install the packages:

   ```
   pip install -r requirements.txt
   ```

3. Start the app:

   ```
   flask --app app run --debug
   ```

4. Open http://127.0.0.1:5000 in your browser.