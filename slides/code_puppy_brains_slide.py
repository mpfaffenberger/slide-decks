import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Code Puppy's Brains")
def code_puppy_brains_slide() -> RenderableType:
    # Create ASCII art for "BRAINS"
    brains_art = pyfiglet.figlet_format("CONTEXT ENGINEERING", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold blue]{brains_art}[/bold blue]\n\n"
        "[bold yellow]Advanced Tool Implementation & Context Management[/bold yellow]\n\n"
        "[dim]The secret sauce that makes me never forget my mission! 🧠✨[/dim]",
        justify="center"
    )

    # Create the context gathering table
    context_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    context_table.add_column("Component", style="bold cyan", width=22)
    context_table.add_column("Implementation", style="", width=45)

    # Add context gathering details
    context_components = [
        ("[green]📁 Context Gathering[/green]", 
         "File listing + ripgrep searching across entire codebases"),
        ("[blue]🤔 Thought Tool[/blue]", 
         "Short-medium term planning & reasoning (my internal monologue)"),
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

    # Create the "Why This Matters" section
    why_matters = Text.from_markup(
        "\n[bold green]💡 Why This Matters 💡[/bold green]\n\n"
        "[cyan]Traditional AI:[/cyan] Forget what they were doing after compactions (GRRRR Claude Code)\n"
        "[cyan]Code Puppy:[/cyan] Maintains mission focus for THOUSANDS of steps (if you raise the 300-step limit)\n"
        "\n[italic]" "The thought tool + protected tokens = Unbreakable concentration" "[/italic]",
        justify="center"
    )

    # Create a technical comparison
    tech_comparison = Text.from_markup(
        "\n[bold yellow]⚙️ Technical Superiority ⚙️[/bold yellow]\n\n"
        "[red]Context Window Management:[/red] Intelligent compaction vs dumb truncation\n"
        "[red]Memory Safety:[/red] Protected tokens + step limits\n"
        "[red]Planning Capability:[/red] Thought tool for strategic reasoning\n"
        "[red]Operational Safety:[/red] Timeouts + process management",
        justify="left"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(context_table), size=8),
        Layout(Align.left(advanced_features), size=10),
        Layout(Align.center(why_matters), size=6),
        Layout(Align.left(tech_comparison), size=6)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🧠 Code Puppy's Advanced Architecture 🧠",
        "blue"
    )

    return final_content