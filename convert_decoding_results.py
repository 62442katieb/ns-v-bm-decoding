from __future__ import division
import numpy as np
import pandas as pd
from scipy.stats import t as t_to_p
from statsmodels.sandbox.stats.multicomp import multipletests


def r_to_p(r):
    """
    From vassarstats.net/textbook/ch4apx.html
    and
    https://stackoverflow.com/questions/23879049/finding-two-tailed-p-value-from-t-distribution-and-degrees-of-freedom-in-python
    """
    n = 228453.
    df = n - 2.
    t = r / (np.sqrt(1 - r**2) / df)
    t /= 3000
    p = t_to_p.sf(np.abs(t), df) * 2
    return p

df = pd.read_csv('/Users/Katie/Dropbox/Data/scripts/decoded_accumbens2.csv', sep=',')
df['r'] = df['accumbens_pFgA_z.nii.gz'].astype('float64')
df['p'] = df['r'].apply(r_to_p)

u = 0.05
p_array = df['p'].values

# FDR
sig_fi, p_corr, _, _ = multipletests(p_array, alpha=u, method='bonferroni',
                                     returnsorted=False)
df['p_corr'] = p_corr
#p_corr = p_array * len(p_array)
#df['p_corr'] = p_corr
df.to_csv('/Users/Katie/Dropbox/Data/scripts/decoded_accumbens_pval.csv', index=False)
