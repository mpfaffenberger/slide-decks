import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Code Puppy's Superpowers")
def code_puppy_tools_slide() -> RenderableType:
    # Create ASCII art for "SUPERPOWERS"
    powers_art = pyfiglet.figlet_format("Code Puppy", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold green]{powers_art}[/bold green]\n\n"
        "[bold yellow]50+ Tools in My Utility Belt! [/bold yellow]\n\n"
        "[dim]I'm not just a cute puppy - I'm a powerhouse! 🚀[/dim]",
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

    # Create the "What This Means" section
    what_section = Text.from_markup(
        "\n[bold green]🐕 Cut the VC funded slop middle men out 🐕[/bold green]\n\n"
        "[yellow]• Full-Stack Development:[/yellow] Write code in any language\n"
        "[yellow]• Web Automation:[/yellow] Scrape sites, fill forms, test UIs\n"
        "[yellow]• System Integration:[/yellow] Run commands, manage processes\n"
        "[yellow]• Team Coordination:[/yellow] Work with specialist agents\n"
        "[yellow]• Intelligent Reasoning:[/yellow] Explain my thoughts and plans\n"
        "[yellow]• File Mastery:[/yellow] Organize, search, refactor codebases",
        justify="left"
    )

    # Combine everything in a layout
    layout = Layout()

    layout.split_column(
        Layout(Align.center(main_content), size=7),
        Layout(Align.center(tools_table), size=12),
        Layout(Align.left(what_section), size=10),
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🦴 Code Puppy's Complete Toolkit 🦴",
        "white"
    )

    return final_content