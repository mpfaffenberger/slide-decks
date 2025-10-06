import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Industry Perspective: Tarek Lahlou")
def andrew_budd_quote_slide() -> RenderableType:
    # Create ASCII art for "QUOTE"
    quote_art = pyfiglet.figlet_format("QUOTE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{quote_art}[/bold blue]\n\n"
        "[bold yellow]Industry Expert Perspective on Vibe Data Science[/bold yellow]\n\n"
        "[dim]Real-world insights from enterprise leadership[/dim]",
        justify="center"
    )

    # Create the speaker profile
    profile_section = Text.from_markup(
        "[cyan]• Individual:[/cyan] [bold white]Dr. Tarek Lahlou, PhD - Electrical Engineering, MIT[/bold white]\n"
        "[cyan]• Title:[/cyan] [bold white]Senior Distinguished Data Scientist[/bold white]\n"
        "[cyan]• Company:[/cyan][bold white]Walmart Global Tech[/bold white]\n"
        "[cyan]• Mike's Commentary:[/cyan][bold white]I've routinely asked Tarek to advise every project for over 5 years (2 companies)[/bold white]\n",
        justify="center"
    )

    # Create the main quote panel
    quote_panel_content = Text.from_markup(
        "\n[bold yellow]💬 Tarek Lahlou on Vibe Data Science 💬[/bold yellow]\n\n"
        "\n" 
        "[italic][bold white] Vibe Coding’s grasp of science and math is shallower than the experts I know, but still far deeper than any company will ever need it to be. [/bold white][/italic]",justify="center"
    )

    quote_panel = Panel(
        quote_panel_content,
        title="[bold green]Perspective[/bold green]",
        border_style="white",
        padding=(1, 2)
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=6),
        Layout(Align.center(profile_section), size=8),
        Layout(Align.center(quote_panel), size=16),
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "Industry Perspective",
        "white"
    )

    return final_content