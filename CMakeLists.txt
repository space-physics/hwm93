cmake_minimum_required(VERSION 3.7)
project(hwm93 Fortran)
enable_testing()

if(CMAKE_BUILD_TYPE STREQUAL Debug)
  add_compile_options(-g -O0)
else()
  add_compile_options(-O3)
endif()

if(${CMAKE_Fortran_COMPILER_ID} STREQUAL GNU)
  add_compile_options(-Wall -march=native -fexceptions -Wline-truncation -Werror=array-bounds)
elseif(${CMAKE_Fortran_COMPILER_ID} STREQUAL Intel)

elseif(${CMAKE_Fortran_COMPILER_ID} STREQUAL PGI)
  list(APPEND FFLAGS -Mallocatable=03)
elseif(${CMAKE_Fortran_COMPILER_ID} STREQUAL Flang)
  list(APPEND FFLAGS -Mallocatable=03)
  link_libraries(-static-flang-libs)
endif()

add_executable(hwm src/hwm93_driver.f src/hwm93_sub.f)
add_test(NAME HMW93 COMMAND hwm)

if(UNIX)
  add_test(NAME compareHWM93 
      COMMAND bash -c "./hwm | diff - ../tests/test.log")
endif()
