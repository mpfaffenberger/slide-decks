import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Privacy-First Alternative: llxprt-code")
def llxprt_alternative_slide() -> RenderableType:
    # Create ASCII art for "LLXPRT"
    llxprt_art = pyfiglet.figlet_format("LLXPRT CODE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold green]{llxprt_art}[/bold green]\n\n"
        "[bold yellow]The Anti-Trojan Open Source Alternative[/bold yellow]\n\n"
        "[dim]Real privacy-focused development tool[/dim]",
        justify="center"
    )

    # Create the comparison table
    comparison_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    comparison_table.add_column("", style="bold cyan", width=15)
    comparison_table.add_column("VC-Funded Tools", style="red", width=25)
    comparison_table.add_column("llxprt-code", style="green", width=25)

    # Add comparison points
    comparisons = [
        ("[yellow]Privacy[/yellow]", "Telemetry & data collection", "Zero privacy invasion"),
        ("[yellow]Funding[/yellow]", "VC-backed (user exploitation)", "Independent developer"),
        ("[yellow]Models[/yellow]", "Limited/provider-locked", "Universal model support"),
        ("[yellow]Future[/yellow]", "Enshittification inevitable", "Privacy-first by design"),
        ("[yellow]Motive[/yellow]", "ROI & exit strategies", "Developer empowerment")
    ]

    for category, vc_funded, llxprt in comparisons:
        comparison_table.add_row(
            Text.from_markup(category),
            Text.from_markup(vc_funded),
            Text.from_markup(llxprt)
        )

    # Create the key features section
    features_section = Text.from_markup(
        "\n[bold green]🚀 Key Features 🚀[/bold green]\n\n"
        "[cyan]• Creator:[/cyan] Andrew Oliver (independent developer)\n"
        "[cyan]• Base:[/cyan] Fork of gemini-cli with privacy improvements\n"
        "[cyan]• Providers:[/cyan] Support for virtually every model provider\n"
        "[cyan]• Philosophy:[/cyan] " "No telemetry, no privacy invasion" "\n"
        "[cyan]• License:[/cyan] Truly open source without strings attached",
        justify="left"
    )

    # Create the recommendation section
    recommendation = Text.from_markup(
        "\n[bold blue]💡 Strongly Recommended 💡[/bold blue]\n\n"
        "[italic]" "Especially if you don't like puppy emojis!" "[/italic]\n\n"
        "[dim]github.com/acoliver/llxprt-code[/dim]",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(comparison_table), size=8),
        Layout(Align.left(features_section), size=8),
        Layout(Align.center(recommendation), size=8)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🛡️ The Legitimate Privacy Alternative 🛡️",
        "white"
    )

    return final_content