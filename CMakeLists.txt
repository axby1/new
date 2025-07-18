cmake_minimum_required(VERSION 3.10)
project(my_cpp_app)

set(CMAKE_CXX_STANDARD 17)

find_package(fmt REQUIRED)

add_executable(my_cpp_app cpp/main.cpp)
target_link_libraries(my_cpp_app PRIVATE fmt::fmt)
