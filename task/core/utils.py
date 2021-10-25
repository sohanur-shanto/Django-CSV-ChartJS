import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, area, colors):
    plt.figure(figsize=(10,5))
    plt.title('scatter plot')
    print(x)
    plt.xticks(rotation = 45)
    plt.xlabel('open')
    plt.ylabel('high')
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    graph = get_graph()
    return graph


def get_boxplot(data):
    plt.figure(figsize=(10,5))
    plt.title('box plot')
    print(data)
    plt.xlabel('open')
    plt.ylabel('high')
    plt.boxplot(data)
    graph = get_graph()
    return graph