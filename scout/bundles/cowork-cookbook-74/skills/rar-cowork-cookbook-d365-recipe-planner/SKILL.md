---
name: "rar-cowork-cookbook-d365-recipe-planner"
description: "A guided planning skill that turns \"I want to automate something in Dynamics 365\" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_recipe_planner", "rar_sha256": "1c3b4425cfc86a5c3d5250975e457e3b2a96017af042f55656e0590b20e8d70f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_recipe_planner_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-recipe-planner:b37a2e1f7cc19449a9db46d0716163493fe63377270de596c442bf8c3801d57c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_recipe_planner`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_recipe_planner_agent.py` is
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

D365 Recipe Planner — A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
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
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_recipe_planner_agent.py` and embedded as the fenced Python below (sha256 1c3b4425cfc86a5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_recipe_planner_agent.py` first:

```bash
python3 d365_recipe_planner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_recipe_planner_agent.py   # or on stdin
python3 d365_recipe_planner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Recipe Planner — A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_recipe_planner',
    "version": '2.0.0',
    "display_name": 'D365 Recipe Planner',
    "description": 'A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'beginner', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'd365-recipe-planner',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-recipe-planner',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c36f119a3c6418a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': '2026-07-28', 'mutates_data': False, 'plugin': 'none', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-recipe-planner', 'uses_skills': {'custom': ['d365-recipe-planner'], 'ootb': [], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 0.5, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class D365RecipePlanner(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecipePlanner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
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
    print(D365RecipePlanner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
