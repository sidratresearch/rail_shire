from rail.estimation.algos import example_module
from rail.estimation.algos.estimate import ShireEstimator
from rail.estimation.algos.inform import ShireInformer

# from rail.estimation.algos.analysis import run_from_inputs
from rail.estimation.algos.io_utils import (  # , load_data_for_run
    hist_outliers,
    json_to_inputs,
    plot_zp_zs_ensemble,
    plot_zp_zs_hdf5BPZ,
)

from ._version import __version__

__all__ = [
    "__version__",
    "json_to_inputs",
    "example_module",
    "ShireInformer",
    "ShireEstimator",
    "hist_outliers",
    "plot_zp_zs_ensemble",
    "plot_zp_zs_hdf5BPZ",
]
