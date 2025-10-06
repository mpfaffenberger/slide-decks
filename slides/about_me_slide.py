import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from utils.common import create_slide_panel
from slides._deck import deck
# This will be imported by the main deck file

@deck.slide(title="About Me")
def about_me_slide() -> RenderableType:
    # Create ASCII art for "ABOUT ME"
    about_art = pyfiglet.figlet_format("ABOUT ME", font="pagga").strip()

    # Process smaller images for this slide
    main_content = Text.from_markup(
        f"[bold green]{about_art}[/bold green]\n\n\n\n"
        "💻 [bold yellow]AI Engineer / Nerd / General of the AI Puppy Army[/bold yellow]\n"
        "🏢 [cyan]Walmart Global Tech[/cyan]\n\n"
        "✨ Save Money | Live Better ✨\n\n"
        "🚀 This presentation was vibe coded with Code Puppy\n"
        "   https://github.com/mpfaffenberger/code_puppy\n"
        "   Using Z.AI's GLM 4.6\n\n"
        "🎯 Spiel is a Python TUI alternative to Powerpoint\n"
        "   The presentation is source controlled here: \n"
        "   https://github.com/mpfaffenberger/slide-decks\n",
        justify="center"
    )

    # Create the legal disclaimer
    from rich.panel import Panel
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
    final_content = create_slide_panel(
        layout,
        "👤 Meet The Vibe Coder 👤",
        "white"
    )

    return final_content