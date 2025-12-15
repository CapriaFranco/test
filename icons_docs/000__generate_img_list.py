import os

COLOR_SUFFIX = "-2af1f1"
EXT = ".svg"

folder = os.getcwd()
lines = []

for file in sorted(os.listdir(folder)):
    if file.endswith(f"{COLOR_SUFFIX}{EXT}"):
        lines.append(
            f'<img src="{file}" style="width:48px;height:48px;" />'
        )

result = "\n".join(lines)

print(result)
