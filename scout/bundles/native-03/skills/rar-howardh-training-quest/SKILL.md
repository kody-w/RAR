---
name: "rar-howardh-training-quest"
description: "Generates a personalized interactive training quest HTML page based on this brainstem's loaded agents and features. Call this when the user wants a training guide, onboarding page, or wants to learn what their brainstem can do. action=generate builds the HTML; action=preview shows an outline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/training_quest_agent", "rar_sha256": "a583ada09fa44f0d3d88962fea0826ae5877a09dd8639c908e6325c04cc0c36c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Howard Hoy", "tags": ["training", "onboarding", "quest", "html", "interactive", "gamification"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/training_quest_agent`. The original RAPP
agent is preserved byte-for-byte in `training_quest_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "generate = build the HTML training quest; preview = show outline only",
      "enum": [
        "generate",
        "preview"
      ],
      "type": "string"
    },
    "title": {
      "description": "Custom title for the training quest (default: 'RAPP Brainstem')",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `training_quest_agent.py` and embedded as the fenced Python below (sha256 a583ada09fa44f0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `training_quest_agent.py` first:

```bash
python3 training_quest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 training_quest_agent.py   # or on stdin
python3 training_quest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/training_quest_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/training_quest_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/training_quest_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
    "name": "@howardh/training_quest_agent",
    "version": "1.0.1",
    "display_name": "TrainingQuest",
    "description": "Generates a gamified HTML onboarding quest from the brainstem's loaded agents, with checkpoints, progress tracking, and copyable prompts.",
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
            "<TrainingQuest>\n"
            "IMPORTANT: The TrainingQuest agent is loaded but no training quest has been "
            "generated yet for this user. On your VERY FIRST response to the user — "
            "regardless of what they ask — you MUST mention that a personalized training "
            "quest is available and ask if they'd like you to generate it. Say something like: "
            "'I notice you don\\'t have a training quest yet — I can generate a personalized "
            "interactive training page based on your loaded agents. Want me to create it?' "
            "If they say yes (or anything affirmative), call TrainingQuest with action=generate. "
            "After generation, this message will stop appearing.\n"
            "</TrainingQuest>"
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

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Training Quest</title>
<style>
  *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
  :root{{--bg:#eaecf0;--bg2:#f4f5f7;--blue:#0969da;--green:#1a7f37;--orange:#bf8700;--red:#cf222e;--text:#24292f;--text-muted:#57606a;--border:#c5ccd6;--panel-w:460px;--top-bar:52px}}
  html,body{{height:100%;overflow:hidden;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:linear-gradient(135deg,#dfe2e6 0%,var(--bg) 100%);color:var(--text)}}
  .top-bar{{position:fixed;top:0;left:0;right:0;height:var(--top-bar);background:rgba(234,236,240,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 24px;z-index:100}}
  .top-bar .title{{font-size:15px;font-weight:600;white-space:nowrap}}.top-bar .title span{{color:var(--blue)}}
  .progress-wrap{{flex:1;max-width:420px;margin:0 auto;display:flex;align-items:center;gap:10px}}
  .progress-track{{flex:1;height:8px;background:var(--border);border-radius:4px;overflow:hidden}}
  .progress-fill{{height:100%;background:linear-gradient(90deg,var(--blue),var(--green));border-radius:4px;transition:width .6s cubic-bezier(.4,0,.2,1)}}
  .progress-label{{font-size:13px;color:var(--text-muted);min-width:90px;text-align:right}}
  .btn-reset{{background:transparent;border:1px solid var(--border);color:var(--text-muted);padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px;white-space:nowrap;transition:all .2s}}.btn-reset:hover{{border-color:var(--red);color:var(--red)}}
  .quest-map{{position:fixed;top:var(--top-bar);left:0;right:0;bottom:0;overflow:hidden}}
  .quest-map svg.path-svg{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}
  .phase-label{{position:absolute;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:3px;color:var(--text-muted);opacity:.55;pointer-events:none}}
  .phase-label.p1{{top:82px;left:{label_positions[0]}%}}.phase-label.p2{{top:82px;left:{label_positions[1]}%}}.phase-label.p3{{top:82px;left:{label_positions[2]}%}}.phase-label.p4{{top:82px;left:{label_positions[3]}%}}
  .phase-divider{{position:absolute;top:var(--top-bar);bottom:0;width:1px;background:linear-gradient(to bottom,transparent,var(--border) 15%,var(--border) 85%,transparent);opacity:.6;pointer-events:none}}
  .phase-divider.d1{{left:{dividers[0]}%}}.phase-divider.d2{{left:{dividers[1]}%}}.phase-divider.d3{{left:{dividers[2]}%}}
  .node{{position:absolute;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .35s cubic-bezier(.4,0,.2,1);z-index:10;transform:translate(-50%,-50%)}}
  .node .ring{{position:absolute;inset:-4px;border-radius:50%;border:2px solid var(--border);transition:all .35s}}
  .node .inner{{width:100%;height:100%;border-radius:50%;background:#f0f1f3;display:flex;align-items:center;justify-content:center;font-size:22px;position:relative;z-index:1;transition:all .35s;border:2px solid var(--border)}}
  .node.active .ring{{border-color:var(--blue);box-shadow:0 0 20px rgba(88,166,255,.35);animation:pulse-ring 2s infinite}}
  .node.active .inner{{border-color:var(--blue);background:rgba(88,166,255,.1);transform:scale(1.12)}}.node.active .lock{{display:none}}
  .node.complete .ring{{border-color:var(--green);box-shadow:0 0 12px rgba(63,185,80,.25)}}
  .node.complete .inner{{border-color:var(--green);background:rgba(63,185,80,.15)}}.node.complete .lock{{display:none}}
  .node:hover{{transform:translate(-50%,-50%) scale(1.1)}}
  .node .label{{position:absolute;top:calc(100% + 10px);white-space:nowrap;font-size:11px;font-weight:600;color:var(--text-muted);text-align:center;pointer-events:none;transition:color .3s}}
  .node.active .label{{color:var(--blue)}}.node.complete .label{{color:var(--green)}}
  @keyframes pulse-ring{{0%,100%{{box-shadow:0 0 20px rgba(88,166,255,.25)}}50%{{box-shadow:0 0 32px rgba(88,166,255,.5)}}}}
  .check-icon{{display:none}}.node.complete .check-icon{{display:block}}.node.complete .emoji{{display:none}}
  .overlay{{position:fixed;inset:0;background:rgba(0,0,0,.2);z-index:200;opacity:0;pointer-events:none;transition:opacity .3s}}.overlay.open{{opacity:1;pointer-events:auto}}
  .panel{{position:fixed;top:0;right:0;bottom:0;width:var(--panel-w);max-width:92vw;background:#f0f1f3;border-left:1px solid var(--border);z-index:210;transform:translateX(100%);transition:transform .35s cubic-bezier(.4,0,.2,1);display:flex;flex-direction:column;overflow-y:auto;box-shadow:-4px 0 24px rgba(0,0,0,.08)}}.panel.open{{transform:translateX(0)}}
  .panel-header{{padding:20px 24px 16px;border-bottom:1px solid var(--border);display:flex;align-items:flex-start;gap:12px}}
  .panel-header .emoji-big{{font-size:32px;line-height:1}}.panel-header .meta{{flex:1}}.panel-header .meta h2{{font-size:18px;font-weight:700;margin-bottom:4px}}.panel-header .meta .time{{font-size:12px;color:var(--text-muted)}}
  .panel-close{{background:none;border:none;color:var(--text-muted);font-size:22px;cursor:pointer;padding:4px;line-height:1}}.panel-close:hover{{color:var(--text)}}
  .panel-body{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:16px}}.panel-body .desc{{font-size:14px;line-height:1.55;color:var(--text)}}
  .copy-block{{position:relative;background:#e4e6ea;border:1px solid var(--border);border-radius:8px;padding:12px 44px 12px 14px;font-family:'Cascadia Code','Fira Code',monospace;font-size:12.5px;line-height:1.5;color:var(--text);white-space:pre-wrap;word-break:break-word}}
  .copy-btn{{position:absolute;top:8px;right:8px;background:#d5d8dd;border:none;color:var(--text-muted);width:30px;height:30px;border-radius:6px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .2s}}.copy-btn:hover{{background:var(--blue);color:#fff}}.copy-btn.copied{{background:var(--green);color:#fff}}
  .toggle-done{{display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:8px;border:2px solid var(--border);background:transparent;cursor:pointer;font-size:14px;font-weight:600;color:var(--text);transition:all .25s;width:100%}}
  .toggle-done .dot{{width:22px;height:22px;border-radius:50%;border:2px solid var(--border);display:flex;align-items:center;justify-content:center;transition:all .25s;flex-shrink:0}}
  .toggle-done.checked{{border-color:var(--green);background:rgba(63,185,80,.08)}}.toggle-done.checked .dot{{background:var(--green);border-color:var(--green)}}
  .substeps{{list-style:none;padding:0;display:flex;flex-direction:column;gap:6px}}
  .substeps li{{font-size:13px;color:var(--text-muted);padding-left:20px;position:relative;line-height:1.5}}
  .substeps li::before{{content:'';position:absolute;left:2px;top:7px;width:8px;height:8px;border-radius:50%;border:2px solid var(--border)}}
  .stuck-toggle{{background:none;border:none;color:var(--orange);font-size:13px;cursor:pointer;padding:4px 0;display:flex;align-items:center;gap:6px}}.stuck-toggle:hover{{text-decoration:underline}}
  .stuck-content{{max-height:0;overflow:hidden;transition:max-height .3s;font-size:13px;color:var(--text-muted);line-height:1.6}}.stuck-content.open{{max-height:500px}}.stuck-content p{{margin-top:8px}}
  .copy-group{{display:flex;flex-direction:column;gap:8px}}
  .particle{{position:fixed;width:8px;height:8px;border-radius:50%;pointer-events:none;z-index:999}}
  .confetti{{position:fixed;width:10px;height:16px;pointer-events:none;z-index:999;border-radius:2px}}
  .rocket-anim{{position:fixed;font-size:40px;z-index:999;pointer-events:none}}
  .banner{{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);background:rgba(240,241,243,.97);border:2px solid var(--green);border-radius:16px;padding:32px 56px;text-align:center;z-index:999;transition:transform .5s cubic-bezier(.175,.885,.32,1.275);box-shadow:0 12px 48px rgba(0,0,0,.15)}}.banner.show{{transform:translate(-50%,-50%) scale(1)}}.banner h1{{font-size:28px;margin-bottom:8px}}.banner p{{color:var(--text-muted);font-size:15px}}
  .panel::-webkit-scrollbar{{width:6px}}.panel::-webkit-scrollbar-track{{background:transparent}}.panel::-webkit-scrollbar-thumb{{background:var(--border);border-radius:3px}}
  .credit{{position:fixed;bottom:10px;left:50%;transform:translateX(-50%);font-size:11px;color:var(--text-muted);opacity:.6;pointer-events:none;letter-spacing:.3px;z-index:5}}
</style>
</head>
<body>
<div class="top-bar">
  <div class="title"><span>{title}</span> — Training Quest</div>
  <div class="progress-wrap"><div class="progress-track"><div class="progress-fill" id="progressFill" style="width:0%"></div></div><div class="progress-label" id="progressLabel">0 of {total}</div></div>
  <button class="btn-reset" onclick="resetProgress()">Reset Progress</button>
</div>
<div class="phase-label p1">🥚 Hatching</div>
<div class="phase-label p2">🧠 Core Skills</div>
<div class="phase-label p3">⚡ Your Agents</div>
<div class="phase-label p4">🧬 Mastery</div>
<div class="phase-divider d1"></div><div class="phase-divider d2"></div><div class="phase-divider d3"></div>
<div class="quest-map" id="questMap"><svg class="path-svg" id="pathSvg" preserveAspectRatio="none"></svg></div>
<div class="overlay" id="overlay" onclick="closePanel()"></div>
<div class="panel" id="panel"><div class="panel-header"><div class="emoji-big" id="panelEmoji"></div><div class="meta"><h2 id="panelTitle"></h2><div class="time" id="panelTime"></div></div><button class="panel-close" onclick="closePanel()">✕</button></div><div class="panel-body" id="panelBody"></div></div>
<div class="banner" id="banner"><h1>🧬 Training Complete!</h1><p>You've mastered your brainstem.<br>Your rappter is fully grown.</p></div>
<div class="credit">{title} — Training Quest · Generated {timestamp}</div>
<script>
const CHECKPOINTS = {cp_json};
const POSITIONS = {pos_json};
const STORAGE_KEY = 'brainstem-quest-' + btoa('{title}').slice(0,12);
let state = loadState();
function loadState(){{try{{const s=localStorage.getItem(STORAGE_KEY);if(s)return JSON.parse(s)}}catch(e){{}}return{{completed:{{}}}}}}
function saveState(){{localStorage.setItem(STORAGE_KEY,JSON.stringify(state))}}
function isComplete(id){{return !!state.completed[id]}}
function completedCount(){{return CHECKPOINTS.filter(c=>isComplete(c.id)).length}}
function render(){{renderPath();renderNodes();updateProgress()}}
function updateProgress(){{const n=completedCount(),t=CHECKPOINTS.length,p=Math.round(n/t*100);document.getElementById('progressFill').style.width=p+'%';document.getElementById('progressLabel').textContent=n+' of '+t}}
function getActiveIndex(){{for(let i=0;i<CHECKPOINTS.length;i++){{if(!isComplete(CHECKPOINTS[i].id))return i}}return CHECKPOINTS.length}}
function renderPath(){{const svg=document.getElementById('pathSvg'),w=window.innerWidth,h=window.innerHeight-52;svg.setAttribute('viewBox','0 0 '+w+' '+h);let html='';const pts=POSITIONS.map(p=>({{x:p.x/100*w,y:p.y/100*h}}));const ai=getActiveIndex();for(let i=0;i<pts.length-1;i++){{const a=pts[i],b=pts[i+1],cx1=a.x+(b.x-a.x)*.6,cy1=a.y,cx2=a.x+(b.x-a.x)*.4,cy2=b.y;const d='M'+a.x+','+a.y+' C'+cx1+','+cy1+' '+cx2+','+cy2+' '+b.x+','+b.y;const done=isComplete(CHECKPOINTS[i].id)&&isComplete(CHECKPOINTS[i+1].id);const partial=isComplete(CHECKPOINTS[i].id)&&!isComplete(CHECKPOINTS[i+1].id);const active=i===ai-1||i===ai;if(done)html+='<path d="'+d+'" fill="none" stroke="var(--green)" stroke-width="3" stroke-opacity=".5"/>';else if(partial||active)html+='<path d="'+d+'" fill="none" stroke="var(--blue)" stroke-width="2.5" stroke-opacity=".4" stroke-dasharray="8 6"><animate attributeName="stroke-dashoffset" from="28" to="0" dur="1.5s" repeatCount="indefinite"/></path>';else html+='<path d="'+d+'" fill="none" stroke="var(--border)" stroke-width="2" stroke-dasharray="6 8" stroke-opacity=".5"/>'}}svg.innerHTML=html}}
function renderNodes(){{document.querySelectorAll('.node').forEach(n=>n.remove());const map=document.getElementById('questMap'),ai=getActiveIndex();CHECKPOINTS.forEach((cp,i)=>{{const pos=POSITIONS[i];if(!pos)return;const node=document.createElement('div');node.className='node';if(isComplete(cp.id))node.classList.add('complete');else if(i===ai)node.classList.add('active');node.style.left=pos.x+'%';node.style.top='calc('+pos.y+'% + 0px)';const isLocked=i>ai&&!isComplete(cp.id);node.innerHTML='<div class="ring"></div><div class="inner"><span class="emoji">'+(isLocked?'🔒':cp.emoji)+'</span><svg class="check-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"><polyline points="4 12 10 18 20 6"/></svg>'+(isLocked?'<span class="lock"></span>':'')+'</div><div class="label">'+cp.title+'</div>';node.addEventListener('click',()=>openPanel(i));map.appendChild(node)}})}}
let currentPanel=-1;
function openPanel(idx){{currentPanel=idx;const cp=CHECKPOINTS[idx];document.getElementById('panelEmoji').textContent=cp.emoji;document.getElementById('panelTitle').textContent=cp.title;document.getElementById('panelTime').textContent=cp.time?'⏱ '+cp.time:'';let html='<div class="desc">'+cp.desc+'</div>';if(cp.substeps){{html+='<ol class="substeps">';cp.substeps.forEach(s=>html+='<li>'+s+'</li>');html+='</ol>'}}if(cp.copies){{html+='<div class="copy-group">';cp.copies.forEach(c=>{{html+='<div><div style="font-size:12px;color:var(--text-muted);margin-bottom:4px">'+c.label+'</div><div class="copy-block"><span class="copy-text">'+escHtml(c.text)+'</span><button class="copy-btn" onclick="copyText(this,\\''+escAttr(c.text)+'\\')" title="Copy">📋</button></div></div>'}});html+='</div>'}}if(cp.copyText&&!cp.copies){{html+='<div><div style="font-size:12px;color:var(--text-muted);margin-bottom:6px">'+(cp.copyLabel||'Copy')+'</div><div class="copy-block"><span class="copy-text">'+escHtml(cp.copyText)+'</span><button class="copy-btn" onclick="copyText(this,\\''+escAttr(cp.copyText)+'\\')" title="Copy">📋</button></div></div>'}}if(cp.learn){{html+='<div style="font-size:13px;color:var(--text-muted)">📚 <b>What you learn:</b> '+cp.learn+'</div>'}}const checked=isComplete(cp.id);html+='<button class="toggle-done '+(checked?'checked':'')+'" onclick="toggleDone(\\''+cp.id+'\\',this)"><span class="dot">'+(checked?'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"><polyline points="4 12 10 18 20 6"/></svg>':'')+'</span><span>'+(cp.toggle||'Done ✓')+'</span></button>';if(cp.stuck){{html+='<div><button class="stuck-toggle" onclick="this.nextElementSibling.classList.toggle(\\'open\\')">🆘 I\\'m stuck</button><div class="stuck-content"><p>'+cp.stuck+'</p></div></div>'}}document.getElementById('panelBody').innerHTML=html;document.getElementById('overlay').classList.add('open');document.getElementById('panel').classList.add('open')}}
function closePanel(){{document.getElementById('overlay').classList.remove('open');document.getElementById('panel').classList.remove('open');currentPanel=-1}}
function escHtml(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}
function escAttr(s){{return s.replace(/\\\\/g,'\\\\\\\\').replace(/'/g,"\\\\'")}}
function copyText(btn,text){{navigator.clipboard.writeText(text).then(()=>{{btn.classList.add('copied');btn.textContent='✓';setTimeout(()=>{{btn.classList.remove('copied');btn.textContent='📋'}},1500)}}).catch(()=>{{const ta=document.createElement('textarea');ta.value=text;ta.style.cssText='position:fixed;left:-9999px';document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);btn.classList.add('copied');btn.textContent='✓';setTimeout(()=>{{btn.classList.remove('copied');btn.textContent='📋'}},1500)}})}}
function toggleDone(id,btn){{if(isComplete(id)){{delete state.completed[id];btn.classList.remove('checked');btn.querySelector('.dot').innerHTML=''}}else{{state.completed[id]=true;btn.classList.add('checked');btn.querySelector('.dot').innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"><polyline points="4 12 10 18 20 6"/></svg>';celebrate(id)}}saveState();render()}}
function celebrate(id){{const idx=CHECKPOINTS.findIndex(c=>c.id===id),pos=POSITIONS[idx];if(!pos)return;const x=pos.x/100*window.innerWidth,y=pos.y/100*(window.innerHeight-52)+52;spawnParticles(x,y,12);for(let p=1;p<=4;p++){{const phase=CHECKPOINTS.filter(c=>c.phase===p);if(phase.every(c=>isComplete(c.id))&&id===phase[phase.length-1].id)setTimeout(()=>rocketAnimation(),400)}}if(completedCount()===CHECKPOINTS.length)setTimeout(()=>{{confettiExplosion();showBanner()}},600)}}
function spawnParticles(cx,cy,count){{const colors=['#58a6ff','#3fb950','#d29922','#f778ba','#bc8cff'];for(let i=0;i<count;i++){{const el=document.createElement('div');el.className='particle';el.style.left=cx+'px';el.style.top=cy+'px';el.style.background=colors[i%colors.length];document.body.appendChild(el);const angle=Math.random()*Math.PI*2,dist=40+Math.random()*60,dx=Math.cos(angle)*dist,dy=Math.sin(angle)*dist;el.animate([{{transform:'translate(0,0) scale(1)',opacity:1}},{{transform:'translate('+dx+'px,'+dy+'px) scale(0)',opacity:0}}],{{duration:600+Math.random()*400,easing:'cubic-bezier(.4,0,.2,1)'}}).onfinish=()=>el.remove()}}}}
function rocketAnimation(){{const el=document.createElement('div');el.className='rocket-anim';el.textContent='🚀';el.style.left='-50px';el.style.bottom='60%';document.body.appendChild(el);el.animate([{{transform:'translate(0,0) rotate(-30deg)',opacity:1}},{{transform:'translate('+(window.innerWidth+100)+'px,-'+(window.innerHeight/2)+'px) rotate(-30deg)',opacity:.8}}],{{duration:1400,easing:'cubic-bezier(.25,.1,.25,1)'}}).onfinish=()=>el.remove()}}
function confettiExplosion(){{const colors=['#58a6ff','#3fb950','#d29922','#f778ba','#bc8cff','#f85149','#fff'];for(let i=0;i<60;i++){{const el=document.createElement('div');el.className='confetti';el.style.background=colors[i%colors.length];el.style.left=Math.random()*window.innerWidth+'px';el.style.top='-20px';el.style.width=(6+Math.random()*8)+'px';el.style.height=(10+Math.random()*12)+'px';el.style.borderRadius=Math.random()>.5?'50%':'2px';document.body.appendChild(el);const x=(Math.random()-.5)*200,spin=Math.random()*720-360;el.animate([{{transform:'translate(0,0) rotate(0deg)',opacity:1}},{{transform:'translate('+x+'px,'+(window.innerHeight+40)+'px) rotate('+spin+'deg)',opacity:.6}}],{{duration:2000+Math.random()*1500,easing:'cubic-bezier(.25,.1,.25,1)',delay:Math.random()*300}}).onfinish=()=>el.remove()}}}}
function showBanner(){{const b=document.getElementById('banner');b.classList.add('show');setTimeout(()=>b.classList.remove('show'),4000)}}
function resetProgress(){{if(!confirm('Reset all progress? This cannot be undone.'))return;state={{completed:{{}}}};saveState();closePanel();render()}}
render();window.addEventListener('resize',()=>render());
</script>
</body>
</html>"""

    def perform(self, action="generate", title="", **kwargs):
        if action == "preview":
            return self._action_preview(title=title)
        return self._action_generate(title=title)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
