"""
check_api.py

Verifies the Roboflow API key and optional workspace access using env vars.

Env vars:
  - ROBOFLOW_API_KEY (required)
  - ROBOFLOW_WORKSPACE (optional; if set, validates access to that workspace)
"""

import os
from roboflow import Roboflow

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass


def main() -> None:
    api_key = os.getenv("ROBOFLOW_API_KEY")
    if not api_key:
        print("❌ Missing ROBOFLOW_API_KEY. Set it in your environment or .env file.")
        return

    print("Attempting to connect to Roboflow...")
    try:
        rf = Roboflow(api_key=api_key)
        workspace_slug = os.getenv("ROBOFLOW_WORKSPACE")
        if workspace_slug:
            workspace = rf.workspace(workspace_slug)
            print("✅ Connection Successful!")
            print(f"Workspace accessible: {workspace.id}")
        else:
            # Fallback: fetch default workspace if available
            workspace = rf.workspace()
            print("✅ Connection Successful!")
            print(f"Default workspace: {workspace.id}")
    except Exception as e:
        print("❌ Connection Failed.")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()