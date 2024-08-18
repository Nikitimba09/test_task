import sys


def load_replacements(config_file):
    replacements = {}
    with open(config_file, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                replacements[key] = value
    return replacements


def process_text_file(text_file, replacements):
    modified_lines = []

    with open(text_file, 'r') as f:
        for line in f:
            original_line = line.strip()
            modified_line = original_line
            replace_count = 0

            for key, value in replacements.items():
                occurrences = modified_line.count(key)
                if occurrences > 0:
                    replace_count += occurrences
                    modified_line = modified_line.replace(key, value)

            if replace_count > 0:
                modified_lines.append((modified_line, replace_count))

    return modified_lines


def main(config_file, text_file):
    replacements = load_replacements(config_file)
    modified_lines = process_text_file(text_file, replacements)

    # Sort rows by number of replacements
    modified_lines.sort(key=lambda x: x[1], reverse=True)

    for line, _ in modified_lines:
        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <config_file> <text_file>")
    else:
        try:
            main(sys.argv[1], sys.argv[2])
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
