import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(kines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
