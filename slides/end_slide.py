import pyfiglet
from pathlib import Path
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from utils.common import resize
from spiel.renderables.image import Image
from slides._deck import deck

# This will be imported by the main deck file
@deck.slide(title="Thank you")
def title_slide() -> RenderableType:
    # Create large ASCII art titles using pyfiglet
    title_art = pyfiglet.figlet_format("Thank you", font="pagga").strip()

    # Process images on the fly
    left_pikachu_path = resize(Path("images/sonic.png"), (24, 24))
    right_pikachu_path = resize(Path("images/tails.png"), (24, 24))

    # Load processed images using Spiel's native Image widget
    left_pikachu = Image.from_file(str(left_pikachu_path))
    right_pikachu = Image.from_file(str(right_pikachu_path))

    # Create title text with teal figlet
    title_text = Text.from_markup(
        f"[bold green]{title_art}[/bold green]\n\n"
        "[bold yellow]Hope you had fun![/bold yellow]\n\n"
        "Special thanks to Patrick Harrison\n"
        "[dim white]...for organizing this event, and being a pillar of our community[/dim white]",
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