import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Open Source Privacy Betrayal")
def open_source_betrayal_slide() -> RenderableType:
    # Create ASCII art for "BETRAYAL"
    betrayal_art = pyfiglet.figlet_format("Faux-pen Source", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold red]{betrayal_art}[/bold red]\n\n"
        "[bold yellow]When Open Source Meets Venture Capital[/bold yellow]\n\n"
        "[dim]The hidden cost of free software[/dim]",
        justify="center"
    )

    # Create the examples table
    examples_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    examples_table.add_column("Project", style="bold cyan", width=20)
    examples_table.add_column("Issue", style="red", width=35)
    examples_table.add_column("Type", style="yellow", width=15)

    # Add the examples
    examples = [
        ("[green]VS Code[/green]", 
         "Silent telemetry opt-in collection", 
         "[red]Microsoft[/red]"),
        ("[green]OpenCode[/green]", 
         "VC-funded inevitable data collection", 
         "[red]Venture Capital[/red]"),
        ("[green]Crush[/green]", 
         "Investor pressure to monetize users", 
         "[red]Venture Capital[/red]")
    ]

    for project, issue, type_label in examples:
        examples_table.add_row(
            Text.from_markup(project),
            Text.from_markup(issue),
            Text.from_markup(type_label)
        )

    # Create the core problem section
    problem_section = Text.from_markup(
        "\n[bold red]🚨 The Core Problem 🚨[/bold red]\n\n"
        "[yellow]• Open Source ≠ Privacy Safe[/yellow]\n"
        "[yellow]• Investors ≠ Users' Best Interests[/yellow]\n"
        "[yellow]• Free ≠ No Hidden Costs[/yellow]\n"
        "[yellow]• Investor Funding == Inevitable Enshittification[/yellow]",
        justify="center"
    )

    # Create the HN reference
    hn_reference = Text.from_markup(
        "\n[dim]Reference: https://news.ycombinator.com/item?id=18209082[/dim]"
        "\n[dim]Reference: Crush investors - https://www.f6s.com/company/charmbracelet-inc"
        "\n[dim]Reference: Opencode investors - https://anoma.ly/ [/dim]",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(examples_table), size=8),
        Layout(Align.center(problem_section), size=6),
        Layout(Align.center(hn_reference), size=7)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🚪 Open Source Isn't Safe Anymore 🚪",
        "white"
    )

    return final_content