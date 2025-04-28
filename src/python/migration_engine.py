import os
import json
from cparser import CParser
from graph_builder import LogicGraph
from llm_transformer import LLMTransformer

class MigrationEngine:
    def __init__(self, model_name="llama3"):
        self.parser = CParser()
        self.graph_builder = LogicGraph()
        self.transformer = LLMTransformer(model_name)
    
    def migrate(self, c_code, visualize=False):
        """
        Migrate C code to Python OOP code
        """
        # Step 1: Parse C code using C++ parser
        parser_output = self.parser.parse_simple_c(c_code)
        
        # Step 2: Build logic graph
        graph = self.graph_builder.build_from_parser_output(parser_output)
        
        # Optional: Visualize the graph
        if visualize:
            self.graph_builder.visualize("code_graph.png")
        
        # Step 3: Convert graph to JSON for LLM
        graph_json = self.graph_builder.to_json()
        
        # Step 4: Transform to Python OOP using LLM
        python_code = self.transformer.transform_to_oop(graph_json)
        
        return {
            "graph": graph_json,
            "python_code": python_code
        }

def main():
    # Example usage
    c_code = """
    #include <stdio.h>
    
    typedef struct {
        float x;
        float y;
    } Point;
    
    void init_point(Point *p, float x, float y) {
        p->x = x;
        p->y = y;
    }
    
    void translate(Point *p, float dx, float dy) {
        p->x += dx;
        p->y += dy;
    }
    
    void print_point(Point *p) {
        printf("Point at (%f, %f)\\n", p->x, p->y);
    }
    
    int main() {
        Point p;
        init_point(&p, 1.0, 2.0);
        print_point(&p);
        translate(&p, 3.0, 4.0);
        print_point(&p);
        return 0;
    }
    """
    
    # Choose a model that's already pulled locally with Ollama
    engine = MigrationEngine(model_name="llama3")
    result = engine.migrate(c_code, visualize=True)
    
    print("Generated Python Code:")
    print(result["python_code"])
    
    # Save output to file
    with open("output.py", "w") as f:
        f.write(result["python_code"])

if __name__ == "__main__":
    main()
