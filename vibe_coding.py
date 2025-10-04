
#!/usr/bin/env python
"""
Vibe Coding: Right For Data Science?
A presentation by Michael Pfaffenberger - October 2025
"""

from spiel import Deck, Slide, present
from rich.console import RenderableType
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
import pyfiglet

deck = Deck(name="Vibe Coding: Is It Right For Data Science?")

@deck.slide(title="Vibe Coding: Is It Right For Data Science?")
def title_slide() -> RenderableType:
    # Create large ASCII art titles using pyfiglet
    title_art = pyfiglet.figlet_format("VIBE CODING", font="bigmono9")
    subtitle_art = pyfiglet.figlet_format("", font="smmono9")
    
    # Build content as a single string with newlines
    content_str = (
        f"[bold cyan]{title_art}[/bold cyan]\n"
        f"[bold magenta]{subtitle_art}[/bold magenta]\n\n"
        "[bold yellow]Is It Right For Data Science?[/bold yellow]\n\n\n"
        "Michael Pfaffenberger\n"
        "[dim white]October 2025[/dim white]"
    )
    
    # Create a single Text object with markup
    content = Text.from_markup(content_str)
    
    return Panel(
        Align.center(content),
        title="",
        border_style="bright_blue",
        padding=(1, 2)
    )

if __name__ == "__main__":
    present(__file__)
