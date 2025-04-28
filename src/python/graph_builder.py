import networkx as nx
import cparser
import matplotlib.pyplot as plt

class LogicGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def build_from_parser_output(self, parser_output):
        """
        Convert parser output to a NetworkX graph
        """
        # Add nodes
        for name, node in parser_output.items():
            self.graph.add_node(name, 
                               type=node.type, 
                               content=node.content)
        
        # Add edges
        for name, node in parser_output.items():
            for child in node.children:
                if child in parser_output:
                    self.graph.add_edge(name, child, type="calls")
        
        return self.graph
    
    def visualize(self, output_file=None):
        """
        Visualize the graph
        """
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos, 
                              node_color="lightblue", 
                              node_size=500)
        
        # Draw edges
        nx.draw_networkx_edges(self.graph, pos, 
                              arrowsize=20, 
                              width=2)
        
        # Draw labels
        nx.draw_networkx_labels(self.graph, pos, font_size=10)
        
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()
    
    def to_json(self):
        """
        Convert graph to JSON for LLM consumption
        """
        nodes = []
        for node_name in self.graph.nodes():
            node_data = self.graph.nodes[node_name]
            nodes.append({
                "id": node_name,
                "type": node_data.get("type", "unknown"),
                "content": node_data.get("content", "")
            })
        
        edges = []
        for source, target, data in self.graph.edges(data=True):
            edges.append({
                "source": source,
                "target": target,
                "type": data.get("type", "unknown")
            })
        
        return {"nodes": nodes, "edges": edges}
