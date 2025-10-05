from spiel import present
from slides._deck import deck

from slides import title_slide
from slides import about_me_slide
from slides import table_of_contents
from slides import agentic_ai_slide
from slides import agent_architecture_slide
from slides import agentic_runtime_slide
from slides import history_of_coding_agents_slide
from slides import enshittification_slide
from slides import vc_leverage_slide
from slides import open_source_betrayal_slide
from slides import privacy_future_slide
from slides import code_puppy_intro_slide
from slides import llxprt_alternative_slide
from slides import code_puppy_slide
from slides import code_puppy_tools_slide
from slides import code_puppy_brains_slide


# Presentation entry point
if __name__ == "__main__":
    present(__file__)