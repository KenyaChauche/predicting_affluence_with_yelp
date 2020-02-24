import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

class CRA:
    def __init__(self):
        self.url = 'https://gisdata.seattle.gov/server/rest/services/COS/CommunityReportingAreas/MapServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
        self.json = requests.get(self.url).json()
        self.geometry = {f['attributes']['GEN_ALIAS'] : f['geometry']['rings'] for f in self.json['features']}
        self.xlim = [1000, -1000]
        self.ylim = [1000, -1000]
        for key in self.geometry:
            for ring in self.geometry[key]:
                    for vertex in ring:
                        self.xlim[0] = min(self.xlim[0], vertex[0])
                        self.xlim[1] = max(self.xlim[1], vertex[0])
                        self.ylim[0] = min(self.ylim[0], vertex[1])
                        self.ylim[1] = max(self.ylim[1], vertex[1])

    def in_poly(p, V):
        return sum(min(V[i][1], V[i+1][1]) <= p[1] < max(V[i][1], V[i+1][1])
                   and (V[i+1][0] - V[i][0]) * (p[1] - V[i][1]) / (V[i+1][1] - V[i][1]) < p[0] - V[i][0] for i in range(len(V) - 1)) % 2
    
    def in_cra(coordinate, cra):
        return in_poly(coordinate, self.geometry[cra])
    
    def to_cra(self, coordinate):
        for cra in self.geometry:
            for ring in self.geometry[cra]:
                if CRA.in_poly(coordinate, ring):
                    return cra
        return 'Not Found'
    
    def poly_plot(V):
        for i in range(len(V) - 1):
            plt.plot([V[i][0], V[i+1][0]], [V[i][1], V[i+1][1]], 'k')
    
    def print_cra(self, cra):
        for ring in self.geometry[cra]:
            CRA.poly_plot(ring)
        plt.title(cra)
        plt.xlabel('Latitude')
        plt.ylabel('Longitude')
        plt.ticklabel_format(useOffset=False)
        plt.show()
        
    def make_city(self, margin = 0.001, figsize = [10, 20]):
        plt.figure(figsize = figsize)
        plt.xlim(self.xlim[0] - margin, self.xlim[1] + margin)
        plt.ylim(self.ylim[0] - margin, self.ylim[1] + margin)
        plt.axis('off')
        for i, key in enumerate(self.geometry.keys()):
            for j, ring in enumerate(self.geometry[key]):
                CRA.poly_plot(ring)
        plt.savefig('sea.png', bbox_inches = 'tight', pad_inches = 0)
        return self
    
    def print_city(self, margin = 0.001):
        im = plt.imread('sea.png')
        xlim = [self.xlim[0] - margin, self.xlim[1] + margin]
        ylim = [self.ylim[0] - margin, self.ylim[1] + margin]
        plt.xlim(*xlim)
        plt.ylim(*ylim)
        plt.axis('off')
        plt.imshow(im, extent = (*xlim, *ylim), aspect = 'auto')