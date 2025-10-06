import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Vibe Coding for Data Science")
def data_science_vibe_coding_slide() -> RenderableType:
    # Create ASCII art for "DATA"
    data_art = pyfiglet.figlet_format("VIBE DATA SCIENCE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{data_art}[/bold blue]\n\n"
        "[bold yellow]Vibe Coding: Weighing the Pros & Cons[/bold yellow]\n\n"
        "[dim]Is agentic AI coding right for data science?[/dim]",
        justify="center"
    )

    figlet = pyfiglet.figlet_format("Let's Find Out!", font="smmono12").strip()

    lets_find_out = Text.from_markup(f"[bold green]{figlet}[/bold green]")

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=14),
        Layout(Align.center(lets_find_out), size=8),
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "📊 Data Science: Vibe Coding Analysis 📊",
        "white"
    )

    return final_content