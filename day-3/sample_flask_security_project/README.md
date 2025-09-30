# Sample Vulnerable Flask App + GitLab CI Security Pipeline

This repository is a small demo project for learning how to integrate security scanners into a GitLab CI pipeline.
It intentionally contains a few insecure patterns so you can see how Bandit, Semgrep, Gitleaks, and OWASP ZAP detect issues.

## What the project contains
- `app.py` - Minimal Flask app with intentional issues:
  - Hardcoded SECRET_KEY
  - Plaintext password storage
  - An `/eval` endpoint that uses `eval()` on user input
- `config.py` - Contains an intentionally hardcoded API token.
- `requirements.txt` - Uses an older Flask version to simulate a vulnerable dependency.
- `.gitleaks.toml` - Simple gitleaks rules to detect AWS-like keys.
- `semgrep.yml` - Semgrep rule to flag `eval`.
- `.gitlab-ci.yml` - Pipeline that runs Bandit, Semgrep, Gitleaks, and OWASP ZAP, saving reports as artifacts.

## Pipeline Stages
1. **Bandit** - Static analyzer for Python (generates `bandit-report.html`).
2. **Semgrep** - Pattern-based static analysis (rules in `semgrep.yml`).
3. **Gitleaks** - Scans for hardcoded secrets (uses `.gitleaks.toml`).
4. **OWASP ZAP** - DAST scan against the running Flask app (generates `zap-report.html`).

## How to run locally (quick)
1. Create a virtualenv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install bandit semgrep gitleaks
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. From another terminal, run scanners:
   ```bash
   bandit -r . -f html -o bandit-report.html
   semgrep --config semgrep.yml --json > semgrep-report.json
   gitleaks detect --source . --report=gitleaks-report.json
   # For ZAP, simplest is to use the Docker image:
   docker run -v $(pwd):/zap/wrk/:rw --network host owasp/zap2docker-stable zap-baseline.py -t http://127.0.0.1:5000 -r zap-report.html
   ```

## Fix one identified issue (example)
- Issue: Hardcoded API token in `config.py`.
- Fix: Move token to an environment variable and update the code to read from `os.environ`.
- After fixing, re-run scanners and compare reports (you should see gitleaks no longer report the token).

## Notes and Caveats
- The `.gitlab-ci.yml` provided assumes your GitLab Runner has permissions to run Docker images (for ZAP job we use the official ZAP image).
- Some CI environments restrict network access or background processes; you may need to adapt the ZAP job to use a separate service/container pattern.
- The pipeline jobs include `|| true` on scanner commands to ensure the job doesn't fail solely because a scanner found issues; artifacts will still be collected.

