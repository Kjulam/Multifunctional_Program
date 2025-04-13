import os, json, importlib.util
def load_module_from_folder(folder_path: str, functions_list: list, modules_dict: dict):
    about_path = os.path.join(folder_path, "about.json")
    main_path = os.path.join(folder_path, "main.py")
    
    if not (os.path.exists(about_path) and os.path.exists(main_path)):
        print(f"文件夹 {folder_path} 不符合要求，跳过加载。")
        return 1

    if folder_path == "__main__":
        return

    with open(about_path, "r", encoding="utf-8") as file:
        about_info = json.load(file)
    
    if about_info["type"] == "plugin":
        return
    
    # 添加功能名称到列表中
    functions_list.append(about_info["name"])
    
    print(f"正在加载功能：{about_info["name"]}")
    
    spec = importlib.util.spec_from_file_location("module.name", main_path)
    func_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(func_module)

    # 将模块存储在字典中以便后续使用
    modules_dict[about_info["name"]] = func_module
    if hasattr(func_module, "main"):
        print(f"成功加载功能：{about_info["name"]}")
        return 0
    else:
        print(f"功能文件夹 {folder_path} 中的 main.py 没有 main 函数，加载失败。")
        return 1

