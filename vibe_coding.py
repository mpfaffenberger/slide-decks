
#!/usr/bin/env python
"""
Vibe Coding: Right For Data Science?
A presentation by Michael Pfaffenberger - October 2025
"""

from spiel import Deck, Slide, present
from spiel.renderables.image import Image
from rich.console import RenderableType
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.columns import Columns
import pyfiglet
from PIL import Image as Img
from PIL.Image import Resampling
from pathlib import Path

def resize(image_path: Path, size: tuple[int, int], transparency_threshold: int = 200) -> Path:
    """Resize image and make white pixels transparent, return path to processed image."""
    # Load and process image
    img = Img.open(image_path)
    img_rgba = img.convert('RGBA')
    resized = img_rgba.resize(size, Resampling.LANCZOS)
    
    # Make white/light pixels transparent
    datas = resized.getdata()
    new_data = []
    for item in datas:
        if item[0] > transparency_threshold and item[1] > transparency_threshold and item[2] > transparency_threshold:
            new_data.append((255, 255, 255, 0))  # Transparent
        else:
            new_data.append(item)

    resized.putdata(new_data)
    
    # Save processed image
    output_path = image_path.parent / f"{image_path.stem}_{size[0]}x{size[1]}_transparent.png"
    resized.save(output_path)
    return output_path

deck = Deck(name="Vibe Coding: Is It Right For Data Science?")

@deck.slide(title="Vibe Coding: Is It Right For Data Science?")
def title_slide() -> RenderableType:
    # Create large ASCII art titles using pyfiglet
    title_art = pyfiglet.figlet_format("VIBE CODING", font="smmono9").strip()
    
    # Process images on the fly
    left_pikachu_path = resize(Path("images/img.png"), (48, 48))
    right_pikachu_path = resize(Path("images/img.png"), (48, 48))
    
    # Load processed images using Spiel's native Image widget
    left_pikachu = Image.from_file(str(left_pikachu_path))
    right_pikachu = Image.from_file(str(right_pikachu_path))
    
    # Create title text
    title_text = Text.from_markup(
        f"[bold cyan]{title_art}[/bold cyan]\n\n"
        "[bold yellow]Is It Right For Data Science?[/bold yellow]\n\n"
        "Michael Pfaffenberger\n"
        "[dim white]October 2025[/dim white]",
        justify="center"
    )
    
    # Create 3-column layout using Layout for better control
    layout = Layout()
    layout.split_row(
        Layout(Align.center(left_pikachu, vertical="middle"), size=48),
        Layout(Align.center(title_text, vertical="middle")),
        Layout(Align.center(right_pikachu, vertical="middle"), size=48)
    )
    content = layout
    
    return content

if __name__ == "__main__":
    present(__file__)
