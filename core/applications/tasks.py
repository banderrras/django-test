from celery import shared_task
import time

@shared_task
def process_application(data):
    print("=== Получена заявка ===")
    print(data)
    time.sleep(2)
    print("=== Обработка завершена ===")
    return True