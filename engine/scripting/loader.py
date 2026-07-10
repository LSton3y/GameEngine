import importlib
import pkgutil


def import_package(package):
    for _, module_name, _ in pkgutil.walk_packages(
        package.__path__,
        package.__name__ + "."
    ):
        importlib.import_module(module_name)