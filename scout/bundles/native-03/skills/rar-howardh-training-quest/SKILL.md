---
name: "rar-howardh-training-quest"
description: "Generates a personalized interactive training quest HTML page based on this brainstem's loaded agents and features. Call this when the user wants a training guide, onboarding page, or wants to learn what their brainstem can do. action=generate builds the HTML; action=preview shows an outline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/training_quest_agent", "rar_sha256": "fc213fa839cf3f39312ba03c31e47e55af61dd636bbcd671d35ee48383c78ab5", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "training_quest_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/training-quest:82af4432088ab4ded405ac070d229299830c042714c453a2ef9e568290f5070f", "kind": "skill"}, "version": "1.0.1", "author": "Howard Hoy", "tags": ["training", "onboarding", "quest", "html", "interactive", "gamification"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/training_quest_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `training_quest_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
