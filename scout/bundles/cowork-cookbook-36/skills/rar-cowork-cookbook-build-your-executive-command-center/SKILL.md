---
name: "rar-cowork-cookbook-build-your-executive-command-center"
description: "Generates an interactive HTML \"Executive Command Center\" dashboard in Microsoft 365 Copilot Cowork, surfacing today's and this week's priorities, meetings, Fabric business metrics, and prescriptive actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_your_executive_command_center", "rar_sha256": "0088d6181d9c170493b061454c10ba3faa4ea30653278e8415577461eb892f91", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_your_executive_command_center`. The original RAPP
agent is preserved byte-for-byte in `build_your_executive_command_center_agent.py` and in the RCI capsule.

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

Build your executive command center — Generates an interactive HTML "Executive Command Center" dashboard in Microsoft 365 Copilot Cowork, surfacing today's and this week's priorities, meetings, Fabric business metrics, and prescriptive actions.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-your-executive-command-center
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_your_executive_command_center_agent.py` and embedded as the fenced Python below (sha256 0088d6181d9c1704…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_your_executive_command_center_agent.py` first:

```bash
python3 build_your_executive_command_center_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_your_executive_command_center_agent.py   # or on stdin
python3 build_your_executive_command_center_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build your executive command center — Generates an interactive HTML "Executive Command Center" dashboard in Microsoft 365 Copilot Cowork, surfacing today's and this week's priorities, meetings, Fabric business metrics, and prescriptive actions.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-your-executive-command-center
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_your_executive_command_center',
    "version": '3.0.3',
    "display_name": 'Build your executive command center',
    "description": 'Generates an interactive HTML "Executive Command Center" dashboard in Microsoft 365 Copilot Cowork, surfacing today\'s and this week\'s priorities, meetings, Fabric business metrics, and prescriptive actions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'integration', 'fabric_iq'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'build-your-executive-command-center',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-your-executive-command-center',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9af37ae5040f1fc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/build-personal-insight-dashboards'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-your-executive-command-center', 'uses_skills': {'custom': [], 'ootb': ['Meetings'], 'plugin': []}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A personal, interactive HTML command center that surfaces what needs your attention this week, where your time is going, and one or two prescriptive recommendations grounded in real signal patterns.'], 'confidence': 1.0, 'deliverable': 'A personal, interactive HTML command center that surfaces what needs your attention this week, where your time is going, and one or two prescriptive recommendations grounded in real signal patterns.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself. A personal, interactive HTML command center that surfaces what needs your attention this week, where your time is going, and one or two prescriptive recommendations grounded in real signal patterns.', 'expected_output': 'A personal, interactive HTML command center that surfaces what needs your attention this week, where your time is going, and one or two prescriptive recommendations grounded in real signal patterns.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': 'Create an interactive HTML dashboard titled "Executive Command Center" that shows me what needs my attention today and this week, based on my work patterns, communications, priorities, and business performance metrics.\n\nInclude:\n\nHeader bar with current week context and an urgent action banner\n\n1-2 high-priority alerts with clear calls to action\n\nThree situational tiles: Today\'s next priority · Busiest Day · Work days Left\n\nKey business metrics from Fabric as a business-health strip - show current value, trend, and flag anything off-target\n\nTabbed view for Meetings, Priorities, and Org Pulse\n\nA 30-day interaction map showing who I work with most and how often\n\nPrescriptive recommendations labeled "Dial Up," "Dial Down," or "Re-engage" - each tied to a specific person or workstream with a clear recommended action\n\nDesign: Clean, executive-ready, built around the question "What should I do differently today?"', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A personal, interactive HTML command center that surfaces what needs your attention this week, where your time is going, and one or two prescriptive recommendations grounded in real signal patterns.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates an interactive HTML "Executive Command Center" dashboard in Microsoft 365 Copilot Cowork, surfacing today\'s and this week\'s priorities, meetings, Fabric business metrics, and prescriptive actions.', 'example_request': 'Build me an Executive Command Center dashboard showing what I should focus on today and this week.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants a daily/weekly executive dashboard of what needs attention, built from their M365 communications, calendar, and Fabric IQ metrics.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BuildYourExecutiveCommandCenter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildYourExecutiveCommandCenter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(BuildYourExecutiveCommandCenter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
