from flask import Flask,render_template,request,redirect,url_for,send_file
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
mat_colors = list(mcolors.CSS4_COLORS.keys())
colormaps = plt.colormaps()
styles = plt.style.available

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/download_image')
def download_image():
    image_path = f'static/graph.png'
    return send_file(image_path, as_attachment=True)

@app.route('/result')
def result():
    return render_template('result.html',path = path)

@app.route('/marker',methods = ['GET'])
def marker():
    if request.method == 'GET':
        return render_template('marker.html')

@app.route('/colormap',methods = ['GET'])
def colormap():
    if request.method == 'GET':
        return render_template('colormap.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/plot', methods=['GET', 'POST'], endpoint='plot')
def plot():
    from graph_ import plot_
    global path
    path = 'plot'

    if request.method == 'GET':
        return render_template('plot.html',styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        marker = request.form.get('marker')
        color = request.form.get('color')
        linestyle = request.form.get('linestyle')
        width = request.form.get('linewidth')

        try:
            x = [float(value) for value in x]
            y =  [float(value) for value in y]
        except:
            return render_template('error.html',message = 'Non valid Values.',path = path)


        if len(y) != len(x):
            return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)

        if not color:
            color = 'red'
        try:
            if not(color.lower() in mat_colors):
                    return render_template('error.html',message = 'Invalid Colors.',path = path)
        except:
            return render_template('error.html',message = 'Invalid Color.')

        if width:
            try:
                width = float(width)
                if width < 0:
                    return render_template('error.html',message = 'Width must be positive.',path = path)
            except:
                return render_template('error.html',message = 'Non valid Width.',path = path)

        if not theme:
            theme = 'default'
        if not title:
            title = ''
        if not xlabel:
            xlabel = ''
        if not ylabel:
            ylabel = ''
        if not marker:
            marker = ''
        if not linestyle:
            linestyle  = 'solid'
        if not width:
            width = 1


        plot_(x,y,theme,color,title,xlabel,ylabel,marker,linestyle,width)
        return redirect(url_for('result'))



@app.route('/pie',methods = ['GET','POST'],endpoint = 'pie')
def pie():
    from graph_ import pie_
    global path
    path = 'pie'

    if request.method == 'GET':
        return render_template('pie.html',styles = styles)
    else:
        data = request.form.get('data').split(',')
        theme = request.form.get('theme')
        labels = request.form.get('labels').split(',')
        percentages = request.form.get('percentages')
        colors = request.form.get('colors').split(',')
        title = request.form.get('title')

        try:
            data = [float(value) for value in data]
        except:
            return render_template('error.html',message = 'Non valid Values.',path = path)

        if labels != ['']:
            if len(data) != len(labels):
                    return render_template('error.html',message = 'Data and Labels must have same lenght.',path = path)
        else:
            labels = ['' for i in range(len(data))]


        if len(data) != len(colors):
            return render_template('error.html',message = 'Data and Colors must have same lenght.',path = path)

        for color in colors:
            if not(color.lower() in mat_colors):
                    return render_template('error.html',message = 'Invalid Colors.',path = path)

        if not theme:
            theme = 'default'
        if not title:
            title = ''

        pie_(data,labels,percentages,colors,title,theme)
        return redirect(url_for('result'))

@app.route('/scatter',methods = ['GET','POST'],endpoint = 'scatter')
def scatter():
    from graph_ import scatter_
    global path
    path = 'scatter'
    if request.method == 'GET':
        return render_template('scatter.html',colormaps = colormaps,styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        alpha = request.form.get('alpha')
        size = request.form.get('size')
        colormap = request.form.get('colormap')
        colorbar = request.form.get('colorbar')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')

    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)

    if len(y) != len(x):
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)

    if alpha:
        try:
            alpha = float(alpha)
        except:
            return render_template('error.html',message = 'Non valid Alpha.',path = path)
        if not(0 < alpha < 1):
            return render_template('error.html',message = 'Alpha must be between 0 and 1.',path = path)

    if size:
        try:
            size = float(size)
            if size < 0:
                return render_template('error.html',message = 'Size must be positive.',path = path)
            size = [size for i in range(len(x))]
        except:
            return render_template('error.html',message = 'Non valid Size.',path = path)


    if not size:
        size = [10 for i in range(len(x))]
    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not alpha:
        alpha = 1

    scatter_(x,y,size,alpha,colormap,colorbar,theme,title,xlabel,ylabel)
    return redirect(url_for('result'))


