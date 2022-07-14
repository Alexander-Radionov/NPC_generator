import PySimpleGUI as sg
from npc_parameter_enums import Stats, LooksFeatures
from npc_generator import NPC
import random
import json


def get_NPC_values(values):
    return [elem for elem in values.keys() if elem.split('_')[0] == "NPC"]


def generate_values(window, event, values):
    for val in get_NPC_values(values):
        if values[f'Checkbox_{val.split("_")[1]}'] == False:
            window[val].update(value=random.choice(window[val].Values))

npc = NPC()
npc_params = npc.__dataclass_fields__
# file_list_column = [
#     [
#         [sg.Text("Best stat:"),
#         sg.Combo([Stats(elem.value).name for elem in Stats], enable_events=True, key='-BEST-')],
#         [sg.Text("Worst stat:"),
#         sg.Combo([Stats(elem.value).name for elem in Stats])],
#         [sg.Text("Looks"),
#         sg.Combo([LooksFeatures(elem.value).name for elem in LooksFeatures])]]
# ]
file_list_column = []
for i, elem in enumerate(npc.get_fields_with_possible_values()):
    text = sg.Text(elem[0])
    combo = sg.Combo(elem[1], enable_events=True, key=f"NPC_{i}_{elem[0]}")
    is_fixed = sg.Checkbox("Is fixed", key=f"Checkbox_{i}")
    ui_elem = [text, combo, is_fixed]
    file_list_column.append(ui_elem)

layout = [[file_list_column], [sg.Button("Generate values")], [sg.Button("Export values")], [sg.Button("Exit")]]


# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Generate values":
        generate_values(window, event, values)

    if event == "Export values":
        css_table = "<table>"
        npc_stats = get_NPC_values(values)
        for k in npc_stats:
            css_table += f"<tr><td>{'_'.join(k.split('_')[2:])}</td><td>{values[k]}</td></tr>"
        css_table += "</table>"
        with open('npc_stats.txt', 'w') as f:
            f.write(css_table)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break


window.close()
