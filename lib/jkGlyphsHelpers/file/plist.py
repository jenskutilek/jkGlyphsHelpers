from __future__ import annotations

import plistlib

from GlyphsApp import GetOpenFile, GetSaveFile
from typing import Any


def load_from_plist(
    message="Load Data From plist",
    filetypes=["plist"],
) -> dict[str, Any] | list[Any] | None:
    file_path = GetOpenFile(message=message, filetypes=filetypes)
    if file_path is None:
        return

    with open(file_path, "rb") as f:
        data = plistlib.load(f)
    return data


def save_as_plist(
    data: dict[str, Any] | list[Any],
    message="Save File As plist",
    ProposedFileName="My File",
    filetypes=["plist"],
) -> None:
    file_path = GetSaveFile(
        message=message, ProposedFileName=ProposedFileName, filetypes=filetypes
    )
    if file_path is None:
        return

    with open(file_path, "wb") as f:
        plistlib.dump(data, f)
