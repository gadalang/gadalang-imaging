from typing import TYPE_CHECKING
import os
import sys
import pytest
from pathlib import Path
from PIL import Image, ImageChops

import gadalang_imaging


TESTS_DIR = Path(__file__).parent
DATA_DIR = TESTS_DIR / "data"
OUTPUT_DIR = TESTS_DIR / "output"
EXPECTED_DIR = TESTS_DIR / "expected"
SAMPLE_IMAGE = DATA_DIR / "sample_image.png"


@pytest.mark.parametrize("transform", ("resize_50",))
def test_transform(transform: str) -> None:
    """Test the transformations."""
    filename = f"{transform}.png"
    output_file = OUTPUT_DIR / filename
    expected_file = EXPECTED_DIR / filename

    output_file.parent.mkdir(exist_ok=True)
    output_file.unlink(missing_ok=True)

    getattr(gadalang_imaging, transform)(target=[SAMPLE_IMAGE], output=str(output_file))

    with Image.open(output_file) as output, Image.open(expected_file) as expected:
        assert output.size == expected.size
        diff = ImageChops.difference(output, expected)
        diff.show()
        # assert not diff.getbbox()
