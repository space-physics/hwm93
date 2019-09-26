cmake_minimum_required(VERSION 3.7)
project(hwm93 Fortran)
enable_testing()

if(${CMAKE_Fortran_COMPILER_ID} STREQUAL GNU)
  add_compile_options(-Wall -march=native -Wline-truncation -Werror=array-bounds)
endif()

add_executable(hwm src/hwm93_driver.f src/hwm93_sub.f)
add_test(NAME HMW93 COMMAND hwm)

if(UNIX)
  add_test(NAME compareHWM93
      COMMAND bash -c "$<TARGET_FILE:hwm> | diff - ${CMAKE_CURRENT_SOURCE_DIR}/tests/test.log")
endif()
