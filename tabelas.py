# -*- coding: utf-8 -*-
"""tabelas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rrDrYidoTl8DuWe1Vw03N-rtcl_PGROx
"""

import scipy as sc
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon
import pandas as pd

sem_Alura = pd.Series([ 7,  8, 6, 6, 10, 4, 2, 5,  9, 2, 4, 9, 1, 10])
com_Alura = pd.Series([10, 10, 9, 9,  9, 7, 5, 8, 10, 6, 3, 7, 4,  8])

T, pvalue = wilcoxon(sem_Alura, com_Alura)
print(T)
print(pvalue)

from scipy.stats import wilcoxon

sem_Alura = pd.Series([ 7,  8, 6, 6, 10, 4, 2, 5,  9, 2, 4, 9, 1, 10])
com_Alura = pd.Series([10, 10, 9, 9,  9, 7, 5, 8, 10, 6, 3, 7, 4,  8])

significancia = 0.10

T, p_valor = wilcoxon(sem_Alura, com_Alura)
print('T =', T)

if(p_valor <= significancia):
    print('Rejeitar H0')
else:
    print('Aceitar H0')

from scipy.stats import mannwhitneyu

sem_exercicios = [7, 6, 7, 8, 6, 8, 6, 9, 5]
com_exercicios = [8, 7, 6, 6, 8, 6, 10, 6, 7, 8]

mannwhitneyu(sem_exercicios, com_exercicios, alternative='greater')

mannwhitneyu(sem_exercicios, com_exercicios, alternative='greater')

from scipy.stats import mannwhitneyu

sem_Exercicios = pd.Series([7, 6, 7, 8, 6, 8, 6, 9, 5])
com_Exercicios = pd.Series([8, 7, 6, 6, 8, 6, 10, 6, 7, 8])

significancia = 0.10

u, p_valor = mannwhitneyu(com_Exercicios, sem_Exercicios, alternative='greater')

print('u =', u)

if(p_valor <= significancia):
    print('Rejeitar H0')
else:
    print('Aceitar H0')

sem_Exercicios = pd.Series([7, 6, 7, 8, 6, 8, 6, 9, 5])
com_Exercicios = pd.Series([8, 7, 6, 6, 8, 6, 10, 6, 7, 8])

mannwhitneyu(com_Exercicios, sem_Exercicios, alternative='greater')