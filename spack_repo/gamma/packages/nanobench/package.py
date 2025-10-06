# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Nanobench(Package):
    """Simple, fast, accurate single-header microbenchmarking functionality for C++11/14/17/20."""

    homepage = "https://github.com/martinus/nanobench"
    url = "https://github.com/martinus/nanobench/archive/refs/tags/v4.3.11.tar.gz"

    maintainers("jvanhare")

    license("MIT", checked_by="jvanhare")

    version(
        "4.3.11",
        sha256="53a5a913fa695c23546661bf2cd22b299e10a3e994d9ed97daf89b5cada0da70",
    )
    version(
        "4.3.10",
        sha256="07ebf949dea04f2ee5e8d7e151dafd25e1ce64716accf40448cd7a8c1bc5374e",
    )
    version(
        "4.3.9",
        sha256="4a7fd8fdd5819e4d1c34ae558df010a0ccf36db0508c41c51cd0181bc04c6356",
    )
    version(
        "4.3.8",
        sha256="0d4e9448318985d94508faea2a7a5bb499da76b8cd56f86f48886fa9b0f49315",
    )
    version(
        "4.3.7",
        sha256="6a2dadb8230370c7fb7a9362be1c3677e44d8e06193a4ecb489a4748ef9483d7",
    )
    version(
        "4.3.6",
        sha256="cfa223fefca8752c0c96416f3440a9b02219f4695a8307db7e8c7054aaed7f01",
    )
    version(
        "4.3.5",
        sha256="205e6cf0ea901f64af971335bfe8011c1f6bd66f6ae678c616da0eddfbe70437",
    )
    version(
        "4.3.4",
        sha256="cbfd5fd9d3522c485aff145e2a24c0477ccd0bf804fb3a1cd3ed95024c7e051e",
    )
    version(
        "4.3.3",
        sha256="388eb8a583257c0ba98d2c4601408a557218382fb0e9f03e318bf65cc889d13d",
    )
    version(
        "4.3.2",
        sha256="730368db7bc6e646afeff6c3c8d1fbc31b5e0eb2754b9f7b270bee9310984e02",
    )

    depends_on("cxx", type="build")

    build_system("generic")

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        mkdirp(join_path(prefix.include, "nanobench"))
        install(
            "src/include/nanobench.h",
            join_path(prefix.include, "nanobench", "nanobench.h"),
        )
