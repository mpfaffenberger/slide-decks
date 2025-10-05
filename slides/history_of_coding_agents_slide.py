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
    timeline_markdown = '''📅 **Late 2022 → Early 2023: The Dawn**
**Tools:** Aider (pre-1.0), early GPT-3.5 Turbo CLI hacks
**Innovation:** First accessible CLI agents with persistent context + Git autonomy

**Q2 2023: Mainstream IDE Integration**
**Tools:** Cursor w/ inline chat (not agentic)
**Innovation:** Project-wide semantic context + "edit this code with ctrl+k"

**Mid-Late 2023: Tab Completers / whispers of agents **
**Tools:** Devin (Smoke in Mirrors), Codeium / Tabnine

**Early 2024: Getting more advanced! **
**Tools:** Claude Code, Cursor 1.0 beta, Aider v0.50+
**Innovation:** Planning, validation steps, embedded mini-agents (BugBot)

**Mid 2024**: The first agents (Devin making people scared)**
**Tools:** Devin (still smoke in mirrors)
**Innovation:** First marketed "fully autonomous software engineer" - multi-agent orchestration

**Late 2024 → 2025: First Real Agentic AI for Software Development**
**Tools:** Cursor, Windsurf with Cascade (was Codeium), Cline, Claude Code
**Innovation:** Persistent state, hierarchical planning, mature agentic CLIs / IDEs

**Present**: Forks of forks, VC funding anything with a pulse, absolute madness
**Tools:** Roo Code, Kilo, Crush, Opencode, Codex CLI, Claude Code, Cursor, Windsurf, Goose
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
