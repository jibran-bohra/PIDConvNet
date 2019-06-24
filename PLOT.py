import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import DATA, random, matplotlib
matplotlib.rcParams.update({'font.size': 18})
matplotlib.rcParams['text.usetex'] = True

def surface_(classes, cnames=['$e^-$', '$\\pi$'], colour = ['g','r']):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    for i,c in enumerate(classes):
        c_track = np.sum(c, axis=0)/len(c)
        X, Y = np.meshgrid(range(24),range(17))
        Z = c_track
        p = ax.plot_surface(X, Y, Z, alpha=0.6)
        p = ax.plot_wireframe(X, Y, Z, label=cnames[i],color = colour[i], alpha = 0.6)
    plt.legend()
    plt.title('Mean tracklet per class')
    #plt.ylabel('Time bin no.')
    #plt.xlabel('Pad no.')
    plt.xticks(np.arange(0, 24, 4))
    plt.yticks(np.arange(0, 17, 3))
    plt.show()

def timespec_(tensor, labels):
    elec = tensor[labels.astype(bool)]
    pion = tensor[(1-labels).astype(bool)]
    classes = [elec,pion]
    cnames = ['$e^-$', '$\\pi$']
    colour = ['g','r']
    fig = plt.figure(figsize=(8,6))
    for i,c in enumerate(classes):
        c_tspec = np.sum(c, axis=(0,1))/c.shape[0]
        plt.plot(range(24), c_tspec ,label=cnames[i])
    plt.legend()
    plt.title('Normalized time spectra')
    plt.ylabel('Time bin no.')
    plt.xlabel('Pad no.')
    plt.grid()
    plt.xticks(np.arange(0, 24, 2))
    plt.show()

def hist_(tensor, labels):
    elec = tensor[labels.astype(bool)]
    pion = tensor[(1-labels).astype(bool)]
    classes = [elec,pion]
    cnames = ['$e^-$', '$\\pi$']
    colour = ['g','r']
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    classes = [elec,pion]
    for i, cl in enumerate(classes):
        flat_cl = cl.flatten()
        nonzero = flat_cl[flat_cl>0]
        counts, bins, patches = axes[i].hist(flat_cl, edgecolor='black')
        axes[i].set_yscale('log')
        axes[i].set_xticks(bins)
        #axes[i].grid()
        axes[i].set_title("ADC histogram with zeros")

def iter_(data, nplots = 6):
    i = random.randint(1,data.shape[0])
    print("Initial tracklet %i:"%i)
    leny = data.shape[1]
    lenx = data.shape[2]
    X, Y = np.meshgrid(range(lenx),range(leny))
    for j in range(nplots):
        Z = data[i+j]
        fig, ax = plt.subplots(figsize=(8,6))
        p = ax.pcolor(X, Y, Z)
        cb = fig.colorbar(p, ax=ax)
        plt.show()
