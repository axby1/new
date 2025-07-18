#include <fmt/core.h>
#include <fstream>

int main() {
    std::ofstream out("cpp_module_output.txt");
    out << "Hello from C++! Computation result: 42" << std::endl;
    out.close();

    fmt::print("C++ module finished computation.\n");
    return 0;
}
