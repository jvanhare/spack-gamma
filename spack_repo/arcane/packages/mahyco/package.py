from spack.package import *

class Mahyco(CMakePackage):
    """MaHyCo"""

    homepage = "https://github.com/cea-hpc/MaHyCo"
    git = "https://github.com/cea-hpc/MaHyCo.git"

    version("master", branch="master")
    version("develop", branch="Mahyco_gpu2")

    variant("cuda", description="Enable CUDA offloading", default=False)
    variant(
        "arcane_cartesian", description="Use Arcane/cea cartesian mesh", default=False
    )
    variant("cuda_prof", description="Enable GPU profiling", default=False)

    depends_on("arcane@3.7")
    depends_on("arcane +cuda", when="+cuda")

    def cmake_args(self):
        return [
            self.define_from_variant("WANT_CUDA", "cuda"),
            self.define_from_variant("WANT_IMPL_CART_ARCANE", "arcane_cartesian"),
            self.define_from_variant("WANT_PROF_ACC", "cuda_prof"),
        ]
