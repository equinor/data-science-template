from flask import Flask, render_template
from IPython.core.display import HTML
from os.path import isfile, join
from os import listdir

app = Flask(__name__, static_url_path='/static')
app.debug = False
graph_dict = dict()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('layouts/index.html',
                           graph0=graph_dict['0'],
                           graph1=graph_dict['1'],
                           graph2=graph_dict['2'])


if __name__ == '__main__':
    graph_path = 'Graph\\'
    graph_files = [f for f in listdir(graph_path) if isfile(join(graph_path, f))]
    for graph_file in graph_files:
        file = open(graph_path + graph_file, 'r')
        graph_dict[graph_file.split('.')[0]] = HTML(file.read())
        print(graph_dict[graph_file.split('.')[0]])

    app.run(host='127.0.0.1', port=8889)