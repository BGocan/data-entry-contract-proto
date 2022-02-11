import datetime
from pathlib import Path

import PySimpleGUI as sg
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "my_contract_template.docx"
doc = DocxTemplate(document_path)

today = datetime.datetime.today()


layout = [
    [sg.Text("Nome Completo:"), sg.Input(key = "NOME_COMPLETO", do_not_clear=False)],
    [sg.Text("Nacionalidade:"), sg.Input(key = "NACIONALIDADE", do_not_clear=False)],
    [sg.Text("Estado Civil:"), sg.Input(key = "ESTADO_CIVIL", do_not_clear=False)],
    [sg.Text("Ocupacao:"), sg.Input(key = "PROFISSAO", do_not_clear=False)],
    [sg.Text("RG:"), sg.Input(key = "RG", do_not_clear=False)],
    [sg.Text("CPF:"), sg.Input(key = "CPF", do_not_clear=False)],
    [sg.Text("Endereco 1:"), sg.Input(key = "ENDERECO", do_not_clear=False)],
    [sg.Text("Numero:"), sg.Input(key = "NUMERO", do_not_clear=False)],
    [sg.Text("MOD:"), sg.Input(key = "MOD", do_not_clear=False)],
    [sg.Text("Endereco 2:"), sg.Input(key = "ENDERECO_2", do_not_clear=False)],
    [sg.Text("CEP:"), sg.Input(key = "CEP", do_not_clear=False)],
    [sg.Text("Acao de:"), sg.Input(key = "ACAO", do_not_clear=False)],
    [sg.Text("Percentual Total:"), sg.Input(key = "PERCENTUAL", do_not_clear=False)],
    [sg.Button("Criar Contrato"), sg.Exit()],
]

window = sg.Window("Gerador de Contratos", layout, element_justification="right")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Criar Contrato":
        # Add calculated fields to our dict
        # Render the template, save new word document & inform user
        doc.render(values)
        output_path = Path(__file__).parent / f"{values['NOME_COMPLETO']}-contrato.docx"
        doc.save(output_path)
        sg.popup("Arquivo Salvo!",f"Arquivo salvo em: {output_path}")




window.close()