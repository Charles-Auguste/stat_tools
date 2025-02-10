from statistics import NormalDist
from typing import Literal

get_z = lambda x: NormalDist().inv_cdf((1 + x) / 2.0)


def __check_input(ConfLvl, MarginErr, PopuProp, PopuSize, how):
    # Small checks
    assert 0 < ConfLvl < 1, "ConfLvl variable must be set between 0 and 1"
    assert 0 < MarginErr < 1, "MarginErr variable must be set between 0 and 1"
    assert 0 < PopuProp < 1, "ConfLvl variable must be set between 0 and 1"
    if PopuSize:
        assert PopuSize > 0, "PopuSize must be an int > 0 or None if undefined number"
    assert how in ("cochran", "yamane"), "how must be one of 'cochran', 'yamane'"
    if how == "yamane":
        assert PopuSize, "For Yamane's method, PopuSize must be specified"


def __return_cochran_infinite_sample_size(ConfLvl, MarginErr, PopuProp) -> int:
    z = get_z(ConfLvl)
    res = (z**2 * PopuProp * (1 - PopuProp)) / MarginErr**2
    if res % 1 > 0:
        return int(res) + 1
    else:
        return int(res)


def __return_yamane_sample_size(MarginErr, PopuSize) -> int:
    res = PopuSize / (1 + PopuSize * MarginErr**2)
    if res % 1 > 0:
        return int(res) + 1
    else:
        return int(res)


def __return_cochran_finite_sample_size(ConfLvl, MarginErr, PopuProp, PopuSize) -> int:
    n0 = __return_cochran_infinite_sample_size(ConfLvl, MarginErr, PopuProp)
    res = n0 / (1 + ((n0 - 1) / PopuSize))
    if res % 1 > 0:
        return int(res) + 1
    else:
        return int(res)


def compute_sample_size(
    ConfLvl: float,
    MarginErr: float,
    PopuProp: float = 0.5,
    PopuSize: float = None,
    how: Literal["cochran", "yamane"] = "cochran",
) -> int:

    __check_input(ConfLvl, MarginErr, PopuProp, PopuSize, how)

    # Run functions
    if how == "yamane":
        return __return_yamane_sample_size(MarginErr, PopuSize)
    elif how == "cochran" and PopuSize:
        return __return_cochran_finite_sample_size(
            ConfLvl, MarginErr, PopuProp, PopuSize
        )
    else:
        return __return_cochran_infinite_sample_size(ConfLvl, MarginErr, PopuProp)
