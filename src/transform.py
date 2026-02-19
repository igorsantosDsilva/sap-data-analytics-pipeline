import pandas as pd
from datetime import datetime


META_INICIAL = 40
INCREMENTO_META = 40

def gerar_tb_snapshot(df_raw):
    hora = datetime.now().hour
    if hora >= 9 and hora <=17:
        return {
            "HORA":f"{hora}:30",
            "SUCESSO": df_raw['Total OM Finalizada '].sum(),
            "INSUCESSO": df_raw['Total OM Insucesso  '].sum(),
            "INICIADAS": df_raw['OMs Iniciadas       '].sum()
        }
        

def atualizar_snapshot(snapshot, caminho_espelho):
    try:
        df = pd.read_excel(caminho_espelho)
    except FileNotFoundError:
        df = pd.DataFrame(
            columns=["HORA", "SUCESSO", "INSUCESSO", "INICIADAS", "META", "DIFERENÇA"]
        )

    df = pd.concat([df, pd.DataFrame([snapshot])], ignore_index=False)

    df["META"] = [
        META_INICIAL + i * INCREMENTO_META
        for i in range(len(df))
    ]

    df["DIFERENÇA"] = df["META"] - df["SUCESSO"]

    df.to_excel(caminho_espelho, index=False)

    return df