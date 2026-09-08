---
name: "rar-cowork-cookbook-build-your-executive-command-center"
description: "Generates an interactive HTML \"Executive Command Center\" dashboard in Microsoft 365 Copilot Cowork, surfacing today's and this week's priorities, meetings, Fabric business metrics, and prescriptive actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_your_executive_command_center", "rar_sha256": "0088d6181d9c170493b061454c10ba3faa4ea30653278e8415577461eb892f91", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
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
