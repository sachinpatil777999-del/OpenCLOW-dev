import ollama
from duckduckgo_search import DDGS

def web_search(query):
    print(f"--- Searching the Web for: {query} ---")
    try:
        results = DDGS().text(query, max_results=3)
        return "\n".join([r['body'] for r in results])
    except Exception as e:
        return f"Search failed: {e}"

def call_agent(agent_name, system_prompt, user_task):
    print(f"\n--- {agent_name} is thinking... ---")
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_task},
    ])
    return response['message']['content']

def run_openclow_v4():
    print("--- OpenCLOW Multi-Agent Session V4 (Web Search Enabled) ---")

    # 1. Real-time Search
    query = "Latest AI breakthroughs March 2026"
    live_data = web_search(query)

    # 2. Researcher analyzes live data
    res_out = call_agent("Researcher", "You are a tech analyst.", f"Summarize the key points from this live data: {live_data}")

    # 3. Writer creates a News Brief
    write_out = call_agent("Writer", "You are a senior tech journalist.", f"Based on this research: {res_out}, write a catchy 3-sentence news update.")

    print("\n--- FINAL LIVE NEWS BRIEF ---")
    print(write_out)

if __name__ == "__main__":
    run_openclow_v4()
