"""Console init py file  contains console terminal related information."""

from espionage.console.c_main import CMain as cMain
from espionage.console.c_davailable import CDAvailable as cAvailable
from espionage.console.c_dbdata import CDBData as cDomainWhois

__all__ = ["cMain", "cAvailable", "cDomainWhois"]
