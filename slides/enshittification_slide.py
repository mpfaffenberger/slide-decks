import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="The Enshittification Cycle")
def enshittification_slide() -> RenderableType:
    # Create ASCII art for "ENSHITTIFICATION"
    enshittify_art = pyfiglet.figlet_format("ENSHITTIFICATION", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold red]{enshittify_art}[/bold red]\n\n"
        "[bold yellow]Why AI Products Degrade [/bold yellow]\n\n",
        justify="center",
    )

    # Create the cycle diagram table
    cycle_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    cycle_table.add_column("Phase", style="bold cyan", width=20)
    cycle_table.add_column("What Happens", style="", width=60)
    cycle_table.add_column("AI Example", style="dim", width=60)

    # Add the cycle phases
    cycle_phases = [
        ("\n[green]1. Golden Age[/green]", "\nAmazing product, great experience", "\nWindsurf Cascade launch - mind-blowing!\n"),
        ("[yellow]2. Betray Users[/yellow]", "Monetize at expense of experience", "Weaker models, slower responses, etc\n"),
        ("[orange]3. Betray Creators[/orange]", "Exploit content contributors", "Users train the next wave of models, no credit given\n"),
        ("[red]4. Enshittify[/red]", "Product becomes less usable at 10x the price", "Claude Code Max 20x users hit weekly limit within hours (rumored)"),
        ("[gray]5. Death[/gray]", "Users flee to next thing", "Move to newer/better models/products\n")
    ]

    for phase, what_happens, ai_example in cycle_phases:
        cycle_table.add_row(
            Text.from_markup(phase),
            Text.from_markup(what_happens),
            Text.from_markup(ai_example)
        )

    # Create the "Why It's Faster" section
    why_section = Text.from_markup(
        "\n[bold red]🔥 Why AI Enshittification Happens 10x Faster In The Age of AI 🔥[/bold red]\n\n"
        "[yellow]• VC Pressure:[/yellow] Multi billion $$$ valuations demand impossible growth\n"
        "[yellow]• Tech Debt:[/yellow] AI models accumulate errors exponentially\n"
        "[yellow]• User Trust:[/yellow] One bad event destroys user trust (goodbye, Replit...)\n"
        "[yellow]• Competition:[/yellow] New models and AI products launch weekly\n"
        "[yellow]• Costs:[/yellow] GPU bills force aggressive monetization",
        justify="left"
    )

    # Create a quote
    quote = Text.from_markup(
        "\n[italic]" "Platforms don't die. They commit suicide." "[/italic] - [dim]Cory Doctorow[/dim]",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(cycle_table), size=15),
        Layout(Align.left(why_section), size=8),
        Layout(Align.center(quote), size=3)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "💀 The Tech Death Spiral 💀",
        "red"
    )

    return final_content
