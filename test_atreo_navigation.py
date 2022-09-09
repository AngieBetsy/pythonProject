from playwright.async_api import async_playwright
import asyncio
import json
import time

"""Exercise Solution to the Atreo application

AutoAtreo class contains a constructor method that loads .json data
async main method handles the test objectives:
    *   Test can navigate through the top bar hitting each item, and finish when
        navigation is complete, and the new page is visible.
    *   Created tests around testing core team page - accessing page and viewing information 
        about specific team member

"""


class AutoAtreo:

    def __init__(self):

        # Data driven and loaded from a json file

        json_file = open('data.json')
        data = json.load(json_file)
        url = "https://atreo.io/"
        systime = str(time.strftime("%d%m%Y")) + str(time.strftime("%H%M%S"))
        self.data = data
        self.url = url
        self.systime = systime

        json_file.close()

    async def test_navigation(self):
        """
        *   Test  navigates through the top bar hitting each item, and finish when
        navigation is complete, and the new page is visible.

        """
        async with async_playwright() as p:
            for every_locator in self.data['locators']:
                """
                *  The below lines of code utilizes the playwright module to launch the browser, 
                   returning instances of Browser and perform actions as necessary to the context 
                   of the test.
                   
                """
                browser = await p.chromium.launch()
                context = await browser.new_context(record_video_dir="./recordings")
                page = await context.new_page()
                await page.goto(self.url)
                await page.screenshot(path=self.systime+"_home.png")
                await page.locator(str(every_locator['resources'])).click()
                await page.screenshot(path=self.systime+"_Resources.png")
                await page.locator(str(every_locator['solutions'])).click()
                await page.screenshot(path=self.systime+"_Solutions.png")
                await page.locator(str(every_locator['pricing'])).click()
                await page.screenshot(path=self.systime+"_Pricing.png")
                await page.locator(str(every_locator['close'])).click()
            await page.close()
            await browser.close()

    async def test_team_page(self):
        """
        *   Test to access the core team page - accessing page and viewing information
        about specific team member

        """
        async with async_playwright() as p:
            for every_locator in self.data['locators']:
                """
                *  The below lines of code utilizes the playwright module to launch the browser, 
                   returning instances of Browser and perform actions as necessary to the context 
                   of the test.
                                
                """
                browser = await p.chromium.launch()
                context = await browser.new_context(record_video_dir="./recordings")
                page = await context.new_page()
                await page.goto(self.url)
                await page.locator(str(every_locator['about_main'])).click()
                await page.locator(str(every_locator['about_team'])).click()
                await page.screenshot(path=self.systime+"_Team.png")
                await page.locator(str(every_locator['team_member'])).click()
                await page.screenshot(path=self.systime+"_TeamMember.png")
            await page.close()
            await browser.close()


a = AutoAtreo()
if __name__ == '__main__':
    asyncio.run(a.test_navigation())
    asyncio.run(a.test_team_page())
