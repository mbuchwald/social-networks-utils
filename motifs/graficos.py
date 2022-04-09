import matplotlib.pyplot as plt
import numpy as np


def graficar_significant_profile(sp, extra_text=None):
    """
    Hace un gráfico del significant profile calculado
    :param sp:
    """
    plt.bar(range(1, len(sp) + 1), sp)
    plt.xticks(range(1, len(sp) + 1))
    plt.hlines(0, 1, len(sp), linestyles="dashed", colors="lightblue")
    plt.ylabel("Significance Profile")
    plt.title("Significant profile per motif" + ((" - " + extra_text) if extra_text is not None else ""))
    plt.show()


def graficar_significant_profiles_conjuntos(sps, labels, extra_text):
    cant_motifs = len(sps[0])
    x = np.arange(1, cant_motifs + 1)

    width = 0.8 / len(sps)
    fig, ax = plt.subplots()

    prop = 0
    mul = 1
    impariedad = 1 - len(sps) % 2
    for i in range(len(sps)):
        ax.bar(x + prop * mul * width + impariedad * width / 2 , sps[i], width, label=labels[i])
        mul *= (-1)
        if (i % 2) == 0:
            prop += 1

    ax.legend()
    ax.set_xticks(x)
    ax.set_ylabel("Significance Profile")
    ax.set_title("Significant profile per motif" + (" - {}".format(extra_text) if extra_text is not None else ""))
    ax.hlines(0, 1, cant_motifs, linestyles="dashed", colors="lightblue")
    plt.show()
