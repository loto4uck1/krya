import PySimpleGUI as sg
import datetime
from utils import get_first_and_last_day_of_month

def display_calendar(selected_month=None, selected_year=None):
    current_date = datetime.datetime.now()

    if selected_month is None:
        selected_month = current_date.month
    if selected_year is None:
        selected_year = current_date.year

    sg.theme('DarkGreen6')

    layout = [
        [sg.Text("Календар:", font=('Helvetica', 14))],
        [sg.Button("Попередній місяць"), sg.Text(f"{datetime.datetime(current_date.year, selected_month, 1).strftime('%B %Y')}", size=(20, 1), font=('Helvetica', 14)), sg.Button("Наступний місяць")],
        [sg.Text("Пн   Вт   Ср   Чт   Пт   Сб   Нд", font=('Helvetica', 12))],
    ]

    first_day_of_month, last_day_of_month, start_of_week = get_first_and_last_day_of_month(selected_year, selected_month)

    day = 1
    for _ in range(6):
        row = []
        for i in range(7):
            if day > last_day_of_month.day:
                break
            if i < start_of_week and day == 1:
                row.append(sg.Text("      ", font=('Helvetica', 12), justification='center'))
            else:
                row.append(sg.Text(f"{day:2d}", font=('Helvetica', 12), justification='center'))
                day += 1
        layout.append(row)

    layout.append([sg.Button("Вийти")])

    window = sg.Window('Календар', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Вийти':
            break
        elif event == 'Попередній місяць':
            selected_month -= 1
            if selected_month == 0:
                selected_month = 12
                selected_year -= 1
        elif event == 'Наступний місяць':
            selected_month += 1
            if selected_month == 13:
                selected_month = 1
                selected_year += 1

        window.close()
        display_calendar(selected_month, selected_year)  # Рекурсивно викликаємо функцію для нового місяця та року

    window.close()
