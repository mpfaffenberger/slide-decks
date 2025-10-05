import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Industry Perspective: Ethan Gold")
def andrew_budd_quote_slide() -> RenderableType:
    # Create ASCII art for "QUOTE"
    quote_art = pyfiglet.figlet_format("QUOTE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{quote_art}[/bold blue]\n\n"
        "[bold yellow]Industry Expert Perspective on Vibe Data Science[/bold yellow]",
        justify="center"
    )

    # Create the speaker profile
    profile_section = Text.from_markup(
        "[cyan]• Name:[/cyan] [bold white]Ethan Gold[/bold white]\n"
        "[cyan]• Title:[/cyan] [bold white]Partner, CTO & Managing Director of Research[/bold white]\n"
        "[cyan]• Company:[/cyan] [bold white]Pula Capital[/bold white]\n"
        "[cyan]• Mike's Commentary:[/cyan] [bold white]Ethan became an AI Engineer years before the term existed[/bold white]\n",
        justify="center"
    )

    # Create the main quote panel
    quote_panel_content = Text.from_markup(
        "\n[bold yellow]💬 Ethan Gold on Vibe Data Science 💬[/bold yellow]\n\n"
        "\n" 
        "[italic][bold white]As a DS and ML leader in the Financial Services industry, there is a significant opportunity for AI Engineering to enhance almost every area [including DS] of the investment pipeline.  We must still exercise caution by using a human-in-the-loop, however, as there are serious implications with real consequences - we have yet to arrive at full automation. If quantitative finance were a solved problem, there would be little to no money to make as the edge would be extracted by the solution - furthermore if that solution existed, it would not be open source or publicly available and would be protected more than nuclear launch codes and kept private for as long as possible.  So do not expect a github repo that will constantly out perform the market for you in a single git pull.[/bold white][/italic]",justify="center"
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