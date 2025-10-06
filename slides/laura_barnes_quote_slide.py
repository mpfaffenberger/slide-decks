import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Academic Perspective: Laura Barnes")
def andrew_budd_quote_slide() -> RenderableType:
    # Create ASCII art for "QUOTE"
    quote_art = pyfiglet.figlet_format("QUOTE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{quote_art}[/bold blue]\n\n"
        "[bold yellow]Academic Expert Perspective on Vibe Data Science[/bold yellow]\n\n"
        "[dim]Real-world insights from enterprise leadership[/dim]",
        justify="center"
    )

    # Create the speaker profile
    profile_section = Text.from_markup(
        "[cyan]• Individual:[/cyan] [bold white]Laura Barnes, PhD - Computer Science, University of South Florida[/bold white]\n"
        "[cyan]• Title:[/cyan] [bold white]Professor, Data Science[/bold white]\n"
        "[cyan]• Company:[/cyan] [bold white]University of Virginia[/bold white]\n"
        "[cyan]• Mike's Commentary:[/cyan] [bold white]Who better to weigh in than an actual professor of DS?.[/bold white]\n",
        justify="center"
    )

    # Create the main quote panel
    quote_panel_content = Text.from_markup(
        "\n[bold yellow]💬 Laura Barnes on Vibe Data Science 💬[/bold yellow]\n\n"
        "\n" 
        "[italic][bold white]I mostly use it in my teaching but from what I've observed with my students, here is my two cents: it's a new way of thinking about building a program but requires you to know your data and how to describe what you want to do. If you don't have computational thinking, it doesn't work. [/bold white][/italic]",justify="center"
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
        "Academic Perspective",
        "white"
    )

    return final_content