import ollama

def call_agent(agent_name, system_prompt, user_task):
    print(f"\n--- {agent_name} is thinking... ---")
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_task},
    ])
    content = response['message']['content']
    print(f"--- {agent_name} completed task. ---")
    return content

def run_openclow_fast():
    print("--- OpenCLOW V5 (Intel Mac Optimized) ---")
    task = "Create a simple Python script for a Pomodoro Timer."

    # 1. Manager Plans
    plan = call_agent("Manager", "Give a brief 2-step coding plan.", task)
    
    # 2. Coder Writes
    code = call_agent("Coder", "Write clean Python code for the plan.", f"Plan: {plan}")
    
    # 3. Reviewer Checks
    review = call_agent("Reviewer", "Check this code for errors in one sentence.", code)

    print("\n--- FINAL OUTPUT ---")
    print(f"PLAN: {plan}\n")
    print(f"CODE:\n{code}\n")
    print(f"REVIEW: {review}")

if __name__ == "__main__":
    run_openclow_fast()
