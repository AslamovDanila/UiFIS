import flet as ft


def main(page: ft.Page):
    page.title = 'Единичные показатели достоверности информации'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_records = ft.TextField(label='Количество обработанных записей', value='120000')
    input_errors = ft.TextField(label='Обнаружено ошибок', value='240')
    input_fixed = ft.TextField(label='Правильно исправлено', value='180')
    input_distorted = ft.TextField(label='Искажено', value='12')

    def calculate(e):
        records = float(input_records.value or 0)
        errors = float(input_errors.value or 0)
        fixed = float(input_fixed.value or 0)
        distorted = float(input_distorted.value or 0)

        if records > 0 and errors > 0:a
            lambda_val = errors / records
            Ki = fixed / errors
            detected = errors - fixed - distorted

            calc_details = f'Дано:\nКоличество записей: {int(records)}\nОбнаружено ошибок: {int(errors)}\nПравильно исправлено: {int(fixed)}\nИскажено: {int(distorted)}\nТолько обнаружено: {int(detected)}\n\n'
            calc_details += f'--- Расчет ---\n\n'
            calc_details += f'а) Вероятность ошибки λ:\n'
            calc_details += f'λ = Nошибок / Nзаписей = {int(errors)} / {int(records)} = {lambda_val:.6f}\n\n'
            calc_details += f'б) Коэффициент исправления ошибок Kи:\n'
            calc_details += f'Kи = Nисправлено / Nобнаружено = {int(fixed)} / {int(errors)} = {Ki:.6f}\n\n'
            calc_details += f'Ответ: λ = {lambda_val:.6f}, Kи = {Ki:.6f}'
        else:
            calc_details = 'Ошибка: значения должны быть больше 0'

        dlg = ft.AlertDialog(
            title=ft.Text('Результат расчета'),
            content=ft.ListView(
                controls=[ft.Text(calc_details, size=14)],
                height=350,
                expand=True
            )
        )
        page.open(dlg)

    page.add(
        ft.Text('Вариант 1: Достоверность информации', size=20, weight=ft.FontWeight.BOLD),
        ft.Text('Расчет вероятности ошибки и коэффициента исправления'),
        input_records, input_errors, input_fixed, input_distorted,
        ft.Button('Рассчитать', on_click=calculate)
    )


if __name__ == "__main__":
    ft.app(target=main)
