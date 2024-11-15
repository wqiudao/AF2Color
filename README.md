# AF2Color

Set colors for atoms in the loaded PDB file based on the atom_plddts values from the JSON file.
Parameters:
- `json_file`: Path to the JSON file containing the atom_plddts values

The JSON file is located in PyMOL's current working directory; otherwise, the full path is required.

<pre> af2color json_file  </pre>

# Data Preparation
We need to prepare three files, located in the same directory:

  1. The script `af2color_local.py`, which needs to be downloaded to the local machine.
  2. The Alphafold prediction result files, including `PDB` or `CIF` format structure files, as well as the corresponding `JSON` format files containing pLDDT values (The predicted local distance difference test).
  3. Structural predictions can be obtained through Alphafold3 online (https://golgi.sandbox.google.com/), which is very fast, but currently limited to 20 predictions per day. Alternatively, you can download from the Alphafold database.
  <img src="https://github.com/wqiudao/AF2Color/blob/main/img/af2_data.png" alt="Alt text" width="800">
-
  <img src="https://github.com/wqiudao/AF2Color/blob/main/img/af2color.png" alt="Alt text" width="800">
-

# install & run
`run af2color_local.py`







<img src="https://github.com/wqiudao/AF2Color/blob/main/img/af2color1.png" alt="Alt text" width="800">
<img src="https://github.com/wqiudao/AF2Color/blob/main/img/af2color2.png" alt="Alt text" width="800">
<img src="https://github.com/wqiudao/AF2Color/blob/main/img/af2color3.png" alt="Alt text" width="800">
<img src="https://github.com/wqiudao/AF2Color/blob/main/img/af2color4.png" alt="Alt text" width="800">


