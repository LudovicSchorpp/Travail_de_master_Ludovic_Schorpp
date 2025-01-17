import os
import multiprocessing as mp
import numpy as np
import pandas as pd
import pyemu
def main():

    try:
       os.remove('.\heads_q.csv')
    except Exception as e:
       print('error removing tmp file:.\heads_q.csv')
    try:
       os.remove('.\heads_pc.csv')
    except Exception as e:
       print('error removing tmp file:.\heads_pc.csv')
    try:
       os.remove('.\heads_map_q.csv')
    except Exception as e:
       print('error removing tmp file:.\heads_map_q.csv')
    try:
       os.remove('.\heads_map_p.csv')
    except Exception as e:
       print('error removing tmp file:.\heads_map_p.csv')
    pyemu.helpers.apply_list_and_array_pars(arr_par_file='mult2model_info.csv')
    pyemu.os_utils.run(r'..\..\..\exe\mf6')


if __name__ == '__main__':
    mp.freeze_support()
    main()

