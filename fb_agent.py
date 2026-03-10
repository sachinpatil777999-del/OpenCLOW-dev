import asyncio
from playwright.async_api import async_playwright

async def fb_login():
    async with async_playwright() as p:
        # headless=False taaki aap apni aankhon se dekh sakein
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print("--- Navigating to Facebook ---")
        await page.goto("https://www.facebook.com/")

        # Login details fill karne ka logic (agar aap use karna chahein)
        # await page.fill('input[name="email"]', "YOUR_EMAIL")
        # await page.fill('input[name="pass"]', "YOUR_PASSWORD")
        # await page.click('button[name="login"]')

        print("--- Page Loaded. Waiting for 10 seconds... ---")
        await asyncio.sleep(10) 
        await browser.close()

if __name__ == "__main__":
    asyncio.run(fb_login())
