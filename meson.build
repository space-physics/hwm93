project('hwm93', 'fortran', default_options : ['default_library=static'])

fc = meson.get_compiler('fortran')
if fc.get_id() == 'gcc'
  add_project_arguments('-Wall', '-march=native', '-Wline-truncation', '-Werror=array-bounds', language: 'fortran')
endif

hwm_exe = executable('hwm', 'src/hwm93_driver.f', 'src/hwm93_sub.f')
test('HMW93', hwm_exe)

#if 'UNIX'
# test('NAME', 'compareHWM93', 'COMMAND', 'bash', '-c', '$<TARGET_FILE:hwm> | diff - ${CMAKE_CURRENT_SOURCE_DIR}/tests/test.log')
#endif
