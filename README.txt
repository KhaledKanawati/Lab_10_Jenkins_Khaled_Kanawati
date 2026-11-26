LAB 10 JENKINS CI/CD
Khaled Kanawati

A Python greeting application with a Jenkins pipeline for setup, linting,
unit testing, code coverage, security scanning and simple local deployment.

Run locally on Windows
Use Python 3.11 or 3.12. From the project folder, run:

  python -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
  .\.venv\Scripts\python.exe run_checks.py

Run with Jenkins
Create a Pipeline job named Python-CI-CD. Choose Pipeline script from SCM,
select Git, enter this repository URL and set the branch to */main.
Set Script Path to Jenkinsfile_Khaled_Kanawati, save and click Build Now.
The build agent needs Git and Python with pip and venv.

Verified results
Build #1 finished SUCCESS on 26 November 2026 using Windows and Python 3.11.7.
All seven tests passed, combined coverage was 94.12%, and Bandit reported
zero findings. The deployed app printed Hello, World from Khaled Kanawati!

Report and evidence
The completed report is lab10_Khaled_Kanawati.docx. The original Jenkins log,
screenshot and build artifacts are in evidence_jenkins/. Open
evidence_jenkins/reports/htmlcov/index.html for the HTML coverage report.
