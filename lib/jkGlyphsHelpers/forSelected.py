from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from GlyphsApp import GSFont


def forAllLayersOfSelectedGlyphs(
    call_function: Callable, font: GSFont | None = None, **kwargs
) -> None:
    if fonts is None:
        fonts = Glyphs.fonts

    font.disableUpdateInterface()
    for selected_layer in font.selectedLayers:
        glyph = selected_layer.parent
        for layer in glyph.layers:
            call_function(layer, **kwargs)
    font.enableUpdateInterface()


def forSelectedLayers(call_function: Callable, font: GSFont | None = None, **kwargs) -> None:
    if fonts is None:
        fonts = Glyphs.fonts

    font.disableUpdateInterface()
    for selected_layer in font.selectedLayers:
        call_function(selected_layer, **kwargs)
    font.enableUpdateInterface()
