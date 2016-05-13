cmake_minimum_required (VERSION 2.8.12)
project(hwm93 Fortran)

add_compile_options(-march=native -fexceptions -Wline-truncation)

add_executable(hwm hwm93_driver.for hwm93_sub.for)

