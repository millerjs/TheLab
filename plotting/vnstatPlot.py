import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize


resolution=5


def vntoi(x, label):
    if "k" in label:
        return float(x)/1e6
    if "M" in label:
        return float(x)/1e3
    if "G" in label:
        return float(x)

def find_bit(row):
    bits = []
    for x in range(len(row)):
        if "bit" in row[x]:
            bits.append(x)
    return bits



# Create plot
plt = matplotlib.pyplot.figure()
ax = axes()

def plotter(path):
    print "Adding %s to plot" % path
    rxs = []
    txs = []
    with open(path, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            bits = find_bit(row)
            RX_LOC = bits[0]
            TX_LOC = bits[1]
            rx_string = row[RX_LOC-1]
            rx_label = row[RX_LOC]
            tx_string =  row[TX_LOC-1]
            tx_label =  row[TX_LOC]
            rx = vntoi(rx_string, rx_label)
            tx = vntoi(tx_string, tx_label)
            rxs.append(rx)
            txs.append(tx)

    rxs_ = []
    txs_ = []
    for i in range(0,len(rxs)-resolution, resolution):
        rxs_.append(mean(rxs[i:i+resolution]))
        txs_.append(mean(txs[i:i+resolution]))

    rxs=rxs_
    txs=txs_

    x = array(range(len(rxs)))*resolution
            
    bbox_props = dict(boxstyle="round4,pad=0.8", fc="cyan", ec="k", lw=2)
    
    xaxis = "Time (s) [%d s resolution]" % resolution
    yaxis = "Speed (Gbps)"
    
    ax.set_xlabel(xaxis)
    ax.set_ylabel(yaxis)
    
    rx_label = path[:-4]
    tx_label = path[:-4]
    
    if max(rxs) > .1:
        plot(x, rxs, alpha=.7, linewidth=3, label=rx_label)
    if max(txs) > .1:
        plot(x, txs, alpha=.7, linewidth=3, label=tx_label)


# Label PLot
for i in range(1,len(sys.argv)-1):
    arg = sys.argv[i]
    plotter(arg)


# Title Plot
insert = sys.argv[-1]
title = insert
ax.set_title(title)

# plt.tight_layout(pad=10)

# handles, labels = ax.get_legend_handles_labels()
# lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-.2))
# ax.grid('on')


# Create Legend
ax.legend( bbox_to_anchor=(1, 1),
          ncol=1, fancybox=True, shadow=True)
# , borderaxespad=1.)


ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# Save  plot
title = insert
plt.set_facecolor('white')
title = title.replace(".dat", "")
title = title.replace(" ", "_")
plt.savefig(title+".png")
print "Saved to %s.png" %title
# savefig(title+".png", box_extra_artists=(lgd,), bbox_inches='tight')
show()

 




        
        
