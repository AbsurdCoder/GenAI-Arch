import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from utils.pre_process import create_log_embeddings

class RootCauseAnalysis:
    def __init__(self, log_entries, embedding_model):
        self.log_entries = log_entries
        self.embeddings = create_log_embeddings(log_entries)
        self.embedding_model = embedding_model
        self.graph = self.build_graph()

    def build_graph(self):
        """
        Build a graph representation of the log entries and their relationships.
        """
        graph = nx.Graph()

        # Add nodes (log entries) to the graph
        for entry in self.log_entries:
            graph.add_node(entry)

        # Add edges (relationships) between log entries
        for i in range(len(self.log_entries)):
            for j in range(i+1, len(self.log_entries)):
                similarity = cosine_similarity([self.embeddings[i]], [self.embeddings[j]])[0][0]
                if similarity > 0.8:
                    graph.add_edge(self.log_entries[i], self.log_entries[j])

        return graph

    def find_root_causes(self, problem_log_entry):
        """
        Identify the potential root causes for the given problem log entry.
        
        Args:
            problem_log_entry (str): The log entry representing the problem to be analyzed.
        
        Returns:
            List[str]: A list of potential root cause log entries.
        """
        # Find the shortest paths from the problem log entry to all other nodes
        shortest_paths = nx.shortest_path(self.graph, source=problem_log_entry)

        # Identify the log entries that are furthest away from the problem log entry
        root_causes = []
        for node, path in shortest_paths.items():
            if node != problem_log_entry and len(path) > 3:
                root_causes.append(node)

        return root_causes