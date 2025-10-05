import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="A Promise")
def promise_slide() -> RenderableType:
    # Create ASCII art for "PROMISE" using pagga font
    promise_art = pyfiglet.figlet_format("PROMISE", font="pagga").strip()
    
    # Main title with the promise
    main_content = Text.from_markup(
        f"[bold green]{promise_art}[/bold green]\n\n"
        "[bold yellow]I can guarantee at least one of the following statements will be true[/bold yellow]\n\n"
        "[dim]as long as you don't leave early...[/dim]",
        justify="center"
    )

    # Create the guarantees table
    guarantees_table = Table(title="", show_header=False, box=None, padding=(0, 1))
    guarantees_table.add_column("#", style="bold cyan", width=5)
    guarantees_table.add_column("Guarantee", style="", width=50)

    # Add the three guarantees
    guarantees = [
        ("1", "[bold green]You will learn something[/bold green]"),
        ("2", "[bold blue]You will laugh[/bold blue]"),
        ("3", "[bold red]You will never get these two hours back[/bold red]")
    ]

    for number, guarantee in guarantees:
        guarantees_table.add_row(
            Text.from_markup(number),
            Text.from_markup(guarantee)
        )

    # Create a footer note
    footer_note = Text.from_markup(
        "\n[italic][dim]" "Choose your adventure wisely..." "[/dim][/italic]",
        justify="center"
    )

    # Create a little visual separator
    separator = Text.from_markup(
        "\n" + "─" * 50 + "\n",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=8),
        Layout(Align.center(separator), size=2),
        Layout(Align.center(guarantees_table), size=10),
        Layout(Align.center(footer_note), size=4)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🤝 The Speaker's Promise 🤝",
        "white"
    )

    return final_content