from __future__ import annotations

import yaml

from GlyphsApp import GetOpenFile, GetSaveFile
from typing import Any


def load_from_yaml(
    message="Load Data From yaml",
    filetypes=["yaml"],
) -> dict[str, Any] | list[Any] | None:
    file_path = GetOpenFile(message=message, filetypes=filetypes)
    if file_path is None:
        return

    with open(file_path, "rb") as f:
        data = yaml.safe_load(f)
    return data


def save_as_yaml(
    data: dict[str, Any] | list[Any],
    message="Save File As yaml",
    ProposedFileName="My File",
    filetypes=["yaml"],
) -> None:
    file_path = GetSaveFile(
        message=message, ProposedFileName=ProposedFileName, filetypes=filetypes
    )
    if file_path is None:
        return

    with open(file_path, "wb") as f:
        yaml.dump(data, f, encoding="utf-8", allow_unicode=True)
