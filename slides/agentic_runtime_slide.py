import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from utils.common import create_slide_panel
from slides._deck import deck
from spiel import Triggers
from textual.scroll_view import ScrollView
from textual.widgets import Static

# This will be imported by the main deck file

@deck.slide(title="Agentic Runtime")
def agentic_runtime_slide(triggers: Triggers) -> RenderableType:
    # Create ASCII art for "RUNTIME"
    runtime_art = pyfiglet.figlet_format("RUNTIME", font="pagga").strip()
    
    # Create the main runtime content
    main_content = Text.from_markup(
        f"[bold green]{runtime_art}[/bold green]\n"
        "[dim]The orchestration layer that manages reasoning, tool calls, "
        "and task execution. The 'brain' behind intelligent behavior.[/dim]",
        justify="center"
    )
    
    # The complete code broken into lines for progressive reveal
    full_code_lines = [
        '# Pydantic AI: Moo Cow Agent Example',
        'from pydantic_ai import Agent',
        'from typing import Literal',
        'from pydantic import BaseModel'
        '',
        '# Create our Moo Cow agent',
        'moo_cow_agent = Agent(',
        '    \'openai:gpt-4o-mini\',',
        '    system_prompt="You are a friendly cow. Your main purpose is to moo!"',
        ')',
        '',
        '@moo_cow_agent.tool_plain',
        'def moo_tool(num_moos: int, moo_intensity: Literal["soft", "loud"]) -> Dict[str, bool | str]:',
        '    """A tool that makes the cow moo!"""',
        '    if num_moos < 1:',
        '        return {"success": False, "msg": "You have to moo at least once"}',
        '    moo = "MOOOO!!!!!"',
        '    if moo_intensity == "soft":',
        '        moo = "moo..."',
        '    for _ in range(num_moos):',
        '        print(moo)',
        '    return {"success": True, "msg": "great job mooing!"}',
        '',
        '# Run the agent',
        'result = moo_cow_agent.run_sync(',
        '    "Please introduce yourself and use your special ability!"',
        ')',
        'print(result.output)',
        '# Expected output: "Hello! I\'m a friendly cow. Moo! 🐄"'
    ]
    
    # Update moo tool to use Pydantic class
    full_code_lines[15] = 'class Moo(BaseModel):'
    full_code_lines[16] = '    num_moos: conint(gt=0)'
    full_code_lines[17] = '    moo_intensity: Literal["soft", "loud"]'
    full_code_lines[18] = ''
    full_code_lines[20] = '@moo_cow_agent.tool_plain'
    full_code_lines[21] = 'def moo_tool(moo: Moo) -> Dict[str, bool | str]:'
    full_code_lines[22] = '    """A tool that makes the cow moo!"""'
    full_code_lines[23] = '    for _ in range(moo.num_moos):'
    full_code_lines[24] = '        moo_sound = "MOOOO!!!!!" if moo.moo_intensity == "loud" else "moo..."'
    full_code_lines[25] = '        print(moo_sound)'
    full_code_lines[26] = '    return {"success": True, "msg": "great job mooing!"}'
    
    # Remove the Dict import since we're using Pydantic
    full_code_lines[1] = 'from pydantic_ai import Agent'
    full_code_lines[2] = 'from pydantic import BaseModel'
    full_code_lines[3] = 'from typing import Literal'
    
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
    
    # Create explanation sections
    explanation_table = Table(title="", show_header=True, header_style="bold cyan", border_style="white")
    explanation_table.add_column("Component", style="bold yellow", width=25)
    explanation_table.add_column("Purpose", style="", width=80)
    
    explanation_table.add_row(
        "Agent Definition",
        Text.from_markup("[dim]Creates the AI agent with a model and personality. The system prompt defines the agent's character and behavior.[/dim]\n")
    )
    explanation_table.add_row(
        "Tool Registration",
        Text.from_markup("[dim]Registers functions the agent can call. @agent.tool_plain for context-independent tools.[/dim]\n")
    )
    explanation_table.add_row(
        "Execution Flow",
        Text.from_markup("[dim]run_sync() triggers the agent's reasoning loop. Agent decides when and how to use its tools.[/dim]\n")
    )
    explanation_table.add_row(
        "Runtime Management",
        Text.from_markup("[dim]Handles prompt processing, tool selection, response generation, and error handling.[/dim]\n")
    )
    
    # Add simple trigger instructions to the explanation
    if total_lines_to_show < len(full_code_lines):
        explanation_table.add_row(
            "💡 Interactive Feature",
            Text.from_markup("[bold cyan]Press \'t\' to reveal the next line of code![/bold cyan] [dim]Starts with 21 lines, each press shows 1 more line.[/dim]")
        )
    else:
        explanation_table.add_row(
            "🎉 Complete!",
            Text.from_markup("[bold green]All code revealed![/bold green] [dim]Press \'t\' again to restart from the beginning.[/dim]")
        )

    code_panel = Panel.fit(
        Markdown(moo_cow_code),
        title="🐄 Moo Cow Agent Example",
        border_style="white",
        title_align="left"
    )
    
    # Create side-by-side layout for code and explanation
    side_by_side_layout = Layout()
    side_by_side_layout.split_row(
        Layout(code_panel, size=140),
        #Layout(explanation_table, size=70)
    )
    
    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=4),
        Layout(side_by_side_layout, size=25)  # Increased size to accommodate trigger hints
    )
    
    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🤖 The Agentic Runtime: Where Magic Happens 🤖",
        "white"
    )
    
    return final_content