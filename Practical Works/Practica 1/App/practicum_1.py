import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Конвертер валют"
    page.window_width = 500
    page.window_height = 600
    
    rates = {"USD": 1.0, "EUR": 0.92, "RUB": 90.0, "GBP": 0.79, "CNY": 7.2}
    
    def load_rates():
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            data = response.json()
            if data["rates"]:
                rates["USD"] = 1.0
                rates["EUR"] = data["rates"].get("EUR", 0.92)
                rates["RUB"] = data["rates"].get("RUB", 90.0)
                rates["GBP"] = data["rates"].get("GBP", 0.79)
                rates["CNY"] = data["rates"].get("CNY", 7.2)
                rates_text.value = f"USD: {rates['USD']:.2f}\nEUR: {rates['EUR']:.2f}\nRUB: {rates['RUB']:.2f}\nGBP: {rates['GBP']:.2f}\nCNY: {rates['CNY']:.2f}"
                status_text.value = "Курсы загружены"
            page.update()
        except:
            status_text.value = "Ошибка загрузки курсов"
            page.update()
    
    def swap_currencies(e):
        from_curr = from_currency.value
        to_curr = to_currency.value
        from_currency.value = to_curr
        to_currency.value = from_curr
        page.update()
    
    def convert(e):
        try:
            amount = float(amount_input.value)
            from_curr = from_currency.value
            to_curr = to_currency.value
            
            usd_amount = amount / rates[from_curr]
            result = usd_amount * rates[to_curr]
            
            result_text.value = f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}"
            page.update()
        except ValueError:
            result_text.value = "Введите корректную сумму"
            page.update()
    
    currencies = ["USD", "EUR", "RUB", "GBP", "CNY"]
    
    from_currency = ft.Dropdown(
        label="Из валюты",
        options=[ft.dropdown.Option(c) for c in currencies],
        value="USD",
        width=150
    )
    
    to_currency = ft.Dropdown(
        label="В валюту",
        options=[ft.dropdown.Option(c) for c in currencies],
        value="RUB",
        width=150
    )
    
    amount_input = ft.TextField(label="Количество", width=300)
    
    result_text = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
    status_text = ft.Text("", color=ft.Colors.GREEN)
    
    rates_text = ft.Text(
        f"USD: {rates['USD']:.2f}\nEUR: {rates['EUR']:.2f}\nRUB: {rates['RUB']:.2f}\nGBP: {rates['GBP']:.2f}\nCNY: {rates['CNY']:.2f}",
        size=16
    )
    
    rates_box = ft.Container(
        content=ft.Column([
            ft.Text("Актуальные курсы (к USD)", size=18, weight=ft.FontWeight.BOLD),
            rates_text,
            ft.ElevatedButton("Обновить курсы", on_click=lambda e: load_rates()),
            status_text
        ]),
        padding=10,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=10
    )
    
    converter_box = ft.Container(
        content=ft.Column([
            ft.Text("Конвертер", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([from_currency, ft.Icon(ft.Icons.SWAP_HORIZ), to_currency]),
            amount_input,
            ft.Row([
                ft.ElevatedButton("Конвертировать", on_click=convert),
                ft.ElevatedButton("Поменять валюты", on_click=swap_currencies)
            ]),
            result_text
        ]),
        padding=10,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=10
    )
    
    page.add(rates_box, ft.Divider(), converter_box)
    load_rates()

ft.app(target=main)
