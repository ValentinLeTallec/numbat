import subprocess
from pathlib import Path
import urllib.parse


SCRIPT_DIR = Path(__file__).parent.resolve()


def generate_example(filename, title, strip_asserts=True, insert_run_link=True):
    path_in = SCRIPT_DIR.parent / "examples" / f"{filename}.nbt"
    path_out = SCRIPT_DIR / "src" / f"example-{filename}.md"
    print(path_in)
    print(path_out)

    code = []
    with open(path_in, "r") as fin:
        for line in fin:
            if not (strip_asserts and "assert_eq" in line):
                code.append(line)

    url = f"https://numbat.dev/?q={urllib.parse.quote_plus(''.join(code))}"

    with open(path_out, "w") as fout:
        fout.write("<!-- This file is autogenerated! Do not modify it -->\n")
        fout.write("\n")
        fout.write(f"# {title}\n")
        if insert_run_link:
            fout.write(f'<a href="{url}"><i class="fa fa-play"></i> Run this example</a>\n')
        fout.write("\n")
        fout.write("``` numbat\n")
        fout.writelines(code)
        fout.write("```\n")


generate_example("acidity", "Acidity")
generate_example("barometric_formula", "Barometric formula")
generate_example("body_mass_index", "Body mass index")
generate_example("factorial", "Factorial", strip_asserts=False)
generate_example("medication_dosage", "Medication dosage")
generate_example("molarity", "Molarity")
generate_example("musical_note_frequency", "Musical note frequency")
generate_example("paper_size", "Paper sizes")
generate_example("pipe_flow_rate", "Flow rate in a pipe")
generate_example("population_growth", "Population growth")
generate_example("recipe", "Recipe")
generate_example("voyager", "Voyager")
generate_example("xkcd_687", "XKCD 687")
generate_example("xkcd_2585", "XKCD 2585")
generate_example("xkcd_2812", "XKCD 2812")

generate_example("numbat_syntax", "Syntax overview", strip_asserts=False, insert_run_link=False)

path_units = SCRIPT_DIR / "src" / "list-units.md"
with open(path_units, "w") as f:
    subprocess.run(["cargo", "run", "--example=inspect"], stdout=f, text=True)

subprocess.run(["mdbook", "build"], text=True)
