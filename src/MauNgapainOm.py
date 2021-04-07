import math
import networkx as nx
import matplotlib.pyplot as plt

print("                          __                        _           ___")           
print("  /\/\   __ _ _   _    /\ \ \__ _  __ _ _ __   __ _(_)_ __     /___\_ __ ___")  
print(" /    \ / _` | | | |  /  \/ / _` |/ _` | '_ \ / _` | | '_ \   //  // '_ ` _ \\")
print("/ /\/\ \ (_| | |_| | / /\  / (_| | (_| | |_) | (_| | | | | | / \_//| | | | | |")
print("\/    \/\__,_|\__,_| \_\ \/ \__, |\__,_| .__/ \__,_|_|_| |_| \___/ |_| |_| |_|")
print("                            |___/      |_|")                                    

#open dan read file nya
path = "C:/Users/Windows/Desktop/Tucil3_13519103/test/{}.txt"
print("test1 : Peta jalan di dalam ITB")
print("test2 : Peta jalan sekitar alun-alun Bandung")
print("test3 : Peta jalan sekitar Buahbatu")
print("test4 : Peta jalan sekitar Dago")
print("test5 : Peta kota-kota di Romania")
print("test6 : Peta tempat-tempat terkenal yang tidak saling berhubungan")
fileName = input("Masukkan file yang ingin diuji (test1-test6): ")
f = open(path.format(fileName), "r")
n = int(f.readline())   #banyak nya node tempat
print()

places = []     #initialize temporary array of places 
adjMat = []     #initialize array for adj matrix   
x = 0 
for line in f:  #masukin adj matrix
    if (x >= n):
        adjMat.append([x.strip("\n") for x in line.split(" ")])
        x+=1
    else: 
        places.append(line.strip("\n"))
        x+=1
# print(places)
# print(adjMat)

#masukin nama, posisi X, dan posisi Y 
nama = []       #nama tempat (node)
posisiX = []    #koordinat X
posisiY = []    #koordinat Y 
for i in places:
    splits = i.split()
    nama.append(splits[0])
    posisiX.append(splits[1])
    posisiY.append(splits[2])
# print(nama)

#MEMBUAT RUMUS EUCLIDEAN (KELUARAN HASIL FLOAT)
def Euclidean(tempatA,tempatB):
    indexA = nama.index(tempatA)
    indexB = nama.index(tempatB)
    xa = float(posisiX[indexA])
    ya = float(posisiY[indexA])
    xb = float(posisiX[indexB])
    yb = float(posisiY[indexB])
    dist = math.sqrt((xa-xb)**2 + (ya-yb)**2) * 100000
    hasil = float("{:.2f}".format(dist))
    return hasil

graph = []          #adj Matrix dengan bobot 
graphTemp = []      #graph temporary
graphList =[]       #list graph terhubung 

#MEMBUAT GRAPH DAN GRAPHLIST 
for i in range(len(adjMat)):
    graph.append([])
    for j in range(len(adjMat[i])):
        if(adjMat[i][j] == '1'):
            graph[i].append(Euclidean(nama[i], nama[j]))
            graphTemp.append(nama[i])
            graphTemp.append(nama[j])
        else:
            graph[i].append(0)
