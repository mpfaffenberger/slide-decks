
import pyfiglet
from pathlib import Path
from PIL import Image as Img
from PIL.Image import Resampling
from rich.console import RenderableType
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from spiel.renderables.image import Image
from rich.panel import Panel

# Keep the resize function in shared utilities
def resize(image_path: Path, size: tuple[int, int]) -> Path:
    """Resize image and replace transparent pixels with terminal background, return path to processed image."""
    # Load and process image
    img = Img.open(image_path)
    img_rgba = img.convert('RGB')
    resized = img_rgba.resize(size, Resampling.LANCZOS)

    # Replace transparent pixels with terminal background (RGB 30,30,30)
    datas = resized.getdata()
    new_data = []
    for item in datas:
        if item[0] < 30 and item[1] < 30 and item[2] < 30:
            new_data.append((30, 30, 30))
        else:
            new_data.append(item)

    resized.putdata(new_data)

    # Save processed image
    output_path = image_path.parent / f"{image_path.stem}_{size[0]}x{size[1]}_matched.png"
    resized.save(output_path)
    return output_path

    # Save processed image
    output_path = image_path.parent / f"{image_path.stem}_{size[0]}x{size[1]}_matched.png"
    resized.save(output_path)
    return output_path

def create_slide_panel(content: RenderableType, title: str, border_style: str = "green") -> Panel:
    """Create a standardized panel for slides."""
    return Panel(
        content,
        title=f"[bold green]{title}[/bold green]",
        border_style=border_style,
        padding=(1, 2)
    )