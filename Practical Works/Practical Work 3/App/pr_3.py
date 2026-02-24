import flet as ft
import math


def main(page: ft.Page):
    page.title = 'Показатели долговечности системы'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_m = ft.TextField(label='Средняя наработка (m), часов', value='2000')
    input_sigma = ft.TextField(label='Среднеквадратическое отклонение (σ), часов', value='400')
    input_q1 = ft.TextField(label='Вероятность отказа Q1', value='0.9')
    input_q2 = ft.TextField(label='Вероятность отказа Q2', value='0.5')
    input_q3 = ft.TextField(label='Вероятность отказа Q3', value='0.005')

    def normal_quantile(p):
        return math.sqrt(2) * (p - 0.5) / (1 - (p - 0.5) ** 2) if 0.01 <= p <= 0.99 else (
            -2.5 if p < 0.01 else 2.5
        )

    def calculate(e):
        m = float(input_m.value or 0)
        sigma = float(input_sigma.value or 0)
        q_values = [float(input_q1.value or 0), float(input_q2.value or 0), float(input_q3.value or 0)]

        calc_details = f'Дано:\nСредняя наработка m = {m} часов\nСреднеквадратическое отклонение σ = {sigma} часов\n\n'

        z_values = []
        for i, q in enumerate(q_values):
            p = 1 - q
            z = normal_quantile(p)
            z_values.append(z)
            t = m + sigma * z

            calc_details += f'--- Расчет для Q({i+1}) = {q} ---\n'
            calc_details += f'P(t) = 1 - Q(t) = 1 - {q} = {p}\n'
            calc_details += f'z = (P - m) / σ = ({p} - {m}) / {sigma} = {z:.4f}\n'
            calc_details += f't = m + σ × z = {m} + {sigma} × {z:.4f}\n'
            calc_details += f't = {t:.2f} часов\n\n'

        calc_details += f'Ответ: t₁ = {m + sigma * z_values[0]:.2f} ч, t₂ = {m + sigma * z_values[1]:.2f} ч, t₃ = {m + sigma * z_values[2]:.2f} ч'

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
        ft.Text('Вариант 1: Показатели долговечности', size=20, weight=ft.FontWeight.BOLD),
        ft.Text('Определение значений наработок до отказа'),
        input_m, input_sigma,
        ft.Text('Вероятности отказа:'),
        input_q1, input_q2, input_q3,
        ft.Button('Рассчитать', on_click=calculate)
    )


if __name__ == "__main__":
    ft.app(target=main)
