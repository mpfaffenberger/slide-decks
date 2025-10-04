import pyfiglet
from pathlib import Path
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.markdown import Markdown
from utils.common import create_slide_panel, resize
from slides._deck import deck
from spiel.renderables.image import Image

# This will be imported by the main deck file

@deck.slide(title="VC Leverage Cascade")
def vc_leverage_slide() -> RenderableType:
    # Create ASCII art for "VC LEVERAGE"
    vc_art = pyfiglet.figlet_format("VC LEVERAGE", font="pagga").strip()

    # Create the main VC leverage content
    main_content = Text.from_markup(
        f"[bold red]{vc_art}[/bold red]\n",
        justify="center"
    )

    # Create the VC leverage diagram as text
    diagram_text = Text.from_markup(
        "[bold cyan]┌─────────────────┐\n"
        "[bold cyan]│   GPU Hardware  │\n"
        "[bold cyan]│   $$$$$$$$$$$   │\n"
        "[bold cyan]└─────────────────┘\n"
        "[yellow] ↓ ↓ ↓ ↓ ↓ ↓ ↓\n"
        "[bold cyan]┌─────────────────┐\n"
        "[bold cyan]│  LLM Providers  │\n"
        "[bold cyan]│   VC Funding    │\n"
        "[bold cyan]│   to buy GPUs   │\n"
        "[bold cyan]└─────────────────┘\n"
        "[yellow] ↓ ↓ ↓ ↓ ↓ ↓ ↓\n"
        "[bold cyan]┌─────────────────┐\n"
        "[bold cyan]│ Agent Startups  │\n"
        "[bold cyan]│   VC Funding    │\n"
        "[bold cyan]│  low prices to  │\n"
        "[bold cyan]│ lure in users   │\n"
        "[bold cyan]└─────────────────┘\n"
        "[yellow] ↓ ↓ ↓ ↓ ↓ ↓ ↓\n"
        "[bold cyan]┌─────────────────┐\n"
        "[bold cyan]│  Users lose     │\n"
        "[bold cyan]│ when investors  │\n"
        "[bold cyan]│   enshittify    │\n"
        "[bold cyan]└─────────────────┘",
        justify="center"
    )

    # Create component descriptions as markdown
    descriptions_markdown = '''🏭 **GPU Hardware**
- Physical computing infrastructure
- The foundation of the entire pyramid
- NVIDIA is super rich

🤖 **LLM Providers - First layer of VC funding**
- OpenAI, Anthropic, etc.
- Take VC money to buy GPUs
- Give away free tier inference / cheap subscriptions 

💻 **LLM Agent Startups - Second layer of funding**
- Cursor, Windsurf, etc
- Take VC money to buy tokens from LLM Providers

🏦 **VC Leverage Multiplier** 
- Each dollar of GPU cost gets marked up multiple times through the cascade!
- Eventually someone has to pay the bill...
- VCs are betting their money that it's going to be YOU.
'''

    descriptions_panel = Panel(
        Markdown(descriptions_markdown),
        title="[bold red]The Double VC Slop Funding Whammy[/bold red]",
        border_style="white",
        padding=(0, 1)
    )

    # Create a flow indicator
    flow_text = Text.from_markup(
        "\n[red]💸 VC Money Flow 💸\n"
        "[dim]Double leverage: Providers AND Agents both need VC funding for same GPUs[/dim]",
        justify="center"
    )

    # Create leverage indicator
    leverage_text = Text.from_markup(
        "\n[bold red]🏦 VC LEVERAGE MULTIPLIER 🏦\n"
        "[yellow]Each dollar of GPU cost gets marked up multiple times through the cascade!\n"
        "[dim]GPU cost → Provider markup → Agent markup → User pays the bill[/dim]",
        justify="center"
    )



    # Load and resize the meme images
    kekw_image = Image.from_file(str(resize(Path("images/kekw.png"), (15, 15))))
    
    # Create TSMC row with KEKW image
    tsmc_row = Layout()
    tsmc_row.split_row(
        Layout(Align.center(kekw_image, vertical="middle"), size=32),
        Layout(Text.from_markup("[bold yellow]TSMC[/bold yellow]", justify="center"))
    )
    
    # Load Poggers image
    poggers_image = Image.from_file(str(resize(Path("images/poggers.png"), (15, 15))))
    
    # Create NVIDIA row with Poggers image
    nvidia_row = Layout()
    nvidia_row.split_row(
        Layout(Align.center(poggers_image, vertical="middle"), size=32),
        Layout(Text.from_markup("[bold green]NVIDIA[/bold green]\n[bold yellow]", justify="center"))
    )
    
    # Load Sadboi image
    sadboi_image = Image.from_file(str(resize(Path("images/sadboi.png"), (15, 15))))
    
    # Create Users row with Sadboi image
    users_row = Layout()
    users_row.split_row(
        Layout(Align.center(sadboi_image, vertical="middle"), size=32),
        Layout(Text.from_markup("[bold blue]Users[/bold blue]", justify="center"))
    )
    
    # Stack the three rows vertically
    image_column = Layout()
    image_column.split_column(
        Layout(tsmc_row, size=8),
        Layout(nvidia_row, size=8),
        Layout(users_row, size=8)
    )

    # Combine everything in a side-by-side layout
    diagram_layout = Layout()
    diagram_layout.split_row(
        Layout(Align.center(diagram_text), size=30),
        Layout(descriptions_panel, size=70),
        Layout(image_column, size=40)
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=4),
        Layout(diagram_layout, size=24),
        Layout(Align.center(flow_text), size=3),
        Layout(Align.center(leverage_text), size=4)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "💸 The VC Leverage Cascade: Double Whammy of Slop 💸",
        "white"
    )

    return final_content