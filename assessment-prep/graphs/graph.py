class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                
        print("The Graph: ", self.graph_dict)
    
    def get_paths(self, start, end, path = []):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return
        
        paths = []
        
        for city in self.graph_dict[start]:
            if city not in path:
                new_paths = self.get_paths(city, end, path)
                for p in new_paths:
                    paths.append(p)
                
                    
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for city in self.graph_dict[start]:
            if city not in path:
                sp = self.get_shortest_path(city, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        
        return shortest_path
        
        
    
if __name__ == "__main__":    
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
        ("New York", "Melrose"),
    ]
    
    route_graph = Graph(routes)
    
    start = "New York"
    end = "New York"
    print(f"Paths between {start} and {end} is: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end} is: ", route_graph.get_shortest_path(start, end))