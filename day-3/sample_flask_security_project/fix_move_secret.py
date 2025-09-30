# Example of a quick fix: do not hardcode token - read from environment.
import os
API_TOKEN = os.environ.get("API_TOKEN", None)
if not API_TOKEN:
    raise RuntimeError("API_TOKEN not set in environment")
