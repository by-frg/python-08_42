#!/usr/bin/env python3
from importlib import metadata, import_module
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lib_dict = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "requests": "Network access",
            "matplotlib": "Visualization",
           }
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


def compare_versions(filename: str, filetype: str) -> None:
    vers_dict: dict[str,str] = {}
    if filetype == "txt":
        f = open(filename, "r")
        l_line = f.read().split("\n")
        vers_dict = {
                     line.split("==")[0].strip():line.split("==")[1].strip() for line in l_line
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
                vers_dict.update({line.split("=")[0].strip() : line.split("=",1)[1].strip('^~ \n"><=')})
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
            print(f"Error: '{lib}' not found. Required version for '{lib}' : {vers}")

#Creating the Arrays & num.computations [NUMPY]
array_x = np.random.randint(15, size=(1000))
array_y = np.random.randint(1000, size=(1000))
y_mean = np.mean(array_y)
y_median = np.median(array_y)
y_std = np.std(array_y)

#Creating the Table [PANDAS]
data = {'worlds': array_x, 'population': array_y}
dframe = pd.DataFrame(data, columns=['worlds', 'population'])
grouped = dframe.groupby("worlds")["population"].sum()
grouped_mean = np.mean(grouped.values)

#Creating the plot [matplotlib]
plt.bar(grouped.index, grouped.values, label = "Population")
plt.axhline(y=grouped_mean, label = "Pop. Mean", color = "red")
plt.legend()
#plt.show()
plt.savefig('matrix_analysis.png')