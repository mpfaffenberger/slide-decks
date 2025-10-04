
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

def resize(image_path: Path, size: tuple[int, int]) -> Path:
    """Resize image and replace transparent pixels with terminal background, return path to processed image."""
    # Load and process image
    img = Img.open(image_path)
    img_rgba = img.convert('RGB')
    resized = img_rgba.resize(size, Resampling.LANCZOS)
    
    # Replace transparent pixels with terminal background (RGB 30,30,30)
    datas = resized.getdata()
    new_data = []
    for item in datas:
        if item[0] < 30 and item[1] < 30 and item[2] < 30:
            new_data.append((30, 30, 30))
        else:
            new_data.append(item)
    
    resized.putdata(new_data)
    
    # Save processed image
    output_path = image_path.parent / f"{image_path.stem}_{size[0]}x{size[1]}_matched.png"
    resized.save(output_path)
    return output_path

deck = Deck(name="Vibe Coding: Is It Right For Data Science?")

@deck.slide(title="Vibe Coding: Is It Right For Data Science?")
def title_slide() -> RenderableType:
    # Create large ASCII art titles using pyfiglet
    title_art = pyfiglet.figlet_format("VIBE CODING", font="pagga").strip()
    
    # Process images on the fly
    left_pikachu_path = resize(Path("images/pika.png"), (24, 24))
    right_pikachu_path = resize(Path("images/charizard.png"), (24, 24))
    
    # Load processed images using Spiel's native Image widget
    left_pikachu = Image.from_file(str(left_pikachu_path))
    right_pikachu = Image.from_file(str(right_pikachu_path))
    
    # Create title text with teal figlet
    title_text = Text.from_markup(
        f"[bold green]{title_art}[/bold green]\n\n"
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


@deck.slide(title="About Me")
def about_me_slide() -> RenderableType:
    # Create ASCII art for "ABOUT ME"
    about_art = pyfiglet.figlet_format("ABOUT ME", font="pagga").strip()
    
    # Process smaller images for this slide
    main_content = Text.from_markup(
        f"[bold green]{about_art}[/bold green]\n\n\n\n"
        "💻 [bold yellow]AI Engineer / Nerd / General of the AI Puppy Army[/bold yellow]\n"
        "🏢 [cyan]Walmart Global Tech[/cyan]\n\n"
        "✨ Save money | live better\n\n"
        "🚀 This presentation was vibe coded with Code Puppy\n"
        "   https://github.com/mpfaffenberger/code_puppy\n"
        "   Using Z.AI's GLM 4.6\n\n"
        "🎯 Spiel is a Python TUI alternative to Powerpoint\n"
        "   The presentation is source controlled here: \n"
        "   https://github.com/mpfaffenberger/slide-decks\n",
        justify="center"
    )
    
    # Create the legal disclaimer
    disclaimer = Panel(
        Text.from_markup(
            "[bold red]⚠️  IMPORTANT LEGAL DISCLAIMER ⚠️[/bold red]\n\n"
            "My views and opinions are not to be construed with Walmart's.\n"
            "All of my words, views, and opinions are my own."
        ),
        title="[bold red]Legal Notice[/bold red]",
        border_style="red",
        padding=(1, 2)
    )
    
    # Create layout with profile image, main content, and disclaimer
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=20),
        Layout(disclaimer)
    )
    
    # Wrap in a panel for consistency
    final_content = Panel(
        layout,
        title="[bold green]👤 Meet The Vibe Coder 👤[/bold green]",
        border_style="white",
        padding=(1, 2)
    )
    
    return final_content


if __name__ == "__main__":
    present(__file__)