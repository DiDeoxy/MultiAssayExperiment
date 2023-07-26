import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import (
        PackageNotFoundError,
        version,
    )
else:
    from importlib_metadata import (
        PackageNotFoundError,
        version,
    )

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "MultiAssayExperiment"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

from .io.anndata import fromAnnData, readH5AD
from .io.interface import makeMAE
from .io.mudata import fromMuData
from .MultiAssayExperiment import MultiAssayExperiment
