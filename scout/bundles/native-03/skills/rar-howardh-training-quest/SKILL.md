---
name: "rar-howardh-training-quest"
description: "Generates a personalized interactive training quest HTML page based on this brainstem's loaded agents and features. Call this when the user wants a training guide, onboarding page, or wants to learn what their brainstem can do. action=generate builds the HTML; action=preview shows an outline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/training_quest_agent", "rar_sha256": "a583ada09fa44f0d3d88962fea0826ae5877a09dd8639c908e6325c04cc0c36c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Howard Hoy", "tags": ["training", "onboarding", "quest", "html", "interactive", "gamification"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/5y7Z7PjZpol+FduaD5U96BK8K5memdhCIAA4Q1BjDa64L337J3/vmBmSlVSV0zs7v2g5CVevI8/zzmRyv/4KVyXop9++utPUr+HU/Il9edPf/4pSed4Koel7LvrkZh26RQu6fwVfg3pNPdd2JTvNPkqu+V6EC/lln4tU1h2ZZd/jWs6L1+Soz6+hjBPv6Jwvo723ddSlPNX9Dk2L2n7p/mr6cPkenQd6pbr7i75ytJwWad0/vmLC5vm+xt7kX7eTb/WOZ2+9vDb2b+by9cySf983R/1l/+fbz5Wry9+Pbv0X00aTt11Ubh8Liqnv3vxFYfdV9L//PWJou/+Lf8R6le0lk0yf7P7CeW//XpgmNKtTPevuej3j89f/bo0ZZf+fGUtPcJ2aNL5p7/+z//rzz+V1+ef/vofP8VNOF9f/eT88Nj85If5xHy90oRdfj0bzqsK3fX7ld6sn9rrqyTNvn789i9z2mR//tWDX3761clffvrz11IuTXp99/n8X/9rfdUwn//1r790Xz9+yuzHe1//9m9fv/z0w/1ffvqHI5+fKb3y3n19DP38799f+PcfZ//lu4lv//3Xv7/1z9741bHfvXJFNZ+fXP973F/9ciw/gvv9l99i/EfHPyH98pPefWXldPXTp1euaNNvXZF+PR7qp7B9ll098cPsp/afZ7/vxJ+/X/S7jHx3+tvj33xO/nlGtL5L/1PQ//L7o7/89N9/V9z/45dfun+0+P3MXTV0y2E0569fzuXl7974PgNf5W8zEa3LV9f/caiK8Bqg9BqH/3z7b2F8nenydXXN9+H5zMzPX1cWz36dvryb9foS7pbtXJHMQ9/N6SeLvw3XLysCwdg/uX1K82u4rtaer5T/NkjnVzjXv750GfhS3evm9oqk/Dbu16k/AMZv8fxnE98jvFwOt7BswqhJvyHCx8JVsY+1PyVfTVmn3yxdXv82quXy85cdnl9z36ZX0Nftn2N//Sc2/nS/krqU8fc7kr775fr50yevF4CFf8z2J5E/grt/w4nfLP4hqv9s6J8C4+/R8FtBfoeAP389L8C68veJLp7S77H9jz/9k/vv3zPyNV9hnxcu/8tV77A7v0cfZtfItOHH+L/++XL8GpnfN9teLsUfAe/nf2KFyZZ/mK6++/P3nmqvNviEspfXzfPSD1/hMFwIe93/8z/t/P8O/mE8/uHEv/70vy6ovLB4Wr859EHK//JfvtQynvq5z5YvO74Q9mtar6Zqr0n8pXM+PpTfoflCqKsQ5adZvp8bpr5Kv+Pd1ah/+z+Lb1utAH8two+h/5bwv/38bRD7qczLq5RfFmMYv3S/TeIFf9dMbJ9hPJf0L9dI/eXz4Vp6X3/7Z9f9PJx/+9ay5fd1ZXGfrhnmtUl//vj9/Oyx715+mik90ni9rmv6q0IXyF3D9efPVPbNp2c+Mc71J8FJOV0B9dP57e4rD3/9XPa3v/3t6qTil+775kC/vu/rGbwO/ObO11/+cgWRNWVeLL90aVz0X3/6j//1p6//++t/99a3yz82jGtv/cjy5aFs69rXtV3W9tu2/rY+w+Rblv/jf/1I5XXN1StfV03KrEy/v3wtxzpNfs2rLTF/QXDiQrErn1cu26GfvgH3Z4ivrv7N38vo59Fn1Rf91bNJOqRdknbx+Q1Yful+y+Q10dccLOWcnX/+wNg3q3/7bcP/e3wd/9uXyhnXWPXNZ7YuN78dul7uu/JK/29V/zvRuOgJ++sVP39pnz67BngKh2IKf9jIwu91+czej9evy8Ov7tqv3Wf7p59UfZuc7+n5Nkll/KOkf/nU/Cvu2/Yq7Pyr7b/juNOHl/Hplwukvzd0OH1KEfeXK+c32hN2cfrffrTUxUfWJvmWv3T6dtOPKiQ/qvKtB3+dw6/vQPCD2PW/If//D6b3S/eN6v0Dy0t/R/LidZquNDTn/47ufXz7bdV/GMFl6gfafE/tfNXqRz/94y2fiQm/07SL1V3wHybhEl7lvC5P+vhClcvP69Tn9wsakjX+Ftpn///lm5mLuSXfueofwP961FwdejXuVVNHutu/C2oe0vhKbvwZ8DAqm3Ipf0TxqfP3G8JmD89PXeNmvfj0Fdb0D5n5u71/+VDwP1/ba23+/NX2SdpcDrdpe7XWn39tzKtFrg+fdvrX71sxuYJOzi5sPz4UaVwPffnJ6mfxp2Fc/C5N3xy7QNX9Btu3Hyz18yX8gf1fi/7Vnn+s7XegvpoDppE/Mpbf749/PMh+585/aKFvWf6RmiuE/prnKzvLxw3k44aV5v/Mke/L6mqja9O03+nu/we3/k6QJf2hX5X7bQKY+EpQe37u+qVDPw48P4Rl/zZG/ykTX9/G7n/8v7D8K8P+h3P2N63wad4fYuFbUJ+p/QNz/aToIwouhnJN/U9/7dam+fNPV5XTP+qHj1S40Ojq+CvFH5VxdfeV7U8bfn777svn0++V3G8Z/rfvAuc3q38I9799/apz/u2b0vnN8b5rPvow7dZLo/zP3+77uPP9hZ8u5bOcw8fh79P32e/favCfveH+oaY/KOt/0pH/ckmFcG2Wv3796bOf/w7Kf/oIiz9YukxN6bhe8Jp8vPuRhb971EcfcvDxaGjC5bvQ+o+ffoWNH2n8wR+u41M4/WX+oCsI/wxd1q7fv2/J69n/lln8ODsX4bXrrsMhTqGXCYjOQgzLoARNKIomkAv+IAohwhSnSPJ6miQUgdIxDVEpgSJ4DGFxDMUoEX8k1EUX4/TfP+ui/Njf+6m+rP5lmdL074+vr5Ifjn935JOS34jMt8747v9//BQR2Ef1Y/Od+f7DgYBHI+ijtobopZNUWbzwpxD0/awMWOiHR/mG3RKW30MLRoPwepvJPfYYScj7nJsZbjytUak6ZMcp10KXKqBsX8ToAi5YdCpQ9KgPtNBQQMlm/s05hO9w7KF4eDi3ajnJ7O0uC7i6GfWaZvJ0y8qCBkEt2ydjPenspM4MfRdB2PctOA6tUbIywG37+xnHJ6iy5V0x/BtepbyD9sL9Ae75TcLvQ0r5iGMqY1AvTILiJNVXscNYJVKmpVY83LZaBzZNy9MtS8g09ZDcVWjGMPNxVSQdr8qKTlsUMF1DlHNaQUPEfM7G7yPI5DuWmbOgLly2v837/jrT/VD3YHsvcQogEkXMCRVC2boIjV7wmTRhSGS9BU3dyj3pQy/AxdAJMKRDwye+EM7AaoW14KNZVvwttP2ul+naASs9ke/86NAGAy8uxe43v35Uo09PbeakcYVg4PNWprr+zkt5L6ngBgFI2rgZR4tO1QtPCY62+3jyM+nnLX7DajFhNS7RC4rOnIbbbz1Cv3p8aeRUDHOTTTHeAoOCpNRwgUkScWwiYWV0HV5FwFOUAa6Tbr4vJ8mIcmXovkkGDJwW0cWLE7+gmdRL+y6HTH+TktzmeRKZnPvZOWXQ+sPEJfChqi5dZEOtwUmwUCZCM49O8JeSUocX8+oqkNzY+8SKfbirjCwmgKhS79fJqAgZau0Bc976EHZTlsW4Ei5JLbpBQbBbBEF5E7Vu1fZWIc147axj0+vAwxZBaadzUhUAeZLwgJHhG9O6ozJTHikaZM7n76xadlhUYxpJffCN0j6vai89UF43FGBbVstSQvR1tjV35mpMf4PxUdyx2juZjULvt5TxAZ7XVbXxHrlfGKvnQcnmlwZp2nDqviU7ZUZMxkSYiWS2602inlvGUp1bTN7xWhbpebvruAdx2NFILzOin+o5eUJbm5o7mDbJXpOaSkEMAEyzX42KOWs430UTFcckYFpNfaT94JQyaozBMHjYTnjMluVlHhpOI5odJtxsGScIpuILIvHZV9swYYpoINYDLPyUO5xJAHxR1ZoF8NXSYj3f6tq/7QkhGWrMjCZrJ0sA49rk3cQZtoY6XAWK7QMam+0ienIzFetMnQYb20PVHgtAND1quSty/ZWu1/o15CAofS6mIufWB7l3p9LctJg9YkE8fpf7bfG9mttFZEyO52G10Xkw06O5cABwypx4OQ92eIEcFjXzcA60msX8Ar3mQtBl7sihssAZiwxPZnkEgM4lGuoBXLDrsRq9tfvMWCj2TI04KuenV1AXeBNgtmdTTT8glK3fqjBHCtcXLAbPromnTDjFQACXRQWTJ7ZFADY7JCGt/jhjhc0p7fksU9bBxhjPWYOZcfVu691xCw4pnwIk3TsDu+HJMxDvw8RyT1WQgwMfuVzOfLEejy7ZkcdGaWEKVrC3iJ0yq5Bb5DOcx2ZSA96KYiFLkaXD3Ka3w2244lfHnXpzLuezacLEV08+npBblfeX3Yug/ZInb5UobgRtpp3r8BScLjfQgcxDbF+ZY9qJalUEdb8nfEJ3cRCFYfe+PxqRM9FFGBlW22A+U9eYKmxQKmZFf5ltJXIpoPodv7/tiM0Kv0Y67OzUWH87oLvXvj/B79etmpuXe/eM9L1pANjmhhZg8/vG3CF1sQAK5qZaKi48T4qmTVKAvUmp3FciWXF0fD9shgoBld6BJGGqbajWMDDpZ9AcASi4gSKTGEfDku6OY3ZzIbAzHZNrMRDo+tv+DG8w85L6IMNUh+HWIcF9b5JrNeQsl4dTWdgmP/Ixpt+QWXSE9RjI2I5Shn1xJIK4meVrJhqDdijfctQkOZa9v3rKY9TiOUtDtVQn7StlI01iFN6Mos+fXI2WjsYyD3fyGXyeghONM3oGkW3BwRS1XpRgWOJJjuKh5BFU9ti2PG7GkWusK3gugT1tYSqaOMFFKu6PVwH4vWUNaeHd2qPepaPQa4VGQSRe6R4EFlTaSWQJJGbsFl0dSJvqMEt2bcFHhxS8+WV6aFRqehB5etsWzy66Y6zKXDB81Q6WQY2BshMjpWMKNKpU7kGV9IZA06Kd8uWJziDdMJzgmo+0Ejba9ihm30sLlcAZyLcsSR8j5x2IIFiUMfUNvIvvG+U9lQNkvZMDhHsC6Lc6dnmWqVIGHIPVrz2WZoNnLdVasJapi9KSv3KJvBOa2J4YT7M0vvoP6iD7/RRalJlBYPbVpwnt214dtpTvDMgprq4wzWbtjReJeaC3gddosTYLbFCoLcfSzdEjgoswBHQ+rZOUI/mRcGoEy+tdJcV7hktx9DZzWdouV4+1Uc4DLMJISQI7qAddBupYBorT9jI8bmZygep0pJgWEbHtLeoQ3++4OQMNVAiWkNKtG+4P6DbtENvdcfrKIhS7ZrNj8GMPYCNPuEVy6LzV323LimPVEAvFtveYEfkYQF6iMPcOWFs9Uo1Lbr1mG6m0R6AfvvCAHzbAsIbSnSSv6fMkZDOjeWQu1S5JZzA5aYKj9JjYQdJ9Bq5B9hiUYohg3HOi4CDbftP+OsqPVBG7TQn9Ku+GSnXdgXnj2e5F7xcyybmuu4RUaW48Wj6BHDdldTUuQvCH9RT3J/8wWyAocwgVuz23mqylYOWwFVseJ80UqZRXGZSDn4fTKub9gW9wBzVc/WBKX7h2QYK4yyK+0CIqAwZ8Qo4z+89nBHCOGYvtg+t2HqUyZtv9YGc6uxfmkWMvEqm9WFi/Nuv8CvKULnOAiJAE4W9L4j6ymyJ7/gzqlJafdBuE3niH4N0a3NchrKDiUM1rmh/tY5SKSBOsVSfNl4icmHqeL9lvYx5H+IDIsIoPL+xoiyZ3kNXhmWSHdsgVZA0Xey/pC99mORRCglUvx+Lz1zPO+jDTVu2pW18m6YYSPFOeoXNjYq84JbVDLLG5mw12UTJFUQ5GtyRDNhXEa+jnjXog7YwG+v7QRvWiFhuKQhfPW0hN4XaXcsFXM2/w3lfUXeJGtU9dgttqM7O3XSF2feMg2tyIPIkYre/9zfaBgwbkCCMAicVkwXHtuMIku7Z5AXYxLkr1sDQZDXmE8mMq8qdohTXB1lGWMSoDRR1ixw3bPH3RNF3M2bvqdlCJcbJdEb3fjVAqD+FiBAYhDICyrS4PqfB87f9lB+obWvMID5uRxze9JHIGfOxvpooVpz6i8sbb2BXPjOVwl9x45bECgzp4CotBCGPV3Jq8urccQ5uNAInD9Gacd/dD7eirrKxPMjrLDI5ksnReiC0Om0gL6ixfFHjLG3fWF0N2dIlXXTFPv/EFPz8WrIbeecu1T8q+e+zjLcZ8dSeFlmdy1GV2HQo9h84UXKOppHN5Ht+7uBZeAdVGT359IE+tbGro2fC50jjU476wQ9fUThBjbUU91SKkLAeQzQtFT7oX13fRkWCq+6PAwaWZuewmQP32zMVLFrlmJjzCB4kEgcXvHMoBzLArkmLfRnO1m3Txi4u60QHulD6Ejh6V4G9YkO++R63D3R9hN19NLPP4WqmYVo42xnBBpjUe15siE0l03wyeDHF+QdV15vKJPvPirYz8zhOnlpPrNWnDJ6HyTZC5hTiDMnjLuHyYacvOqmK7H1ms5OVyF+6jotpBXnRP9WIkyyFNz2Qs47skYWRQOnkTMJcgYADcGO7c8A5OOy2R2ysIYMsTtBc0ja1xq7211LS7XQFH9gqYzjteWMhgFCWFajnAx3Hn3QjuKjy9KbRJy9xrn5XNfHEZJwoYVtHsKh7VGSWP8GB11SESnpnMpSPZumXrun3HK2ceq1K+ECdEaHSF0cQepddBLvwjIa1BjOEbMVOBfTfb7iF7saM10a4JA8GG7FndAxnT+thA6vrR4ofZ4gZ0WjygvwP9OWYLhgJiBgda2i5BmOPtMxzjM8IUwgjw24xWyUzVlzIj5Hi9kBp4EmIfsXbr4NoNeN3Fi4UpCoJEDsy773ZNUxZo3mJvhpWnrm3K7NguUQmtiODRLXQ/s+/tXdPG6tzohXrNj26Ym0frGRfqEDAL+jEkNk4DDlQB94b8sibJMjjNHi8KkWx6MkTymb1iaulDdzniQhkPl/fllvBrlmEqpMydx20CFniVrFaTrs2czkDa9YNnh40WEify7FkJZwOer7wwbyU+1BbDH6p9oZiSXKOXT2Ik0m00spiFrfM80/RBS9/OQJkKmHXFNSiA5+1CxXe1n5mmIocnmNJTopVU9O9eDq6v+vka7PGFPMxTCYyejR+vaYrrVHP7Jp9sbXZ1TDWUUlaly1hKqRKPaU7mvVEeahZ/WgMAEaOqfHY1dRugbQ8Pt9l9lu7lZ0FcnHBLsnG/tGGcgm4k9Czt5xTCFwIx1LiHKFUv5+JaTqUMNpIyjrO8B3LLcL1EcEVpAcRLcMsu8oxHk2m+NMT3U3N4ju/ChgRI+hYaW2qTlIFHjAVazc1Nb+TrrWt3k5cEHLLVXWIa+nZTx9Vim8ATo01lHmy3ztRYFGMo9O+us8VXZN4Mv8HKUvQUDhmnu0H0HMyrZy+MIeufHeiGL3VFexh6BEtOp9ELqlSxMAnW62XoBhGaVTIG+wLeO2f46+FWLtqOemm9AE9l15AnHzquEv2YBc8xjPubPQ4HEWBSR3YFYLBB6d57gPJGN6YfjfpyDtOp6cCZbbWN7HxcemfzB3dRtGE8LNTemAsSWw1pLTQx2lCYrMVAyzfxrsHp9kyWnHpg0CVzwQEwpdtC8vPLyMDq+gbLMsxokAHjYAP1QdK1IWLYOJu/ZYT9VIZgAw1W2pJGS/29l8Uyxg3DlO/Yo5HxEBXOCvRvLgChNhotXD+YDNW59PQq4AAwBVlOmHvnvdkwu3VoKoSdUp3QJKxwP7TY9JqfDznEtHzP3v0D250XxN6sdxaGigvvLRKJ6fCCkmKo0SYkJhVnlV5UK8kcyaXtObQul2iootsczWPVWeVLeVlAOF4BCyCrBQdhXtU38C5NTa6SmhZUvThVO2tBHpZcwaJKFFVM3Dyn4PcMOG4iLLIXmyMsFVKk19beVNHiXva1AgzjeJyNw98MHsMEtUcHqxsAYOAKLb87NbK2Nt5YEYTe8ZauRCiSizDBmFGVIfLOcfbzRjB26FuPEs9PB6AoY7wbrPGyOKTWad1pRmILyKiUEtnXqKbR5F1fPRapBch2pAZldy+8H8izDb2NeZfBFRAobPhQP+BbbcwzHY2xEnFDfi2PyrondqePb+VVMlCj8rC7LbJ4i5H1lrXPoDPVg/d0x5wj6ZG+DG/tgumig1a7PaRi7Ea8eVZPKtAkXHehtLXMtzL2FZCKRobEM4ze7MDv5DDSRSzjgzY5kjoYBHyuGdE58LiTBvkCvGes5XY9p0oIi6LTwEVnqSbAjBUMuz3yFBSOn8TRg/UYLw1W8aqHg8b1fBczO1zgk8GVNVIq/+YtVGZYj23Yidl+Ujm4OSgIuAZW+GGAH6jnTmY8bqQKRcal3UrvyLlHJOexa78KRn6/0/CQ46qVEbvxc8W5+OWAAPep3Eawuj3UN3cT7IbpRVIPi74N6sY1CTLK33YGagdm4AfzzFsWe+T54rDEO0Awi6CQEbjasygh3Xw6fKLhZlXU8Ltm2ZXHV51g5sxACcfu43O59tA0b+G23pEOpFi8yLC+4d+ioJNUtA4lhIHuPX50CoRtFd1w971jbl0n3ezBbnJtfqrDZCqBuRYp21WWErp3hbVuDaxY4evU3PvmCnXbyjzxjm8Jhc/uDd6zkgUBSqaVLrI3yGVzqgo2TdUeHVIF901ix1m1MOM1FpERKWU3hi8dbcNFqYUHUJmomq5oja2SfG3Lh6JJwlvvjtdjIdPOSJhSb4fX/irOc3ArZGJtrHnyUQRN8sBY9MDlYgISSX519/th6Btv9n6BBpS/W+vt7lM1mvNLKfZ4tQ4M8Ir3YZdh5L4ld/4U3k6VpjlXPu2+TzrcHW/1dY8088ekUUJImtd4HWqmQRbHBdFLf6Cm+368SfOtblTcXErlLbcVLSJmKx9hFiKnTCmBBdddke9eK2Fv6YChRobLt8U1iL+nWJVzHT/xBo7IoKS4grVzsXITpJcagGhs4iTFQ/qJYS0eYbMRs7QR49TtPFdZT7v3jpctg/Wavltv6EFSrbPiFb2/d3cj8PkA91D1opnU18h2/XUg0Ld5ImNlvO4KHJePh75ugtXRtJWmbj9VbX4eO/pMR/xh+/6Bl83UKtKlq2ALrkzDlZ4hYYf0tWKEYn1zSXI7k8PFkrw/Dhd9c74rKBsqtLLdo2PU2oxsAHq41HM8s5qt6p7KXSyj9aGJh+wQZ4kHbrDmEU/9c4glX9omyoqW6nWO8IOumLHrVGLq4lmgl5KtZBGoNQB4igTVuwNeQ2CohlO/Im/+BZ0ngzB3W69WN9fyHtrZcbLs5gFeGKZVd+RsZEC661MBuPtEiCLDIDGUSxUi7OIiURFkYB3TICCfVoS8P5KVQfujgRnt9Xikzqm7BSAUtwAeS7N7lS743mQDD3eJ6wybGIonlTx8n47gZkfeawXM83ts0nDh3jfQWjbNTAK4eHqzowdhOMJPdTMdFDK6Hozo+36/ISoQc5N6Ec5AXhUGbR+P/iWV3jtKVGujllvr0hpc1ghZmHso+cEsZf4iqOhs01ZDxtbQh3NgNoxuVFHdoS53G7gowAUpehi5/w7a+lQUBu+0uxo8M9gWtJZSoBpAWnYho5EwQozQ3LX1sJcirsY7lPrj5TgLhotxnMkXXSKB0Wf9tBvILgeDwAEpygMUvNKYbtsC26u0uuYrzF5jzivTjcSfLxLEE9/QQnwQj1g2h+0UYdbm03nRYfdJwlP1Lnrg3poGyyJRbYa3oRhBeH8b2uuSj2fki0Tu1Wl6iPTRhjvvkgwsPwWNG3tTS/WJt5wLDysPp+RppjRq9Z1b+B4UCj49C3r7r/l+D1UosFT7DPWh8EiBWihfqvt60ACZE5yyI1eseFSZFsZ30rglY9udxdFiVyb1QMg07HGXOZpkS89xvNpYsoI136WFNQn0VCw+q0Zx80zorJkzxPb6HLhrcznYHXMirBEIR50w4amZqxUWOH1jxxCkSc2jWGXfq5mXg7LD1H6iGU1Dj1Yl2MIoMLd5PYor+V0elRGKssCDe75ZYBuWai5glTuMp8rzusla+UVER8osyTA48OICCtXC4+KhaxpFvHiwDi2Pj8THWmZC4WXGBQpa2ofvNRHrzY7fz52a+X1yWbSQ4HOv+GqRYqMXaNsbXF0FAge+qGxGHn3eGaHF7KPVxu5sUeCR5ncuhonijhsh4rwp00XMHhwydbT6kiFo5MKbEzZCZlVvF1RCviI6dB8u82Bx9aoyB+AkUmscoAsArX5Ri8m+ATRju/Byzu4MzwJ7pB4hpgwbpjXH07AF5ZfqTL2JMTJ4T8QpIjFMRye0BBG0FyGw7Gnd7BOQdG4OVrQw1hvdsdxVDN6Cqo1CzC2eZQoDNASgcwPRzvh6o9mQOEa6SjUw2VcvCwD5FLr2fvJcOgB9/5Bk4BLhjya96aY6ZSIlz5dilpEd4rQUMQL+ArUAJkyLHwRjV7g35gDh6z5gCrAyMSpptwEuc0V50HY3N9aLaVO7DlWO65tmnuYjNsEOuXMk8KT1XdEYqBzohwwKZqrry9wwGFzdhXhbKXPGGJr0QR2/+ZcWpdsYuA1phl1bz1dNltalGZinAsJRvEzlJeQnyXlffXvkdUzCOTlgXgNWQBUNyvmS0E5GmclQIVAzBYpebVTY76TmI9bFvt3nhqComrD77MnDeV9LytULqxxryT6fl6wNc2ez3GjoiQZjcDzMsZtadvMmvNgoJmyj9ryNjEC0npR3dhsPoDavmq18NB5K7XTdCj3grPAcBn6AbK1Yd2hRpXeaKZQGh2I9iFIjoyFW+izDQyqHvUPBfOPipdnmW2+/Kc+7hfYBZW/MNfelglcfA+9CsrNtyB2YxKPQ/TD3PXgnHn2aNCzeL96108P+kIf+BcvrhYmsMlHpcl6ElS92hq96USY7iS0cM0tH/sAuHZhm+eMleO1+XyihgwtnqEpQxFlQ87fJuV2zu1jam33eqtrjRZC1nxNh9PCavHb/pJwCAIDURS13NX3nrom3lYXYt609iDi3xfexu9rQuD3rCImK8beguUXoc0ZJqhYU8YwTuqTGyODJDL1NIu4gPkvUb4GwoRv7HDpCOCe98KO6JyfuVpVhOLlcq3dpL+vvS5JThIjfLt4Z6RIDelC0JRfZkwIsXt4y4BICSOYGxXnkxY+PtNcESrmfWzY9K2xjH9nd1wzk8ThzrI2FHZcvJPbRl8GloVBuxtzVWVo1QvwwWHKfk2d5iwUgRrjHA+xUkX/h1fvanGT0KnWiWbOoRYOMnBD0aF5GSlA5+1C4otjj/nnbTNEm1wx4YKbfP8aAHldHlxOUzsoBrfiW1r1HlUsgWHgl1pOZM/gaPxkLZ+25dls8mHMV5XVphAq+FurCdxMDujd9oGpeOl3enrQpUqaQ2eicL1OREcX55gwNX0JSYZxETOQdRdY7Se7NjSztVLsPwMW0LpB76A0DN7Jv0sJQ4xQp4TCPLE3VVbgpVXZaHk+3rfIGPwbngvY703dxTgvY8+LPWNi49486dZQTro/YyrsU7RlxtrUgub+VyAREyckDckYucXKfaTN0HysWDlpHV+4yPyctG1JxFJpwBaiDpHwWaIhVHXCjsXQMEjb1afEsRt02CjT45AnLgR4/0z5pEW+87VwDKjHN1tf+KlBogBpRhk4FN3uWBiwYS24O1G6p73tUrZmXTn0eXAfoOQk/dRkfk9HMwhwQR/si6dQbBBF+wzaSvoEnK8/UOt3TufZk47VlcpH7qVICb+2EdJS/QQiwyDW+9fHLjhkSW07m3qLM2SUJYd2LB8icgoOSimdVecxfsPc4z3JXufAaMEW8RW/Yk2hT9rehQjE9ODmNkf3BIO1OAlp21UvmLTFPvdMCGlbSWWlUGLqQZ3q9uX5iBr7TrSGon2Z2g6E4Uk/UBLB+S9xBix/vCSmW7AIzd8i6wUoNu+4OerS1kCPpTBjWOK8QtjTb48ZFD2zAMQ99OMNa2bpSzqAi2yO/ZNewHsrzxegyIrt8ykfmxfWkOyGNGb6VF5nxjQZ+Vx4DOTunTvCdRXZnoSSNecbkEy8EvS96/Ghmgil5HyfCZz/eQf5swMuvAq5RxntSPBAO5b2EO4VpDb99Fw4f3cOJqkZgBALRxmzqgAmYCl9w6UDTlWJBNGGRd9Zc2Ta07uoxOZhzHGnF9StHCJHxjVdHIL33xxk+YwGabapTiNS4DfdafuCtyJJKoXbv9XY4xCGTFz4rlrvvp+RJJmuHsSOLUt5nMyRjx+YDCDikJWeCYTUF0r1iHstrH8dR2J2Eb60IyEXdwd6yRrIv9p7vzqQzHOEUFMetpA8P59DO5YuoxntUORm4v2kT3fDlZQ16KsiBa9IVJFNOuSiPZ22JDuEQvLZH/n20jvN2KXu8bhH5YgdSlHV5CuiN26adrd9kVXE6vaxK+VVP1qO1iYdHVOFg+vwaXRCG3/3y2LHGwl3/2jCX4Dqggc9nNNyoi2BKsdM/sG0PyIfO7sVpPmX1jtIFq1v35UTMUHibesHXjvK4RF91aYwF2dQuOiO7ws43Oo1GM6QVLjOWdDFC8jgBLkNUDAACdcXwvB8k5OmpjJ8PTORdewbuWv0lvgp506FtU8mQf1xcQS4oswCDfWxd9+zm7E6Zgt6Rp/T5Bz8JvwevbpCYo7zptGNgla3I2GqUz97yioOCn6C759Yl8ZXlvqgujgClVQjH69kwoue18xod1/7h3paM54Je23nmBeeEOM9nc/XuGmaThgdRaBPYdL/bMSUIikmedHPsyrZDQzJnIJuLKkkw4CIbFR7jcaRnsZheMvxwAZsBscBTt8ah8gk3btYc2RLA8u7Q2PhdCF2p2MAlqmXnHovv9QkoEgpiyTbdO0bHIl3b7OFu2YqPK3ZAusgNHMSChWv5kniRDDJTynavWxZFiS+Zd5ohQ4h8WSJLYw4YNqQlpQJM80i8gpNUmSV6i9eXtjz9UmeEO8LfwUnUH8ozwRepLj//r5wnWU5aN4a0B4Ux2Mu7uFF5Tp3pmyWC6mGIFQgYCyhcbM7HzBw9A13PGJBs7CqwWHPQyxAG4kkfhv64vV8HmZeSLaiO042o0k39Yfde1LGsVdsi2AL3W8PnqqlGzpTpeGego8O62XlJsxdGi9saENKFx4B2Nslbg83sIhxaO8cWkPqZgiJTqlvi85lMlCkHr13L3kGES0gmGlm/BbuMFkfUP5AWVLBSMR24GC7QvWWejlqHcQ78AcJbts17RQIJAA5PLH1Gg1FaeFfJpz6YWDOKQR29H4raPwoBw7Kto2/INU3SeXPpaMXcK+7DHOp9t4k88o0WyUYSMsPH4G0pGOtu5NYUXjrovPs0DYhUAi7Lq56Z1Gpv0p3cWf+NKSRBPClzAgSkmeZ7d4yFdXpxYqkyxV4SDR3m8rZPTOeNggFeggZsr6Lu9iveLwblN6+BeLrPt/0mnsHw7vaVvpbGirD9UksE8DBwxzARCda8R9I5O/GsjTbSPX+ZS4ckoacOvFEvtZuxvgegFbz499NbEdjRpN5JuYsWPql5MGJNj18CaQvViiozXBiEnWSOp+aNCvR3dbmRloAcGwwBZEySAqgMJC+w2wpltxZcKuk8PKIlZMdTaO/BsAUceES8NcU1d8+LdrvMm8+pewSHtRfwDfPqV4Q3UNSz8uOdP+uVgGfEsJ5Jbw2oEaTB6bYqJeEZi6HrdgssT8XRDXv4Ud42G1u5odVUrFl6uIYAzNTfiFkFG4xntrYrn8Z48V44KbfeBFOxTfLahplYnXi7zYXkpF4N8kbf6NkqpYID8osf54fx9sSEexQ+FXcCdJC6GiNiuzD2K1mIunnfn2FbcyPojjQty46YzOqmanTr8orvL/QNSPU8AOT64KcBe0zXjNbP07BWQcF3YHk0Nwjgbpqh1dzmPDGjLue7UO+9W/Er4xLeWtQXy7+VBG7TOrcVyUMjn1Ory4YrOk9TNcK2eGnxziuXrlFC3jyEOxm01M3fRVZvJd6BrxGtXG9WOzZnswVc4QnPpZKotBB1X8KI8Y+37VKae4CP15QOB4SQ8ARUZ+sFzNMhy6hc8zzVg+GiS7USHEKb3qFTfDnsFnM001iiZU+XcAbmVyJNQcXmeitr58txBVqjyQrDJqnHCK9G01fky9zcPnOyLKsJplXo0Yk4nU42vNV1Sc32NDOcLXM+MnOP1Lh0v2423Hnio0WbDwgnCTY1hTAeF0YrvfWpAOZrzvEHZd4Rb23T95AKBDLcgcy23zdSsxcWvT+dVQVhmEDgWz55UDAkUr/S08VZfD9XkwZTJFnUNUdjDNq6wfwj9ZoXBwPGhApwzIagdsQhFXqAGHBGicwGy75Xc+VcvTu8YT5ZahZSAcKD3C4ruGQzT3VepDLQLBauzLhnyg70eyTew85/EsxSLVy65W7q0Ux+9o+G967lHmNL2RFYoxP9ccxyc62Z7kX1MAoOtXFXwroQdk95BXK/sW6RxUhFLfnu+qS486wFeiFfP4l6nHHOFmj2voG3xpj1zHzxT0BNEJxUschXeZBxJ5TZQ7pGE6kt+w5bb0MZEYp1an7kKqbBDvh8mAeRZy7J88RD1jyC1qiHtxgG7uGgOFN07lUwpUkTddhjSvi9Qpmul8yjESxyhDzMUW2wVOKfAQEfjxPdU1nYg31iAZI5PKxcAoekQNbdwPdMOSB5dK+MG9PooMbqPiME6gONOZ/JUl8klsxe2PqWrWhliPfGFW8hgO9Vfk7XFGNICxwzmpCUzbQtkjsu30uQ9XAj8FGtna2KItCeEafJBYMRW6KPoYeltYZrgXun2rCnVVOkwe18P2iANozJA1CImB4tSQ1vPWJeeleBkJmrD0NNBYMswFIST9l4nn0maZCXJpGrei+sAEKdXWTLZC5mLfAmFAIwkyIh4zd8yDy4rH/xyqpRVgYwt30QGxQIRkfExlcTg63hgZV4qUoIOdkM87BXBQX87ZXeVZSX92QzJwKQas/vEgfkHTOulPvN1US2LhBkyrNEShuZj3p05GvJtqwGptPkvRYUpRbvzRDrFVM3MBarMw7qGLy7KKbgGlq5F4GA35Kf087J4hZEEVVjyMCG6fa9lZw9dKIwS6Yb7OpgDvmVTYIxnapqDuuslREGOPGANeFoIClUn5EOnigrWdgs3mlsH78PZCE4pq/FC1gl0atSYG8CC2Vr/HxybwkGrVUStUmQ6sdIbMNp0uyQ7xtmsHVdm75JtFs+29kz5k6aC3ReBZ/MERY0juP3ZuOb/slCGBnT4MjI7q2rj34R7p3Dr0MDlo4Un5vBZaH45M4qMJiNRf0DpjwihLd1IXA6LpNUgjcbNbPnASTDHX6pZ7Og9M4i/cXggqwsblA4n3AX+8iCiO5OhRSVXNP8ekrmpe/AQJd4/10v3MuK2m3c6023IIDYIriiaRuZNlqESTGOfEZAbWd2pDciMfaRQivGIivn9HkEFXlIA8zwfsfC2BB6N12dBN7FfredferCC9gpQ0cdHMWYxoVuYD9RFyDpEV83N0uih7qXt5xEgKF0mXQzxc1FeoegZopJIpMj/FZ/pOYLdEWMRxz5jeHji2NA1KOMIbTO0R5u9gisSM9PoUDm95iXeVLwjeil6IasOPcOfEnk8K5Wy+ALzh4u7WpOsNH4cS4gedQj4+jWdmNVg/l29vQ+7aPgdSNjmZsiSNBDcsjpXjQjJ0vGobCtC8R77rG2lGczyaGUHxGWARDqpoGYvyiIdu758CC9EVF8+OYNWhKzL9k328jQpIxhZWPM7lk03AABN3VHm29JgKjig4UkIHzotRq/dLR+1QHJuZ6cwVNdQBzdF4QX7/PL5bszHhbOrTgriNsjek6H3lTVpN5IiVQSdjB6gxW02AtsGh4YSiV3Ixyt187MJUyqpxmxc232/lsBZDbuRLQN2fPkHnR6I6R3te295FeVXsZllFXFu6CwmxY+7DveZXudV/1rY4RJzc3OYe9iWwKKsg65gtpl/IZGzusXs2xWLwfbXhkd1eRuz/SeprdEHJkQhbzylkQPYdfIeLt2PhkVaPZC7mj8auTOSj3szDHgqtZTe8GwMoEDsqQ5ssArPcNPul984eLj3ui5h9ZWixbSLGPxnXfq7noSxJhzlxpgB+dZuulxKy5mbEb25BBILS9o5OkX8CDcuQkQnD19qWmobqKfE5y+SBS+/gSqOlWdKiwqWITKRObi3KQbxJfljb/7SX+rkI2sIU9CentcOYUbc7nNfH0ItdAla5K1DNPtH2ice0IA8MC7VcRdTbVqNZ0+4h3dcaccLO4yyrP95s4gL9+ghiqfxYIpz26HCBcnatC76CJWZOB0t8F2hk06Frhibmc1gU6iDdWVnErrFCkTVNJXMs9tV+VLuZYbE+dKo6gFgNAEkjZLvrXw+ly4Y031a/D2s82jw2AYZWjtwyij3VnYaxpHoqmLFO0yIdBskpTrkAluJLSSweaQ6qztEr5c1IlYYUUrn8p6wRbgvV6yXpd55C6vU5z857SQ8BDZOhvhozbLieHu4vYWdB5JNjWATWYTYd0ewOzdQOUBlzIUvEbLcu6Q+IiHWacxUUAh+9hU/gWRyaUn5NYPXUd7Cw8xbdCU2Cw9v/MltIdnPWn9/BimUnn7OOcWIw+QF6o4BUfMilsRQDHspVCa5Dpc8C/c5qQxswjNPBaeKNzsBS1ii/tjdJukgzzbief35NkNhNYmsQkpOMrN+5zLsW4rnxhk9XFahIQH/kX8Vz+eOwW8c+NMDtAoTeH+rL39yfED765pUT9QQQyRV3uibOqnbdLio0+Hb5CKZDm7LYicPsn3/W3gNDG/OzIIxiRs0SIl0Bf8TO4J8KB0ELBt2UDxh3ouOEVwN0V7KJp9zyc47kP6mRzLxYCZPE4gjFCI4RW1/N22T2i0JrO19F5aQzcTh6nqtMokulnfwjcM+5OvyQv++RsCkozTpQ6BR8NB196lu4Z0eG5I3unR0yVSAnixzJpc0SQmjor4rji5zhF2xh+7MT0yk6XrVc3tCbFlqJvvlYsbNuC0h1f1T+U12n70vPcd0YxDxT0PiSDlmz0HplJZewfdmyVAbUpN88JEyLH0ZuEVPaJBtqlQTCEiuaUbv47POiafKPaE8XcDA2nS7iYim+751DbyGm5fZvvzLRACRlwFTdDjtpnptbS0wM9GJQ3g2wWirzlNNyTokJL222cjnnHKmjMytbfYj/rljEXaoHRhzfszlpuw2LvGcYTsIPAWIBCCJh5kU0BTFz94TE9J7HhmiqyhbMW5rKHdjxJ22VdQO6dg4YZsiQu/7B4e1WoVBleDOjlSPlZcslLTHStjxeQ9SB8D7CMX9h31GACn/CAggxmh2ATeI0ACtCrAinwmyHCyjiO93pV3h9WiubgLeGQdMcY5w86QEjBji8TP/HnRRwQKIUimyywyuOjOdFQkqukQIEeuuS3d5cg2D9OlacuKA3FbGoF9ch+huwnubgFGqifxlCJqWLwkLSma181ToPfyQniiV/2R9sPRndNrt/JjyXFdq+R1XQwrwdWkS+UyX4eoim4UNyU+hp54TwdVFi8eIZYpAfY6MmOZe+I2FvYJCR8HD6J6yDjFvcgyq7dLOvNDRVBgzeIGp+8E49qVF7/BacVvUHeSSGn2h1FCihxZYXh5raPPtvps0qHlcUjIj3KmK/P9BJ63C9lf2VChAprDFEikgmbUqZ2TYNK+A2RksNh5qN2lct+wNgfSa8u1PrBK/BaszCt9FNBTA711HZ5KqU3TKyqSq3mLQeL72BaLPev4/hAdMj7BbtMuSh/59gLWLwNsVpQUE+P99GfvCN7xEqqKWm+4BtvwQ1qRdXEi/9oSA26RZ4cdyxaJYs+BVLUaNDIXovMytHXV+T02nuKMZFVFGqlWHo52POzupA0gmbBmOHaubw5PJ4gI8r1IimJHu1S8yrCJEU07ls5Y+VIYrRmDG++914s9IkswLYWwRk6ZvKFAkxu9kqIzpdAnZ9CF1b/BBpQ8j5Qomc+IS3HAzxyy0GhQIWsBJvEkkXUOhGuk0olqoPzyRM0hTjJJDAP7DLCqErrYO7dHrSw7ylW1nX53K0pMKttzUoRdTxcO4kYFWvc1byvSAkoUL4p1LDY+6dd8UkZBPtNTNbP4WJQoxTMguhu3oT3u/XsxIvJ5B6bpvT2ZlHcB4a2Yw2tr6L7kynrGCh5YW5h8IDeEDzXUpF93wZGptyvm5sKYt5VXwFC3tP2d1Isv07S3YSB8onGJ0pemT8oFlRbKw2aNKG1wRIshiertTp8pFJl33JnolLYCD/WULvXJfrqIvjGKHLfRqYzz9bI28SQVpMVmr+YccEVHGyrMUx64dMkNqu/pLhNVCsuAejpiDXJelu59vN2yI8+3rGDf1DCHbEWu8PSWKXcjbAsdoWVbXUpbGf11kqbRQj5t0vVwktqKbk3VEHjREEvQ+K8AOvfndtSh74CraIDnq6P6oHm/1Pg50RkmrgN6PJ7P+7JnWa1CwHzIacDhxFO9SLk4A1eGexrNwyNK1Vqv7QGTATfi/59WzmNnWiVJw/fybzk9uMK11AtM4W1RWGkWeO89Ut/78B0z3Rqpd7MEkYrIJDPifYV4srsfENtXGHJXk/uV1jmZhgJPGzwopLMJA0p3xCykI4RMMCqIE6TP42DNwah86lLMBPC+pOVjN5ZEA8ULzgnVJ04wBTkEZ5j79JyJ0BADNG8AzUQGSgRiBT8fOSY6/wBMtEcDAJ1BgsmJ/aXus38i+VsHx8v1TrtSezFUuTltkWcLCGuBuRO1E9NBHztz4cEJsN/08tUTOLudK8mGlIXVUSGHCJxnQ+R2wm19IFGvCRtPomNlkjYRZLWE0ADxpg+HS7eAHXKkW9+9gjDCruaVlbBErTu3rQgYjEkhpm1VyTwpAe9viOwEJ2uI2XR3R/gACvMCsO9Xg74fJOuvEY/yZStkuwaN457GdefmWtz7bVrJBdy17xvx44/TrkKHGjCymeW8xjoiRcaX249j15dpMBv6IDV2BLMXQsodt5NkGZvIwsWmFjXYW9lxmp1QyrLLxJwiBV4mCfieyKO37/ylHVHifbotdKifH6451CvIEzHDTf0SRZCZ/nUY6LOmMHFKX7zE4wRXaz6Na3hF1+vDsxD6mftm1K6dgz/xhKbhNDakLhn3h1mfBcm6KBKdLo4+UU7VKRmCfkiY9YxjrG6z1H1/mwj0DNDVIzZut32SQCdIXf9ysw47RHN8mS0EeLyDqiuLiy1q3cZGYXmzygOl24i9X1M9xeAHfTyNoKDL3mwRhbCYbu2vavPaQNXJMpqwjJ70eOI5Q9KWKRbVMDLu61HAm7jF12HZCPIC+A0AZzwqudhFtmNqyG22HFIFinDssmiZ/JrDtwGt2lroGHUWP/h7yS78QwO0q6zvL7BQDf4UDXfH9dKfgEdTpR7DgIa8e57Ow9WrkMBH4SU6oBd5vV28KL2IWIXH2ZPajotJP2ETnwg92j5cmv2wdMPajw3BRbIRhIqzMFKP8Yy7byylyqEtmMCNKY1NXyxW9BRkChuocDtaJkb96lMCRUHtazdHsgz9vNXjYkZZrh0CDMMj7MKLIA6SMcoCm6LYm8eqZua6fBo/KBnEj75+FWjw9H+PjCJiW8XvEDAEKkc+CpoBOLw+8NdU+yg+KXzKM7IJM4xrX3nDldZWIYglr3dfPP6t4kawgtpA2N2B7N6cAJHxUaSP56xodFujo0T74tLFvhaZnRkIrgmveCqL78uU4Z4u30J4vL7OzpCAnQd0ROlLt7IewuMCFS5x+PPtRdHQ+ZW86nnSGlsFgXrw1YjTGtIr+RebCpVLWCmzQZ8AsXmugHxI5IXmhdLoymj3u8bpgg8FhuaLrR/tlTOVscpbFW9OBCoJse1IIz39vrhdu2L2gla+2Y0zj60NMLY8R826gM97MkYdYgv80WU7A5j66K/GsXblyUKU2395hZikR1frlcE+wsYrXoUSy48ZmJY7sLes89cyJ7D3OzLIQnM6M+Bzgy8rTCK9aQ1o2/qM/ViMQ2ZvPfEoKT0iVi5P8+tiDIbRiLNC3A03gwaxR80loIXgKXRuyrUg1NBD8NnkcQgEc3TPqSSy3jkEuedqB1RCvVjFp0tO0SU+3D6BWFOqamnJx98betkigH6jORaqgnU9dl+cOFVqA/Nz8uw9JM0C7LUF6Y29q+iYQunigTZ+gOMIrc14Kw0UUbcoy4kerla08gtyVhWGYMdbCyRZ811XnqtgAb+4YLvEV030Ip59KfPaMLaZoTa2CwSUuKOdz0VqnYqnAM0En5VOCRaCNlfK6yxQGFkZQIaHg0UhhXOGWTCq/ZKVZRXQX54uacTqj6odfh//5xKsB7/6BJITYEfHj5UK+dfzTLXLs4pKzBzkkjL5onciGrX2jiE3ErghPgaArxY2podWadI3ybrvpX9dZ5zoNZiwugdvcwPZQ0ZMrVhYJzlaS/JEydwZchi2Rbf6DbyjFh2/LZR1Y0ZdIYm4KKI7WTkSYf0oMW7M50anAku2irP3bveTqoLqY2+WksStKN50obt+xsv419iaxQfDxE3jXZ199adpz8bYw0MvXxBbDmFPW6diZb0sAlUD4XuRmmC64zNOEddwsBKPda5c9/PEDt+6GfwXadVpMNgTsdQ8YBIEX+D4IxLItwryqvianpdYmCX3rfkED9utxLnBiKn+HBoCkGTcTGfKpe7CvmkR2shF+27AfAajIiQBsS8GPrd6rUS6gN7+Y3/UToUf4RSMMOeLCU0D8nq0MyOjVsi+pzuZos0VhQkn6QacvsDU9Xg8Z/3L2Bxo1JRutOO3jZnCUniogz8Ft7dZwe/nevQEr9bWGebcJN0ChhFw0GufSUAMWMZHO7alhFqpXTuVWTG8ihFP6WVAmnwfNjq8EX2CBmIICqfdMafmDXnCPuR2EOzFcsOgqvLOn/sV0suqFEH+rdS278Sj3b2Z+YKQp6Td4AL9i5dI8PierTx6MU9TxntMQscrosbplozRwDiKMGDv3W29MTjcabMgKbV3mbEZEzlV6ls8ipF8t4ROvsFCRE5U2sEPHcdFAQn8p+xKu1HYl/qRCPfMSxITQepg/CM9XlpWX+82AfvW4ic3uJIoD5AJvT5bCSveZL/Y8CvRM6iEscbCzVSih6wLeJWFoXRUPAG4lsMFHPkIqNt+deUiV873ume/FbvYdHCIt54yz2DadZr3XFgFcHI6GBCfqlcSDEaUcVFWWQi2JAQZPY+CN1IrmR/rsSal9AgE51qnFakgpCb1e1dKV1s6uMxIQe+/OEwj2e1bAVGwMymLjddzppMb8j1M2hthUTAD2gQJdj41njfJYICcNXWylEYah0H6BOwCOgTh0icR9E0OcH4tcFgZiBYAQWFQ5vbYxZXHxdSx1f2NiyN82t8CpG+1yU0L+9DvTj8CzUpAcRrj1qW5rbmeO8FMbRIGt426VcSgQAmIvNDTRTU3INgzOTpDFPJkNKA5goRYfgqBUFCEAYr3KwmN+e0yUbxeiHrImhHX0c26nRm+cQ3pLiiJqaMAQOzuvo9j/s4SSTbDedIjmHwJva/H55BEK+dJ8cpIE+kDtDdQV3e7gBu0dCa6ZMuomugcDhBICIoy4Wyjk7VuuZLpSy48+uOM8w53rQ8XDkZ9bs9hTdI56BosdrPZAoQvGhOG8kVQEJl1UBzJ/jtSS81glPACoBPmtrVUJDlmG4Hz54Mqqi8P1KccunqZ8bRpSdDejuvg3rp9i7gGYw477GTD8iaeluBNk/YQZSgrBPv1NmkpKc4t11iorqI1gXrKjIHXu8+Thu84LsMnwN89GFIFKVbOVozkkuve+Dlv1rJ9QaGvgvUS1UCb58ikHDt3R3GECA//BJh5kZPZLfSlIv3H6x3Z/QTkW5wUSumqPM87rLToTTRCxEoaB2sMSOlbw69nLGJhTKfFbHSRj5K30NZY10frRlpJMftJvaRIqXcHwOsgvPRdSsrAeZT1iTBD1dWkLfpycBujSbYY3lzvZGV9qjQ2jPZlJzrFR2v6frHjRqSiktpT7ln2Rjlwdnc+haSb62bQ6pMW0Df1+4AxdMb1jaPC5n6RnsRXyJ72cfYOTe4jtxO41qfUROSiNx+5E67h/PhEhvvCCAOdNwWAn6HTcCBxGEb2tVZitF8DTuXz47HQlRwkGyVLBiUSyJ8dpCAgYc6JZfSaipwQgWAUvY6x0QQaGoiyS+StgyT8hMAJeuEA2yxRVmw6Wo9VFods9La8xT2JOppqjnMHJww4CR4FIqvvpxHwVXpGXJIx8B7E3Q7qGrwqagPl0tOZ8cZyDSianEpiq72jvZoZtzDCFcqJA0Fp2se+IWZsSP2CRqoGqMciyQor1swOOHBZ8TxgGBvALVemssUYx2NK1oq4hvdHDKEF1tG7d2KXQ7dL9rb4iGnJvPNMPeJBmGIDK1bF1+F+AmVTa+CtdRTiBWozfjo7JdIr7OClpJTDk5BeHS48aD2VaToywz7AGWat+qXDlOdr4tsY++6nq2x6/yl6VFw1uLvv5NG/QKzEFuoU2rCCBUmAJDJj8UDT9D/+8eu3Xz+oxz8xbv8BHfrD8Pp/w4X9Qf0a9idmn2Q/KLQfTOLff4/19/+UwH//9mtOqif8H7Czpd2KP1Fif6LO/vbXyL9NfyLo/i/X+Q9e3RoVPwjs/53p8+C/6NzPxV+jy7Vrf/3276zc56qIuh+wYvQXue13vuvvNLYnrf+Cf/3zfwAC58/Us1wAAA== -->