@app.route('/scatter3d',methods = ['GET','POST'],endpoint = 'scatter3d')
def scatter3d():
    from graph_ import scatter3d_
    global path
    path = 'scatter3d'
    if request.method == 'GET':
        return render_template('scatter3d.html',colormaps = colormaps,styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        z = request.form.get('z').split(',')
        alpha = request.form.get('alpha')
        size = request.form.get('size')
        colormap = request.form.get('colormap')
        colorbar = request.form.get('colorbar')
        view = request.form.get('view')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        zlabel = request.form.get('zlabel')

    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
        z =  [float(value) for value in z]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)

    if view:
        view = view.split(',')
        if len(view) != 2:
            return render_template('error.html',message = 'Invalid View.',path = path)
        try:
            view = [float(value) for value in view]
        except:
            return render_template('error.html',message = 'Invalid View.',path =path)
    else:
        view = [30,-60]

    if len(y) != len(x) :
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)
    if len(z) != len(x) :
        return render_template('error.html',message = 'X and Z must have same Lenght.',path = path)


    if alpha:
        try:
            alpha = float(alpha)
        except:
            return render_template('error.html',message = 'Non valid Alpha.',path = path)
        if not(0 < alpha < 1):
            return render_template('error.html',message = 'Alpha must be between 0 and 1.',path = path)
    if size:
        try:
            size = float(size)
            if size < 0:
                return render_template('error.html',message = 'Size must be positive.',path = path)
            size = [size for i in range(len(x))]
        except:
            return render_template('error.html',message = 'Non valid Size.',path = path)


    if not size:
        size = [10 for i in range(len(x))]
    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not zlabel:
        zlabel = ''
    if not alpha:
        alpha = 1

    scatter3d_(x,y,z,size,alpha,colormap,colorbar,theme,title,xlabel,ylabel,zlabel,view)
    return redirect(url_for('result'))


@app.route('/bar',methods = ['GET','POST'],endpoint = 'bar')
def bar():
    from graph_ import bar_
    global path
    path = 'bar'
    if request.method == 'GET':
        return render_template('bar.html',styles = styles)
    else:
        y = request.form.get('y').split(',')
        theme = request.form.get('theme')
        labels = request.form.get('labels').split(',')
        colors = request.form.get('colors')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        alpha = request.form.get('alpha')
        rotation = request.form.get('rotation')

        try:
            y =  [float(value) for value in y]
        except:
            return render_template('error.html',message = 'Non valid Values.',path = path)

        if colors:
            colors = colors.split(',')
            if len(colors) > len(y):
                return render_template('error.html',message = 'Colors lenght must be less than or equal to Y.',path = path)
            for color in colors:
                if not(color.lower() in mat_colors):
                    return render_template('error.html',message = 'Invalid Colors.',path = path)

        if len(y) != len(labels):
            return render_template('error.html',message = 'Labels and Y must have same Lenght.',path = path)

        if rotation:
            try:
                rotation = float(rotation)
            except:
                return render_template('error.html',message = 'Non valid Rotation.',path = path)

        if alpha:
            try:
                alpha = float(alpha)
            except:
                return render_template('error.html',message = 'Non valid Alpha.',path = path)
            if not(0 < alpha < 1):
                return render_template('error.html',message = 'Alpha must be between 0 and 1.',path = path)

        if not theme:
            theme = 'default'
        if not title:
            title = ''
        if not xlabel:
            xlabel = ''
        if not ylabel:
            ylabel = ''
        if not alpha:
            alpha = 1
        if not colors:
            colors = 'red'
        if not rotation:
            rotation = 180
        bar_(y,theme,colors,alpha,title,xlabel,ylabel,labels,rotation)
        return redirect(url_for('result'))


@app.route('/surface3d',methods = ['GET','POST'],endpoint = 'surface3d')
def surface3d():
    from graph_ import surface3d_
    global path
    path = 'surface3d'
    if request.method == 'GET':
        return render_template('surface3d.html',colormaps = colormaps,styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        z = request.form.get('z').split(',')
        colormap = request.form.get('colormap')
        colorbar = request.form.get('colorbar')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        zlabel = request.form.get('zlabel')
        view = request.form.get('view')

    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
        z =  [float(value) for value in z]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)
    
    if view:
        view = view.split(',')
        if len(view) != 2:
            return render_template('error.html',message = 'Invalid View.',path = path)
        try:
            view = [float(value) for value in view]
        except:
            return render_template('error.html',message = 'Invalid View.',path =path)
    else:
        view = [30,-60]
    if len(y) != len(x) :
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)
    if len(z) != len(x) :
        return render_template('error.html',message = 'X and Z must have same Lenght.',path = path)

    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not zlabel:
        zlabel = ''

    surface3d_(x,y,z,colormap,colorbar,theme,title,xlabel,ylabel,zlabel,view)
    return redirect(url_for('result'))

@app.route('/trisurf',methods = ['GET','POST'],endpoint = 'trisurf')
def trisurf():
    from graph_ import trisurf_
    global path
    path = 'trisurf'
    if request.method == 'GET':
        return render_template('trisurf.html',colormaps = colormaps,styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        z = request.form.get('z').split(',')
        colormap = request.form.get('colormap')
        colorbar = request.form.get('colorbar')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        zlabel = request.form.get('zlabel')
        view = request.form.get('view')

    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
        z =  [float(value) for value in z]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)

    if view:
        view = view.split(',')
        if len(view) != 2:
            return render_template('error.html',message = 'Invalid View.',path = path)
        try:
            view = [float(value) for value in view]
        except:
            return render_template('error.html',message = 'Invalid View.',path =path)
    else:
        view = [30,-60]

    if len(y) != len(x) :
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)

    if len(z) != len(x) :
        return render_template('error.html',message = 'X and Z must have same Lenght.',path = path)

    if len(y) < 3 and len(x) < 3:
        return render_template('error.html',message = 'X and Y must have a length of at last 3.',path = path)

    if y == x:
        return render_template('error.html',message = 'X and Y must consist of at least 3 unique points.',path = path)


    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not zlabel:
        zlabel = ''

    trisurf_(x,y,z,colormap,colorbar,theme,title,xlabel,ylabel,zlabel,view)
    return redirect(url_for('result'))

