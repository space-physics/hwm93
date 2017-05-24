cmake_minimum_required (VERSION 2.8.12)
project(hwm93 Fortran)

add_compile_options(-march=native -fexceptions -Wline-truncation)

add_executable(hwm fortran/hwm93_driver.f fortran/hwm93_sub.f)

