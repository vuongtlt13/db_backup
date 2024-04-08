import importlib.util
import importlib.util
import os.path
import pkgutil
import sys
from typing import List

from driver import Driver


def load_module_from_path(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def find_supported_drivers(supported_drivers: List):
    import tools
    modules = pkgutil.iter_modules(tools.__path__)
    for module in modules:
        driver = module.name

        version_modules = pkgutil.iter_modules(
            [os.path.join(tools.__path__[0], driver)])
        for version_module in version_modules:
            version = version_module.name
            version_module_path = os.path.join(tools.__path__[0], driver, version,
                                               "__init__.py")
            module = load_module_from_path(f"dbbackup.{driver}.{version}",
                                           version_module_path)
            db_driver = Driver(
                name=driver,
                version=version,
                file_path=os.path.join(tools.__path__[0], driver, version)
            )
            supported_drivers.append(db_driver)
