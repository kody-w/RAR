---
name: "rar-cowork-cookbook-upsell-identification"
description: "Find the best expansion opportunity in your book this week and arrive with a pitch already built."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/upsell_identification", "rar_sha256": "5dcc9d0a5e848efb1783e4380d203b0bd66c9d7cd9f4813d8690ce8835a272b1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/upsell_identification`. The original RAPP
agent is preserved byte-for-byte in `upsell_identification_agent.py` and in the RCI capsule.

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

Upsell identification — Find the best expansion opportunity in your book this week and arrive with a pitch already built.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/upsell-identification
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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `upsell_identification_agent.py` and embedded as the fenced Python below (sha256 5dcc9d0a5e848efb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `upsell_identification_agent.py` first:

```bash
python3 upsell_identification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 upsell_identification_agent.py   # or on stdin
python3 upsell_identification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Upsell identification — Find the best expansion opportunity in your book this week and arrive with a pitch already built.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/upsell-identification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/upsell_identification',
    "version": '2.0.1',
    "display_name": 'Upsell identification',
    "description": 'Find the best expansion opportunity in your book this week and arrive with a pitch already built.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'upsell-identification',
        "upstream_url": 'https://coworkcookbook.com/recipes/upsell-identification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13f3dab5252a62bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/upsell-identification', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class UpsellIdentification(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'UpsellIdentification'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(UpsellIdentification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
