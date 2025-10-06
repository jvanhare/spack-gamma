# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Inja(CMakePackage):
    """A Template Engine for Modern C++."""

    homepage = "https://github.com/pantor/inja"
    url = "https://github.com/pantor/inja/archive/refs/tags/v3.4.0.tar.gz"

    maintainers("jvanhare")

    license("MIT", checked_by="jvanhare")

    version(
        "3.4.0",
        sha256="7155f944553ca6064b26e88e6cae8b71f8be764832c9c7c6d5998e0d5fd60c55",
    )
    version(
        "3.3.0",
        sha256="e628d994762dcdaa9a97f63a9b8b73d9af51af0ffa5acea6bdbba0aceaf8ee25",
    )
    version(
        "3.2.0",
        sha256="825e1f0076504b5aac99cc9ad8c4cbfdc33e57c06c40353f2d7b93a33caae17d",
    )
    version(
        "3.1.0",
        sha256="f4210493e7e3c62d3050ca6e5e9dd72823ec4125a469fa9b28519d7f32fc9731",
    )
    version(
        "3.0.0",
        sha256="99cdb0d90ab1adff9ec63b40a867ec14e1b217fe2d7ac07a6124de201de4ffd0",
    )
    version(
        "2.2.0",
        sha256="a3ba855dd413410b39e0043109c6d7ca6ac9503a93027933641267b749d72673",
    )
    version(
        "2.1.0",
        sha256="038ecde8f6dbad5d3cedb6ceb0853fd0e488d5dc57593a869633ecb30b0dfa6e",
    )
    version(
        "2.0.1",
        sha256="d5e88438891f36e1d9b0657a294bd73e9c2608e675380e22161e39f7f6ae5802",
    )
    version(
        "2.0.0",
        sha256="c48639f1d808f91b3a663e09dd4199bfba24be29592510d9c3881b753c34b7fd",
    )
    version(
        "1.0.0",
        sha256="c534bd5086a60efe4123ee5c5e65260fb0729b847f46e4d27c95a7c075ebe1ef",
    )

    depends_on("cxx", type="build")
    depends_on("nlohmann-json@3.8.0:")

    build_system("generic")

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        install_tree("include", prefix.include)
