import asyncio
import ollama
import os
import glob
from datetime import datetime
import pytz
from playwright.async_api import async_playwright

# 1. TIER-1 TIMEZONE LOGIC
def is_it_posting_time():
    # USA Eastern Time (New York) check kar rahe hain
    tz_ny = pytz.timezone('America/New_York')
    ny_now = datetime.now(tz_ny)
    
    # Tier-1 mein subah 9 AM se 11 AM ke beech sabse zyada engagement hota hai
    if 9 <= ny_now.hour <= 11:
        return True
    return False

async def generate_viral_caption():
    print("--- AI (Llama 3.2-1B) Viral Caption likh raha hai... ---")
    prompt = """
    Write a viral Facebook caption for a Tier-1 audience (USA/UK). 
    Topic: Success and Luxury.
    Requirements: 
    - Use a 'Hook' in the first line.
    - Ask a question to get more 'Comments'.
    - Use 3 high-trending emojis.
    - Professional but engaging English.
    """
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

async def run_viral_flow():
    # Time check (Optional: Abhi testing ke liye isse bypass kar sakte hain)
    # if not is_it_posting_time():
    #     print("Not the best time for Tier-1 engagement. Waiting...")
    #     return

    caption = await generate_viral_caption()
    
    # Desktop se image uthana
    desktop_path = os.path.expanduser("~/Desktop/*.png")
    images = glob.glob(desktop_path)
    if not images:
        print("Desktop par koi image nahi mili!")
        return
    image_path = max(images, key=os.path.getctime)

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context("./fb_session", headless=False)
        page = await context.new_page()

        print(f"--- Posting for Global Audience ---")
        await page.goto("https://www.facebook.com/")
        await asyncio.sleep(5)

        try:
            # Facebook Post Logic
            await page.click("text=Photo/video")
            await asyncio.sleep(3)
            async with page.expect_file_chooser() as fc_info:
                await page.click("text=Add Photos/Videos")
            file_chooser = await fc_info.value
            await file_chooser.set_files(image_path)
            
            await page.keyboard.type(caption)
            print(f"Viral Caption: {caption}")
            
            # Post Button par focus
            print("--- Ready! Check karke Post dabayein ---")
            await asyncio.sleep(20) 
        except Exception as e:
            print(f"Error: {e}")
        
        await context.close()

if __name__ == "__main__":
    asyncio.run(run_viral_flow())
