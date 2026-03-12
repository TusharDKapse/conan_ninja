from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.env import VirtualBuildEnv
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch"
    test_type = "explicit"
    generators = "VirtualBuildEnv"
    
    def requirements(self):
        self.tool_requires(self.tested_reference_str)

    def test(self):
        if can_run(self):
            # check that cmake runs
            self.run("ninja --version")

