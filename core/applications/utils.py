import openpyxl
from .tasks import process_application

def process_excel_file(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    for row in ws.iter_rows(min_row=2, values_only=True):  # Пропускаем заголовок
        data = {
            "name": row[6],
            "city": row[14],
            "phone": row[2],
            # добавьте нужные поля
        }
        process_application.delay(data)  # ставим в очередь