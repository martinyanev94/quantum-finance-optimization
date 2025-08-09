class LoadBalancer:
    def __init__(self):
        self.servers = []
        self.index = 0

    def add_server(self, server):
        self.servers.append(server)

    def route_order(self, order):
        if not self.servers:
            raise Exception("No servers available to handle the order.")
        server = self.servers[self.index % len(self.servers)]
        self.index += 1
        server.process_order(order)

class Server:
    def __init__(self, id):
        self.id = id

    def process_order(self, order):
        print(f"Server {self.id} processed order: {order}")

# Initialize Load Balancer and Servers
lb = LoadBalancer()
lb.add_server(Server(1))
lb.add_server(Server(2))
lb.add_server(Server(3))

# Simulate incoming orders
for i in range(10):
    lb.route_order(f"Order {i+1}")