@app.route('/plot3d',methods = ['GET','POST'],endpoint = 'plot3d')
def plot3d():
    from graph_ import plot3d_
    global path
    path = 'plot3d'
    if request.method == 'GET':
        return render_template('plot3d.html',styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        z = request.form.get('z').split(',')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        zlabel = request.form.get('zlabel')
        view = request.form.get('view')
        color = request.form.get('color')
        width = request.form.get('linewidth')

    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
        z =  [float(value) for value in z]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)

    if view:
        view = view.split(',')
        if len(view) != 2:
            return render_template('error.html',message = 'Invalid View.',path = path)
        try:
            view = [float(value) for value in view]
        except:
            return render_template('error.html',message = 'Invalid View.',path =path)
    else:
        view = [30,-60]

    if len(y) != len(x) :
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)

    if len(z) != len(x) :
        return render_template('error.html',message = 'X and Z must have same Lenght.',path = path)
    
    if not color:
        color = 'red'
        try:
            if not(color.lower() in mat_colors):
                    return render_template('error.html',message = 'Invalid Colors.',path = path)
        except:
            return render_template('error.html',message = 'Invalid Color.')

    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not zlabel:
        zlabel = ''
    if not width:
        width = 1

    plot3d_(x, y, z, theme, color, title, xlabel, ylabel, zlabel, width, view)
    return redirect(url_for('result'))



@app.route('/contour',methods = ['GET','POST'],endpoint = 'contour')
def contour():
    from graph_ import contour_
    global path
    path = 'contour'
    if request.method == 'GET':
        return render_template('contour.html',colormaps = colormaps,styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        z = request.form.get('z').split(',')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        zlabel = request.form.get('zlabel')
        view = request.form.get('view')
        colormap = request.form.get('colormap')
        colorbar = request.form.get('colorbar')
        
    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
        z =  [float(value) for value in z]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)

    if view:
        view = view.split(',')
        if len(view) != 2:
            return render_template('error.html',message = 'Invalid View.',path = path)
        try:
            view = [float(value) for value in view]
        except:
            return render_template('error.html',message = 'Invalid View.',path =path)
    else:
        view = [30,-60]

    if len(y) != len(x) :
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)

    if len(z) != len(x) :
        return render_template('error.html',message = 'X and Z must have same Lenght.',path = path)
    
    if len(z) < 2:
        return render_template('error.html',message = 'X, Y and Z must have a length of at last 2.',path = path)


    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not zlabel:
        zlabel = ''


    contour_(x, y, z, theme, colormap,colorbar, title, xlabel, ylabel, zlabel, view)
    return redirect(url_for('result'))


@app.route('/wireframe',methods = ['GET','POST'],endpoint = 'wireframe')
def wireframe():
    from graph_ import wireframe_
    global path
    path = 'wireframe'
    if request.method == 'GET':
        return render_template('wireframe.html',styles = styles)
    else:
        x = request.form.get('x').split(',')
        y = request.form.get('y').split(',')
        z = request.form.get('z').split(',')
        theme = request.form.get('theme')
        title = request.form.get('title')
        xlabel = request.form.get('xlabel')
        ylabel = request.form.get('ylabel')
        zlabel = request.form.get('zlabel')
        view = request.form.get('view')
        color = request.form.get('color')
        
    try:
        x = [float(value) for value in x]
        y =  [float(value) for value in y]
        z =  [float(value) for value in z]
    except:
        return render_template('error.html',message = 'Non valid Values.',path = path)

    if view:
        view = view.split(',')
        if len(view) != 2:
            return render_template('error.html',message = 'Invalid View.',path = path)
        try:
            view = [float(value) for value in view]
        except:
            return render_template('error.html',message = 'Invalid View.',path =path)
    else:
        view = [30,-60]

    if len(y) != len(x) :
        return render_template('error.html',message = 'X and Y must have same Lenght.',path = path)

    if len(z) != len(x) :
        return render_template('error.html',message = 'X and Z must have same Lenght.',path = path)

    if not color:
        color = 'red'
        try:
            if not(color.lower() in mat_colors):
                    return render_template('error.html',message = 'Invalid Colors.',path = path)
        except:
            return render_template('error.html',message = 'Invalid Color.')

    if not theme:
        theme = 'default'
    if not title:
        title = ''
    if not xlabel:
        xlabel = ''
    if not ylabel:
        ylabel = ''
    if not zlabel:
        zlabel = ''


    wireframe_(x, y, z, theme, color, title, xlabel, ylabel, zlabel, view)
    return redirect(url_for('result'))


