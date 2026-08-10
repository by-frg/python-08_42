#! /usr/bin/env python3
from importlib import metadata, import_module
import sys

# dictionary to use in for cycle
lib_dict = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "matplotlib": "Visualization",
           }
print("\nLOADING STATUS: Loading Programs...")
print("\nChecking Dependencies:")
# fail list to print failures only once and outside cycle
lib_fail: list[str] = []
for lib, msg in lib_dict.items():
    try:
        module = import_module(lib)
        print(f"[OK] {module.__name__} ({metadata.version(lib)})", end=" ")
        print(f"- {msg} ready")
    except Exception:
        print(f"[KO] {lib}")
        lib_fail.append(lib)
if len(lib_fail) > 0:
    print(
          f"\nMissing modules: {', '.join(lib_fail)}"
          "\n\nInstalling with pip requirements.txt, run:"
          "\n $>pip install -r requirements.txt"
          "\nInstalling with Poetry, run:"
          "\n $>poetry install"
        )
    sys.exit(1)


# subject requests a compare function that compares vrsion installed vs require
# create dictionary with module:version, with 2 conditions: .txt and .toml
# in subject .toml function is not authorized so I did manual cycle
def compare_versions(filename: str, filetype: str) -> None:
    vers_dict: dict[str, str] = {}
    if filetype == "txt":
        f = open(filename, "r")
        l_line = f.read().split("\n")
        vers_dict = {
                     line.split("==")[0].strip(): line.split("==")[1].strip()
                     for line in l_line
                     if "==" in line
                    }
        f.close()
    elif filetype == "toml":
        f = open(filename, "r")
        in_section = False
        for line in f:
            if "[" in line:
                if "tool.poetry.dependencies" in line:
                    in_section = True
                else:
                    in_section = False
            elif in_section and "=" in line and "python" not in line:
                vers_dict.update(
                                 {
                                    line.split("=")[0].strip():
                                    line.split("=", 1)[1].strip('^~ \n"><=')
                                 }
                                )
        f.close()
    else:
        print("Invalid filetype: use 'txt' or 'toml'")
        return None
    for lib, vers in vers_dict.items():
        try:
            print(
                f"{lib:<10} >> inst: {metadata.version(lib):<7} | req: {vers}"
                )
        except ModuleNotFoundError:
            print(
                  f"Error: '{lib}' not found. Required version for "
                  f"'{lib}' : {vers}"
                 )


print("\nComparing installed versions with requirements")
print(">> .TXT:")
compare_versions("requirements.txt", "txt")
print("\n>> .TOML:")
compare_versions("pyproject.toml", "toml")

# programa so corre isto se passar a validacao inicial
# (se n tiver sys.exit para o programa)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating the Arrays & num.computations [NUMPY]
print("\nAnalysing Matrix Data...")
array_x = np.random.randint(15, size=(1000))
array_y = np.random.randint(50, size=(1000))

# Creating the Table [PANDAS]
print("Processing 1000 Data points...")
data = {'zones': array_x, 'agents': array_y}
dframe = pd.DataFrame(data, columns=['zones', 'agents'])
grouped = dframe.groupby("zones")["agents"].sum()
grouped_mean = np.mean(grouped.values)

# Creating the plot [matplotlib]
print("Generating visualization...")
plt.bar(grouped.index, grouped.values, label="Agents Detected")
plt.axhline(y=grouped_mean, label="Avg. Agents per zone", color="red")
plt.legend()
plt.xlabel("Matrix Zones")
plt.ylabel("Agents Detected")
# plt.show()
plt.savefig('matrix_analysis.png')

print("\nAnalysis Complete")
print("Results saved to: matrix_analysis.png")
