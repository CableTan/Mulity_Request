from ILP.Graph_generator import GraphGeneratorGrid2Dimport randomimport pickleimport osclass Request(object):    def __init__(self):        self.request_id = -1        self.src_node   = None        self.dst_node   = None        self.request_bw = -1        self.life_time  = -1        self.pop_time   = -1class RequestGenerator(object):    def __init__(self,G):        self.G      = G        self.count  = 0    def generate_one_request(self, k, life_time, pop_time):        req = Request()        req.request_id = k        _list = random.sample(list(self.G.nodes()),2)        req.src_node = _list[0]        req.dst_node = _list[1]        req.request_bw = 1        req.life_time = life_time        req.pop_time = pop_time        return req    def generate_requests(self, k,life_time, pop_time):        requests = []        for i in range(k):            requests.append(self.generate_one_request(i, life_time, pop_time))        return requests    def save_request_model(self, req, path, filename):        if not os.path.exists(path):            os.mkdir(path)        with open(path+filename,'wb') as model:            pickle.dump(req, model)    def load_request_model(self,path):        with open(path,'rb') as model:            load = pickle.load(model)            model.close()        return load