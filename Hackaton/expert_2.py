# -*- coding: utf-8 -*-
"""Expert_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s_jbFTGX4jNUOohV-L1MEFgcPglpswcn
"""

import fitz
import pdfplumber
import difflib
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the 'punkt' resource
nltk.download('punkt')

def find_similar_titles(pdf_path, header_text, threshold=0.6):
    titles = []
    header_text = header_text.lower()

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                text_lines = text.split('\n')
                for line in text_lines:
                    line = line.lower()
                    similarity = difflib.SequenceMatcher(None, header_text, line).ratio()

                    if similarity > threshold:
                        title = {
                            'text': line,
                            'similarity': similarity,
                            'page': page_number + 1
                        }
                        titles.append(title)

    return titles

def find_similar_lines(text, header_text, threshold=0.6):
    lines = []
    header_text = header_text.lower()

    for line in text:
        line_lower = line.lower()  # Изменение регистра строки
        similarity = difflib.SequenceMatcher(None, header_text, line_lower).ratio()

        if similarity > threshold:
            lines.append(line)

    return lines

def create_marked_pdf(pdf_path, similar_lines, output_path):
    doc = fitz.open(pdf_path)

    for line in similar_lines:
        for page in doc:
            text_instances = page.search_for(line, hit_max=1)

            for text_instance in text_instances:
                x0, y0, x1, y1 = text_instance
                rect = fitz.Rect(x0, y0, x1, y1)
                underline_annot = page.add_underline_annot(rect)
                underline_annot.colors["stroke"] = (0, 0, 0)  # Установка цвета подчеркивания
                underline_annot.update()

    doc.save(output_path)
    doc.close()

    print("Помеченный PDF-файл создан по пути:", output_path)

# Путь к исходному PDF-файлу
pdf_path = "/path/to/input/pdf/file.pdf"

# Ввод текста эталона пользователем
header_text = input("Введите текст эталона: ")

# Путь к новому файлу
output_path = "/path/to/output/pdf/file.pdf"

# Извлечение полного текста из PDF
doc = fitz.open(pdf_path)
full_text = [line.strip() for page in doc for line in page.get_text().split("\n")]
doc.close()

# Поиск строк с похожим текстом
similar_lines = find_similar_lines(full_text, header_text)

# Создание помеченного PDF-файла
create_marked_pdf(pdf_path, similar_lines, output_path)

# Вывод информации о сходстве и страницах
for line in similar_lines:
    print("Заголовок:", line['text'])
    print("Сходство:", line['similarity'])
    print("Страница:", line['page'])
    print()

print("Помеченный PDF-файл создан по пути:", output_path)