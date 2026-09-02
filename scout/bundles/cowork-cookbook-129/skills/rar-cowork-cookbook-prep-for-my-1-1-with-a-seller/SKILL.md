---
name: "rar-cowork-cookbook-prep-for-my-1-1-with-a-seller"
description: "Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_my_1_1_with_a_seller", "rar_sha256": "3ad8663cde83893b7fe1f882c0b280d23f48a317415b453d8d8791cbead4a0bf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prep_for_my_1_1_with_a_seller_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/prep-for-my-1-1-with-a-seller:7bf270986eafe3a7f9cd5a92aeaaaf904b95e54f79e8a8671fe05525433bed69", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/prep_for_my_1_1_with_a_seller`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prep_for_my_1_1_with_a_seller_agent.py` is
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
