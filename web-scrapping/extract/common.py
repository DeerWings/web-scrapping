import yaml


__config = None


def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.full_load(f)

    return __config

