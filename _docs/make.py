from importlib import import_module

MODULES = [
    'compas_fabrication',
    'compas_fabrication.fabrication.robots.rfl'
]

if __name__ == '__main__':
    for name in MODULES:
        obj = import_module(name)

        print obj

        with open('source/pages/reference/{0}.rst'.format(name), 'wb+') as fp:
            fp.write(obj.__doc__)
