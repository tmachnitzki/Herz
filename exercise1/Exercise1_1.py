import matplotlib
matplotlib.use('agg')
from socket import gethostname
from netCDF4 import Dataset
import glob
from mpl_toolkits.basemap import Basemap, cm
from datetime import datetime as dt
import numpy as np
import matplotlib.pyplot as  plt
from functions import print_nc_info
from Task1 import exercise1
from Task2 import exercise2
from Task3 import exercise3
from Task4 import exercise4
from Task5 import exercise5
from Task6 import exercise6
from Task7 import exercise7
from Task8 import exercise8
from Task9 import exercise9
from Task10 import exercise10
from Task11 import exercise11




if __name__ == "__main__":

    print(gethostname())

    path = "/work/mh1049/u300844/ICON/icon-nwp/experiments/nh_ape_nwp_ss17/"
    files = glob.glob(path + "nh_ape_nwp*ML*.nc")
    level_files = glob.glob(path + "nh_ape_nwp*PL*.nc")
    print(files)

    nc = Dataset(files[1])
    data_lons = nc.variables["lon"][:].copy()
    data_lats = nc.variables["lat"][:].copy()
    # data_time = nc.variables["time"][:].copy().astype(str)
    print_nc_info(nc)
    # exercise1(nc,data_lats)
    # data = nc.variables["tot_prec"][0,:,:].copy()
    nc.close()

    exercise2(files,data_lats)
    exercise3(files,data_lats)
    exercise4(files)
    exercise5(files,data_lats)
    # exercise6(files,data_lons,data_lats) #not usefull
    exercise7(files,level_files,data_lons,data_lats)
    exercise8(level_files)
    exercise9(level_files)
    exercise10(level_files)
    exercise11(files)
