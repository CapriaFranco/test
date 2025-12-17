import os

PATH = "icons_docs/"
COLOR_SUFFIX = "-2af1f1"
EXT = ".svg"

folder = os.getcwd()
lines = []

# 1. Renombrar archivos
for file in os.listdir(folder):
    if not file.lower().endswith(EXT):
        continue

    name = file[:-4]

    if name.endswith(COLOR_SUFFIX):
        continue

    new_name = f"{name}{COLOR_SUFFIX}{EXT}"
    os.rename(
        os.path.join(folder, file),
        os.path.join(folder, new_name)
    )

# 2. Generar lista HTML
for file in sorted(os.listdir(folder)):
    if file.endswith(f"{COLOR_SUFFIX}{EXT}"):
        lines.append(
            f'<img src="{PATH}{file}" style="width:48px;height:48px;" />'
        )

result = "\n".join(lines)
print(result)
print("Renombrado y listado completo.")
