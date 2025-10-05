import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Context Engineering")
def code_puppy_brains_slide() -> RenderableType:
    # Create ASCII art for "CONTEXT"
    context_art = pyfiglet.figlet_format("CONTEXT ENGINEERING", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{context_art}[/bold blue]\n\n"
        "[bold yellow]Tool Implementation & Context Management[/bold yellow]\n\n"
        "[dim]Technical approach to maintaining agent focus and memory[/dim]",
        justify="center"
    )

    # Create the context gathering table
    context_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    context_table.add_column("Component", style="bold cyan", width=22)
    context_table.add_column("Implementation", style="", width=45)

    # Add context gathering details
    context_components = [
        ("[green]📁 Context Gathering[/green]", 
         "File listing + searching across entire codebases - uses ripgrep"),
        ("[blue]🤔 Thought Tool[/blue]", 
         "Short-medium term planning & reasoning for task coordination"),
        ("[purple]💻 Shell Command Tool[/purple]", 
         "Streaming output with time limits & process lifecycle management"),
        ("[orange]🔄 Context Management[/orange]", 
         "Auto/Manual compaction via truncation or summarization")
    ]

    for component, implementation in context_components:
        context_table.add_row(
            Text.from_markup(component),
            Text.from_markup(implementation)
        )

    # Create the advanced features section
    advanced_features = Text.from_markup(
        "\n[bold red]🚀 Advanced Context Management Features 🚀[/bold red]\n\n"
        "[yellow]• Protected Tokens:[/yellow] 50,000 (configurable) tokens protected during compaction\n"
        "[yellow]• Manual Controls:[/yellow] /compact (summarize) & /truncate (hard cut)\n"
        "[yellow]• Smart Compaction:[/yellow] Configurable thresholds for automatic compaction\n"
        "[yellow]• Chain of Thought:[/yellow] Never loses track of final goal\n"
        "[yellow]• Safety Limits:[/yellow] 300-step (configurable) limit prevents infinite loops\n",
        justify="left"
    )

    # Create the "Technical Benefits" section
    benefits_section = Text.from_markup(
        "\n[bold green]💡 Technical Benefits 💡[/bold green]\n\n"
        "[cyan]Standard Approach:[/cyan] Context loss during compaction affects task continuity\n"
        "[cyan]Protected Token Model:[/cyan] Maintains task focus across thousands of operations\n"
        "\n[italic]" "Thought tool integration + protected tokens = sustained task awareness" "[/italic]",
        justify="center"
    )

    # Create technical comparison
    tech_comparison = Text.from_markup(
        "\n[bold yellow]⚙️ Technical Implementation Comparison ⚙️[/bold yellow]\n\n"
        "[red]Context Management:[/red] Intelligent compaction vs simple truncation\n"
        "[red]Memory Protection:[/red] Configurable protected token allocation\n"
        "[red]Planning Integration:[/red] Thought tool for task coordination\n"
        "[red]Safety Mechanisms:[/red] Step limits and timeout controls",
        justify="left"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(context_table), size=8),
        Layout(Align.left(advanced_features), size=10),
        Layout(Align.center(benefits_section), size=6),
        Layout(Align.left(tech_comparison), size=6)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🏗️ Context Engineering Architecture 🏗️",
        "white"
    )

    return final_content