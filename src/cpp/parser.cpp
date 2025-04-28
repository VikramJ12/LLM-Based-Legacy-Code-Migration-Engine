#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>
#include <unordered_map>
#include <regex>

namespace py = pybind11;

class CParser {
public:
    struct Node {
        std::string type;
        std::string name;
        std::string content;
        std::vector<std::string> children;
    };

    std::unordered_map<std::string, Node> parse_simple_c(const std::string& code) {
        std::unordered_map<std::string, Node> nodes;
        
        // Very simplified parsing for demonstration
        // Extract function definitions using regex
        std::regex func_regex(R"((\w+)\s+(\w+)\s*\(([^)]*)\)\s*\{([^}]*)\})");
        
        auto begin = std::sregex_iterator(code.begin(), code.end(), func_regex);
        auto end = std::sregex_iterator();
        
        for (std::sregex_iterator i = begin; i != end; ++i) {
            std::smatch match = *i;
            std::string return_type = match[1];
            std::string func_name = match[2];
            std::string params = match[3];
            std::string body = match[4];
            
            // Create function node
            Node func_node;
            func_node.type = "function";
            func_node.name = func_name;
            func_node.content = return_type + " " + func_name + "(" + params + ") {" + body + "}";
            
            // Extract function calls (simplified)
            std::regex call_regex(R"((\w+)\s*\()");
            auto calls_begin = std::sregex_iterator(body.begin(), body.end(), call_regex);
            auto calls_end = std::sregex_iterator();
            
            for (std::sregex_iterator j = calls_begin; j != calls_end; ++j) {
                std::smatch call_match = *j;
                std::string called_func = call_match[1];
                if (called_func != func_name) {  // Ignore recursive calls for simplicity
                    func_node.children.push_back(called_func);
                }
            }
            
            nodes[func_name] = func_node;
        }
        
        return nodes;
    }
};

PYBIND11_MODULE(cparser, m) {
    m.doc() = "C Parser Module";
    
    py::class_<CParser::Node>(m, "Node")
        .def(py::init<>())
        .def_readwrite("type", &CParser::Node::type)
        .def_readwrite("name", &CParser::Node::name)
        .def_readwrite("content", &CParser::Node::content)
        .def_readwrite("children", &CParser::Node::children);
    
    py::class_<CParser>(m, "CParser")
        .def(py::init<>())
        .def("parse_simple_c", &CParser::parse_simple_c, "Parse simple C code");
}
