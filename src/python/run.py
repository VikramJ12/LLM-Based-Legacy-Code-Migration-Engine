import sys
from migration_engine import MigrationEngine

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <c_file_path> [model_name]")
        return
    
    c_file_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "llama3"
    
    try:
        with open(c_file_path, 'r') as f:
            c_code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    print(f"Using model: {model_name}")
    engine = MigrationEngine(model_name)
    result = engine.migrate(c_code, visualize=True)
    
    output_file = c_file_path.replace('.c', '.py')
    with open(output_file, 'w') as f:
        f.write(result["python_code"])
    
    print(f"Migration completed. Output saved to {output_file}")
    print(f"Graph visualization saved to code_graph.png")

if __name__ == "__main__":
    main()
