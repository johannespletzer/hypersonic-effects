import os
import requests
import pytest
import numpy as np
from pathlib import Path

from package import calculate_rf as rf

ZENODO_URL = (
    "https://zenodo.org/records/10948393/files/"
    "Emission_Inventory_H2O_Optimized_v0.2_MR3_Fleet_BRU-MYA_2075.nc?download=1"
)

CACHE_DIR = Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)
CACHE_FILE = CACHE_DIR / "Emission_Inventory.nc"

@pytest.fixture(scope="module")
def cached_nc_file():
    """Download and cache the NetCDF file if not already present."""
    if not CACHE_FILE.exists():
        print(f"Downloading dataset to {CACHE_FILE}...")
        response = requests.get(ZENODO_URL)
        response.raise_for_status()
        with open(CACHE_FILE, "wb") as f:
            f.write(response.content)
    return str(CACHE_FILE)

def test_rf_pipeline_from_nc(cached_nc_file):
    """Test RF model pipeline using actual NetCDF inventory (cached offline)."""
    inventory = rf.EmissionInventory(cached_nc_file)

    inventory.drop_vertical_levels()

    net_rf = inventory.total_rf()
    net_emis = inventory.total_emis()

    # Expected values from the notebook

    expected_net_rf = 174.73488237274864
    expected_net_emis = [84627046.4, 293423.65, 650378.37]

    assert isinstance(net_rf, float)
    assert isinstance(net_emis, list), "total_emis() should return a list"
    assert len(net_emis) == 3, "Expected 3 values in total_emis() output"
    assert all(isinstance(x, float) for x in net_emis), "All emission values should be floats"
    assert all(x > 0 for x in net_emis), "All emission values should be positive"

    # Exact value checks (allowing for small numerical tolerance)
    assert abs(net_rf - expected_net_rf) < 1e-3, f"Unexpected net_rf: {net_rf}"
    for i, (actual, expected) in enumerate(zip(net_emis, expected_net_emis)):
        assert abs(actual - expected) < 1e3, f"Mismatch in net_emis[{i}]: {actual} vs {expected}"
