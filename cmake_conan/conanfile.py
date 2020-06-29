from conans import ConanFile, tools
import re, os

class CMakeConanFile(object):
    generators = "cmake_paths"
    _cmake_project_re = re.compile(r"^\s*(project)\s*\(\s*([\w-]+)\s+(VERSION)\s+([0-9]+\.[0-9]+(\.[0-9]+)*)(\s+(DESCRIPTION)\s+\"(.*)\"){0,1}(\s+(HOMEPAGE_URL)\s+\"(.*)\"){0,1}(\s+(LANGUAGES)\s+.*){0,1}\)", re.IGNORECASE|re.MULTILINE)
    _content = None        
    
    def set_version(self):
        if not self._content:
            self._content = tools.load(os.path.join(self.recipe_folder, "CMakeLists.txt"))
        re_result = self._cmake_project_re.search(self._content)
        if re_result==None:
            raise Exception("Could not extract version number from CMakeLists.txt file")
        self.version = re_result.group(4).strip()
        
    def set_name(self):
        if not self._content:
            self._content = tools.load(os.path.join(self.recipe_folder, "CMakeLists.txt"))
        re_result = self._cmake_project_re.search(self._content)
        if re_result==None:
            raise Exception("Could not extract package name from CMakeLists.txt file")
        self.name = re_result.group(2).strip()
        #setting description and url is currently not possible
        #if re_result.group(8)!=None:
        #    self.description = re_result.group(8).strip()
        #if re_result.group(11)!=None:
        #    self.url = re_result.group(11).strip()


class CMakeConanFileReq(ConanFile):
    name = "cmake_conan_file_req"
    version = "1.0" 
