from spack.package import *

class Arccon(CMakePackage):
    """A CMake build system for HPC simulation codes."""

    homepage = "https://arcaneframework.github.io"
    url = "https://github.com/arcaneframework/framework/releases/download/arccon-v1.2.0/arccon-1.2.0.src.tar.gz"
    git = "https://github.com/arcaneframework/framework.git"

    version(
        "1.0.0",
        sha256="1f276325251c407c141cb6b5e223f06ac7ef41f128714d5d98d27b5d41b0dbcc",
        url="https://gitlab.com/cea-ifpen/arccon/-/archive/v1.0.0/arccon-v1.0.0.tar.bz2",
    )
    version(
        "1.1.0",
        sha256="34434f8fdd21dc72668bdb02c77a917357d467c0646b9338199492d02c3681f5",
        url="https://gitlab.com/cea-ifpen/arccon/-/archive/v1.1.0/arccon-v1.1.0.tar.bz2",
    )
    version(
        "1.2.0",
        sha256="bdea35e4c559c85cca7bd82d1a9d8859c465832c645baa127595952131933002",
    )
    version(
        "1.3.0",
        sha256="524fcf1f4c020092b2dede5fda6255f1dc02202c03ea609329d3f89bcdd45032",
    )
    version(
        "1.4.0",
        sha256="89220ab783c0325dca3e7e0f22240f8e8723440a52806f3d0db6bdb3bdb95f80",
    )
    version(
        "1.5.0",
        sha256="9e0b4719fd8a8d6e7fc59d19b4619851d772d9d97ce55ff3d4c0e40376d21b29",
    )

    version("main", branch="main")

    # FIXME: Add dependencies if required.
    depends_on("cmake@3.11:", type=("build", "link"))
