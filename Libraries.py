import subprocess
sub = subprocess.run(["pip", "list", "--disable-pip-version-check"],
                     stdout=subprocess.PIPE,
                     universal_newlines=True)
pkgs = (line.rstrip().split() for line in sub.stdout.split("\n")[2:-1])
print("{0:<30}{1:<30}".format('Nombre de Paquete', 'Versión'))
for paquete, version in pkgs:
    print("{0:<30}{1:<30}".format(paquete, version))
