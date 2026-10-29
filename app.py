from datetime import datetime
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

portal_state = {
    "intern": {
        "name": "Sheriff",
        "role": "Web Development Intern",
        "department": "Core Engineering & AI Systems",
        "company": "Shortfundly",
        "start_date": "2026-10-28",
        "review_date": "2026-11-20",
        "mentor": "Principal Technical Lead",
        "system_status": "Optimal (99.9% Uptime)"
    },
    "modules": [
        {
            "id": 1,
            "title": "Responsive UI Architecture & Design",
            "description": "Production-grade mobile-first design using HTML5, CSS3, and JavaScript ES6 with fluid grid layouts.",
            "status": "Verified & Completed",
            "progress": 100,
            "deadline": "2026-11-05",
            "priority": "High"
        },
        {
            "id": 2,
            "title": "API Integration & State Management",
            "description": "Secure REST endpoints, robust asynchronous state handling, and client-side error boundaries.",
            "status": "In Progress",
            "progress": 75,
            "deadline": "2026-11-12",
            "priority": "Critical"
        },
        {
            "id": 3,
            "title": "Git Version Control & Documentation",
            "description": "Branch strategy configuration, repository settings management, GitHub code push, and deployment logs.",
            "status": "Pending",
            "progress": 25,
            "deadline": "2026-11-20",
            "priority": "High"
        }
    ],
    "audit_logs": [
        {"id": 501, "timestamp": "2026-10-28 10:00 AM", "channel": "Secure Mail", "subject": "Module 1 Directive & Repository Guidelines", "status": "Delivered & Read"},
        {"id": 502, "timestamp": "2026-10-29 11:30 AM", "channel": "System API", "subject": "Automated Code Verification & Syntax Audit", "status": "Passed Successfully"},
        {"id": 503, "timestamp": "2026-10-29 02:15 PM", "channel": "Calendar", "subject": "Final Evaluation Milestone Lock", "status": "Scheduled (Nov 20)"}
    ]
}

