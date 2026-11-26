LAB 10 JENKINS CI CD
Khaled Kanawati

Status: Python checks passed locally. The Jenkins pipeline has NOT been run.
You do not need Jenkins installed on this computer. Use the provided Jenkins
machine later to validate the pipeline and finish the build evidence.

Contents
- app.py and tests/: personalized greeting and seven unit tests.
- Jenkinsfile_Khaled_Kanawati: Setup, Lint, Test, Coverage, Security Scan, Deploy.
- deploy.py: copies the app to deployment/current, verifies it, writes a manifest.
- requirements.txt: the four pinned Python tools used for validation.
- run_checks.py: repeat the Python checks without Jenkins.
- lab10_Khaled_Kanawati.docx: brief report with measured local results.
- evidence_local/: saved local reports and the tested deployment.
- JENKINS_VALIDATION.txt: exact setup, run, evidence and submission steps.

Optional local checks (Python 3.11 or 3.12 recommended)
Open a terminal in this jenkins_project folder.

Windows PowerShell:
  python -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
  .\.venv\Scripts\python.exe run_checks.py

Linux or macOS:
  python3 -m venv .venv
  .venv/bin/python -m pip install -r requirements.txt
  .venv/bin/python run_checks.py

These commands create reports/ and deployment/current/. Open the full HTML
coverage report at reports/htmlcov/index.html. Preserve its companion files.

To finish on Jenkins
Push this folder's contents to a Git repository. Create a Pipeline job named
Python-CI-CD, choose Pipeline script from SCM, Git, the repository URL and
*/main. Set Script Path to Jenkinsfile_Khaled_Kanawati. Run Build Now.

Then add the real Jenkins console output, build status and stage screenshots
to the report, and create a text file with the actual GitHub URL for Moodle.
See JENKINS_VALIDATION.txt for the complete checklist. This ZIP is a prepared,
locally checked package; the required successful Jenkins build is still pending.
