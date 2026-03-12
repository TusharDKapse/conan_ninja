from conan import ConanFile
from conan.tools.files import copy, get
import os

class NinjaConan(ConanFile):
    name = "ninja"
    version = "1.13.2"
    package_type = "application"

    settings = "os", "arch"

    exports_sources = "toolchain/*"
    
    def build(self):
        if self.settings.os == "Windows":
            url = ("https://github.com/ninja-build/ninja/releases/download/v1.13.2/ninja-win.zip")
            
            get(self, url, destination=self.build_folder)
        elif self.settings.os == "Linux":
            url = ("https://github.com/ninja-build/ninja/releases/download/v1.13.2/ninja-linux.zip")
            
            get(self, url, destination=self.build_folder)
        else:
            raise Exception("Unsupported OS")

    def package(self):
        bin_path = os.path.join(self.package_folder, "bin")
        copy(self, "*", src=self.build_folder, dst=bin_path)
        ninja_path = os.path.join(bin_path, "ninja")
        os.chmod(ninja_path, 0o755)
        
    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.buildenv_info.append_path("PATH", bin_path)
