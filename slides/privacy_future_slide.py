import pyfiglet
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from utils.common import create_slide_panel
from slides._deck import deck

@deck.slide(title="Privacy & The Future of Local AI")
def privacy_future_slide() -> RenderableType:
    # Create ASCII art for "PRIVACY"
    privacy_art = pyfiglet.figlet_format("PRIVACY & THE FUTURE", font="pagga").strip()
    
    # Main title
    main_content = Text.from_markup(
        f"[bold green]{privacy_art}[/bold green]\n\n"
        "[bold yellow]Data Control and Local Model Horizons[/bold yellow]\n\n"
        "[dim]From cloud dependence to hardware sovereignty[/dim]",
        justify="center"
    )

    # Create the data flow table
    data_table = Table(title="", show_header=True, box=None, padding=(0, 1))
    data_table.add_column("Approach", style="bold cyan", width=25)
    data_table.add_column("Data Flow", style="", width=70)
    data_table.add_column("Privacy Level", style="bold", width=15)

    # Add data flow scenarios
    data_scenarios = [
        ("[red]Wrapper Services[/red]",
         "Your code → Wrapper → Foundation Model", 
         "[red]Double Exposure[/red]"),
        ("[yellow]Direct Access[/yellow]",
         "Your code → Claude Code/Codex CLI → Anthropic/OpenAI",
         "[yellow]Single Exposure[/yellow]"),
        ("[yellow]Direct Access[/yellow]",
         "Your code → Your agent → Foundation Model",
         "[yellow]Single Exposure[/yellow]"),
        ("[blue]Privately Hosted Models[/blue]",
         "Your code → Your agent → Your hardware",
         "[green]Full Privacy[/green]"),
    ]

    for approach, data_flow, privacy in data_scenarios:
        data_table.add_row(
            Text.from_markup(approach),
            Text.from_markup(data_flow),
            Text.from_markup(privacy)
        )

    # Create the hardware reality section
    hardware_section = Text.from_markup(
        "\n[bold red]🔧 Hardware Reality Check 🔧[/bold red]\n\n"
        "[yellow]• Current Challenge:[/yellow] Consumer GPUs can't run GLM 4.6 or Qwen3 Coder 480b\n"
        "[yellow]• My Setup:[/yellow] Frame.Work AI 395 Max, 128GB shared memory, 225 gb/s memory bandwidth :(\n"
        "[yellow]• Limitation:[/yellow] Memory bandwidth too low for large models\n"
        "[yellow]• Rule of Thumb:[/yellow] Bandwidth (GB/s) ÷ Model Size (GB) ≈ Tokens/sec\n"
        "[yellow]• MOE Advantage:[/yellow] Mixture of Experts use fewer parameters per inference",
        justify="left"
    )

    # Create the China/VC disruption section
    disruption_section = Text.from_markup(
        "\n[bold yellow]🌏 Open Source LLM to The Rescue 🌏[/bold yellow]\n\n"
        "[green]• Distillation Masters:[/green] DeepSeek, Z.AI, Mistral, Qwen etc.\n"
        "[green]• Price Advantage:[/green] Z.AI - 1/10th the cost of Anthropic models\n",
        justify="left"
    )

    # Create the vision section
    vision_section = Text.from_markup(
        "\n[bold green]🚀 The Vision 🚀[/bold green]\n"
        "[cyan]Today:[/cyan] Best models from OpenAI/Anthropic (cloud-dependent)\n"
        "[cyan]Tomorrow:[/cyan] Fully open source models + private hardware\n"
        "[cyan]Tough Goal:[/cyan] Bypass foundation model providers entirely, get us as close to the GPUs as possible!\n"        
        "[cyan]Should we pool our resources?:[/cyan] Collective of consumers buying enterprise hardware just to keep our data safe? \n"
        "[cyan]Result:[/cyan] True privacy + cost control + no API limits",
        justify="center"
    )

    # Combine everything in a layout
    layout = Layout()
    layout.split_column(
        Layout(Align.center(main_content), size=6),
        Layout(Align.center(data_table), size=5),
        Layout(Align.left(hardware_section), size=6),
        Layout(Align.left(disruption_section), size=6),
        Layout(Align.center(vision_section), size=9)
    )

    # Wrap in a panel for consistency
    final_content = create_slide_panel(
        layout,
        "🔒 Privacy-Focused AI Future 🔒",
        "white"
    )

    return final_content