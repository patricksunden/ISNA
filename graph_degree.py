'''generates a graph in which nodes corresponds to hashtags and an edge 
between nodes indicates that there's at least one tweet where the both
hashtags are in the same tweet'''

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #Used to display Chinese labels normally

#read hashtags from csv files
smokefree_f = pd.read_csv('scraped_tweets_smokefree_30.csv')
nosmoking_f = pd.read_csv('scraped_tweets_nosmoking_30.csv')
quitsmoking_f = pd.read_csv('scraped_tweets_quitsmoking_30.csv')
quittingsmoking_f =pd.read_csv('scraped_tweets_quittingsmoking_30.csv')
smokingkills_f = pd.read_csv('scraped_tweets_smokingkills_30.csv')
stopsmoking_f = pd.read_csv('scraped_tweets_stopsmoking_30.csv')
tobaccofree_f = pd.read_csv('scraped_tweets_tobaccofree_30.csv')

smokefree = smokefree_f['hashtags'].tolist()
nosmoking = nosmoking_f['hashtags'].tolist()
quitsmoking = quitsmoking_f['hashtags'].tolist()
quittingsmoking = quittingsmoking_f['hashtags'].tolist()
smokingkills = smokingkills_f['hashtags'].tolist()
stopsmoking = stopsmoking_f['hashtags'].tolist()
tobaccofree = tobaccofree_f['hashtags'].tolist()

hashtags = []
hashtags.append(smokefree)
hashtags.append(nosmoking)
hashtags.append(quitsmoking)
hashtags.append(quittingsmoking)
hashtags.append(smokingkills)
hashtags.append(stopsmoking)
hashtags.append(tobaccofree)


#empty graph for composing
G = nx.empty_graph(0)

for hashtag in hashtags:
    for x in hashtag:
        if x != '[]':
            x = x.lower()
            x = x.strip('][').split(', ')
            graph = nx.complete_graph(x)
            G = nx.compose(G, graph)

nx.draw(G, with_labels=True)
plt.savefig("graph.png")

centrality_total = 0
total_variance = 0
betweenness_total_variance = 0
betweenness_centrality_total = 0

print("Number of nodes: ", nx.number_of_nodes(G))
print("Number of edges", nx.number_of_edges(G))

centrality_dict = nx.degree_centrality(G)
centralitylist = list(centrality_dict.values())

for i in range(0, len(centralitylist)):
   centrality_total += centralitylist[i]
average_degree_centrality = centrality_total/len(centralitylist)
print("average degree centrality: ", average_degree_centrality)


for i in range(0, len(centralitylist)):
    total_variance += (centralitylist[i] - average_degree_centrality)**2

var = (total_variance/len(centralitylist))
print("Variance of degree centrality: ", var)



betweenness_centrality_dict = nx.betweenness_centrality(G)
betweennesslist = list(betweenness_centrality_dict.values())
for i in range(0, len(betweennesslist)):
    betweenness_centrality_total += betweennesslist[i]
average_betweenness_centrality = betweenness_centrality_total/len(betweennesslist)
print("average betweenness centrality: ", average_betweenness_centrality)


for i in range(0, len(betweennesslist)):
    betweenness_total_variance += (betweennesslist[i] - average_betweenness_centrality)**2

var1 = (betweenness_total_variance/len(betweennesslist))
print("Variance of betweenness centrality: ", var1)

if nx.is_connected(G):
    print("Diameter of the graph: ", nx.diameter(G))
else:
    print("Diameter of the graph is infinite")

print("Average clustering coefficient of the graph: ", nx.average_clustering(G))
print("size of largest component: ", len(max(nx.connected_components(G))))

#Tehtävä 5
### Info about the above graph

def highestRankedNodes(G):
    '''Five nodes with highest degree, kat'z, pagerank, closeness and betweenness centrality'''
    degreeCent = []
    katzCent = []
    pagerankCent = []
    closeCent = []
    betweenCent = []
    
    alpha = 1 /(1+ max(nx.adjacency_spectrum(G)))
    katzDict = nx.katz_centrality(G, alpha)
    pagerankDict = nx.pagerank(G)
    closeDict = nx. closeness_centrality(G)
    
    
    for i in range(0,10):
        k = max(centrality_dict, key=centrality_dict.get)
        v = centrality_dict.get(k)
        degreeCent.append((k, v))
        centrality_dict.pop(k)
    
    for i in range(0, 5):
        k = max(katzDict, key=katzDict.get)
        v = katzDict.get(k)
        katzCent.append((k, v))
        katzDict.pop(k)
    for i in range(0, 5):
        k = max(pagerankDict, key=pagerankDict.get)
        v = pagerankDict.get(k)
        pagerankCent.append((k, v))
        pagerankDict.pop(k)
    for i in range(0, 5):
        k = max(closeDict, key=closeDict.get)
        v = closeDict.get(k)
        closeCent.append((k, v))
        closeDict.pop(k)
    for i in range(0, 5):
        k = max(betweenness_centrality_dict, key=betweenness_centrality_dict.get)
        v = betweenness_centrality_dict.get(k)
        betweenCent.append((k, v))
        betweenness_centrality_dict.pop(k)
        
    print("---FIVE HIGHEST NODES--- \n")
    print("Degree centrality: ", degreeCent)
    
    print("Katz Centrality: ", katzCent)
    print("Pagerank centrality: ", pagerankCent)
    print("Closeness centrality: ", closeCent)
    print("Betweenness centrality:", betweenCent)
    
    return 0
    
highestRankedNodes(G)
    