sumEdges = 0 
for i in range(len(graphTemp)//2): 
    graphList.append([])
    for j in range(2): 
        graphList[i].append(graphTemp[sumEdges])
        sumEdges+=1
# print(graph)
# print(graphList)
# print(nama)

#BUAT LIST YANG BERISI JARAK GARIS LURUS MENUJU KE TEMPAT YANG DITUJU
def getStraightDistance(): 
    dict = {}
    for key in nama:
        dict[key] = Euclidean(key, ke)
    return dict

#UNTUK MENCARI PATH (KELUARAN LIST INDEX YANG DILALUI)
def searchPath(startPoint, endPoint):
    # euclideanDict =  Euclideantempat(endPoint)
    path = []
    path.append(nama.index(startPoint))
    startPointIndex = nama.index(startPoint)
    while (startPointIndex != nama.index(endPoint)):
        temp = {}
        for i in range(n):
            if graph[startPointIndex][i] != 0:
                # print('tidaknol')
                if graph[startPointIndex][i] != straightDistDict[nama[startPointIndex]]:
                    # print("gak langsung bos")
                    sum = graph[startPointIndex][i] + straightDistDict[nama[i]]
                    temp[i] = sum
                else: 
                    sum = graph[startPointIndex][i]  #BAHAYA KALO MISALNYA ANGKA EUCLIDIAN NYA BISA SAMA PERSIS
                    temp[i] = sum
                    # startPointIndex = nama.index(endPoint)
            # else:
            #     print('nol')
        # print(temp)
        #buat biar ga bolak balik dan ga masuk ke jalan buntu
        for i in path:
            for key in temp.copy():
                #cek kalo udh lewat 
                if key == i:
                    del temp[key]
        #cek kalo ga buntu 
        for key in temp.copy():
            banyakjalur = 0  
            for x in range(n):
                if graph[key][x] != 0:
                    banyakjalur += 1
            # print(banyakjalur)
            if banyakjalur <= 1 and key != nama.index(endPoint):
                del temp[key] 
                # print("kedelete")
        # print(temp)
        if not temp:
            # print("Jaka sembung bawa golok, ga nyambung goblok")
            path.clear()
            return path
        else:
            minDist = min(temp, key=temp.get)
        # print(minDist)
        path.append(minDist)
        startPointIndex = minDist
    # print(path)
    return path 

#UNTUK BUAT LIST PATH YANG DILALUI OLEH SEARCH PATH 
def jalur(path): 
    templist = []
    for i in range(len(path)-1): 
        templist.append([])
        for j in range(2):
            templist[i].append(nama[path[i+j]])
    return templist

#UNTUK MENAMPILKAN GRAF 
def drawFinalGraph(graph):
    # nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    G=nx.Graph()
    # for node in nodes:
    #     G.add_node(node)
    G.add_nodes_from(nama)
    for edge in graph:
        G.add_edge(edge[0], edge[1], color='black')

    #KASIH WARNA KE NODE 
    val_map = {}
    for key in path:
        val_map[nama[key]] = 0.0 

    #KASIH WARNA KE EDGE
    for x in range(len(pathdone)):
        G.add_edge(pathdone[x][0],pathdone[x][1],color='r')
    
    colors = nx.get_edge_attributes(G,'color').values()

    values = [val_map.get(node, 0.25) for node in G.nodes()]
    cek = 0 
    for i in values:
        if i == 0.0 : 
            cek +=1
    # GAMBAR GRAF NYA
    pos = nx.planar_layout(G)
    if cek == n :
        nx.draw(G, pos, with_labels=True, node_color='y', edge_color=colors)
    else:
        nx.draw(G, pos, with_labels=True,cmap=plt.get_cmap('plasma_r'), node_color=values, edge_color=colors)
    plt.show()

def drawInitGraph(graph):
    # extract nodes from graph
    # nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    # create networkx graph
    G=nx.Graph()
    # add nodes
    # for node in nodes:
    #     G.add_node(node)
    G.add_nodes_from(nama)
    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])
    val_map = {}
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    # draw graph
    pos = nx.planar_layout(G)
    nx.draw(G, pos, with_labels=True, cmap=plt.get_cmap('plasma_r'), node_color=values)
    # show graph
    plt.show()

def measureSumDistance(path):
    sum = 0
    for i in range(len(path)-1):
        sum += graph[path[i]][path[i+1]]
    return sum

print("Berikut simpul yang dapat dipilih: " + str(nama))
print()
choice = input("Apakah ingin menampilkan graf peta? (Y/N) ").lower()
if choice == 'y':
    print()
    print("Tutup window yang terbuka untuk melanjutkan...")
    drawInitGraph(graphList)
dari = input("Masukkan simpul asal: ")
ke = input("Masukkan simpul tujuan: ")

straightDistDict = getStraightDistance()
path = searchPath(dari,ke)
if len(path) != 0:
    print()
    print("Jalan yang dilalui adalah: ")
    for i in path:
        print(nama[i], end=' ')
    print()
    sumDistance = measureSumDistance(path)
    print("dengan jarak yang ditempuh: " + str(float("{:.2f}".format(sumDistance))) + " meter")
else:
    print()
    print("Tidak terdapat jalur yang menyambungkan simpul asal dan tujuan")

pathdone = jalur(path)
drawFinalGraph(graphList)