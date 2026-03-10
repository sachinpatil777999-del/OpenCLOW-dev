import ollama

def call_agent(agent_name, system_prompt, user_task):
    print(f"\n--- {agent_name} is working... ---")
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_task},
    ])
    return response['message']['content']

def run_openclow_fast():
    print("--- OpenCLOW Professional (Intel Mac Optimized) ---")
    task = "Create a simple Python login script."

    # Step 1: Manager
    plan = call_agent("Manager", "Give a 1-line plan.", task)
    
    # Step 2: Coder
    code = call_agent("Coder", "Write short Python code.", f"Plan: {plan}")
    
    # Step 3: Reviewer
    check = call_agent("Reviewer", "Check for bugs in 1 sentence.", code)

    print("\n--- RESULTS ---")
    print(f"PLAN: {plan}")
    print(f"CODE:\n{code}")
    print(f"REVIEW: {check}")

    with open("final_report.txt", "w") as f:
        f.write(f"CODE:\n{code}\n\nREVIEW:\n{check}")

if __name__ == "__main__":
    run_openclow_fast()
