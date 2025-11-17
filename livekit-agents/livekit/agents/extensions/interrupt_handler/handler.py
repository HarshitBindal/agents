import os

IGNORED_WORDS = os.getenv("IGNORED_WORDS", "uh,umm,hmm,uhmm,uhm,haan,huh").split(",")

class InterruptHandler:
    def __init__(self):
        self.agent_speaking = False

    def update_agent_state(self, is_speaking: bool):
        self.agent_speaking = is_speaking

    def process_user_input(self, text: str):
        words = text.lower().strip().split()

        only_filler = all(w in IGNORED_WORDS for w in words)

        if self.agent_speaking:
            if only_filler:
                return "IGNORED"
            else:
                return "STOP_AGENT"
        else:
            return "NORMAL_INPUT"
