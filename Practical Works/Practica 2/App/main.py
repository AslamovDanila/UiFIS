import flet as ft
import random

russian_words = [
    "дом", "кот", "собака", "свет"
]

word_images = {
    "дом": "https://picsum.photos/200/200?random=1",
    "кот": "https://picsum.photos/200/200?random=2",
    "собака": "https://picsum.photos/200/200?random=3",
    "дерево": "https://picsum.photos/200/200?random=4",
    "река": "https://picsum.photos/200/200?random=5",
    "гора": "https://picsum.photos/200/200?random=6",
    "солнце": "https://picsum.photos/200/200?random=7",
    "луна": "https://picsum.photos/200/200?random=8",
    "звезда": "https://picsum.photos/200/200?random=9",
    "море": "https://picsum.photos/200/200?random=10",
    "лес": "https://picsum.photos/200/200?random=11",
    "птица": "https://picsum.photos/200/200?random=12",
    "рыба": "https://picsum.photos/200/200?random=13",
    "цветок": "https://picsum.photos/200/200?random=14",
    "трава": "https://picsum.photos/200/200?random=15",
    "небо": "https://picsum.photos/200/200?random=16",
    "земля": "https://picsum.photos/200/200?random=17",
    "огонь": "https://picsum.photos/200/200?random=18",
    "вода": "https://picsum.photos/200/200?random=19",
    "ветер": "https://picsum.photos/200/200?random=20",
    "дождь": "https://picsum.photos/200/200?random=21",
    "снег": "https://picsum.photos/200/200?random=22",
    "лед": "https://picsum.photos/200/200?random=23",
    "тепло": "https://picsum.photos/200/200?random=24",
    "холод": "https://picsum.photos/200/200?random=25",
    "день": "https://picsum.photos/200/200?random=26",
    "ночь": "https://picsum.photos/200/200?random=27",
    "утро": "https://picsum.photos/200/200?random=28",
    "вечер": "https://picsum.photos/200/200?random=29",
    "зима": "https://picsum.photos/200/200?random=30",
    "весна": "https://picsum.photos/200/200?random=31",
    "лето": "https://picsum.photos/200/200?random=32",
    "осень": "https://picsum.photos/200/200?random=33",
    "работа": "https://picsum.photos/200/200?random=34",
    "игра": "https://picsum.photos/200/200?random=35",
    "школа": "https://picsum.photos/200/200?random=36",
    "книга": "https://picsum.photos/200/200?random=37",
    "ручка": "https://picsum.photos/200/200?random=38",
    "стол": "https://picsum.photos/200/200?random=39",
    "стул": "https://picsum.photos/200/200?random=40",
    "окно": "https://picsum.photos/200/200?random=41",
    "дверь": "https://picsum.photos/200/200?random=42",
    "стена": "https://picsum.photos/200/200?random=43",
    "пол": "https://picsum.photos/200/200?random=44",
    "потолок": "https://picsum.photos/200/200?random=45",
    "еда": "https://picsum.photos/200/200?random=46",
    "вкус": "https://picsum.photos/200/200?random=47",
    "запах": "https://picsum.photos/200/200?random=48",
    "звук": "https://picsum.photos/200/200?random=49",
    "свет": "https://avatars.mds.yandex.net/i?id=c749e09fa7371e78593935929cbc6038_l-4328551-images-thumbs&n=13"
}

def get_random_word():
    return random.choice(russian_words)

def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

async def main(page: ft.Page):
    page.title = "Puzzle Word Game"
    page.theme_mode = ft.ThemeMode.LIGHT

    original_word = get_random_word()
    shuffled_word = shuffle_word(original_word)

    shuffled_text = ft.Text(f"Перемешанное слово: {shuffled_word}", size=20)
    hint_image = ft.Image(src=word_images[original_word], width=200, height=200)
    guess_field = ft.TextField(label="Угадайте слово", width=300)
    result_text = ft.Text("", size=16)

    def check_guess(e):
        guess = guess_field.value.strip().lower()
        if guess == original_word.lower():
            result_text.value = "Правильно! Вы угадали слово."
            result_text.color = ft.Colors.GREEN
        else:
            result_text.value = "Неправильно. Попробуйте еще раз."
            result_text.color = ft.Colors.RED
        page.update()

    def new_word(e):
        nonlocal original_word, shuffled_word
        original_word = get_random_word()
        shuffled_word = shuffle_word(original_word)
        shuffled_text.value = f"Перемешанное слово: {shuffled_word}"
        hint_image.src = word_images[original_word]
        guess_field.value = ""
        result_text.value = ""
        page.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_guess)
    new_button = ft.ElevatedButton("Новое слово", on_click=new_word)

    page.add(
        ft.Column([
            shuffled_text,
            hint_image,
            guess_field,
            ft.Row([check_button, new_button]),
            result_text
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
