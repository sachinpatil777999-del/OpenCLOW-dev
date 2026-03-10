import asyncio
from playwright.async_api import async_playwright

async def fb_login():
    # Apni details yahan dalein
    USER_EMAIL = "your_email@example.com"
    USER_PASS = "your_password123"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Window dikhne ke liye
        context = await browser.new_context()
        page = await context.new_page()

        print("--- Navigating to Facebook ---")
        await page.goto("https://www.facebook.com/")

        # Email aur Password fill karna
        print("--- Filling Login Details ---")
        await page.fill('input[name="email"]', USER_EMAIL)
        await page.fill('input[name="pass"]', USER_PASS)

        # Login button click karna
        print("--- Clicking Login Button ---")
        await page.click('button[name="login"]')

        # Wait karein taaki aap dekh sakein login hua ya nahi
        print("--- Waiting for 10 seconds to check result ---")
        await asyncio.sleep(10) 

        await browser.close()

if __name__ == "__main__":
    asyncio.run(fb_login())
