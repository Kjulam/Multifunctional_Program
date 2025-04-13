import uuid
def uuid_generate(generating_name):
    return uuid.uuid5(uuid.NAMESPACE_DNS, generating_name)

def main():
    pass
