import os

COLOR_SUFFIX = "-2af1f1"
EXT = ".svg"

folder = os.getcwd()

for file in os.listdir(folder):
    if not file.lower().endswith(EXT):
        continue

    name = file[:-4]

    if name.endswith(COLOR_SUFFIX):
        continue  # ya tiene el sufijo

    new_name = f"{name}{COLOR_SUFFIX}{EXT}"
    os.rename(
        os.path.join(folder, file),
        os.path.join(folder, new_name)
    )

print("Renombrado completo.")
