#!/usr/bin/env python

import codecs

crypt = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
rot13 = lambda s : codecs.getencoder("rot-13")(s)[0]

# Answer
print(rot13(crypt))