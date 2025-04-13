import os, pathlib, importlib, sys

def load_modules():
    if not os.path.exists("funcs"):
        os.makedirs("funcs")
    if not os.path.exists("funcs/addons"):
        os.makedirs("funcs/addons")

    modules = {}
    module_dir = pathlib.Path("funcs")
    
    for file in module_dir.glob("*.py"):
        if file.name == "__init__.py":
            continue
        
        module_name = file.stem
        try:
            module = importlib.import_module(f"funcs.{module_name}")
            if hasattr(module, "NAME") and hasattr(module, "run"):
                modules[module.NAME] = module.run
                print(f"成功加载模块: {module.NAME}")
            else:
                print(f"加载 {module_name} 失败：缺少 NAME 或 run() 定义")
                sys.exit()
        except Exception as e:
            print(f"加载 {module_name} 失败: {str(e)}")
            sys.exit()
    return modules

