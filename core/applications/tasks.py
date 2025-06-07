import os

from celery import shared_task
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

from .models import ApplicationLog


@shared_task
def process_application(data):
    success = False
    message = ''

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            try:

                page.goto(
                    "https://docs.google.com/forms/d/e/1FAIpQLSf_nlUG2nKxCtJuuYKVcH8JEPXjezmLA49_wRLCtHweXVjttQ/viewform")
                page.get_by_role("textbox", name="Фамилия").click()
                page.get_by_role("textbox", name="Фамилия").fill(data.get('phone'))
                page.get_by_role("textbox", name="Имя").click()
                page.get_by_role("textbox", name="Имя").fill(data.get('name'))
                page.get_by_role("textbox", name="Город").click()
                page.get_by_role("textbox", name="Город").fill(data.get('city'))
                page.get_by_role("button", name="Submit").click()

                # Скриншот успешного результата
                os.makedirs("screenshots", exist_ok=True)
                screenshot_path = f"screenshots/norm_123.png"
                page.screenshot(path=screenshot_path)

                success = True
                message = f"Поиск '123' выполнен успешно"

            except PlaywrightTimeoutError as e:
                message = f"Playwright timeout: {str(e)}"

            except Exception as e:
                message = f"Ошибка внутри Playwright: {str(e)}"

            finally:
                context.close()
                browser.close()

    except Exception as e:
        message = f"Ошибка запуска Playwright: {str(e)}"

    # Запись результата в БД
    ApplicationLog.objects.create(
        city="Москва",
        success=success,
        message=message
    )