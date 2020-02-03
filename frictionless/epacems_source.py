# -*- coding: utf-8 -*-

from datetime import datetime, timezone
import re

from . import core
from . import licenses
from . import contributors

"""
Provide datapackage details specific to the Eia860 archives
"""

epacems_source = {
    "name": "EPA CEMS Source",
    "title": "EPA CEMS Source",
    "description": "US EPA hourly Continuous Emissions Monitoring System "
                   "(CEMS) data, archived from "
                   "ftp://newftp.epa.gov/dmdnload/emissions/hourly/monthly",
    "profile": "data-package",
    "keywords": [
        "epa", "us", "emissions", "pollution", "ghg", "so2", "co2", "sox",
        "nox", "load", "utility", "electricity", "plant", "generator", "unit",
        "generation", "capacity", "output", "power", "heat content", "mmbtu",
        "steam", "cems", "continuous emissions monitoring system", "hourly"
        "environmental protection agency", "ampd", "air markets program data"
        ],
    "licenses": [licenses.us_govt, licenses.cc_by],
    "homepage": "https://catalyst.coop/pudl/",
    "sources": [
        {
            "title": "US Environmental Protection Agency",
            "path": "ftp://newftp.epa.gov/dmdnload/emissions/hourly/monthly"
        }
    ],
    "contributors": [contributors.catalyst_cooperative]
}


def epacems_resource(name, url, size, md5_hash):
    """
    Produce the resource descriptor for a single file

    Args:
        name: str, file name: must include a 4 digit year, and no other 4 digits
        url: str, url to download the file from Zenodo
        size: int, size it bytes
        md5_hash: str, the md5 checksum of the file

    Return: frictionless datapackage file resource descriptor, per
            https://frictionlessdata.io/specs/data-resource/
    """
    match = re.search(r"([\d]{4})([\w]{2})([\d]{2})", name)

    if match is None:
        raise ValueError("Invalid filename %s" % name)

    year, state, month = match.groups()
    year = int(year)
    month = int(month)

    title, file_format = name.split(".")
    mt = core.MediaType[file_format].value

    return {
        "profile": "data-resource",
        "name": name,
        "path": url,
        "title": title,
        "parts": {"year": year, "month": month, "state": state},
        "encoding": "utf-8",
        "mediatype": mt,
        "format": file_format,
        "bytes": size,
        "hash": md5_hash
    }

def datapackager(dfiles):
    """
    Produce the datapackage json for the epacems archival collection.

    Args:
        metadata: dict of fixed metadata descriptors

    Returns:
        dict of fields suited to the frictionless datapackage spec
            https://frictionlessdata.io/specs/data-package/
    """
    resources = [epacems_resource(
        x["filename"],
        x["links"]["self"],
        x["filesize"], x["checksum"])

        for x in dfiles]

    return dict(**epacems_source,
                **{"resources": resources,
                   "created": datetime.now(timezone.utc).isoformat()})