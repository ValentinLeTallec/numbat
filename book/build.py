import subprocess
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent


def generate_example(filename, title, strip_assets):
    path_in = SCRIPT_DIR.parent / "examples" / f"{filename}.nbt"
    path_out = SCRIPT_DIR / "src" / f"example-{filename}.md"

    code = []
    with open(path_in, "r") as fin:
        for line in fin:
            if not strip_assets or "assert_eq" not in line:
                code.append(line)

    with open(path_out, "w") as fout:
        fout.write("<!-- This file is autogenerated! Do not modify it -->\n")
        fout.write("\n")
        fout.write(f"# {title}\n")
        fout.write("\n")
        fout.write("``` numbat\n")
        fout.writelines(code)
        fout.write("```\n")


generate_example("acidity", "Acidity", True)
generate_example("barometric_formula", "Barometric formula", True)
generate_example("body_mass_index", "Body mass index", True)
generate_example("factorial", "Factorial", False)
generate_example("medication_dosage", "Medication dosage", True)
generate_example("molarity", "Molarity", True)
generate_example("musical_note_frequency", "Musical note frequency", True)
generate_example("paper_size", "Paper sizes", False)
generate_example("pipe_flow_rate", "Flow rate in a pipe", True)
generate_example("population_growth", "Population growth", True)
generate_example("recipe", "Recipe", True)
generate_example("voyager", "Voyager", True)
generate_example("xkcd_687", "XKCD 687", True)
generate_example("xkcd_2585", "XKCD 2585", True)
generate_example("xkcd_2812", "XKCD 2812", True)
generate_example("workhours", "Workhours", True)

generate_example("numbat_syntax", "Syntax overview", False)

path_units = SCRIPT_DIR / "src" / "list-units.md"
with open(path_units, "w") as f:
    subprocess.run(["cargo", "run", "--example=inspect"], stdout=f, text=True)

subprocess.run(["mdbook", "build"], text=True)