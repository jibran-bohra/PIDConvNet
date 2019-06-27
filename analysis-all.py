import numpy as np
import matplotlib.pyplot as plt
from TOOLS import DATA, MODELS, LOG, METRICS
import random, matplotlib, datetime, os

run_no = '000265378/'
dataname = 'all/'
directory = 'data/output/' + run_no + dataname
raw_data = np.load(directory + '0_tracks.npy')
raw_info = np.load(directory + '0_info_set.npy')
print("Loaded: %s" % directory)

dataset, infoset = DATA.process_1(raw_data, raw_info)
X, y = DATA.shuffle_(dataset/1024, infoset[:,0])
print("Electron occurence: %.2f" % (100*sum(y)/len(y)))

conv_size1 = 8
conv_size2 = 16
dense_size1 = 256
dense_size2 = 64

stamp = datetime.datetime.now().strftime("%d-%m-%H%M%S")
mname = "conv-%d-%d-filters-dense-%d-%d-nodes-"%(conv_size1,
    conv_size2, dense_size1, dense_size2)
tensorboard, csvlogger = LOG.logger_(run_no, 'test/', mname, stamp)

net1 = MODELS.new
net1.compile(optimizer='adam', loss='binary_crossentropy', metrics=[METRICS.pion_con, METRICS.prec, METRICS.F1])
net1.fit(x=X, y=y, batch_size = 100, epochs=10, validation_split=0.4, callbacks=[tensorboard, csvlogger])
net1.summary()
