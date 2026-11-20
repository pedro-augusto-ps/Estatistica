import math
from scipy import stats


def media_padrao_Z(amostra, h0, alfa, media_amostral, desvio_populacional, bilateral = True):
    """Utiliza-se a distribuição Z quando o desvio populacional é conhecido."""
    if bilateral == True:
        z_critico = stats.norm.ppf(1 - alfa / 2)
    else:
        z_critico = stats.norm.ppf(1 - alfa)
    calculo = (media_amostral - h0) / (desvio_populacional/ math.sqrt(amostra))
    print(z_critico)
    print(calculo)

media_padrao_Z(25, 200, 0.05, 195, 10)

def media_padrao_T(amostra, h0, alfa, media_amostral, desvio_amostral, bilateral = True):
    """Utiliza-se a distribuição T quando o desvio populacional não é conhecido."""

    gl = amostra - 1

    t_critico = stats.t.ppf(alfa, df=gl)
    calculo = (media_amostral - h0) / (desvio_amostral / math.sqrt(amostra))
    print(t_critico)
    print(calculo)

media_padrao_T(16, 50, 0.05, 53, 6)