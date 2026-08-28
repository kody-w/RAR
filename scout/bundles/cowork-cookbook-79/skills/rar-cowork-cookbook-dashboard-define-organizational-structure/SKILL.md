---
name: "rar-cowork-cookbook-dashboard-define-organizational-structure"
description: "Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_organizational_structure", "rar_sha256": "745c9b4f1d090b999e659bb359b512711baf57da4e4244158ac416f78bd226c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_organizational_structure_agent.py` and in the RCI capsule.

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

Define organizational structure Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
      "type": "string"
    },
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 745c9b4f1d090b99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_organizational_structure_agent.py` first:

```bash
python3 dashboard_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_organizational_structure_agent.py   # or on stdin
python3 dashboard_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_organizational_structure',
    "version": '2.0.1',
    "display_name": 'Define organizational structure Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cc5c9486ebf52de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:define', 'word:structure'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class DashboardDefineOrganizationalStructure(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(DashboardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
