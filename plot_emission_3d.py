"""Python file to read emission inventory files from the folder
   and return the radiative forcing in an excel file."""

import sys

try:
    filepath = sys.argv[1]
except IndexError:
    print("\n\tFilepath required: \
            python3 plot_emission_3d.py <filepath>\n")
    sys.exit(1)

from package import calculate_rf as rot
from package import visualize as vis


def main():
    """Loads file and starts plotting procedure."""

    emission_inventory = rot.EmissionInventory(filepath)

    df = emission_inventory.data

    vis.world3d(df["Latitude"], df["Longitude"], df["Altitude [km]"], df["H2O [kg]"])


if __name__ == "__main__":
    main()
