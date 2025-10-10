from spack.package import *

class Qama(CMakePackage):
    """Quicksilver bench for Arcane: QAMA"""

    homepage = "https://arcaneframework.github.io/"
    git = "https://github.com/arcaneframework/arcane-benchs.git"

    version("main", branch="main")

    depends_on("arcane")

    root_cmakelists_dir = "qama"
