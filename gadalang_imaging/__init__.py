"""Imaging nodes for gada."""
from __future__ import annotations
from pathlib import Path
from PIL import Image


def resize(target: str, scale: int, output: str | None = None) -> None:
    """Resize an image.

    :param target: input path
    :param scale: scale value
    :param output: output path
    """
    path = Path(target)
    output = (
        output
        if output is not None
        else str(path.parent / (path.stem + f"_{scale}" + path.suffix))
    )

    with Image.open(path) as im:
        ratio = scale / 100.0
        im.resize((int(im.width * ratio), int(im.height * ratio)), Image.BICUBIC).save(
            output
        )


def resize_50(target: list[str], output: str | None = None) -> None:
    """Resize an image by 50%.

    :param target: input path
    :param output: output path
    """
    if output is not None and len(target) > 1:
        raise ValueError("output must be None with more than 1 target")

    for t in target:
        try:
            resize(target=t, scale=50, output=output)
        except Exception as e:
            print(e)
