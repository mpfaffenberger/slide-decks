import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from spiel import Deck

# This will be imported by the main deck file
def create_agentic_ai_slide(deck: Deck) -> None:
    
    @deck.slide(title="Agentic AI Spectrum")
    def agentic_ai_slide() -> RenderableType:
        # Create ASCII art for "AGENTIC AI"
        agentic_art = pyfiglet.figlet_format("AGENTIC AI", font="pagga").strip()
        
        # Create the main agentic AI content
        main_content = Text.from_markup(
            f"[bold green]{agentic_art}[/bold green]\n\n"
            "[bold yellow]The 5 Categories of Agentic Intelligence[/bold yellow]\n\n",
            justify="center"
        )
        
        # Create the 5 categories table
        table = Table(title="", show_header=True, header_style="bold cyan", border_style="green")
        table.add_column("[bold]Category[/bold]", style="bold", width=25)
        table.add_column("[bold]Description[/bold]", style="", width=60)
        
        # Add the 5 categories with proper Text objects
        table.add_row(
            Text.from_markup("[bold yellow]1) Simple Chatbots[/bold yellow]"),
            Text.from_markup("1 input → 1 output. Basic Q&A, single-turn conversations.\n[dim]Examples: Basic customer service bots, simple FAQ systems.[/dim]")
        )
        table.add_row(
            Text.from_markup("[bold yellow]2) Function-Calling Chatbots[/bold yellow]"),
            Text.from_markup("Fixed workflow with multi-step processes. RAG is a prime example.\n[dim]Fixed input → Fixed output. Tool use but predictable flow.[/dim]")
        )
        table.add_row(
            Text.from_markup("[bold yellow]3) Interactive Agents[/bold yellow]"),
            Text.from_markup("Unlimited agentic steps using tools + reasoning.\n[dim]Relentlessly solves user-provided tasks. Dynamic, adaptive workflows.[/dim]")
        )
        table.add_row(
            Text.from_markup("[bold yellow]4) Fully Autonomous Agents[/bold yellow]"),
            Text.from_markup("Like #3 but 100% autonomous. No human invocation.\n[dim]Connected to event streams, data feeds. Self-directed operation.[/dim]")
        )
        table.add_row(
            Text.from_markup("[bold yellow]5) Multi-Agent Swarms[/bold yellow]"),
            Text.from_markup("Multiple agents working together. Specialized roles,\n[dim]coordination, emergence. Collective intelligence systems.[/dim]")
        )
        
        # Create a visual hierarchy diagram
        complexity_indicator = Text.from_markup(
            "\n[green]🔹 Complexity & Autonomy ↑[/green]\n"
            "[dim]Simple → Complex → Autonomous → Collective[/dim]",
            justify="center"
        )
        
        # Combine everything in a layout
        layout = Layout()
        layout.split_column(
            Layout(Align.center(main_content), size=8),
            Layout(Align.center(table), size=25),
            Layout(Align.center(complexity_indicator), size=4)
        )
        
        # Wrap in a panel for consistency
        final_content = create_slide_panel(
            layout,
            "🤖 Understanding the AI Agent Spectrum 🤖",
            "green"
        )
        
        return final_content