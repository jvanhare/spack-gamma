# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libmeshb(CMakePackage):
    """A library to handle the *.meshb file format."""

    homepage = "https://github.com/LoicMarechal/libMeshb"
    url = "https://github.com/LoicMarechal/libMeshb/archive/952a157.tar.gz"
    maintainers("jvanhare")
    license("MIT", checked_by="jvanhare")
    version(
        "952a157",
        sha256="db9d3091ecb7fb3478c26f0ca51535cb9f0bbac4beed7f2c9fdb539880f4a957",
    )
    depends_on("c", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = ["-DCMAKE_BUILD_TYPE=Release", "-DBUILD_SHARED_LIBS=ON"]
        return args
