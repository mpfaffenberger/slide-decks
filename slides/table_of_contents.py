import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

# This will be imported by the main deck file

@deck.slide(title="Table of Contents")
def table_of_contents_slide() -> RenderableType:
    # Create ASCII art for "AGENDA"
    agenda_art = pyfiglet.figlet_format("AGENDA", font="pagga").strip()

    # Create the main agenda content
    main_content = Text.from_markup(
        f"[bold green]{agenda_art}[/bold green]\n\n"
        "[bold yellow]What We'll Explore Today[/bold yellow]\n\n",
        justify="center"
    )

    # Create the agenda items table
    table = Table(title="", show_header=False, box=None, padding=(0, 1))
    table.add_column("#", style="bold cyan", width=3)
    table.add_column("Topic", style="", width=50)

    # Add the agenda items
    agenda_items = [
        ("1", "[bold yellow]Introduction to Agentic AI[/bold yellow]", "Understanding the AI Agent Spectrum"),
        ("2", "[bold yellow]History of Coding Agents[/bold yellow]", "From Simple Tools to Advanced Assistants"),
        ("3", "[bold yellow]The Enshittification Cycle[/bold yellow]", "Why It's Happening Faster Than Ever"),
        ("4", "[bold yellow]Meet Code Puppy[/bold yellow]", "Vibe Coding in Action"),
        ("5", "[bold yellow]Data Science: Good Fit?[/bold yellow]", "Analysis & Opinions"),
        ("6", "[bold yellow]iPuppy Notebooks[/bold yellow]", "Interactive Data Science"),
        ("7", "[bold yellow]Our Changing Tech World[/bold yellow]", "This has happened before...")
    ]

    for number, title, subtitle in agenda_items:
        table.add_row(
            number,
            Text.from_markup(f"{title}\n[dim]└── {subtitle}[/dim]")
        )

    # Create a footer
    footer = Text.from_markup(
        "[green]🚀 Let's dive into the world of Vibe Coding! 🚀[/green]",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=8),
        Layout(Align.center(table), size=22),
        Layout(Align.center(footer), size=3)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "📋 Today's Presentation Roadmap 📋",
        "white"
    )

    return final_content