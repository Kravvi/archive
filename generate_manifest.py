#!/usr/bin/env python3
"""
Сканирует папки в images/ и генерирует manifest.json.
- home/   → только .webp
- остальные → только .jpg / .jpeg
Сортировка: natural sort (числовая), без учёта регистра.
"""

import os
import json
import re

def natural_keys(text):
    """Ключ для числовой сортировки: '2' < '10'."""
    return [
        int(c) if c.isdigit() else c.lower()
        for c in re.split(r'(\d+)', text)
    ]

def main():
    base = 'images'
    manifest = {}

    if not os.path.isdir(base):
        print(f'Папка {base} не найдена — создаю пустой манифест')
        with open('manifest.json', 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
        return

    for category in os.listdir(base):
        category_path = os.path.join(base, category)
        if not os.path.isdir(category_path):
            continue

        files = []
        for f in os.listdir(category_path):
            if category == 'home':
                if f.lower().endswith('.webp'):
                    files.append(f)
            else:
                if f.lower().endswith(('.jpg', '.jpeg')):
                    files.append(f)

        files.sort(key=natural_keys)
        manifest[category] = files
        print(f'{category}: {len(files)} файлов')

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print('manifest.json успешно создан')

if __name__ == '__main__':
    main()