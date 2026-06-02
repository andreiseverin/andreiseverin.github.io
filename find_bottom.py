with open('f:/Cobol training/mainframe-academy/src/app/dashboard/page.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'bottomPanel' in line or 'spool' in line or 'cics' in line or 'tso' in line:
        print(f"{i+1}: {line.strip()}")
