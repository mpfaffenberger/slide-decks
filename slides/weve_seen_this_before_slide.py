from rich.console import RenderableType
from rich.align import Align
from slides._deck import deck
from spiel import Triggers
from spiel.renderables.image import Image





@deck.slide(title="we've seen this before...")
def weve_seen_this_before_slide(triggers: Triggers) -> RenderableType:
    # Load both images
    xkcd1 = Image.from_file("images/xkcd4.png")
    xkcd2 = Image.from_file("images/xkcd3.png")
    
    # Choose which image to display based on trigger count
    # Each 't' press toggles between images
    current_image = xkcd1 if len(triggers) % 2 == 0 else xkcd2
    
    # Center the image
    return Align.center(current_image, vertical="middle")