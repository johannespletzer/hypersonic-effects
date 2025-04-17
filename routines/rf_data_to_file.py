"""Python file to read emission inventory files from the folder
and return the radiative forcing in an excel file."""

import sys

from package import calculate_rf as rot

try:
    filepath = sys.argv[1]
    outfile = sys.argv[2]
except IndexError:
    print(
        "\n\tFilepaths for input and output equired: \
            python3 plot_emission_3d.py <input_path> <output.csv>\n"
    )
    sys.exit(1)


def main():
    """Loads file and starts plotting procedure."""

    emission_inventory = rot.EmissionInventory(filepath)

    data_frame = emission_inventory.data

    data_frame.to_csv(outfile, index=False)


if __name__ == "__main__":
    main()
