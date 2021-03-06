# -*- coding: utf-8 -*-
"""Provide datapackage details specific to the EIA Form 923 archives."""

from . import core
from . import licenses
from . import contributors

eia923_raw = {
    "name": "pudl-raw-eia923",
    "title": "PUDL Raw EIA Form 923",
    "description":
        "The EIA Form 923 collects detailed monthly and annual "
        "electric power data on electricity generation, fuel "
        "consumption, fossil fuel stocks, and receipts at the power plant "
        "and prime mover level.",
    "profile": "data-package",
    "keywords": [
        "fuel", "boiler", "generator", "plant", "utility", "cost", "price",
        "natural gas", "coal", "eia923", "energy", "electricity", "form 923",
        "receipts", "generation", "net generation", "monthly", "annual", "gas",
        "fuel consumption", "MWh", "energy information administration", "eia",
        "mercury", "sulfur", "ash", "lignite", "bituminous", "subbituminous",
        "heat content"
    ],
    "licenses": [licenses.us_govt, ],
    "homepage": "https://catalyst.coop/pudl/",
    "sources": [
        {
            "title": "US Energy Information Administration",
            "path": "https://www.eia.gov/electricity/data/eia923/"
        }
    ],
    "contributors": [contributors.catalyst_cooperative]
}


def datapackager(dfiles):
    """
    Produce the datapackage json for the eia923 archival collection.

    Args:
        dfiles: iterable of file descriptors, as expected from Zenodo.
            https://developers.zenodo.org/#deposition-files

    Returns:
        dict: fields suited to the frictionless datapackage spec
        https://frictionlessdata.io/specs/data-package/
    """
    return core.annual_resource_datapackager(eia923_raw, dfiles)
