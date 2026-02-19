import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from config.settings import PATH_IMG, PATH_IMG_SAVE, PATH_DATASET_RELATORIO_HORARIO

def gerador_img():
    df_final = pd.read_excel(PATH_DATASET_RELATORIO_HORARIO)
    fig = plt.figure(figsize=(10, 5))
    gs = GridSpec(2, 1, height_ratios=[0.8, 2.2])

    ax_top = fig.add_subplot(gs[0])
    ax_top.axis('off')

    img = plt.imread(PATH_IMG)
    ax_top.imshow(img)
    ax_top.set_xlim(0, img.shape[1])
    ax_top.set_ylim(img.shape[0], 0)

    ax_top.text(
        img.shape[1] / 2,
        img.shape[0] + 10,
        "Acompanhamento por hora",
        ha='center',
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

    ax = fig.add_subplot(gs[1])
    ax.axis('off')

    tabela = ax.table(
        cellText=df_final.values,
        colLabels=df_final.columns,
        loc='upper center',
        cellLoc='center'
    )

    tabela.auto_set_font_size(False)
    tabela.set_fontsize(10)
    tabela.auto_set_column_width(col=list(range(len(df_final.columns))))

    for (row, col), cell in tabela.get_celld().items():
        
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#1976D2')
            cell.set_height(0.08)
        else:
            cell.set_facecolor('#f5f5f5' if row % 2 == 0 else '#ffffff')

            if df_final.columns[col] == "DIFERENÇA":
                valor = df_final.iloc[row-1, col]

                if valor < 0:
                    cell.set_facecolor('#ffcdd2')
                    cell.set_text_props(color='red', weight='bold')
                else:
                    cell.set_facecolor('#c8e6c9')
                    cell.set_text_props(color='green', weight='bold')

    plt.subplots_adjust(top=0.9, bottom=0.05)

    plt.savefig(PATH_IMG_SAVE, bbox_inches='tight', dpi=300)
    plt.close()