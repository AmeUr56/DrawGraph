import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


file = f'static/graph.png'

def plot_(x,y,theme,color,title,xlabel,ylabel,marker,linestyle,width):
    plt.switch_backend('Agg')
    plt.style.use(theme)
    plt.plot(x,y,color = color,marker = marker,linestyle = linestyle,linewidth = width)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(file)
    plt.close()


def pie_(data,labels,percentages,colors,title,theme = 'default'):
  plt.switch_backend('Agg')
  plt.style.use(theme)
  if percentages:
    plt.pie(data,labels = labels,colors = colors,autopct ='%1.1f%%')
  else:
    plt.pie(data,labels = labels,colors = colors)
  plt.title(title)
  plt.axis('equal')
  plt.savefig(file)
  plt.close()


def scatter_(x,y,size,alpha,colormap,colorbar,theme,title,xlabel,ylabel):
  plt.switch_backend('Agg')
  plt.style.use(theme)
  plt.scatter(x,y,s = size,alpha = alpha,cmap = colormap,c= y)
  if colorbar:
    plt.colorbar()
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.savefig(file)
  plt.close()

def scatter3d_(x,y,z,size,alpha,colormap,colorbar,theme,title,xlabel,ylabel,zlabel,view):
  plt.switch_backend('Agg')
  plt.style.use(theme)
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  scatter = ax.scatter(x, y, z,s = size,alpha = alpha,cmap = colormap,c = z)
  if colorbar:
    cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
  plt.title(title)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_zlabel(zlabel)
  ax.view_init(view[0],view[1])
  plt.savefig(file)
  plt.close()

def bar_(y,theme,colors,alpha,title,xlabel,ylabel,labels,rotation):
  plt.switch_backend('Agg')
  plt.style.use(theme)
  plt.bar(labels,y,color = colors,alpha = alpha)
  plt.xticks(rotation=rotation)
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.savefig(file)
  plt.close()

def surface3d_(x,y,z,colormap,colorbar,theme,title,xlabel,ylabel,zlabel,view):
  plt.switch_backend('Agg')
  plt.style.use(theme)
  x,y = np.meshgrid(x, y)
  z = np.array(z)
  z_2d = np.expand_dims(z, axis=0)
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  surface = ax.plot_surface(x,y,z_2d,cmap = colormap)
  if colorbar:
    cbar = fig.colorbar(surface, ax=ax, pad=0.1)
  plt.title(title)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_zlabel(zlabel)
  ax.view_init(view[0],view[1])
  plt.savefig(file)
  plt.close()

def trisurf_(x,y,z,colormap,colorbar,theme,title,xlabel,ylabel,zlabel,view):
  plt.switch_backend('Agg')
  plt.style.use(theme)
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  surface = ax.plot_trisurf(x,y,z,cmap = colormap)
  if colorbar:
    cbar = fig.colorbar(surface, ax=ax, pad=0.1)
  plt.title(title)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_zlabel(zlabel)
  ax.view_init(view[0],view[1])
  plt.savefig(file)
  plt.close()
  
def plot3d_(x, y, z, theme, color, title, xlabel, ylabel, zlabel, width, view):
    plt.switch_backend('Agg')
    plt.style.use(theme)
    fig = plt.figure()
    ax = plt.axes(projection='3d') 
    ax.plot(x, y, z, c=color, linewidth=width)
    plt.title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.view_init(view[0], view[1])
    plt.savefig(file)
    plt.close()
    
def contour_(x, y, z, theme, colormap,colorbar, title, xlabel, ylabel, zlabel, view):
    plt.switch_backend('Agg')
    plt.style.use(theme)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x,y = np.meshgrid(x, y)
    z = np.outer(z, np.ones_like(z))
    contour = ax.contour3D(x, y, z, cmap = colormap)
    if colorbar:
      cbar = fig.colorbar(contour, ax=ax, pad=0.1)
    plt.title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.view_init(view[0], view[1])
    plt.savefig(file)
    plt.close()

def wireframe_(x, y, z, theme, color, title, xlabel, ylabel, zlabel, view):
    x,y,z = np.array(x),np.array(y),np.array(z)
    plt.switch_backend('Agg')
    plt.style.use(theme)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x,y = np.meshgrid(x, y)
    z_2d = np.expand_dims(z, axis=0)
    wireframe = ax.plot_wireframe(x, y, z_2d,color = color)
    plt.title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.view_init(view[0], view[1])
    plt.savefig(file)
    plt.close()