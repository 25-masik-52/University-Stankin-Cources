cmake_minimum_required(VERSION 3.16)

project(exam LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core)

configure_file(${CMAKE_SOURCE_DIR}/person.xml ${CMAKE_BINARY_DIR}/person.xml COPYONLY)

add_executable(exam
  main.cpp
)
target_link_libraries(exam Qt${QT_VERSION_MAJOR}::Core)

include(GNUInstallDirs)
install(TARGETS exam
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