ULTIMATE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shortfundly Ultra Enterprise Portal | Sheriff Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #030712;
            --bg-surface: #0b0f19;
            --bg-card: #111827;
            --accent: #6366f1;
            --accent-hover: #4f46e5;
            --accent-glow: rgba(99, 102, 241, 0.35);
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --border-line: rgba(255, 255, 255, 0.08);
            --success: #10b981;
            --warning: #f59e0b;
            --info: #06b6d4;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }
        body { background-color: var(--bg-base); color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }

        header {
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-line);
            padding: 16px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .brand-logo { background: linear-gradient(135deg, #6366f1, #a855f7); color: white; width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 18px; box-shadow: 0 0 20px var(--accent-glow); }
        .brand-text h1 { font-size: 18px; font-weight: 700; color: var(--text-main); letter-spacing: 0.4px; }
        .brand-text span { font-size: 12px; color: var(--text-muted); font-weight: 500; }

        .nav-pills { display: flex; gap: 8px; background: var(--bg-card); padding: 5px; border-radius: 12px; border: 1px solid var(--border-line); }
        .nav-pill {
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 9px 18px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            font-size: 13px;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .nav-pill:hover { color: var(--text-main); background: rgba(255,255,255,0.04); }
        .nav-pill.active { color: white; background: var(--accent); box-shadow: 0 4px 15px var(--accent-glow); }

        .workspace { max-width: 1350px; width: 100%; margin: 32px auto; padding: 0 24px; flex: 1; }
        .tab-content { display: none; animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
        .tab-content.active { display: block; }

        @keyframes slideUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }

        .panel {
            background: var(--bg-card);
            border: 1px solid var(--border-line);
            border-radius: 20px;
            padding: 36px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }
        .panel::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent); }
        
        .panel-heading { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px; border-bottom: 1px solid var(--border-line); padding-bottom: 18px; }
        .panel-heading h2 { font-size: 22px; font-weight: 700; color: var(--text-main); }
        .panel-heading p { font-size: 13px; color: var(--text-muted); margin-top: 6px; }

        .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 24px; }
        .metric-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-line);
            border-radius: 14px;
            padding: 24px;
            position: relative;
            transition: transform 0.2s;
        }
        .metric-card:hover { transform: translateY(-3px); border-color: rgba(99, 102, 241, 0.3); }
        .metric-card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent); border-top-left-radius: 14px; border-bottom-left-radius: 14px; }
        .metric-card span { font-size: 12px; font-weight: 600; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.6px; }
        .metric-card h3 { font-size: 22px; font-weight: 700; color: var(--text-main); margin-top: 10px; }

        .table-responsive { overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; text-align: left; }
        th, td { padding: 18px; border-bottom: 1px solid var(--border-line); font-size: 14px; }
        th { background: rgba(3, 7, 18, 0.6); color: var(--text-muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; }
        td { color: var(--text-main); }
        td small { color: var(--text-muted); display: block; margin-top: 5px; font-size: 13px; }

        .badge { padding: 6px 14px; border-radius: 30px; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }
        .badge-success { background: rgba(16, 185, 129, 0.12); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.25); }
        .badge-info { background: rgba(6, 182, 212, 0.12); color: #22d3ee; border: 1px solid rgba(6, 182, 212, 0.25); }
        .badge-warning { background: rgba(245, 158, 11, 0.12); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.25); }

        .action-select {
            background: var(--bg-base);
            color: var(--text-main);
            border: 1px solid var(--border-line);
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 13px;
            cursor: pointer;
            outline: none;
        }

        .progress-track { width: 100%; background: rgba(255,255,255,0.06); height: 8px; border-radius: 4px; overflow: hidden; margin-top: 8px; }
        .progress-fill { background: linear-gradient(90deg, #6366f1, #a855f7); height: 100%; border-radius: 4px; transition: width 0.3s ease; }

        .ai-layout { display: grid; grid-template-columns: 320px 1fr; gap: 24px; }
        @media(max-width: 950px) { .ai-layout { grid-template-columns: 1fr; } }

        .ai-sidebar { background: var(--bg-surface); border: 1px solid var(--border-line); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; gap: 14px; }
        .ai-sidebar h3 { font-size: 14px; font-weight: 700; color: var(--text-main); margin-bottom: 4px; }
        .quick-action-btn {
            background: rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.2);
            color: #c7d2fe;
            padding: 13px 16px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s ease;
        }
        .quick-action-btn:hover { background: rgba(99, 102, 241, 0.2); color: white; transform: translateX(4px); }

        .chat-terminal { display: flex; flex-direction: column; height: 540px; background: var(--bg-surface); border: 1px solid var(--border-line); border-radius: 16px; overflow: hidden; }
        .chat-history { flex: 1; padding: 24px; overflow-y: auto; display: flex; flex-direction: column; gap: 16px; scroll-behavior: smooth; }
        
        .chat-bubble { max-width: 80%; padding: 15px 20px; border-radius: 16px; font-size: 14px; line-height: 1.6; }
        .chat-bubble.bot { background: var(--bg-card); color: var(--text-main); align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid var(--border-line); }
        .chat-bubble.user { background: var(--accent); color: white; align-self: flex-end; border-bottom-right-radius: 4px; font-weight: 500; box-shadow: 0 4px 15px var(--accent-glow); }

        .chat-input-row { display: flex; padding: 18px; background: var(--bg-card); border-top: 1px solid var(--border-line); gap: 14px; }
        .chat-input-row input { flex: 1; background: var(--bg-base); border: 1px solid var(--border-line); padding: 14px 20px; border-radius: 12px; color: var(--text-main); font-size: 14px; outline: none; transition: border-color 0.2s; }
        .chat-input-row input:focus { border-color: var(--accent); }
        .send-action-btn { background: var(--accent); color: white; border: none; padding: 0 30px; border-radius: 12px; font-weight: 700; cursor: pointer; transition: background 0.2s; box-shadow: 0 4px 15px var(--accent-glow); }
        .send-action-btn:hover { background: var(--accent-hover); }
    </style>
</head>
<body>

    <header>
        <div class="brand-box">
            <div class="brand-logo">SF</div>
            <div class="brand-text">
                <h1>Shortfundly Ultra Enterprise Portal</h1>
                <span>Executive Internship Suite</span>
            </div>
        </div>
        <div class="nav-pills">
            <button class="nav-pill active" onclick="switchTab('overview', this)">Overview</button>
            <button class="nav-pill" onclick="switchTab('modules', this)">Task Modules</button>
            <button class="nav-pill" onclick="switchTab('logs', this)">Review & Logs</button>
            <button class="nav-pill" onclick="switchTab('assistant', this)">AI Intelligence</button>
        </div>
    </header>

    <div class="workspace">
        
        <!-- OVERVIEW TAB -->
        <div id="overview" class="tab-content active">
            <div class="panel">
                <div class="panel-heading">
                    <div>
                        <h2>Executive Summary Dashboard</h2>
                        <p>Welcome back, <b>{{ intern.name }}</b>. All lifecycle tracking parameters are fully synchronized.</p>
                    </div>
                </div>

                <div class="metrics-grid">
                    <div class="metric-card">
                        <span>Assigned Position</span>
                        <h3>{{ intern.role }}</h3>
                    </div>
                    <div class="metric-card" style="--accent: #06b6d4;">
                        <span>Department</span>
                        <h3>{{ intern.department }}</h3>
                    </div>
                    <div class="metric-card" style="--accent: #10b981;">
                        <span>Final Review Milestone</span>
                        <h3>November 20, 2026</h3>
                    </div>
                    <div class="metric-card" style="--accent: #f59e0b;">
                        <span>Infrastructure Status</span>
                        <h3 id="sysStatus">{{ intern.system_status }}</h3>
                    </div>
                </div>
            </div>
        </div>

        <!-- TASK MODULES TAB -->
        <div id="modules" class="tab-content">
            <div class="panel">
                <div class="panel-heading">
                    <div>
                        <h2>Development Modules & Interactive Verification Matrix</h2>
                        <p>Update your module execution status dynamically; changes persist locally.</p>
                    </div>
                </div>

                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Module Specification</th>
                                <th>Target Deadline</th>
                                <th>Execution Progress</th>
                                <th>Interactive Status Control</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for mod in modules %}
                            <tr>
                                <td>#{{ mod.id }}</td>
                                <td>
                                    <b>{{ mod.title }}</b>
                                    <small>{{ mod.description }}</small>
                                </td>
                                <td>{{ mod.deadline }}</td>
                                <td style="width: 200px;">
                                    <span id="prog-text-{{ mod.id }}" style="font-size: 12px; font-weight: 700;">{{ mod.progress }}% Complete</span>
                                    <div class="progress-track">
                                        <div id="prog-bar-{{ mod.id }}" class="progress-fill" style="width: {{ mod.progress }}%;"></div>
                                    </div>
                                </td>
                                <td>
                                    <select class="action-select" id="select-{{ mod.id }}" onchange="updateModuleStatus({{ mod.id }})">
                                        <option value="Verified & Completed" {% if mod.status == 'Verified & Completed' %}selected{% endif %}>Verified & Completed</option>
                                        <option value="In Progress" {% if mod.status == 'In Progress' %}selected{% endif %}>In Progress</option>
                                        <option value="Pending" {% if mod.status == 'Pending' %}selected{% endif %}>Pending</option>
                                    </select>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- REVIEW & LOGS TAB -->
        <div id="logs" class="tab-content">
            <div class="panel">
                <div class="panel-heading">
                    <div>
                        <h2>Review Schedule & Automated Audit Logs</h2>
                        <p><b>Final Review Date:</b> November 20, 2026 | Secure transmission history and mentor feedback logs[cite: 1, 2].</p>
                    </div>
                </div>

                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>Timestamp</th>
                                <th>Communication Channel</th>
                                <th>Audit Subject</th>
                                <th>Verification & Delivery Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for log in audit_logs %}
                            <tr>
                                <td>{{ log.timestamp }}</td>
                                <td><b>{{ log.channel }}</b></td>
                                <td>{{ log.subject }}</td>
                                <td><span class="badge badge-success">{{ log.status }}</span></td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- AI ASSISTANT TAB -->
        <div id="assistant" class="tab-content">
            <div class="panel">
                <div class="panel-heading">
                    <div>
                        <h2>Shortfundly Enterprise AI Intelligence Assistant</h2>
                        <p>Intelligent assistant configured to parse your tasks, audit verification status, and review timelines[cite: 1, 2].</p>
                    </div>
                </div>

                <div class="ai-layout">
                    <div class="ai-sidebar">
                        <h3>Quick Prompt Triggers</h3>
                        <div class="quick-action-btn" onclick="fireQuery('Show my current development modules')">📌 Query Active Modules</div>
                        <div class="quick-action-btn" onclick="fireQuery('What is my final review target?')">📅 Inspect Review Date</div>
                        <div class="quick-action-btn" onclick="fireQuery('Verify secure email notification logs')">✉ Audit Email & Logs</div>
                        <div class="quick-action-btn" onclick="fireQuery('Show GitHub version control requirements')">🔗 GitHub Repository Status</div>
                    </div>

                    <div class="chat-terminal">
                        <div class="chat-history" id="chatHistory">
                            <div class="chat-bubble bot"><b>Enterprise Bot:</b> Hello Sheriff! I am your Shortfundly AI Assistant. How can I assist you with your internship requirements today[cite: 1, 2]?</div>
                        </div>
                        <div class="chat-input-row">
                            <input type="text" id="userInputBox" placeholder="Ask regarding tasks, review date, or email status..." autocomplete="off" onkeypress="checkKey(event)">
                            <button class="send-action-btn" onclick="submitMessage()">Transmit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            // Load saved status from localStorage
            [1, 2, 3].forEach(id => {
                const savedStatus = localStorage.getItem(`module_status_${id}`);
                if(savedStatus) {
                    const selectEl = document.getElementById(`select-${id}`);
                    if(selectEl) {
                        selectEl.value = savedStatus;
                        updateUIElements(id, savedStatus);
                    }
                }
            });
        });

        function switchTab(tabId, pillElement) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.nav-pill').forEach(p => p.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            pillElement.classList.add('active');
        }

        function updateModuleStatus(id) {
            const selectEl = document.getElementById(`select-${id}`);
            const val = selectEl.value;
            localStorage.setItem(`module_status_${id}`, val);
            updateUIElements(id, val);
        }

        function updateUIElements(id, status) {
            const bar = document.getElementById(`prog-bar-${id}`);
            const text = document.getElementById(`prog-text-${id}`);
            if(status === 'Verified & Completed') {
                bar.style.width = '100%';
                text.innerText = '100% Complete';
            } else if(status === 'In Progress') {
                bar.style.width = '65%';
                text.innerText = '65% Complete';
            } else {
                bar.style.width = '20%';
                text.innerText = '20% Complete';
            }
        }

        function checkKey(e) {
            if (e.key === 'Enter') { submitMessage(); }
        }

        function fireQuery(text) {
            document.getElementById('userInputBox').value = text;
            submitMessage();
        }

        async function submitMessage() {
            const inputBox = document.getElementById('userInputBox');
            const chatHistory = document.getElementById('chatHistory');
            const query = inputBox.value.trim();
            if(!query) return;

            chatHistory.innerHTML += `<div class="chat-bubble user">${query}</div>`;
            inputBox.value = '';
            chatHistory.scrollTop = chatHistory.scrollHeight;

            try {
                const resp = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: query })
                });
                const data = await resp.json();
                chatHistory.innerHTML += `<div class="chat-bubble bot"><b>Enterprise Bot:</b> ${data.reply}</div>`;
                chatHistory.scrollTop = chatHistory.scrollHeight;
            } catch (err) {
                chatHistory.innerHTML += `<div class="chat-bubble bot"><b>Enterprise Bot:</b> Connection failure with the local Flask server.</div>`;
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(ULTIMATE_TEMPLATE, intern=portal_state["intern"], modules=portal_state["modules"], audit_logs=portal_state["audit_logs"])

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    user_msg = request.json.get("message", "").lower()

    if "module" in user_msg or "task" in user_msg:
        reply = "All three core modules (Responsive UI, API Integration, and Git Version Control) have been fully engineered, structured, and verified for your internship dashboard[cite: 1, 2]."
    elif "review" in user_msg or "date" in user_msg or "20" in user_msg:
        reply = f"Your official Shortfundly Final Project Review is locked for <b>{portal_state['intern']['review_date']}</b>[cite: 1]. Ensure all requirements are completed before this milestone!"
    elif "mail" in user_msg or "email" in user_msg or "log" in user_msg or "audit" in user_msg:
        reply = "System audit logs confirm that task assignments, requirement feedback, and review alerts have been successfully dispatched via secure channels[cite: 1, 2]."
    elif "github" in user_msg or "repo" in user_msg:
        reply = "Make sure your code repository is updated, structured cleanly with `app.py`, and documented properly for final review submission[cite: 1, 2]."
    elif "hello" in user_msg or "hi" in user_msg or "vanakkam" in user_msg:
        reply = f"Hello Sheriff! Welcome back to your Shortfundly Ultra Enterprise Portal[cite: 1, 2]."
    else:
        reply = "I can guide you through your module verification metrics, final review milestones, and audit logs. Feel free to use the quick action prompt triggers on the left!"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)