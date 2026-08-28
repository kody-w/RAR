---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-certifications-and-compliance"
description: "Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance", "rar_sha256": "93fe72dbeec7ab8381dcbb09e66efbeafadc8a14ac13264dee8e3fdbc7eafbcb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and in the RCI capsule.

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

Track supplier certifications and compliance Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 93fe72dbeec7ab83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` first:

```bash
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py   # or on stdin
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier certifications and compliance Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance',
    "version": '2.0.0',
    "display_name": 'Track supplier certifications and compliance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b671e8e5418187c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/track-supplier-certifications-and-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-track-supplier-certifications-and-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefTrackSupplierCertificationsAndCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackSupplierCertificationsAndCompliance'
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
    print(ScheduledBriefTrackSupplierCertificationsAndCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
