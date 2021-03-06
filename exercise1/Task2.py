import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

def exercise2(file_list,data_lats):
    # loading data from all files:
    cl_array = np.zeros([len(file_list),len(data_lats)]).astype(float)
    months = []
    for i,file in enumerate(sorted(file_list)):
        nc = Dataset(file)
        cl_array[i,:] = np.mean(nc.variables["clct"][0,:,:].copy(),axis=1)
        m = str(nc.variables["time"][0].copy())
        m = int(m[:6])
        # print(m)
        months.append(m)

    # averaging over months:
    m_last = months[0]
    same = []
    cl_monthly = np.zeros([2,len(data_lats)]).astype(float)
    counter = 0
    for i,m in enumerate(months):
        if m == m_last:
            same.append(cl_array[i,:])
        else:
            same = np.asarray(same)
            cl_monthly[counter,:] = np.mean(same,axis=0)
            counter += 1
            same = []

        m_last = m


    # plotting results:
    months = np.asarray(months)


    print(data_lats.shape)
    fig2,ax = plt.subplots()
    ax.plot(data_lats,cl_monthly[0],label="January")
    ax.plot(data_lats,cl_monthly[1],label="February")
    # im = ax.pcolor(data_lats,np.arange(0,3),cl_monthly)
    # plt.yticks(ticks,labels)
    # plt.colorbar(im, label="Cloud Fraction [%]")
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Cloud Fraction [%]")
    ax.set_title("Monthly zonal mean cloud Fraction")
    ax.set_xlim(-90,90)
    ax.set_ylim(0,100)
    plt.legend(loc="best")
    plt.show()
    plt.savefig("Images/Task2.pdf")
    plt.close()