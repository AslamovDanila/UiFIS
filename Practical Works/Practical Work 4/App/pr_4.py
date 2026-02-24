import flet as ft
import math


def main(page: ft.Page):
    page.title = 'Комплексные показатели надежности'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_t = ft.TextField(label='Средняя наработка на отказ (T), часов', value='200')
    input_tv = ft.TextField(label='Среднее время восстановления (Tв), часов', value='2')

    def calculate(e):
        T = float(input_t.value or 0)
        Tv = float(input_tv.value or 0)

        if T > 0 and Tv > 0:
            lambda_val = 1 / T
            mu = 1 / Tv
            Kg = mu / (lambda_val + mu)
            Kp = lambda_val / (lambda_val + mu)

            calc_details = f'Дано:\nT = {T} часов\nTв = {Tv} часов\n\n'
            calc_details += f'--- Расчет ---\n'
            calc_details += f'Интенсивность отказов: λ = 1/T = 1/{T} = {lambda_val:.6f} 1/ч\n'
            calc_details += f'Интенсивность восстановления: μ = 1/Tв = 1/{Tv} = {mu:.6f} 1/ч\n\n'
            calc_details += f'Коэффициент готовности:\n'
            calc_details += f'Kг = μ / (λ + μ) = {mu:.6f} / ({lambda_val:.6f} + {mu:.6f}) = {mu:.6f} / {lambda_val + mu:.6f} = {Kg:.6f}\n\n'
            calc_details += f'Коэффициент простоя:\n'
            calc_details += f'Kп = λ / (λ + μ) = {lambda_val:.6f} / ({lambda_val:.6f} + {mu:.6f}) = {lambda_val:.6f} / {lambda_val + mu:.6f} = {Kp:.6f}\n\n'
            calc_details += f'Ответ: Kг = {Kg:.6f}, Kп = {Kp:.6f}'
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
        ft.Text('Вариант 1: Комплексные показатели надежности', size=20, weight=ft.FontWeight.BOLD),
        ft.Text('Расчет коэффициента готовности и коэффициента простоя'),
        input_t, input_tv,
        ft.Button('Рассчитать', on_click=calculate)
    )


if __name__ == "__main__":
    ft.app(target=main)
