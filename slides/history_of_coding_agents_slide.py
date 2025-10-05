import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.markdown import Markdown
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="History of Coding Agents - Timeline")
def history_of_coding_agents_timeline_slide() -> RenderableType:
    # Create ASCII art for "HISTORY"
    history_art = pyfiglet.figlet_format("HISTORY", font="pagga").strip()
    
    # Create the main history content
    main_content = Text.from_markup(
        f"[bold green]{history_art}[/bold green]\n"
        "[bold yellow]The Evolution of Agentic AI Coding Tools[/bold yellow]\n"
        "[dim]From simple CLI hacks to autonomous software engineers[/dim]",
        justify="center"
    )
    
    # Create timeline content as markdown
    timeline_markdown = ''' 
### 2023: Tab Completers / Fill in the middle / Unit test writers!
 - Codeium /Tabnine / Copilot / Starcoder / VS Code Plugins

### Mid 2024: The first agents (Devin making people scared)
 - Devin (smoke in mirrors)
 - First marketed "fully autonomous software engineer" 

### Early 2025: First Real Agentic AI for Software Development
 - Cursor, Windsurf with Cascade (was Codeium), Cline, Claude Code
 - Persistent state, hierarchical planning, mature agentic CLIs / IDEs

### Present: Forks of forks, VC funding anything with a pulse, absolute madness
 - Roo Code, Kilo, Crush, Opencode, Codex CLI, Claude Code, Cursor, Windsurf, Goose
'''

    # Create timeline panel
    timeline_panel = Panel(
        Markdown(timeline_markdown),
        title="[bold cyan]📜 Coding Agent Evolution Timeline[/bold cyan]",
        border_style="white",
        padding=(1, 2)
    )
    
    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=6),
        Layout(timeline_panel, size=23)
    )
    
    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "📜 History of Agentic Coding Tools: Timeline 📜",
        "white"
    )
    
    return final_content
