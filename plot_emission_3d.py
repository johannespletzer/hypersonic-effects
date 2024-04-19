"""Python file to read emission inventory files from the folder
   and return the radiative forcing in an excel file."""

from package import calculate_rf as rot
from package import visualize as vis


def main():
    """Main code. Loads files and extracts labels, calculates
    radiative forcing, writes to excel file."""

    filepath = "/work/bd1062/b309159/TUHH/STRATOFLY-MR3-2024/Emission_Inventory_NO_Optimized_v0.2_MR3_Fleet_BRU-MYA_2075.nc"
    emission_inventory = rot.EmissionInventory(filepath)

    df = emission_inventory.data

    vis.world3d(df["Latitude"], df["Longitude"], df["Altitude [km]"], df["H2O [kg]"])


if __name__ == "__main__":
    main()
