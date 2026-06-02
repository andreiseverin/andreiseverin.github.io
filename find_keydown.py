with open('f:/Cobol training/mainframe-academy/src/components/ISPFEmulator.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'addEventListener' in line or 'keydown' in line or 'handleKeyDown' in line or 'onKeyDown' in line:
        print(f"{i+1}: {line.strip()}")
