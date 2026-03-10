import asyncio
from playwright.async_api import async_playwright

async def fb_login():
    async with async_playwright() as p:
        # headless=False taaki aap dekh sakein browser kaise khul raha hai
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print("--- Navigating to Facebook ---")
        await page.goto("https://www.facebook.com/")
        
        print("--- Page Loaded Successfully ---")
        # Yahan aap manual login kar sakte hain test ke liye
        await asyncio.sleep(10) 
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(fb_login())
