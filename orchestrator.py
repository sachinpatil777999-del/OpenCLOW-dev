import ollama

def call_agent(agent_name, system_prompt, user_task):
    print(f"\n--- {agent_name} is thinking... ---")
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_task},
    ])
    content = response['message']['content']
    print(f"{agent_name} Response: {content}")
    return content

def run_multi_agent_flow():
    print("Starting OpenCLOW Multi-Agent Session...")

    # Agent 1: Researcher
    research_task = "List 3 core features of a multi-agent AI system."
    research_data = call_agent("Researcher", "You are a technical researcher.", research_task)

    # Agent 2: Technical Writer
    writer_task = f"Turn this research into a professional summary: {research_data}"
    final_report = call_agent("Writer", "You are a professional technical writer.", writer_task)

    print("\n--- Final Output ---")
    print(final_report)

if __name__ == "__main__":
    run_multi_agent_flow()
