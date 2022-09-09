from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://atreo.io/")
    page.screenshot(path="home.png")
    page.locator('//li[contains(@id,"menu-item")]//a[contains(text(),"Resources")]').click()
    page.screenshot(path="Resources.png")
    page.locator('//li[contains(@id,"menu-item")]//a[contains(text(),"Solutions")]').click()
    page.screenshot(path="Solutions.png")
    page.locator('//li[contains(@id,"menu-item")]//a[contains(text(),"Pricing")]').click()
    page.screenshot(path="Pricing.png")
    page.locator('//div[@id="form_request_quote"]//div[@class="modal-content"]//button[@aria-label="Close"]['
                 '@class="close"]').click()
    page.locator('//div[@class="box-nav desktop"]//div[@class="menu-main-navigation-container"]//ul//li//span['
                 'contains(text(),"Show submenu of About")]').click()
    page.locator('//li[@id]//ul//li//a[contains(text(),"Team")]').click()
    page.screenshot(path="Team.png")
    page.locator('//h4[contains(text(),"John Bennett")]').click()
    page.screenshot(path="TeamMember.png")
    page.close()
    browser.close()
