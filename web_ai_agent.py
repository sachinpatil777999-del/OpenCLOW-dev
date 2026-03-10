import asyncio
from playwright.async_api import async_playwright
import ollama

async def get_web_data(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        # Page ka text content nikalna
        text = await page.inner_text('body')
        await browser.close()
        return text[:2000]  # Pehle 2000 characters base model ke liye kafi hain

def analyze_with_ai(web_text):
    print("\n--- AI is analyzing web content... ---")
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'system', 'content': 'You are a research assistant. Summarize the following web data into 3 bullet points.'},
        {'role': 'user', 'content': web_text},
    ])
    return response['message']['content']

async def main():
    url = "https://pypi.org/project/playwright/"
    print(f"Fetching data from: {url}")
    raw_data = await get_web_data(url)
    summary = analyze_with_ai(raw_data)
    print("\n--- WEB SUMMARY ---")
    print(summary)

if __name__ == "__main__":
    asyncio.run(main())
