import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app", "patrul_robot_project"))

from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
