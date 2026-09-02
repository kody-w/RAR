---
name: "rar-cowork-cookbook-demo-data-develop-product-roadmap"
description: "Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_product_roadmap", "rar_sha256": "c903bdbc815fa19b10b51e129769d42097a000d1d3b045d9733b56fed8e59d5b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_product_roadmap_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-product-roadmap:366d21c5df81e96e3b0d577c004fdd2fbbb2044858a1128cf756794c866663a3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_product_roadmap`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_product_roadmap_agent.py` is
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

Develop product roadmap Demo Data Generator — Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 c903bdbc815fa19b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_product_roadmap_agent.py` first:

```bash
python3 demo_data_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_product_roadmap_agent.py   # or on stdin
python3 demo_data_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Demo Data Generator — Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_product_roadmap',
    "version": '2.0.0',
    "display_name": 'Develop product roadmap Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50578c0979f70e71',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopProductRoadmap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProductRoadmap'
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
    print(DemoDataDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
