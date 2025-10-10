from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage


class Qama(CMakePackage):
    """Quicksilver bench for Arcane: QAMA"""

    homepage = "https://arcaneframework.github.io/"
    git = "https://github.com/arcaneframework/arcane-benchs.git"

    version("main", branch="main")

    depends_on("arcane")

    root_cmakelists_dir = "qama"
