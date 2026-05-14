from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>DevSecOps Pipeline</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container { text-align: center; padding: 40px; max-width: 800px; }
        h1 { font-size: 2.5em; margin-bottom: 10px; color: #00d4ff; }
        h2 { font-size: 1.3em; font-weight: 300; margin-bottom: 40px; color: #aaa; }
        .badge {
            display: inline-block;
            background: #00c853;
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-bottom: 40px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        .card {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 20px;
        }
        .card .icon { font-size: 2em; margin-bottom: 10px; }
        .card h3 { font-size: 0.95em; color: #00d4ff; margin-bottom: 5px; }
        .card p { font-size: 0.8em; color: #aaa; }
        .version {
            margin-top: 30px;
            font-size: 0.85em;
            color: #666;
        }
        .version span { color: #00d4ff; }
    </style>
</head>
<body>
    <div class="container">
        <h1>&#128274; DevSecOps CI/CD Pipeline </h1>
        <h2>Automated Compliance Scans for Containerized Applications</h2>
        <div class="badge">&#9679; LIVE — Deployed on AWS ECS Fargate</div>

        <div class="grid">
            <div class="card">
                <div class="icon">&#128260;</div>
                <h3>AWS CodePipeline</h3>
                <p>Automated 4-stage CI/CD pipeline triggered on every GitHub push</p>
            </div>
            <div class="card">
                <div class="icon">&#128269;</div>
                <h3>Trivy Scanner</h3>
                <p>Container image scanned for CVEs — blocks deploy on CRITICAL findings</p>
            </div>
            <div class="card">
                <div class="icon">&#9989;</div>
                <h3>Checkov IaC Scan</h3>
                <p>Terraform infrastructure scanned for 29 policy compliance checks</p>
            </div>
            <div class="card">
                <div class="icon">&#128230;</div>
                <h3>Amazon ECR</h3>
                <p>Docker image stored with native scan-on-push enabled</p>
            </div>
            <div class="card">
                <div class="icon">&#9729;</div>
                <h3>ECS Fargate</h3>
                <p>Serverless container deployment — no EC2 management needed</p>
            </div>
            <div class="card">
                <div class="icon">&#128202;</div>
                <h3>CloudWatch</h3>
                <p>Container logs and pipeline metrics monitored in real time</p>
            </div>
        </div>

        <div class="version">
            Version <span>1.0</span> &nbsp;|&nbsp; Built by <span>TEAM 3</span> &nbsp;|&nbsp; AWS CodeBuild + CodePipeline
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
