import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.markdown import Markdown
from utils.common import create_slide_panel
from slides._deck import deck
from spiel import Triggers

@deck.slide(title="Meet Code Puppy")
def code_puppy_slide(triggers: Triggers) -> RenderableType:
    # Create ASCII art for "CODE PUPPY"
    code_puppy_art = pyfiglet.figlet_format("CODE PUPPY", font="pagga").strip()
    
    # Create the main Code Puppy content
    main_content = Text.from_markup(
        f"[bold green]{code_puppy_art}[/bold green]\n"
        "[dim]Born on a rainy weekend in May 2025, when Windsurf & Cursor started degrading...[/dim]",
        justify="center"
    )

    # Create the "Why I built Code Puppy" markdown content
    reasons_markdown = '''## 🔴 Why I Built Code Puppy
### 🌪️ **Windsurf Cascade Issues**
- Limited Auto Execution (20 steps)
- Only one copy allowed - no multi-boxing!
- Can't run 5 or 10 agents simultaneously
### 🔒 **SDK Limitations**  
- Couldn't invoke Windsurf/Cursor at SDK level
- No microservice deployment capability
### 📉 **Performance Degradation**
- Models responding more slowly
- Tool call failures increased dramatically
- During the week before creation: barely usable!
- Models disappearing, getting pulled / increasing in cost 
'''

    # Create markdown panel
    reasons_panel = Panel(
        Markdown(reasons_markdown),
        title="[bold red]The Problems[/bold red]",
        border_style="white",
        padding=(0, 1)
    )


    # Create the "About Code Puppy" markdown content
    features_markdown = '''## 🟢 About Code Puppy

### 💻 **Command-Line First**
- Fully CLI-driven - no graphical UI
- "We don't need IDEs anymore"

### ⚖️ **Lightweight Architecture**
- Same code generation capabilities as mainstream tools
- Written in pure Python

### 🔬 **Pydantic AI Powered**
- Battle-tested - huge community support
- Production-ready agent patterns

### 🧠 **Privacy First**
 - Fully open source
 - Absolutely NO telemetry
'''

    # Create markdown panel
    features_panel = Panel(
        Markdown(features_markdown),
        title="[bold green]The Solution[/bold green]",
        border_style="white",
        padding=(0, 1)
    )

    # Create side-by-side layout for problems and solutions
    comparison_layout = Layout()
    comparison_layout.split_row(
        Layout(reasons_panel, size=70),
        Layout(features_panel, size=70)
    )
    
    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=4),
        Layout(comparison_layout, size=25)
    )
    
    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🐕 Meet Code Puppy: Open Source Alternative 🐕",
        "white"
    )
    
    return final_content