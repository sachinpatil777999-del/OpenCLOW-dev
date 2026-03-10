import asyncio
from playwright.async_api import async_playwright

async def fb_login():
    async with async_playwright() as p:
        # headless=False taaki aap dekh sakein browser kaise kaam kar raha hai
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print("--- Navigating to Facebook ---")
        await page.goto("https://www.facebook.com/")

        print("--- Page Loaded. Waiting for 10 seconds ---")
        # Yahan aap manual check kar sakte hain ya automation logic add kar sakte hain
        await asyncio.sleep(10) 

        print("--- Closing Browser ---")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(fb_login())
