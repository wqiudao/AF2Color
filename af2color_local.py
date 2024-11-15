import json
from pymol import cmd

def af2color(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    plddts = data["atom_plddts"]
    atoms = cmd.get_model("all").atom
    if len(atoms) != len(plddts):
        print("Warning: The number of atoms does not match the number of plddts data!")
        return
    for i, atom in enumerate(atoms):
        plddt = plddts[i]
        if plddt >= 90:
            color_name = "neptunium"
        elif 70 <= plddt < 90:
            color_name = "cyan"
        elif 50 <= plddt < 70:
            color_name = "gold"
        else:
            color_name = "phosphorus"
        atom_selection = f"id {atom.index}"
        cmd.color(color_name, atom_selection)
cmd.extend("af2color", af2color)



