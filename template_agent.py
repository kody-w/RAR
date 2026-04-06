"""
YOUR AGENT NAME — Describe what your agent does in one sentence.

╔══════════════════════════════════════════════════════════════╗
║  RAPP AGENT TEMPLATE                                        ║
║                                                              ║
║  How to use:                                                 ║
║  1. Give this file to any LLM (ChatGPT, Copilot, Claude)    ║
║  2. Tell it what you want your agent to do                   ║
║  3. It fills in the blanks and writes the perform() logic    ║
║  4. Save the result as  your_agent_name_agent.py             ║
║  5. Submit at  https://kody-w.github.io/RAR/submit.html     ║
║                                                              ║
║  Rules:                                                      ║
║  - One file. Everything goes here. No extra files.           ║
║  - File name MUST end with _agent.py                         ║
║  - snake_case everywhere (no dashes)                         ║
║  - perform() MUST return a string                            ║
║  - No network calls in __init__()                            ║
║  - No hardcoded secrets — use os.environ.get()               ║
╚══════════════════════════════════════════════════════════════╝

Example prompt for your LLM:

  "Using this template, build me an agent that [YOUR IDEA HERE].
   Fill in the manifest, write the perform() method, and make
   sure it returns a string. Keep it in one file."
"""

import os

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",

    # CHANGE THESE — replace @your_username with your GitHub username
    "name": "@your_username/your_agent_name",
    "version": "1.0.0",
    "display_name": "Your Agent Name",
    "description": "What your agent does in one sentence.",
    "author": "Your Name",

    # Tags help people find your agent — pick 2-5 keywords
    "tags": ["keyword1", "keyword2"],

    # Pick ONE category:
    #   core, pipeline, integrations, productivity, devtools,
    #   b2b_sales, b2c_sales, energy, federal_government,
    #   financial_services, general, healthcare, human_resources,
    #   it_management, manufacturing, professional_services,
    #   retail_cpg, slg_government, software_digital_products
    "category": "general",

    "quality_tier": "community",

    # List any environment variables your agent needs (empty = none)
    # Example: ["OPENAI_API_KEY", "MY_API_TOKEN"]
    "requires_env": [],

    # Don't change this — every agent depends on BasicAgent
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


# This import lets your agent run inside the RAPP ecosystem
try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    # Fallback so the file also runs standalone: python your_agent_name_agent.py
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class YourAgentName(BasicAgent):
    """
    RENAME this class to match your display_name (no spaces).
    Example: display_name "Weather Checker" → class WeatherChecker
    """

    def __init__(self):
        # This MUST match the display_name in __manifest__
        super().__init__(__manifest__["display_name"], {})

        # Set up any state your agent needs (no network calls here)
        # Example:
        # self.default_city = "Seattle"

    def perform(self, **kwargs):
        """
        This is where your agent does its work.

        - kwargs contains whatever the caller passes in
        - MUST return a string (never None, never a dict)
        - Handle errors gracefully — return an error message, don't crash
        - If you need an API key, get it from os.environ.get()

        Example kwargs your agent might accept:
            query = kwargs.get("query", "")
            user_id = kwargs.get("user_guid", "")
        """

        # ──────────────────────────────────────────────
        # YOUR LOGIC GOES HERE
        #
        # Delete this placeholder and write your agent's
        # actual behavior. Must return a string.
        # ──────────────────────────────────────────────

        # Example: check for required env var
        # api_key = os.environ.get("MY_API_KEY")
        # if not api_key:
        #     return "Error: MY_API_KEY not set in environment."

        return "Hello from your new agent! Replace this with real logic."


# This lets you test your agent locally: python your_agent_name_agent.py
if __name__ == "__main__":
    agent = YourAgentName()
    result = agent.perform()
    print(result)
