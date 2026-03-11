import asyncio
import ollama
import os
import glob
from playwright.async_api import async_playwright

async def generate_caption():
    print("--- AI (Llama 3.2-1B) Caption likh raha hai... ---")
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': 'Write a short luxury motivation caption with emojis for Facebook.'},
    ])
    return response['message']['content']

def get_latest_image():
    # Aapke Desktop se sabse latest image (.jpg ya .png) dhundega
    desktop_path = os.path.expanduser("~/Desktop/*.png") # Aap ise .jpg bhi kar sakte hain
    list_of_files = glob.glob(desktop_path)
    if not list_of_files:
        return None
    return max(list_of_files, key=os.path.getctime)

async def auto_post():
    caption = await generate_caption()
    image_path = get_latest_image()
    
    if not image_path:
        print("Error: Desktop par koi image nahi mili!")
        return

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            "./fb_session", 
            headless=False
        )
        page = await context.new_page()

        print(f"--- Facebook par ja rahe hain... ---")
        await page.goto("https://www.facebook.com/")
        await asyncio.sleep(5)

        try:
            print(f"--- Image upload ho rahi hai: {os.path.basename(image_path)} ---")
            
            # Photo/Video button par click
            await page.click("text=Photo/video")
            await asyncio.sleep(3)

            # File upload handle karna
            async with page.expect_file_chooser() as fc_info:
                # FB ka default "Add Photos/Videos" area click
                await page.click("text=Add Photos/Videos")
            file_chooser = await fc_info.value
            await file_chooser.set_files(image_path)
            
            # Caption type karna
            await page.keyboard.type(caption)
            
            print("--- Sab kuch ready hai! 'Post' button khud dabayein check karne ke liye. ---")
            await asyncio.sleep(15) 

        except Exception as e:
            print(f"Error logic: {e}")
        
        await context.close()

if __name__ == "__main__":
    asyncio.run(auto_post())
