__author__ = 'mimirerelala'

import json
import os


#Import JSON data
with open('all_packages.json') as all_packages :
    all_packages_data = json.load(all_packages)
    all_packages.close()

with open('dependencies.json') as dependencies:
    dependencies_data = json.load(dependencies)
    dependencies.close()


def check_if_installed(pack):
    """Return a boolean value to tell if a package is installed"""
    if os.path.exists('installed_modules/'+ pack):
        return True
    else:
        return False


def meet_dependencies(pack):
    """Check if the current packaged has met its dependencies"""
    does_meet = True
    for dep in all_packages_data[pack]:
        if (check_if_installed(dep)):
            continue
        else:
            does_meet = False
    return does_meet


def install_package(pack):
    """Install a packagem, by first checking if it is not already installed and if dependencies are met"""
    if check_if_installed(pack):
        print "Package " + pack + " already installed!"
        list_to_install.remove(pack)
        return
    elif not meet_dependencies(pack):
        return
    else:
        print "Installing package " + pack + " on the disK!"
        os.mkdir('installed_modules/' + pack)
        list_to_install.remove(pack)
    return

def get_dependencies(package):
    """Recursively find dependencies and collect them in the variable list_to_install list"""
    if check_if_installed(package):
        print "Package " + package + " already installed!"
    else:
        print "Checking " + package + " ..."
        print "Getting dependencies for package " + package
        list_to_install.append(package)
        if len(all_packages_data[package])==0:
            print "Package " + package  + " has no dependencies!"
        else:
            for dependencies in all_packages_data[package]:
                print "Package "  + package  + " depends on " + dependencies
                get_dependencies(dependencies)
    return




#main action!!!

#list ti hold packages to be installed
list_to_install = []

#get all needed packages and dependencies recursively
for value in dependencies_data['dependencies']:
    get_dependencies(value)

#install packages and dependecies in reverse order
num_packages = len(list_to_install)
for pkg in range(num_packages):
    install_package(list_to_install[num_packages-pkg-1])