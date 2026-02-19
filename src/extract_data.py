# ================== IMPORTS ==================
import os
import time
import psutil
import subprocess
import win32com.client

from datetime import datetime
from config.settings import SAP_USER, SAP_PASSWORD, SAP_PATH_SOURCE, SAP_TRANSACTION, PATH_DATASET_REPORT

# ================== SAP - CONTROLE ==================
def is_sap_gui_running():
    return any(
        proc.info["name"] == "saplogon.exe"
        for proc in psutil.process_iter(["name"])
    )

def terminate_sap_gui():
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == "saplogon.exe":
            proc.terminate()
            proc.wait()

def connect_to_sap():
    print("[INFO] Iniciando SAP GUI...")
    if is_sap_gui_running():
        print("[INFO] SAP já estava aberto. Reiniciando...")
        terminate_sap_gui()
        time.sleep(5)

    subprocess.Popen(SAP_PATH_SOURCE)
    time.sleep(10)

    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    print("[OK] Conectado ao SAP GUI")
    return application

def login_sap(application):
    print("[INFO] Realizando login no SAP...")
    connection = application.OpenConnection("PRD [PRODUÇÃO]", True)
    session = connection.Children(0)

    session.findById("wnd[0]/usr/txtRSYST-BNAME").text = SAP_USER
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = SAP_PASSWORD
    session.findById("wnd[0]").sendVKey(0)

    time.sleep(5)
    print("[OK] Login realizado com sucesso")
    return session


def baixar_relatorio(session):
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = SAP_TRANSACTION
    session.findById("wnd[0]").sendVKey (0)
    session.findById("wnd[0]").sendVKey (17)
    session.findById("wnd[1]/usr/txtENAME-LOW").text = SAP_USER
    session.findById("wnd[1]/usr/txtENAME-LOW").setFocus()
    session.findById("wnd[1]/usr/txtENAME-LOW").caretPosition = 5
    session.findById("wnd[1]").sendVKey (8)
    session.findById("wnd[0]/usr/ctxtSO_DATA-LOW").text = datetime.now().strftime('%d/%m/%Y')
    session.findById("wnd[0]/usr/ctxtSO_DATA-HIGH").text = datetime.now().strftime('%d/%m/%Y')
    session.findById("wnd[0]/usr/ctxtSO_DATA-HIGH").setFocus()
    session.findById("wnd[0]/usr/ctxtSO_DATA-HIGH").caretPosition = 8
    session.findById("wnd[0]").sendVKey (8)
    session.findById("wnd[0]/shellcont/shell/shellcont[1]/shell[0]").pressButton ("LAYOUT1")
    session.findById("wnd[1]/usr/ctxtDY_PATH").text = PATH_DATASET_REPORT
    session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "zwm117.xls"
    session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
    session.findById("wnd[1]/tbar[0]/btn[0]").press()