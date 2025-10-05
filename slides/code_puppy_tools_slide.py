import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Code Puppy: Tool Overview")
def code_puppy_tools_slide() -> RenderableType:
    # Create ASCII art for "Toolkit"
    toolkit_art = pyfiglet.figlet_format("Agent Toolkit", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold green]{toolkit_art}[/bold green]\n\n"
        "[bold yellow]50+ Available Tools for Code Tasks[/bold yellow]\n\n"
        "[dim]Comprehensive development and automation capabilities[/dim]",
        justify="center"
    )

    # Create the tools overview table
    tools_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    tools_table.add_column("Category", style="bold cyan", width=30)
    tools_table.add_column("Tool Count", style="bold green", width=30)
    tools_table.add_column("Key Abilities", style="", width=50)

    # Add the tool categories
    tool_categories = [
        ("\n[blue]📁 File Operations[/blue]", "\n5 tools", "\nRead, write, edit, search files and directories"),
        ("\n[green]💻 System Commands[/green]", "\n1 tool", "\nExecute terminal commands and run scripts"),
        ("\n[purple]🧠 Agent Management[/purple]", "\n3 tools", "\nCoordinate with other agents and share reasoning"),
        ("\n[red]🌐 Browser Automation[/red]", "\n38 tools!", "\nFull web scraping, form filling, UI automation"),
        ("\n[yellow]📊 Total Arsenal[/yellow]", "\n50+ tools", "\nComplete development and automation suite")
    ]

    for category, count, abilities in tool_categories:
        tools_table.add_row(
            Text.from_markup(category),
            Text.from_markup(count),
            Text.from_markup(abilities)
        )

    # Create the "Development Capabilities" section
    capabilities_section = Text.from_markup(
        "\n[bold green]🛠️ Development Capabilities[/bold green]\n\n"
        "[yellow]• Full-Stack Development:[/yellow] Code generation in multiple languages\n"
        "[yellow]• Web Automation:[/yellow] Browser control and UI testing\n"
        "[yellow]• System Integration:[/yellow] Command execution and process management\n"
        "[yellow]• Multi-Agent Coordination:[/yellow] Collaboration with specialized agents\n"
        "[yellow]• Reasoning Transparency:[/yellow] Explainable decision-making processes\n"
        "[yellow]• Codebase Management:[/yellow] File organization, search, and refactoring",
        justify="left"
    )

    # Combine everything in a layout
    layout = Layout()

    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(tools_table), size=12),
        Layout(Align.left(capabilities_section), size=10),
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "📋 Comprehensive Agent Toolkit 📋",
        "blue"
    )

    return final_content