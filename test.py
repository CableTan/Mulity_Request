from Request_Model.Request_Model import RequestGenerator
from ILP.Graph_generator import GraphGeneratorGrid2D

directory = 'DQN/Graph_and_Net_Model/model/23021217_55/'
graph_name = 'graph_model.pkl'
request_name = 'request_model_1000.pkl'
Graph_model = GraphGeneratorGrid2D(5, 5, 1).load_graph_model(directory+graph_name)
G = Graph_model.G
Requests = RequestGenerator(G)
# request_list = Requests.generate_requests(1000, 0, 0)
# Requests.save_request_model(request_list,directory,request_name)
# print(request_list[1].src_node,request_list[1].dst_node)
print(Graph_model.src_node)

load_request_model = Requests.load_request_model(directory+request_name)
print(load_request_model[9].src_node,load_request_model[9].dst_node)



