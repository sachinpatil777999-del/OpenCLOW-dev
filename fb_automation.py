import asyncio
from playwright.async_api import async_playwright

async def fb_login():
    async with async_playwright() as p:
        # 'persistent_context' use kar rahe hain taaki login session save rahe
        # Isse aapko bar-bar login nahi karna padega
        context = await p.chromium.launch_persistent_context(
            "./fb_session", 
            headless=False
        )
        page = await context.new_page()

        print("--- Navigating to Facebook ---")
        await page.goto("https://www.facebook.com/")
        
        print("--- Waiting 60 seconds (Pehli baar manually login kar lijiye) ---")
        # 60 seconds milenge login details daalne ke liye
        await asyncio.sleep(60) 
        
        await context.close()

if __name__ == "__main__":
    asyncio.run(fb_login())
