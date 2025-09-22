"""
download_dataset.py

Downloads a Roboflow dataset for a given workspace, project, and version
using the YOLOv8 format. Credentials and identifiers are read from env vars
or a local .env file for safety.

Required env vars:
  - ROBOFLOW_API_KEY
  - ROBOFLOW_WORKSPACE (slug)
  - ROBOFLOW_PROJECT (slug)
  - ROBOFLOW_VERSION (integer)
Optional:
  - ROBOFLOW_FORMAT (default: "yolov8")
"""

import os
import sys
from roboflow import Roboflow

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # dotenv is optional; proceed if not available
    pass


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main() -> int:
    try:
        api_key = get_required_env("ROBOFLOW_API_KEY")
        workspace_slug = get_required_env("ROBOFLOW_WORKSPACE")
        project_slug = get_required_env("ROBOFLOW_PROJECT")
        version_str = get_required_env("ROBOFLOW_VERSION")
        data_format = os.getenv("ROBOFLOW_FORMAT", "yolov8")

        try:
            version_number = int(version_str)
        except ValueError:
            raise RuntimeError("ROBOFLOW_VERSION must be an integer")

        print("Connecting to Roboflow...")
        rf = Roboflow(api_key=api_key)

        # Access the project via workspace → project(slug)
        workspace = rf.workspace(workspace_slug)
        project = workspace.project(project_slug)

        print(
            f"Downloading dataset: workspace={workspace_slug} project={project_slug} version={version_number} format={data_format}"
        )
        dataset = project.version(version_number).download(data_format)

        print(f"Dataset downloaded successfully to: {dataset.location}")
        return 0
    except Exception as exc:
        print("Failed to download dataset.")
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())