#!/bin/bash

echo "--- 🚀 Starting OpenCLOW Gateway System ---"

# 1. Check if Ollama is running, if not start it
if ! pgrep -x "ollama" > /dev/null
then
    echo "Starting Ollama service..."
    brew services start ollama
    sleep 2
else
    echo "✅ Ollama is already running."
fi

# 2. Go to project folder and activate virtual environment
cd ~/openclow/OpenCLOW-dev
if [ -f "../venv/bin/activate" ]; then
    source ../venv/bin/activate
    echo "✅ Virtual Environment Activated."
else
    echo "❌ Error: Virtual Environment not found!"
    exit 1
fi

# 3. Pull latest code from GitHub (Internet recovery)
echo "Checking for code updates from GitHub..."
git pull origin main

# 4. Final Status
echo "--- ✅ SYSTEM READY ---"
echo "Aap ab 'python orchestrator.py' ya 'python whatsapp_agent.py' chala sakte hain."
bash
