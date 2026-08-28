---
name: "rar-howardh-training-quest"
description: "Generates a personalized interactive training quest HTML page based on this brainstem's loaded agents and features. Call this when the user wants a training guide, onboarding page, or wants to learn what their brainstem can do. action=generate builds the HTML; action=preview shows an outline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/training_quest_agent", "rar_sha256": "fc213fa839cf3f39312ba03c31e47e55af61dd636bbcd671d35ee48383c78ab5", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Howard Hoy", "tags": ["training", "onboarding", "quest", "html", "interactive", "gamification"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `training_quest_agent.py` and embedded as the fenced Python below (sha256 fc213fa839cf3f39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `training_quest_agent.py` first:

```bash
python3 training_quest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 training_quest_agent.py   # or on stdin
python3 training_quest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
