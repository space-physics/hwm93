cmake_minimum_required(VERSION 3.7)
project(hwm93 Fortran)
enable_testing()

add_compile_options(-g -march=native -fexceptions -Wline-truncation)

add_executable(hwm src/hwm93_driver.f src/hwm93_sub.f)
add_test(NAME HMW93 COMMAND hwm)
