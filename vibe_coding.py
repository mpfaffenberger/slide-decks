from spiel import Deck, present
from slides.title_slide import create_title_slide
from slides.about_me_slide import create_about_me_slide
from slides.agentic_ai_slide import create_agentic_ai_slide

# Create the deck
deck = Deck(name="Vibe Coding: Is It Right For Data Science?")

# Import all slides (order matters!)
create_title_slide(deck)
create_about_me_slide(deck)
create_agentic_ai_slide(deck)

# Presentation entry point
if __name__ == "__main__":
    present(__file__)