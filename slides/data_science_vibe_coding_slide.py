import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Vibe Coding for Data Science")
def data_science_vibe_coding_slide() -> RenderableType:
    # Create ASCII art for "DATA"
    data_art = pyfiglet.figlet_format("DATA SCIENCE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{data_art}[/bold blue]\n\n"
        "[bold yellow]Vibe Coding: Weighing the Pros & Cons[/bold yellow]\n\n"
        "[dim]Is agentic AI coding right for data workflows?[/dim]",
        justify="center"
    )

    # Create pros table
    pros_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    pros_table.add_column("[green]✅ PROS[/green]", style="bold green", width=40)
    pros_table.add_column("Impact", style="", width=60)

    pros = [
        ("[green]Rapid Prototyping[/green]", "Quick EDA, visualization, and model testing"),
        ("[green]Automated Data Cleaning[/green]", "Handle missing values, outliers, preprocessing"),
        ("[green]Documentation Generation[/green]", "Auto-create analysis reports and notebooks"),
        ("[green]Multi-language Flexibility[/green]", "Python, R, SQL, Julia - switch seamlessly"),
        ("[green]Experiment Automation[/green]", "Run multiple analysis approaches quickly"),
        ("[green]Code Review & Debugging[/green]", "Catch statistical errors and logic bugs")
    ]

    for pro, impact in pros:
        pros_table.add_row(
            Text.from_markup(pro),
            Text.from_markup(impact)
        )

    # Create cons table
    cons_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    cons_table.add_column("❌ CONS", style="bold red", width=40)
    cons_table.add_column("Risk Level", style="", width=60)

    cons = [
        ("[red]Statistical Understanding[/red]", "May miss domain-specific statistical nuances"),
        ("[red]Data Privacy Risks[/red]", "Sensitive data processed by cloud models"),
        ("[red]Reproducibility Issues[/red]", "Random generation, hard to version control"),
        ("[red]Domain Knowledge Gap[/red]", "Lacks industry-specific context and experience"),
        ("[red]Result Validation[/red]", "Can't intuitively know if results 'make sense'"),
        ("[red]Complex ML Pipelines[/red]", "Struggles with sophisticated ML engineering")
    ]

    for con, risk in cons:
        cons_table.add_row(
            Text.from_markup(con),
            Text.from_markup(risk)
        )

    # Create the verdict section
    verdict_section = Text.from_markup(
        "\n[bold yellow]⚖️ The Verdict ⚖️[/bold yellow]\n\n"
        "[cyan]🟢 BEST FOR:[/cyan] Exploratory analysis, prototyping, documentation, routine tasks\n"
        "[cyan]🔴 AVOID FOR:[/cyan] Production ML, sensitive data, critical decision-making\n"
        "[cyan]🟡 HYBRID APPROACH:[/cyan] AI-assisted development + human validation\n\n"
        "[italic]" "Think of it as a co-pilot, not the pilot-in-command" "[/italic]",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=6),
        Layout(Align.center(pros_table), size=8),
        Layout(Align.center(cons_table), size=8),
        Layout(Align.center(verdict_section), size=8)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "📊 Data Science: Vibe Coding Analysis 📊",
        "blue"
    )

    return final_content