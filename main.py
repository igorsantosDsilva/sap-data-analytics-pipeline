import pandas as pd
from src.extract_data import connect_to_sap, login_sap, baixar_relatorio
from src.transform import gerar_tb_snapshot, atualizar_snapshot
from src.load_data import gerador_img
from config.settings import PATH_CSV, PATH_SNAPSHOT

# EXTRACT
application = connect_to_sap()
session = login_sap(application)
baixar_relatorio(session)

# TRANSFORM
df_raw= pd.read_csv(PATH_CSV, sep="\t", encoding="latin1")
snapshot = gerar_tb_snapshot(df_raw)
df_final = atualizar_snapshot(snapshot, PATH_SNAPSHOT)

#LOAD
gerador_img()


