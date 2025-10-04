
import pyfiglet
from pathlib import Path
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from utils.common import create_slide_panel, resize
from slides._deck import deck
from spiel import Triggers
from spiel.renderables.image import Image
from textual.scroll_view import ScrollView
from textual.widgets import Static
@deck.slide(title="Agentic Runtime")
def agentic_runtime_slide(triggers: Triggers) -> RenderableType:
    # Create ASCII art for "RUNTIME"
    runtime_art = pyfiglet.figlet_format("Pydantic AI", font="pagga").strip()
    
    # Create the main runtime content
    main_content = Text.from_markup(
        f"[bold green]{runtime_art}[/bold green]\n"
        "[dim]The orchestration layer that manages reasoning, tool calls, "
        "and task execution. The 'brain' behind intelligent behavior.[/dim]\n",
        justify="center"
    )
    
    # The complete code as a single multiline string
    full_code = '''# Pydantic AI: Moo Cow Agent Example
from pydantic_ai import Agent
from pydantic import BaseModel, Field
from typing import Literal
from pydantic.types import conint

# Create our Moo Cow agent
moo_cow_agent = Agent(
    'openai:gpt-4o-mini',
    system_prompt="You are a friendly cow. Your main purpose is to moo!"
)

class Moo(BaseModel):
    num_moos: conint(gt=0) = Field(..., description="Number of times to moo")
    moo_intensity: Literal["soft", "loud"] = Field(default="loud", description="How loud to moo")

class MooResult(BaseModel):
    success: bool = Field(..., description="Whether the moo operation was successful")
    msg: str = Field(..., description="Message about the moo operation")
    total_moos: int = Field(..., description="Total number of moos performed")

@moo_cow_agent.tool_plain
def moo_tool(moo: Moo) -> MooResult:
    """A tool that makes the cow moo!"""
    for _ in range(moo.num_moos):
        moo_sound = "MOOOO!!!!!" if moo.moo_intensity == "loud" else "moo..."
        print(moo_sound)
    
    return MooResult(
        success=True,
        msg=f"Great job mooing {moo.num_moos} times with {moo.moo_intensity} intensity!",
        total_moos=moo.num_moos
    )

# Run the agent
result = moo_cow_agent.run_sync(
    "Please introduce yourself and use your special ability!"
)
print(result.output)
# Expected output: "Hello! I'm a friendly cow. Moo! 🐄"'''
    
    full_code_lines = full_code.split('\n')
    
    # Calculate how many lines to show based on trigger count
    # Start with 21 lines, each 't' press adds 1 more line
    trigger_count = len(triggers)
    lines_per_trigger = 1  # Show 1 new line per trigger
    total_lines_to_show = min(len(full_code_lines), 21 + trigger_count * lines_per_trigger)
    
    # Implement sliding window: max 21 lines visible at once
    max_visible_lines = 21
    
    if total_lines_to_show > max_visible_lines:
        # Show sliding window of last 21 lines
        start_line = total_lines_to_show - max_visible_lines
        visible_lines = full_code_lines[start_line:total_lines_to_show]
        visible_code = '```python\n' + '\n'.join(visible_lines) + '\n```'
    else:
        # Show from beginning, no clipping needed
        visible_lines = full_code_lines[:total_lines_to_show]
        visible_code = '```python\n' + '\n'.join(visible_lines) + '\n```'
    
    moo_cow_code = visible_code
    
    # Process moo cow image on the fly
    moo_cow_path = resize(Path("images/moo-cow.png"), (64, 64))
    
    # Load processed image using Spiel's native Image widget
    pixelated_moo_cow = Image.from_file(str(moo_cow_path))

    code_panel = Panel.fit(
        Markdown(moo_cow_code),
        title="🐄 Moo Cow Agent Example",
        border_style="white",
        title_align="left"
    )
    
    # Create side-by-side layout for code and explanation
    side_by_side_layout = Layout()
    side_by_side_layout.split_row(
        Layout(code_panel, size=100),
        Align.center(Layout(pixelated_moo_cow, size=25))
    )
    
    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=5),
        Layout(side_by_side_layout, size=24)  # Increased size to accommodate trigger hints
    )
    
    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🤖 The Agentic Runtime: Where Magic Happens 🤖",
        "white"
    )
    
    return final_content