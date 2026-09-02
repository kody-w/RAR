---
name: "rar-cowork-cookbook-upsell-identification"
description: "Find the best expansion opportunity in your book this week and arrive with a pitch already built."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/upsell_identification", "rar_sha256": "b38d258a531fcf523748fff8473682194181626f8bd13f32268dcceaa7e9f8c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "upsell_identification_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/upsell-identification:acd08e0a3c1808db9d367108a19bae3bcdeb8017c6ac5b858f0afe5b63987a75", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/upsell_identification`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `upsell_identification_agent.py` is
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
