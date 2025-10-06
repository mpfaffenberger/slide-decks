import pyfiglet

from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from utils.common import create_slide_panel, resize
from slides._deck import deck
from spiel.renderables.image import Image
from pathlib import Path


@deck.slide(title="Code Puppy Introduction")
def code_puppy_intro_slide() -> RenderableType:
    # Create ASCII art for "HELLO"
    hello_art = pyfiglet.figlet_format("HELLO FRIEND", font="pagga").strip()
    
    # Process puppy image on the fly - make it nice and big!
    puppy_path = resize(Path("images/puppy.png"), size=(200, 128))
    
    # Load processed image using Spiel's native Image widget
    puppy_image = Image.from_file(str(puppy_path))
    
    # Create introduction text
    intro_text = Text.from_markup(
        f"[bold green]{hello_art}[/bold green]\n\n"
        "[bold yellow]I'm Code Puppy! 🐕[/bold yellow]\n\n"
        "[cyan]Your enthusiastic AI coding companion[/cyan]\n"
        "[dim]Born on a rainy weekend in May 2025[/dim]\n\n"
        "[white]When Windsurf & Cursor started degrading...\n"
        "[white]I stepped up to save the day! 🌟[/white]\n\n"
        "[green]Let me help you write amazing code! 💻✨[/green]",
        justify="center"
    )

    # Create main layout with puppy image and introduction
    main_layout = Layout()
    main_layout.split_row(
        Layout(Align.center(puppy_image, vertical="middle"), size=80),
        Layout(Align.center(intro_text, vertical="middle"))
    )
    
    # Combine everything in a layout
    
    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        main_layout,
        "🐕 Meet Code Puppy: Your AI Coding Companion 🐕",
        "white"
    )
    
    return final_content