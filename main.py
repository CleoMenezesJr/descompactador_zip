import PySimpleGUI as sg
import zipfile

sg.theme('dark grey 9')

layout  = [
    [sg.Text('Escolha o arquivo .ZIP')],
    [sg.InputText(key='zipFile'), sg.FileBrowse()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Descompactador', layout)

event, values = window.read()


zip_file = values['zipFile']
zip_object = zipfile.ZipFile(file=zip_file, mode='r')
zip_object.extractall("unzipFiles/")