from typing import Dict, Any
import ollama

class LLMTransformer:
    def __init__(self, model_name="llama3"):
        """
        Initialize with the model name to use with Ollama
        """
        self.model_name = model_name
        # Verify the model is available
        try:
            # Attempt to use the model to ensure it's pulled
            ollama.chat(model=model_name, messages=[
                {"role": "user", "content": "test"}
            ])
        except Exception as e:
            print(f"Error with model {model_name}: {e}")
            print(f"Please run 'ollama pull {model_name}' first")
            raise
    
    def transform_to_oop(self, graph_json: Dict[str, Any]) -> str:
        """
        Transform the graph representation into OOP Python code using Ollama
        """
        # Create natural language description of the graph
        nl_description = self._graph_to_nl(graph_json)
        
        # Create the prompt for the LLM
        prompt = f"""
        Convert this C code represented as a graph into object-oriented Python code.
        
        Graph description:
        {nl_description}
        
        Please identify potential classes, convert functions to methods, and follow Python best practices 
        including type hints. Organize the code using proper OOP principles.
        
        Return only the Python code without explanations.
        """
        
        # Call Ollama
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are an expert code migration assistant."},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        
        return response['message']['content'].strip()
    
    def _graph_to_nl(self, graph_json: Dict[str, Any]) -> str:
        """
        Convert the graph JSON to natural language description
        """
        description = []
        
        # Describe nodes
        for node in graph_json["nodes"]:
            if node["type"] == "function":
                description.append(f"Function '{node['id']}': {node['content']}")
        
        # Describe edges
        for edge in graph_json["edges"]:
            if edge["type"] == "calls":
                description.append(f"Function '{edge['source']}' calls function '{edge['target']}'")
        
        return "\n".join(description)
