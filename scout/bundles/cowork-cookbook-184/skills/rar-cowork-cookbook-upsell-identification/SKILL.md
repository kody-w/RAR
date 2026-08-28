---
name: "rar-cowork-cookbook-upsell-identification"
description: "Find the best expansion opportunity in your book this week and arrive with a pitch already built."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/upsell_identification", "rar_sha256": "b38d258a531fcf523748fff8473682194181626f8bd13f32268dcceaa7e9f8c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `upsell_identification_agent.py` and embedded as the fenced Python below (sha256 b38d258a531fcf52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `upsell_identification_agent.py` first:

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
    "version": '2.0.0',
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
