LAB 10 JENKINS CI CD
Khaled Kanawati

Validated on Jenkins: Python-CI-CD build #1 finished SUCCESS on 26 November 2026.
Agent: Windows, Python 3.11.7. All six stages completed: Setup, Lint, Test,
Coverage, Security Scan and Deploy. Seven tests passed; combined line/branch
coverage was 94.12%; Bandit reported zero findings and zero scan errors.

Repository: https://github.com/KhaledKanawati/Lab_10_Jenkins_Khaled_Kanawati
Tested commit: cdbfc82db1565d0123340bb82ba25a45e37eb7b3

Files
- Jenkinsfile_Khaled_Kanawati: the exact pipeline from the successful build.
- app.py, deploy.py, tests/, requirements.txt: the tested Python project.
- lab10_Khaled_Kanawati.docx: completed report with real Jenkins results.
- evidence_jenkins/: original console log, screenshot, original archive.zip,
  extracted artifacts, and a build summary derived from those records.
- evidence_jenkins/reports/htmlcov/index.html: full Jenkins coverage report.
- github_link.txt: actual repository link for Moodle.
- JENKINS_VALIDATION.txt: verified build record and reproduction settings.
- SUBMISSION.txt: final upload checklist.

Optional local run from this folder
Windows:
  python -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
  .\.venv\Scripts\python.exe run_checks.py
Linux/macOS: use python3 and .venv/bin/python instead.

Jenkins creates its own virtual environment. It archives reports and the
local release before cleaning the workspace. The archived app can be run
with python app.py after extraction. Preserve the complete htmlcov folder.
The deployed manifest records build 1 and the correct app hash; its commit
field uses the local fallback. The console log records the tested Git commit.
