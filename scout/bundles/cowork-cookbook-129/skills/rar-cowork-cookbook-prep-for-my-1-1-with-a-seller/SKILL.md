---
name: "rar-cowork-cookbook-prep-for-my-1-1-with-a-seller"
description: "Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_my_1_1_with_a_seller", "rar_sha256": "3ad8663cde83893b7fe1f882c0b280d23f48a317415b453d8d8791cbead4a0bf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prep_for_my_1_1_with_a_seller`. The original RAPP
agent is preserved byte-for-byte in `prep_for_my_1_1_with_a_seller_agent.py` and in the RCI capsule.

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

Prep for my 1:1 with a seller — Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_my_1_1_with_a_seller_agent.py` and embedded as the fenced Python below (sha256 3ad8663cde83893b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_my_1_1_with_a_seller_agent.py` first:

```bash
python3 prep_for_my_1_1_with_a_seller_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prep_for_my_1_1_with_a_seller_agent.py   # or on stdin
python3 prep_for_my_1_1_with_a_seller_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prep for my 1:1 with a seller — Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prep_for_my_1_1_with_a_seller',
    "version": '2.0.0',
    "display_name": 'Prep for my 1:1 with a seller',
    "description": "Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prep-for-my-1-1-with-a-seller',
        "upstream_url": 'https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '309c9ee888e989b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prep-for-my-1-1-with-a-seller', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PrepForMy11WithASeller(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepForMy11WithASeller'
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
    print(PrepForMy11WithASeller().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
