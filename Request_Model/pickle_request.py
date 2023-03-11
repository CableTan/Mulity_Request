# -*- coding: UTF-8 -*-from Request_Model import RequestGeneratorimport randomfrom Request_Model import Taskimport dillimport timefrom datetime import datetimefrom wireless_sdn_heapdict import heapdictclass PickleRequests(object):    def __init__(self, number_nodes, param_poisson=0.02):        self.str_time = time.strftime("%M%S") + str(int(int(datetime.utcnow().strftime('%f')) / 1000))        self.number_nodes = number_nodes        self.param_poisson = param_poisson  # 0.02, 0.04, ...        self.param_exponential = 1000        self.time_max     = 10000        self.finished     = False        self.request_generator = RequestGenerator(number_nodes)        # THIS ONE IS THE MOST IMPORTANT.        self.hd = heapdict()        # a = int(random.expovariate(1.0000 / self.param_exponential))        # print(a)        tic = 0        list_tic_new_requests = [0]        while True:            tic += int(random.expovariate(self.param_poisson))            if tic <= self.time_max:                list_tic_new_requests.append(tic)            else:                break        self.hq = heapdict()        for t in list_tic_new_requests:            task = Task()            task.task_time = t            task.flag_new_requests = True            self.hq[t] = (t, task)    def start(self):        while len(self.hq):            (_time, (_t, task)) = self.hq.popitem()            current_time = task.task_time            if _time != current_time or _time != _t:                print("NOT EQUAL")                return            if current_time > self.time_max:                break            if task.flag_new_requests:                life_time = int(random.expovariate(1.0000 / self.param_exponential))                pop_time = current_time + life_time                requests = self.request_generator.generate_requests(life_time, pop_time)                task.tuple_poptime_requests = (pop_time, requests)                (_, task_future) = self.hq.setdefault(pop_time, (pop_time, Task()))                task_future.task_time = pop_time                task_future.flag_expire_requests = True            self.hd[current_time] = (current_time, task)    def save(self):        with open(self.str_time + "_arrival_0" + str(1000 + int(100 * \            self.param_poisson))[-2:] + "_requests_pickle", 'wb') as f:            dill.dump(self, f)    # see: https://stackoverflow.com/questions/2709800/how-to-pickle-yourself    def load(self, obj):        dill.load(obj)        # self.__dict__.update(dill.loads(obj).__dict__)if __name__ == "__main__":    pickle = PickleRequests(20)    # with open('../DQN_Multi/1852779_arrival_004_requests_pickle') as f:    #     print(type(f))    #     pickle.load(f)    # i = 0    # for param_poisson in [0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16]:    #     instance = PickleRequests(20, param_poisson=param_poisson)    #     instance.start()    #     instance.save()    #     i += 1