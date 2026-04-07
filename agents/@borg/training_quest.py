"""
Training Quest Generator — Generates a personalized interactive training quest
HTML based on the brainstem's currently loaded agents and features.

On first contact, this agent scans the loaded agents, reads their metadata
and docstrings, and produces a self-contained HTML training quest tailored
to THIS brainstem's specific capabilities.

The quest always includes core brainstem training (auth, soul, models, memory,
agent management) and adds dynamic checkpoints for each loaded agent.

## Usage Examples

1. "Generate my training quest"
   → TrainingQuest action=generate
   → Builds a personalized HTML quest and opens it

2. "Regenerate my training with a custom title"
   → TrainingQuest action=generate, title="HOLO's Training Academy"

3. "What would my training quest cover?"
   → TrainingQuest action=preview
   → Shows the outline without generating the HTML
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@borg/training_quest",
    "version": "1.0.0",
    "display_name": "TrainingQuest",
    "description": "Generates a personalized interactive training quest HTML page based on the brainstem's loaded agents — auto-discovers capabilities and builds a gamified onboarding experience with progress tracking, copy-to-clipboard prompts, and celebrations.",
    "author": "Howard Hoy",
    "tags": ["training", "onboarding", "quest", "html", "interactive", "gamification"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import os
import re
import glob as glob_mod
from datetime import datetime

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent


# Agents to skip in the dynamic section (they're covered in core training)
_CORE_AGENTS = {
    "BasicAgent", "ManageMemory", "ContextMemory", "TrainingQuest",
}

# Category mappings for known agent patterns
_AGENT_CATEGORIES = {
    "research": ["Borg", "DeepBrief", "HackerNews", "Sentinel"],
    "simulation": ["WarRoom", "TinyWorld", "Pipeline"],
    "creation": ["Deliverable", "DemoVideo", "PromptToVideo", "LTXPromptGen", "PersonaFactory"],
    "infrastructure": ["HoloNaming", "Bridge", "Telegram", "RARRemoteAgent", "Portal", "Anvil"],
    "custom": [],  # everything else
}


class TrainingQuestAgent(BasicAgent):
    """Generates a personalized training quest for this brainstem."""

    def __init__(self):
        self.name = "TrainingQuest"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generates a personalized interactive training quest HTML page "
                "based on this brainstem's loaded agents and features. "
                "Call this when the user wants a training guide, onboarding page, "
                "or wants to learn what their brainstem can do. "
                "action=generate builds the HTML; action=preview shows an outline."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["generate", "preview"],
                        "description": "generate = build the HTML training quest; preview = show outline only",
                    },
                    "title": {
                        "type": "string",
                        "description": "Custom title for the training quest (default: 'RAPP Brainstem')",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__()
        # Check if a quest was already generated
        out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "deliverables")
        existing = os.path.join(out_dir, "my-training-quest.html")
        self._quest_generated = os.path.isfile(existing)
        self._quest_path = existing if self._quest_generated else None

    def system_context(self):
        """On first load, tell the LLM to offer generating the training quest."""
        if self._quest_generated:
            return None
        return (
            "\n"
            "IMPORTANT: The TrainingQuest agent is loaded but no training quest has been "
            "generated yet for this user. On your VERY FIRST response to the user — "
            "regardless of what they ask — you MUST mention that a personalized training "
            "quest is available and ask if they'd like you to generate it. Say something like: "
            "'I notice you don\\'t have a training quest yet — I can generate a personalized "
            "interactive training page based on your loaded agents. Want me to create it?' "
            "If they say yes (or anything affirmative), call TrainingQuest with action=generate. "
            "After generation, this message will stop appearing.\n"
            ""
        )

    def _discover_agents(self):
        """Discover loaded agents by scanning the agents directory."""
        agents_dir = os.environ.get("AGENTS_PATH", "")
        if not agents_dir or not os.path.isdir(agents_dir):
            # Try relative to this file
            agents_dir = os.path.dirname(os.path.abspath(__file__))
        if not os.path.isdir(agents_dir):
            return []

        discovered = []
        for fpath in sorted(glob_mod.glob(os.path.join(agents_dir, "*_agent.py"))):
            fname = os.path.basename(fpath)
            if fname == "basic_agent.py":
                continue
            info = self._read_agent_info(fpath, fname)
            if info and info["name"] not in _CORE_AGENTS:
                discovered.append(info)
        return discovered

    def _read_agent_info(self, fpath, fname):
        """Extract agent info from a file without importing it."""
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(8000)
        except OSError:
            return None

        # Extract agent name from self.name = "..."
        name_match = re.search(r'self\.name\s*=\s*["\']([^"\']+)["\']', content)
        agent_name = name_match.group(1) if name_match else fname.replace("_agent.py", "").replace("_", " ").title()

        # Extract description from metadata
        desc_match = re.search(r'"description"\s*:\s*\(\s*"((?:[^"\\]|\\.)*)"\s', content)
        if not desc_match:
            desc_match = re.search(r'"description"\s*:\s*"((?:[^"\\]|\\.)*)"', content)
        description = desc_match.group(1) if desc_match else ""
        description = description.replace('\\"', '"').replace("\\n", " ").strip()
        if len(description) > 200:
            description = description[:197] + "..."

        # Extract docstring examples
        doc_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        docstring = doc_match.group(1) if doc_match else ""
        examples = []
        for line in docstring.splitlines():
            line = line.strip()
            if line.startswith('"') and line.endswith('"'):
                examples.append(line.strip('"'))
            elif "→" in line and line[0].isdigit():
                prompt = line.split('"')
                if len(prompt) >= 2:
                    examples.append(prompt[1])
        examples = examples[:4]  # max 4 examples

        # Extract parameters
        params = []
        prop_matches = re.findall(r'"(\w+)"\s*:\s*\{\s*"type"\s*:\s*"(string|integer|number|boolean)"', content)
        for pname, ptype in prop_matches:
            if pname not in ("type", "name", "description"):
                params.append(pname)

        # Determine category
        category = "custom"
        for cat, members in _AGENT_CATEGORIES.items():
            if agent_name in members:
                category = cat
                break

        return {
            "name": agent_name,
            "filename": fname,
            "description": description,
            "examples": examples,
            "params": params[:5],
            "category": category,
        }

    def _build_agent_checkpoint(self, agent, idx):
        """Build a checkpoint dict for a discovered agent."""
        emojis = {
            "research": "🔬", "simulation": "⚔️", "creation": "🎨",
            "infrastructure": "🔧", "custom": "✨",
        }
        emoji = emojis.get(agent["category"], "✨")

        copies = []
        for ex in agent["examples"]:
            label = ex[:40] + "..." if len(ex) > 40 else ex
            copies.append({"label": label, "text": ex})

        if not copies:
            if agent["params"]:
                copies.append({
                    "label": f"Try {agent['name']}",
                    "text": f"Use the {agent['name']} agent to help me with something"
                })
            copies.append({
                "label": f"What can {agent['name']} do?",
                "text": f"Tell me everything about the {agent['name']} agent — what does it do and how do I use it?"
            })

        desc = agent["description"] if agent["description"] else f"The {agent['name']} agent."
        # Escape single quotes for JS
        desc = desc.replace("'", "\\'").replace("\n", " ")

        return {
            "id": f"agent-{agent['name'].lower().replace(' ', '-')}",
            "emoji": emoji,
            "title": agent["name"],
            "time": "5 min",
            "desc": desc,
            "copies": copies,
            "learn": f"{agent['name']} agent, parameters: {', '.join(agent['params']) if agent['params'] else 'see description'}",
            "toggle": f"Tried {agent['name']} ✓",
            "filename": agent["filename"],
        }

    def _action_preview(self, title="", **kwargs):
        """Show what the training quest would cover."""
        agents = self._discover_agents()
        lines = [
            f"# Training Quest Preview — {title or 'RAPP Brainstem'}",
            "",
            "## Phase 1: 🥚 Hatching (always included)",
            "1. Hatch Your Brainstem — auth setup, start the server",
            "2. First Conversation — open localhost:7071, chat",
            "3. Customize Your Soul — edit soul.md personality",
            "4. Switch Models — try different LLMs at runtime",
            "",
            "## Phase 2: 🧠 Core Skills (always included)",
            "5. Memory System — persistent memory across sessions",
            "6. Meet Your Agents — browse the agent panel in the web UI",
            "",
            f"## Phase 3: ⚡ Your Agents ({len(agents)} discovered)",
        ]
        for i, a in enumerate(agents, 7):
            lines.append(f"{i}. **{a['name']}** — {a['description'][:80]}{'...' if len(a.get('description','')) > 80 else ''}")

        n = 7 + len(agents)
        lines.extend([
            "",
            f"## Phase 4: 🧬 Mastery (always included)",
            f"{n}. Agent Anatomy — understand name, metadata, perform()",
            f"{n+1}. Write an Agent — ask brainstem to create one for you",
            f"{n+2}. Swap & Customize — hot-swap, experimental/, AGENTS_PATH",
            f"{n+3}. Share & Ecosystem — export, import, drag-and-drop, RAR registry",
            "",
            f"**Total: {n+3} checkpoints**",
            "",
            "Run `action=generate` to build the interactive HTML quest.",
        ])
        return "\n".join(lines)

    def _action_generate(self, title="", **kwargs):
        """Generate the full training quest HTML."""
        quest_title = title or "RAPP Brainstem"
        agents = self._discover_agents()

        # Build all checkpoints
        checkpoints = self._build_core_checkpoints()
        agent_cps = [self._build_agent_checkpoint(a, i) for i, a in enumerate(agents)]
        mastery_cps = self._build_mastery_checkpoints()

        # Assign phases
        phase1 = checkpoints["hatching"]       # phase 1
        phase2 = checkpoints["core"]           # phase 2
        phase3 = agent_cps                     # phase 3 (dynamic)
        phase4 = mastery_cps                   # phase 4

        all_cps = []
        for cp in phase1:
            cp["phase"] = 1
            all_cps.append(cp)
        for cp in phase2:
            cp["phase"] = 2
            all_cps.append(cp)
        for cp in phase3:
            cp["phase"] = 3
            all_cps.append(cp)
        for cp in phase4:
            cp["phase"] = 4
            all_cps.append(cp)

        # Generate positions
        positions = self._generate_positions(
            len(phase1), len(phase2), len(phase3), len(phase4)
        )

        # Build HTML
        html = self._render_html(quest_title, all_cps, positions)

        # Save
        out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "deliverables")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "my-training-quest.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        self._quest_generated = True
        self._quest_path = out_path

        # Auto-open in browser
        import webbrowser
        webbrowser.open(f"file://{os.path.abspath(out_path)}")

        total = len(all_cps)
        agent_names = [a["name"] for a in agents]
        return (
            f"## ✅ Training Quest Generated!\n\n"
            f"**File:** `{out_path}`\n\n"
            f"**{total} checkpoints** across 4 phases:\n"
            f"- 🥚 Hatching ({len(phase1)} steps): auth, first chat, soul, models\n"
            f"- 🧠 Core Skills ({len(phase2)} steps): memory, agent panel\n"
            f"- ⚡ Your Agents ({len(phase3)} steps): {', '.join(agent_names[:8])}{'...' if len(agent_names) > 8 else ''}\n"
            f"- 🧬 Mastery ({len(phase4)} steps): create, swap, share agents\n\n"
            f"Open the file in your browser to start the quest!"
        )

    def _build_core_checkpoints(self):
        """Static core checkpoints — always included."""
        hatching = [
            {
                "id": "auth-setup", "emoji": "🥚",
                "title": "Hatch Your Brainstem", "time": "5 min",
                "desc": "Your brainstem needs a GitHub account with Copilot access to come alive. No API keys — just authenticate with GitHub and start the server.",
                "copies": [
                    {"label": "Mac/Linux", "text": "cd rapp_brainstem && ./start.sh"},
                    {"label": "Windows", "text": "cd rapp_brainstem; .\\start.ps1"},
                    {"label": "Direct", "text": "python brainstem.py"},
                ],
                "toggle": "Brainstem is running ✓",
                "stuck": "Run gh auth login first. If you see 'Sign in with GitHub' in the web UI, click it for device-code OAuth. The brainstem auto-detects tokens from gh CLI, GITHUB_TOKEN env var, or .copilot_token file.",
            },
            {
                "id": "first-chat", "emoji": "💬",
                "title": "First Conversation", "time": "3 min",
                "desc": "Open localhost:7071 in your browser. Type anything and see your brainstem respond. It uses your soul.md personality on every turn.",
                "copies": [
                    {"label": "Say hello", "text": "Hello! What can you do?"},
                    {"label": "Test tool calling", "text": "What agents do you have loaded right now?"},
                    {"label": "Test reasoning", "text": "Explain the difference between RAG and fine-tuning in one paragraph"},
                ],
                "toggle": "Had my first conversation ✓",
                "stuck": "Make sure brainstem.py is running (check your terminal). If you see 'unauthenticated', click 'Sign in with GitHub'. The brainstem runs 100% locally — your data never leaves your machine except for the LLM API call.",
            },
            {
                "id": "customize-soul", "emoji": "👻",
                "title": "Customize Your Soul", "time": "5 min",
                "desc": "Edit soul.md to change how your brainstem talks, what it knows, and how it behaves. Changes are live immediately — no restart needed.",
                "copies": [
                    {"label": "Example personality", "text": "You are a senior solutions architect. Speak with precision but use simple analogies. Always consider security, scalability, and cost."},
                ],
                "toggle": "Customized my soul ✓",
                "stuck": "The soul file is at rapp_brainstem/soul.md. Set SOUL_PATH in .env to point elsewhere. Reloads every chat request — no restart needed.",
            },
            {
                "id": "switch-models", "emoji": "🔄",
                "title": "Switch Models", "time": "3 min",
                "desc": "Click the model name in the top-right of the web UI to switch between GPT-4o, Claude, GPT-4.1, and more. No restart needed.",
                "copies": [
                    {"label": "List models", "text": "curl http://localhost:7071/models"},
                    {"label": "Check health", "text": "curl http://localhost:7071/health"},
                ],
                "toggle": "Switched models ✓",
                "stuck": "The model picker is in the top-right corner of the chat UI. Default is gpt-4o from .env GITHUB_MODEL. Falls back automatically if a model fails.",
            },
        ]
        core = [
            {
                "id": "memory-system", "emoji": "🧠",
                "title": "Memory System", "time": "10 min",
                "desc": "Your brainstem has persistent memory. Tell it things about yourself — it remembers across sessions. ManageMemory stores, ContextMemory recalls into every turn.",
                "copies": [
                    {"label": "Store a preference", "text": "Remember that I prefer Python over JavaScript, and I always want type hints in my code"},
                    {"label": "Store project context", "text": "Remember that I'm working on a healthcare AI platform called MediAssist"},
                    {"label": "Test recall", "text": "What do you remember about me?"},
                ],
                "toggle": "Memory is working ✓",
                "stuck": "Memory is stored as JSON in .brainstem_data/. ManageMemory writes when you say 'remember that...'. ContextMemory injects memories into the system prompt every turn via system_context().",
            },
            {
                "id": "browse-agents", "emoji": "🤖",
                "title": "Meet Your Agents", "time": "5 min",
                "desc": "Open localhost:7071 and click the 🤖 icon in the top-right toolbar. This is your agent control panel — browse, export, and delete agents.",
                "copies": [
                    {"label": "List agents", "text": "What agents do you have loaded? Give me a one-line description of each."},
                    {"label": "API check", "text": "curl http://localhost:7071/agents"},
                ],
                "toggle": "I know my agents ✓",
                "stuck": "The agents panel is the 🤖 icon in the top-right toolbar. Agents are *_agent.py files in agents/ (not subfolders). They reload from disk on every chat — no restart needed.",
            },
        ]
        return {"hatching": hatching, "core": core}

    def _build_mastery_checkpoints(self):
        """Static mastery checkpoints — always included."""
        return [
            {
                "id": "agent-anatomy", "emoji": "🔬",
                "title": "Agent Anatomy", "time": "10 min",
                "desc": "Understand the 3 building blocks: name (identity), metadata (what the LLM sees), perform() (what happens when called). Plus optional system_context() for always-on injection.",
                "copies": [
                    {"label": "View BasicAgent", "text": "Show me the BasicAgent base class code"},
                    {"label": "What is system_context?", "text": "Explain system_context() — which agents use it and why?"},
                ],
                "toggle": "I understand agent anatomy ✓",
                "stuck": "Every agent extends BasicAgent. The description in metadata tells the LLM WHEN to call it. perform() must accept **kwargs. Returns a string. Override system_context() to inject text into the system prompt every turn.",
            },
            {
                "id": "write-agent", "emoji": "🛠️",
                "title": "Create an Agent", "time": "10 min",
                "desc": "Just ask your brainstem to create one! Describe what you want in plain English — it writes the .py file and drops it in agents/. Live on the next chat.",
                "copies": [
                    {"label": "Create an agent", "text": "Create me a new agent called QuoteOfTheDay that returns an inspiring quote when I ask for motivation. Save it to the agents folder."},
                    {"label": "Create with params", "text": "Create me a new agent called UnitConverter that converts between metric and imperial units."},
                    {"label": "Iterate", "text": "Change the QuoteOfTheDay agent so it has categories: motivation, humor, philosophy."},
                ],
                "toggle": "Created an agent ✓",
                "stuck": "Just describe the agent you want in chat. Your brainstem knows the BasicAgent pattern. Key rules: file named *_agent.py, class extends BasicAgent, perform() accepts **kwargs, returns a string. Auto-installs missing pip packages.",
            },
            {
                "id": "swap-agents", "emoji": "🔄",
                "title": "Swap & Customize", "time": "5 min",
                "desc": "Hot-swap agents via the web UI: click 🤖 in the toolbar, 🗑️ to delete, ↓ to export. Move files to agents/experimental/ to disable without deleting.",
                "copies": [
                    {"label": "List loaded", "text": "curl http://localhost:7071/agents"},
                    {"label": "Ask brainstem", "text": "How many agents do you have loaded right now?"},
                ],
                "toggle": "Swapped agents ✓",
                "stuck": "agents/experimental/ is excluded from auto-loading. Set AGENTS_PATH in .env for per-project agent sets. Agents reload from disk on every chat request.",
            },
            {
                "id": "share-agents", "emoji": "🤝",
                "title": "Share & Ecosystem", "time": "5 min",
                "desc": "Drag a .py file onto the chat page at localhost:7071 to import. Click ↓ to export. Agents are self-contained Python — share via email, Slack, or git.",
                "copies": [
                    {"label": "Export", "text": "curl http://localhost:7071/agents/export/deep_brief_agent.py -o deep_brief_agent.py"},
                    {"label": "Import", "text": "curl -X POST http://localhost:7071/agents/import -F \"file=@my_agent.py\""},
                    {"label": "RAR registry", "text": "What agents are available in the RAR registry?"},
                ],
                "toggle": "Training quest complete 🏆",
                "stuck": "The agents panel (🤖 icon, top-right) has ↓ export and 🗑️ delete buttons. Drag .py files onto the page to import. The RARRemoteAgent connects to the community RAPP Agent Registry.",
            },
        ]

    def _generate_positions(self, n1, n2, n3, n4):
        """Generate non-overlapping node positions using proportional columns."""
        total = n1 + n2 + n3 + n4
        counts = [n1, n2, n3, n4]

        # Give each phase proportional width (minimum 15% each)
        weights = [max(c, 2) for c in counts]
        total_w = sum(weights)
        widths = [w / total_w * 100 for w in weights]

        # Ensure minimum width
        for i in range(4):
            if widths[i] < 15:
                deficit = 15 - widths[i]
                widths[i] = 15
                # Steal from the largest
                largest = widths.index(max(widths))
                widths[largest] -= deficit

        # Build column boundaries
        boundaries = []
        x = 0
        for w in widths:
            boundaries.append((x + 2, x + w - 2))  # 2% padding each side
            x += w

        positions = []
        for phase_idx, count in enumerate(counts):
            x_min, x_max = boundaries[phase_idx]
            x_mid = (x_min + x_max) / 2
            x_swing = (x_max - x_min) * 0.35  # how far nodes swing left/right

            # Distribute nodes vertically with even spacing
            if count <= 1:
                y_positions = [50]
            else:
                # Space nodes evenly from top to bottom, with margin
                y_top = 16
                y_bottom = 82
                step = (y_bottom - y_top) / (count - 1) if count > 1 else 0
                y_positions = [y_top + i * step for i in range(count)]

            for i, y in enumerate(y_positions):
                # Alternate left/right of center for winding effect
                if i % 2 == 0:
                    x = x_mid - x_swing
                else:
                    x = x_mid + x_swing
                positions.append({"x": round(x, 1), "y": round(y, 1)})

        return positions

    def _render_html(self, title, checkpoints, positions):
        """Render the complete HTML training quest."""
        # Convert checkpoints to JS
        js_cps = []
        for cp in checkpoints:
            obj = {
                "id": cp["id"],
                "phase": cp["phase"],
                "emoji": cp["emoji"],
                "title": cp["title"],
                "time": cp.get("time", "5 min"),
                "desc": cp["desc"],
                "toggle": cp.get("toggle", "Done ✓"),
            }
            if cp.get("copies"):
                obj["copies"] = cp["copies"]
            if cp.get("copyText"):
                obj["copyText"] = cp["copyText"]
                obj["copyLabel"] = cp.get("copyLabel", "Copy")
            if cp.get("substeps"):
                obj["substeps"] = cp["substeps"]
            if cp.get("stuck"):
                obj["stuck"] = cp["stuck"]
            if cp.get("learn"):
                obj["learn"] = cp["learn"]
            js_cps.append(obj)

        cp_json = json.dumps(js_cps, indent=2)
        pos_json = json.dumps(positions, indent=2)
        total = len(checkpoints)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Compute proportional phase widths for CSS
        counts = [0, 0, 0, 0]
        for cp in checkpoints:
            counts[cp["phase"] - 1] += 1
        weights = [max(c, 2) for c in counts]
        total_w = sum(weights)
        widths = [w / total_w * 100 for w in weights]
        for i in range(4):
            if widths[i] < 15:
                deficit = 15 - widths[i]
                widths[i] = 15
                largest = widths.index(max(widths))
                widths[largest] -= deficit

        # Phase label positions (centered in each column)
        label_positions = []
        x = 0
        for w in widths:
            label_positions.append(round(x + 1, 1))
            x += w
        # Divider positions (between columns)
        dividers = []
        x = 0
        for i, w in enumerate(widths[:-1]):
            x += w
            dividers.append(round(x, 1))

        return f"""









  {title} — Training Quest
  0 of {total}
  Reset Progress

🥚 Hatching
🧠 Core Skills
⚡ Your Agents
🧬 Mastery



<h2></h2>✕
<h1>🧬 Training Complete!</h1><p>You've mastered your brainstem.<br>Your rappter is fully grown.</p>
{title} — Training Quest · Generated {timestamp}


"""

    def perform(self, action="generate", title="", **kwargs):
        if action == "preview":
            return self._action_preview(title=title)
        return self._action_generate(title=title)
