import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

# This will be imported by the main deck file

@deck.slide(title="Agent Architecture")
def agent_architecture_slide() -> RenderableType:
    # Create ASCII art for "ARCHITECTURE"
    arch_art = pyfiglet.figlet_format("Information Flow", font="pagga").strip()

    # Create the main architecture content
    main_content = Text.from_markup(
        f"[bold green]{arch_art}[/bold green]\n\n"
        "[bold yellow]How Data Moves Within An Agentic AI System[/bold yellow]\n\n",
        justify="center"
    )

    # Create the architecture diagram using a table
    diagram_table = Table(title="", show_header=False, box=None, padding=0)
    diagram_table.add_column("component", justify="center")

    # Build the diagram flow
    diagram_table.add_row(Text.from_markup("[bold cyan]┌─────────────────┐"))
    diagram_table.add_row(Text.from_markup("[bold cyan]│ GPU Hardware    │"))
    diagram_table.add_row(Text.from_markup("[bold cyan]└─────────────────┘"))
    diagram_table.add_row(Text.from_markup("[green] ↓ ↑       "))
    diagram_table.add_row(Text.from_markup("[bold cyan]┌─────────────────┐"))
    diagram_table.add_row(Text.from_markup("[bold cyan]│ Foundation Model│"))
    diagram_table.add_row(Text.from_markup("[bold cyan]└─────────────────┘"))
    diagram_table.add_row(Text.from_markup("[green] ↓ ↑       "))
    diagram_table.add_row(Text.from_markup("[bold cyan]┌─────────────────┐"))
    diagram_table.add_row(Text.from_markup("[bold cyan]│ Agentic Runtime │"))
    diagram_table.add_row(Text.from_markup("[bold cyan]└─────────────────┘"))
    diagram_table.add_row(Text.from_markup("[green] ↓ ↑       "))
    diagram_table.add_row(Text.from_markup("[bold cyan]┌─────────────────┐"))
    diagram_table.add_row(Text.from_markup("[bold cyan]│ Invocation Layer│"))
    diagram_table.add_row(Text.from_markup("[bold cyan]└─────────────────┘"))

    # Create component descriptions
    descriptions = Table(title="", show_header=True, header_style="bold cyan", border_style="white")
    descriptions.add_column("Component", style="bold yellow", width=30)
    descriptions.add_column("Function", style="", width=80)

    descriptions.add_row(
        "GPU Hardware",
        Text.from_markup("[dim]Physical computing infrastructure. Provides the raw processing power for model inference and training.[/dim]\n")
    )
    descriptions.add_row(
        "Foundation Model",
        Text.from_markup("[dim]Core AI model (LLM, multimodal, etc.). The brain that understands and generates responses.[/dim]\n")
    )
    descriptions.add_row(
        "Agentic Runtime",
        Text.from_markup("[dim]Agent orchestration layer. Manages tool calls, reasoning loops, and task planning/execution. Includes \"system prompt\" / instructions. [/dim]\n")
    )
    descriptions.add_row(
        "Invocation Layer",
        Text.from_markup("[dim]API/Interface layer. Handles user requests, authentication, and response formatting. Includes \"user prompt\". [/dim]\n")
    )

    # Create a flow indicator
    flow_text = Text.from_markup(
        "[green]⬆️ Bidirectional Data Flow ⬆️\n"
        "[dim]Each layer communicates bidirectionally[/dim]",
        justify="center"
    )

    # Combine everything in a side-by-side layout
    diagram_layout = Layout()
    diagram_layout.split_row(
        Layout(Align.center(diagram_table), size=35),
        Layout(Align.center(descriptions), size=100)
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=6),
        Layout(diagram_layout, size=20),
        Layout(Align.center(flow_text), size=3)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🏗️ Agent Information Flow 🏗️",
        "white"
    )

    return final_content