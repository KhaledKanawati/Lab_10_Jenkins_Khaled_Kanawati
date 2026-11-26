"""Copy the trusted application to a local release and verify it."""

import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil


ROOT = Path(__file__).resolve().parent
EXPECTED = "Hello, World from Khaled Kanawati!"


def deploy(destination):
    """Create a local release with a smoke check and a SHA256 manifest."""
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "app.py"
    shutil.copy2(ROOT / "app.py", target)
    namespace = runpy.run_path(str(target))
    greeting = namespace["greet"]("World")
    if greeting != EXPECTED:
        raise RuntimeError("Deployed application failed the smoke check")
    manifest = {
        "application": "app.py",
        "author": "Khaled Kanawati",
        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "build_number": os.environ.get("BUILD_NUMBER", "local"),
        "commit": os.environ.get("GIT_COMMIT", "local"),
        "smoke_output": greeting,
    }
    (destination / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Deployed to {destination}")
    print(greeting)
    return manifest


if __name__ == "__main__":
    deploy(ROOT / "deployment" / "current")
