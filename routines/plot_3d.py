"""
Script to visualize emission data in 3d using mayavi and allowing to take snapshots 
"""

import argparse

from pandas import read_csv

from package import visualize as vis


def main():
    """Main function to execute visualization script"""

    parser = argparse.ArgumentParser(
        prog="plot_3d.py", description="The script visualizes emission data in 3d"
    )

    parser.add_argument("infile", help="Path to emission data file (csv)")
    parser.add_argument(
        "--save",
        action="store_true",
        help="A switch to save mayavi figure to output_3d.png",
    )

    args = parser.parse_args()

    # Prepare data
    data_frame = read_csv(args.infile, delimiter=',')

    # Plot data
    try:
        vis.world3d(
            data_frame["Latitude"],
            data_frame["Longitude"],
            data_frame["Altitude [km]"],
            data_frame["H2O [kg]"],
            save=args.save,
        )
    except NameError:
        vis.world3d(
            data_frame["Latitude"],
            data_frame["Longitude"],
            data_frame["Altitude [km]"],
            data_frame["H2O [kg]"],
        )


if __name__ == "__main__":

    main()
