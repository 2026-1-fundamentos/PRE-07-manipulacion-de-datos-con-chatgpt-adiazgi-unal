"""Autograding script."""

import os


def test_01():
    """Test word count job."""

    assert os.path.exists("files/output/summary.csv")
    assert os.path.exists("files/plots/top10_drivers.png")
    
summary.to_csv("files/output/summary.csv", index=False)
