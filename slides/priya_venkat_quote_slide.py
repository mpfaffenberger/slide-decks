import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Industry Perspective: Priya Venkat")
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
        "[cyan]• Name:[/cyan] [bold white]Priya Venkat[/bold white]\n"
        "[cyan]• Title:[/cyan] [bold white]Distinguished Data Scientist[/bold white]\n"
        "[cyan]• Company:[/cyan] [bold white]Walmart Global Tech, Transaction Systems[/bold white]\n"
        "[cyan]• Mike's Commentary:[/cyan] [bold white]Priya develops and ships high impact DS/ML models to prod.[/bold white]\n",
        justify="center"
    )

    # Create the main quote panel
    quote_panel_content = Text.from_markup(
        "\n[bold yellow]💬Priya Venkat on Vibe Data Science 💬[/bold yellow]\n\n"
        "\n" 
        "[italic][bold white] Vibe coding enables rapid prototyping without the need to write code line by line. Data scientists and AI/ML practitioners become composers and conductors of a digital ensemble — defining the intent, setting the rhythm and tone, while GenAI tools orchestrate that vision into model pipelines and prototypes. "
        "Code agents play a pivotal role in exploratory data analysis, translating high-level intent into impactful visualizations and insights. This intuitive, collaborative process sparks creativity, accelerates experimentation, and fosters adaptive problem solving. "
        "Yet, production-ready solutions still require structure — reviewable, reproducible workflows underpinned by unit tests, version control, and governance. As vibe coding evolves, the discipline of code review, testing, and evaluation remains essential at every level, ensuring harmony between creative flow and technical rigor. [/bold white][/italic]",justify="center"
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