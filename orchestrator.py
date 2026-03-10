import numpy as np
import requests

def run_system():
    print("--- OpenCLOW Multi-Agent System Starting ---")
    agents = ["Researcher", "Writer", "Reviewer"]
    for agent in agents:
        print(f"Status: {agent} is active.")
    print("--- System Ready for Task ---")

if __name__ == "__main__":
    run_system()
