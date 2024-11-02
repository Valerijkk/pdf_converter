from pdf2docx import Converter  # Импортируем класс Converter из библиотеки pdf2docx
import tkinter as tk  # Импортируем библиотеку tkinter для создания графических интерфейсов
from tkinter import filedialog  # Импортируем модуль filedialog для открытия диалоговых окон выбора файлов
import os  # Импортируем модуль os для работы с файловой системой

# Создаем главное окно приложения и скрываем его, так как нам не нужно отображать GUI
root = tk.Tk()
root.withdraw()

# Открываем диалоговое окно для выбора PDF файла
pdf_file = filedialog.askopenfilename(
    title="Выберите PDF файл",  # Заголовок окна выбора файла
    filetypes=[("PDF файлы", "*.pdf")],  # Фильтр для отображения только PDF файлов
)

# Проверяем, был ли выбран файл пользователем
if not pdf_file:
    print("PDF файл не выбран.")  # Выводим сообщение, если файл не выбран
    exit()  # Завершаем программу

# Открываем диалоговое окно для выбора места и имени для сохранения DOCX файла
docx_file = filedialog.asksaveasfilename(
    title="Сохранить как DOCX",  # Заголовок окна сохранения файла
    defaultextension=".docx",  # Расширение по умолчанию
    filetypes=[("DOCX файлы", "*.docx")],  # Фильтр для отображения только DOCX файлов
)

# Проверяем, был ли указан путь для сохранения файла
if not docx_file:
    print("Место сохранения DOCX файла не выбрано.")  # Выводим сообщение, если путь не указан
    exit()  # Завершаем программу

# Выполняем конвертацию PDF в DOCX
try:
    cv = Converter(pdf_file)  # Создаем объект конвертера с выбранным PDF файлом
    cv.convert(docx_file)     # Конвертируем PDF в DOCX и сохраняем по указанному пути
    cv.close()                # Закрываем конвертер
    print(f"Файл успешно конвертирован и сохранен как {docx_file}")  # Сообщаем об успешной конвертации
except Exception as e:
    print(f"Произошла ошибка при конвертации: {e}")  # Выводим сообщение об ошибке, если она произошла