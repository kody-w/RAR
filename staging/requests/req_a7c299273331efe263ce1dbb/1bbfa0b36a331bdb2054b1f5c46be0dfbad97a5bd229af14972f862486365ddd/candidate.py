"""FirstHour: your first hour with your Brainstem, as one agent.

Drag this file onto your Brainstem window and click OK. Then say: teach me my first hour.
It is one file that does one job, like every agent. Read it: the six steps are below, in plain words.

Your AI, as files you own.
1. Learn it in an hour. It thinks the way you do, so you can see how it works.
2. Run it on any computer. Mac, Windows or Linux. Its memory stays in your own folder.
3. Hand it to anyone. It is just files. One agent is one file.
"""
try:
    from agents.basic_agent import BasicAgent
except ImportError:  # outside a Brainstem, for example the registry's own tests
    from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/first_hour_agent",
    "version": "1.0.0",
    "display_name": "FirstHour",
    "description": "Walks you through your first hour with your Brainstem, one step at a time.",
    "author": "@kody-w",
    "tags": ["first-hour", "learn", "getting-started"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

STEPS = [
    ("Get your Brainstem.",
     "You already did: you are talking to it. It runs while its Terminal window is open. "
     "Paste the install line again any time to bring it back, memory and all."),
    ("Talk to it.",
     "Tell me one thing to remember about you, like your favorite coffee. "
     "Tomorrow, ask me what I remember. My memory is a file in your Brainstem's folder."),
    ("See what it can do.",
     "Click the circled plus at the top right (it says Manage installed agents when you point at it). "
     "Each one listed is an agent: one file that does one job. I am one of them: FirstHour."),
    ("Read an agent.",
     "Click Export next to ManageMemory. Your browser saves a small file, usually in Downloads. "
     "Drag it into a chat with any AI and ask: Explain this in plain words. "
     "It is a short program for one job: saving what you ask me to remember."),
    ("Make your own.",
     "In that same chat, ask for a new agent just like it, for a chore you repeat, as a file you can download. "
     "Drag that file onto this window and click OK when it asks. I use it on your next message. "
     "If it says the agent did not load, paste that message into the chat and ask for a fix."),
    ("Hand it on.",
     "Export your new agent and send the file to a friend. They drag it onto their Brainstem and it works "
     "the same way. Or share it in the registry: https://github.com/kody-w/RAR"),
]


class FirstHourAgent(BasicAgent):
    def __init__(self):
        self.name = "FirstHour"
        self.metadata = {
            "name": self.name,
            "description": (
                "Walks someone through their first hour with their Brainstem, one step at a time. "
                "Call it when they ask to learn, get started, take the tour, or want the next step. "
                "Give the step back in your own short words and end by offering the next step."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "step": {"type": "integer", "description": "Which step, 1 to 6. Use 1 to start.",
                             "minimum": 1, "maximum": 6}
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, step=1, **kwargs):
        try:
            step = max(1, min(len(STEPS), int(step)))
        except (TypeError, ValueError):
            step = 1
        title, text = STEPS[step - 1]
        after = (f" When you are ready, say next for step {step + 1} of {len(STEPS)}."
                 if step < len(STEPS) else
                 " That is the hour. Tomorrow I am still here, on your computer, remembering. "
                 "Your AI, as files you own.")
        return f"Step {step} of {len(STEPS)}: {title} {text}{after}"
