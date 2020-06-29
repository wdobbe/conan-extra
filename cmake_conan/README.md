# CMakeConanFile
Class derived from ConanFile that will read package name and version from toplevel CMakeLists.txt.

# How to use
You must specify the name and version using the 'project()' [cmake command](https://cmake.org/cmake/help/latest/command/project.html).
The toplevel CMakeLists.txt is expected to exist in the same directory where your conanfile.py is located.
Example:

```cmake
project(mylib VERSION 6.1.0
              DESCRIPTION "My super cool library"
              HOMEPAGE_URL "https://url.to.your.lib"
              LANGUAGES C)
```

In your conanfile.py add the following attributes to the ConanFile object:

```python
    python_requires = "cmake_conan_file_req/1.0@dynniq/testing"
    python_requires_extend = "cmake_conan_file_req.CMakeConanFile"
```

Example:
```python
    class MyLibConan(ConanFile):
        #name, version are read from toplevel CMakeLists.txt
        python_requires = "cmake_conan_file_req/1.0@user/testing"
        python_requires_extend = "cmake_conan_file_req.CMakeConanFile"
        description = "My cool library"
        url = "https://url.to.your.lib"
        license = "MIT"
        settings = "os", "compiler", "build_type", "arch"
        options = { "shared": [True, False] }
        default_options = { "shared": True }
        exports_sources = ["*"]
```
# Requirements
conan >= 1.26.0

# Known limitations
  * The project() cmake command allows to specify also the homepage URL and the project description. You can add these but the CMakeConanFile will not use them because Conan currently doesn't support setting the 'url' or 'description' attributes from external sources.
  * You must specify the project() command options in the order listed in the cmake documentation (and in the example above).
  * Comments inside the project() command are not supported.
