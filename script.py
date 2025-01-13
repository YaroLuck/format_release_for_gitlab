import os

# Названия входного и выходного файлов
INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    result = []
    current_header = None

    for line in lines:
        stripped_line = line.strip()

        # Если строка пустая, пропускаем её
        if not stripped_line:
            continue

        # Если строка не начинается с квадратной скобки, это заголовок
        if not stripped_line.startswith("["):
            # Добавляем заголовок с форматированием
            current_header = stripped_line
            result.append(f"**{current_header}**\n")
        else:
            # Добавляем задачи под текущим заголовком
            result.append(f"- {stripped_line}\n")

    # Сохраняем результат в файл
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(result)

    print(f"Файл успешно преобразован и сохранён как '{output_file}'")

if __name__ == "__main__":
    # Проверяем, существует ли входной файл
    if not os.path.exists(INPUT_FILENAME):
        print(f"Файл '{INPUT_FILENAME}' не найден в текущей директории.")
    else:
        process_file(INPUT_FILENAME, OUTPUT_FILENAME)
