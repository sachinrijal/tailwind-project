# import os

# folder_path = r"C:\Users\Lenovo\Desktop\tailwind_landing_page\assests"

# files = sorted(os.listdir(folder_path))

# count = 4

# for file in files:
#     if file.startswith("asset%20"):
#         old_path = os.path.join(folder_path, file)

#         extension = os.path.splitext(file)[1]

#         new_name = f"c{count}{extension}"
#         new_path = os.path.join(folder_path, new_name)

#         os.rename(old_path, new_path)
#         print(f"Renamed: {file} → {new_name}")

#         count += 1

import sys


def process_cases(case_index, total_cases, lines, line_index, outputs):
    if case_index >= total_cases:
        return outputs

    if line_index >= len(lines):
        return outputs

    # Read X
    try:
        x = int(lines[line_index].strip())
    except:
        outputs.append("-1")
        return process_cases(case_index + 1, total_cases, lines, line_index + 1, outputs)

    line_index += 1

    numbers = []
    if line_index < len(lines):
        numbers = list(map(int, lines[line_index].strip().split()))
    line_index += 1

    if len(numbers) != x:
        outputs.append("-1")
    else:
        filtered = filter(lambda v: v <= 0, numbers)
        total = sum(map(lambda v: v ** 4, filtered))
        outputs.append(str(total))

    return process_cases(case_index + 1, total_cases, lines, line_index, outputs)


def main():
    lines = sys.stdin.read().strip().splitlines()
    print('lines : ',lines)
    if not lines:
        return

    try:
        total_cases = int(lines[0].strip())
    except:
        return

    outputs = []
    process_cases(0, total_cases, lines, 1, outputs)

    if outputs:
        sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()