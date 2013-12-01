#!/usr/bin/python2
#carojasq@correo.udistrital.edu.co
#GICOGE Research Group
#Udistrital
import sys

def loaddata(file_name):
	archivo=open(file_name,"r")
	arreglos=[[],[]]
	for line in archivo:
		linea=line.replace("\n","").split("\t")
		arreglos[0].append(linea[0])#+ " " + linea[1])
		arreglos[1].append(int(linea[1]))
	suma=sum(arreglos[1])
	for i in range(len(arreglos[1])):
		porcentaje=(arreglos[1][i]+0.0)/suma
		arreglos[0][i]=arreglos[0][i]+" " + "{0:.2f}".format(porcentaje*100)
		arreglos[1][i]=(arreglos[1][i]+0.0)/suma
	return arreglos


def pie_pygal(data,output):
	import pygal
	pie_chart = pygal.Pie()
	pie_chart.title = 'GO Distribution'
	#print data
	for el in range(len(data[0])):
		pie_chart.add(data[0][el], data[1][el])
	pie_chart.render_to_png(output, dpi=72)


def pie_matplot(data,output):
	import matplotlib 
	matplotlib.use('Agg')
	import matplotlib.pyplot as plt
	labels=data[0]
	fracs=[]
	suma=0
	for el in data[1]:
		suma+=el
	for el in data[1]:
		fracs.append(el/suma)
	import matplotlib 
	plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True, labeldistance=0.3)
	plt.savefig(output)

def pie_google(data, output):
	from pygooglechart import PieChart3D
	chart = PieChart3D(750, 400)
	chart.add_data(data[1])
	chart.set_pie_labels(data[0])
	print chart.get_url()
	chart.download(output)


def pie_pycha(data, output):
	import cairo
	import pycha.pie
	#Custom pycha dataset
	dataset=[]
	for n in range(len(data[1])):
		dataset.append((data[0][n], [[0, data[1][n]]]))
	print dataset
	options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=d[0]) for i, d in enumerate(dataset)],
                'rotate':90 ,
                'showLines':True,
            }
        },
        'legend': {
            'hide': True,
        },
        'title': 'Pie Chart',
    }
	surface =cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 800)
	chart = pycha.pie.PieChart(surface, options)
	chart.addDataset(dataset)
	chart.render()
	surface.write_to_png(output)

def usage():
	print """ This script generates a Pie diagram from a tabbed file
	GraphPie.py File.tab Output.png GraphTitle """
	exit()

def main():
	if len(sys.argv)!=3:
		usage()
	in_data=sys.argv[1]
	outimg=sys.argv[2]
	pie_pygal(loaddata(in_data),outimg)
	print "The chart has been generated on %s" % outimg



main()
