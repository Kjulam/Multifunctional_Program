def try_import_uuid_generater():
    try: from funcs.uuid_generater.main import uuid_generate
    except ImportError:
        print("缺少依赖：uuid_generater")
        return 1
    return 0

from funcs.__main__.commands import *
if not try_import_uuid_generater(): from funcs.uuid_generater.main import uuid_generate
def main():
    print_title("uuid_ugigqi")
    print(f"_{str(uuid_generate(input())).replace("-", "_")}") # type: ignore

