---
name: "rar-cowork-cookbook-adaptive-card-analyze-asset-utilization"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_asset_utilization", "rar_sha256": "63d18793cb053871d1cf33e04ece4f7e1476323e7c17f552f701c9bba3fd4f5d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_analyze_asset_utilization_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-analyze-asset-utilization:b49dc63e6d07140003ed9a7c95d5c061340b7debb60c1d6b4ab37629253b9a4d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_analyze_asset_utilization`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_analyze_asset_utilization_agent.py` is
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

Analyze asset utilization Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 63d18793cb053871…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_asset_utilization_agent.py` first:

```bash
python3 adaptive_card_analyze_asset_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_asset_utilization_agent.py   # or on stdin
python3 adaptive_card_analyze_asset_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset utilization Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_asset_utilization',
    "version": '2.0.0',
    "display_name": 'Analyze asset utilization Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-asset-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d0de65dc478ba4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-utilization'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-analyze-asset-utilization', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardAnalyzeAssetUtilization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeAssetUtilization'
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
    print(AdaptiveCardAnalyzeAssetUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjWJLtX2FiPlTVkJliB2Vbmz2EJBACIbSwVbZFsYPYd0G9+u/vIkXkMt010z02Zk9pGSGJe3057n7cL8TvL3bXRkX98vnl7Ns5xNtpGkd+Ddm5B3HFUNQJ+FUkDvgPuUXe1rHTtUXdvHx48fzGreOyjYscbD/Whde5fgPZUO13je2kPsR6Nrjc+xBn1x4knpUD1OR22URFCxUB0GGn4+RDdtP4LdS1cRpP9iwOalq77RooKGrIzxzf8+I8hOIc8uwmcgogrPkALthxCn6DNRffzppPwCT/bmdl6jcvn3/924eXGLx/+fz7i5sCDcDEd3Nma9inbnZWff2mGchI7TwEi8sR4DJ/Lv0a2JGBrzw/gN4+/dz4afAB+o//SAa7DptfPn/JobfXl5f536nLoTbyobawm9b3INcubQeoacdPEJsO9tgAmNquzmfAGgBrHn567vwmqSihv87Xfn4q+RT67c9fXgpgwsPWLy+/zM5/eam7+f2nWUr58y+f0mLw659/+San6Zyb77azMGD1p9e3z29iwcJvS+PgofWvQOozvI7/5eU75+bX0+7ZT7Dz5dOtiPOfn4LLuuj93M5d/+df/kysG/luksZN+0/J/fUpOPJtD/j0ZvgvHx4g/w2C3xz6KvPP1ZYgrP+KJ2D5u7oP0BtQfyb7gf9/Ep3GOaiFd8T/obh/tAH+K/Trn/r2X234AAVfXtZ+CtK7nmvvM/T76/m44X79yfv25U9/+wOI/m/FnIuudh8SXjM7jwO/aV9ff/2peXz9099+/akrQa6Bmnvt6vQfyfxHuD70/IDg26qff9wL9F/zJC+GHPqa6dDvRflv9R+fIM1OY+/b981n6Pt6mV8wNDvxrvQJwXc10wBbv8Pxl5c/AE3kwJvOfVwGVf7v/w7JsVsXTRG00NktuhYCAW7jzJ+Nv0RxA13eivq3834nSZ8y7zcIfDuXO6AIu0tbiK8BOUGgHuaIzx4Auvvt/7gPQv3ovhHqwn4jpFcXMNLrGx2+Pujw9Ts6/O0TdImA9qKOwxgsgk7s8QjZoZ+3s95HhjRd9rGfVQOz4if1nLjdTDtNl/p/gX77J3W9PsR+KsfZpS85iJENAudBrZ+VRW3XcToCvgac5Yyt/xHwLeCVukhTx3YTaP7RlZ9mnPTIz9/Qc0Ff8e++27U+lBYusD+IAUd/AAnQFCnoDu2MaZPEaQp5cQ0AK+rx0YAA7p9nYb/99psDmP9L/iRlHHo2nmYBFnw1GPr4saz9II3DqP2S+25UQD/9/sdP0P+F/qtdD+GzjiOA4gEbSOz02atAlXYZWNZAc4oACnpE8fc/nvGYrctBpwS1FQex/9gMpH1LidmDZ5DeIwR8nk306zdNP+IGDRHABYpbgBao9+bDl3wWUYCl9RA3/juIz81P6N9D/tQzx6R5wxDEKaiL7LH2kY1zMN2i9j5BuwD6ihRwF8S1nSMaFU0LErj0c8/P3RHstNtvIcxBz25AijTB+AHqGuDqLPk3B4iewckAUdntb5DMHUHPK1LwYwbooR7sLvJ4Dvxbzj6/BkLqn0COrd5FfIIOPkATKu3aLqPabvzHusB+ZgTode/7gXAbyv0Bmlu8P8fokbyPzGP/dKo4P6eKH6eSLx2GoAT0/398edjO86cNz142a2hzuJzMZ6LNc9fs93NUAyPEQ/Kjar6NFe8M9M7NX/I0BsGpx788VwaP3HquefJdV4PEObGnh/y5yuuH3LgFGTKHvK7nrLa/5O9N4AMAB8SnmV0EhZzMtFB8VThffbc0Ao7On78NBNAz+eaiAGkNlZ2Txi4U+L73qIA2quf6egsGSBd/RhgUhBv94BUEpINUAPIhYEQM8hY0igd0B1AnM8yPpP+6PJ7HrPIZWw8CheR/gvQ5r0FuNpDjg1lpXgNQ+OkhCsp8gDEw8SvCTWSXT2PmWfjNQHuORZHZrf99BN4ughyduw3Q97UAgVTAvy3AcgBBAPV1f0b2q51vsQLGZnMxPDb9GO43X6Hvu9Vf5iIENn5rBWB8f6TuN3AAc9dZ8yAj0IKTBpR55r8lEMiER0//9GzLz77/1ZbPf3cA+PlfOyM8Gu31x8h9hqK2LZvPi8WzGb73wk9ukS1AjsSl33ztix/nXvXxrc4+Purs43d19oP4J1qfoX/NxB9EvOX2Zwj9hHxC5ktS7Ppz8r69ACLcx5X5kZivfslP/rdQv+XDzHKAeZ3xa7N5XwI6Tlj74bz42XyauWcNoE0+OO/RPL6mw1uxAErNw7lTNsV3RTz7NAf3Gbuv3Awu5TPre/O0F/rzcSidzW/8l895l6YfXnI78//pY9BMwiBtASTzEQqUEBih2th/fPo6Ts0ffjwGPooLsIJXfJ5rDDQ8MPp+gL5OsR+g93PF47yWd+Bg9es8Qc8qwVLw6+var2dMx38Bx7l2LGfzn4eleXB7G6j/3oi5tIDFgM6b2Zb3Wp01/p0Q8CYM/frvhSiPN3b6RhiA0+c2CbrzW5k3wE4PzFaAyvu5/EBFAaLswIa/VwP01H7Vgcbsze5+w++bW8XTlz8eMLTPE+fvL+/EMb9/TgnP5AEb/tWBbkb2vRG/zvLtWcpj7HoA/RhcX4GT8dxwv7sUztPD6zMlXz4D8vE/vMxw1jGYxqfHYfvlaRTw5tvICyQAGvnYzAPEAlQUkATaejl7kgAK/E7B/HXsPdbPbz7/6Zz83/DBZ4dYei6F+5SH0CiBIAjue0ubdpekR7oIheIE4tCe7zgU4qIe5RC2g9MUtsRI3FnahAdsmaOa2W+2LNA5HsCLr6D/T0f4l6cY0EwwkgJyKNxDGXqJuw5C4gyNeqgb4LiPEL7rEwHtowRN4Rju0y5KBySJBTSCukvHsfHAIwJytvR9enza9vo+qb9H6MkOr4BWs3i2HLNtl3EBLN6StinXxxEHd30UQz0a6CWXeMAwPuE/MHhufYvSHMSn+3Mag8ERjG39rOf3t6jPqUkRYKVANDv2+eIWS82mDcm5R8ZyogKzuDGFeAYdRhLA6alVthsNw83Eu8EqkqAbgmJFM4m6lb6K6US+FwdREcbVMTsbdUd3+0vKjzkC5xuCUc+N0ONBSdJ0Ka42u7vilmQb3G3ZHhG5IiaZlBfuWdQnjjkcSi8Vx7C51cOVJnVjH/R9qi1sSuMzjZMRYo/oqW+N4mCXCyOf6LjL3C1etevtQbp3zPLktJe0KhMzUqSDaJBxk7mlNvbmoEV+sTMM3iG2GCBTiT4ReoQw/UTCXj4lk5cbtDJp2EIJhpuV0VoYu9VhZPFbqmX1tazaVO/1a61sttPEN0bM48Oga8QVE93zQY4yoz8MsKd2xqZzCFGLVNE2q5NbKxeGan2OnK5adUeKSxOZQtiUl+R24HkS35WtmLOy58cof/LLclfTa7tSTJBUedWZ58vSKC+V3qnMZVCZLI6IRAlKToZrRZRFfahO99tIhgmlEru9WqGjamELXU5znOZ51eBJ8VDIHNJxQXYfOp/SQoEcaemgZ4Z6l84oT8R7q5GuxanpFgYuceN406WTbXU2i8sC2q4c7hhi+OWqbO3e9zfI1dc1zcQui6XO80sBVWrU4i7hcUKVfMUnB/cypVGx7Ijjldn6S1dc9ctA4EJR3IUeJpTR0nPiA9IZAkcHt2rs+o3meyl/ZNomr03fvNpXHsGUe5STqW7V7WkDG/cVqVm6GB5cs6PZxaGoZczOxrIkKu9k3I64NeyMm5J38o4Lllbsyun2uDrf85VUqUzE0C0AzGqc6xiR9MEyb24WpLBZyYjMnzdSoQduugyvvOUpwVU7OOC/cje01Cfcg+4GJbYywmZxU4KmObLVkVFMJ1Nv++uCEfBb7AW9sV4KCiOImHRoWHh1PpFB08eSdxD3anezFvo53i/1UrudiObGn81gu+0yGZ3ia3hbVUnDGidHyuBrwXLSpUK5ylKnLbq7KgVzH8NisakOU0hFbr/fXncWq6D8VTsZ9ul8N3GT3sUyl9vjyWh4d3W+9nGVatZgSyGR0vlCOQyH/p6OBINMBXy5DnGc5Il5l6xsc/ay3QhMXx42vb5bbJPFhbp2ck0dqFyG16Xq7F2JxMTFsCCCUr/xRlRdLvdRi3tvMaSu043Thi0Sce9wSts0BZkW+O0cKpfWpFjztjKQ6ch0XCIvvLOUCJja79Fkf97fdvmeRoq9P5ZTqO7VM6zdFn1cksHVpk56lBSVsjgKiRs7O1Oi7xXn2b0mJSkxlTTfGoFWTqo0iWeddUMWPp3j2MpKZ21Tm1uCYpcYHGvTncnxvinpagOvpTGZrEkw5FxIN32cBpQF01IrjEe61Ye2USndDKjD5roW0+t1TwZtP50C45pGw35ke0ddWTHGd1tL6w2F31An55po99WBcMyRQMpsr29rrmtlagc8jJWrhxiZXPGlf7kvrqgVIzU5UeNBrBl7rUZ9X1dtbVkr1kct3bqakkCsTbpy7CMpKFVktDCydvFzf1tcvYUo1f3Rvq735BI15Ws3hnHfBofrzTvReOKhoCh48aoLp4otE+VAHU4r/cYJI87XAbPKk7FLShguhCg5NN7ZrdpTjjCN7iDbfdEVuKPdlprv2N5u4bLSUG7ZrXhxUrY/UocFKk1s3Am8qe7l8nDa9K0pVlaL4fWJOKGrKgo3GULEVGJEl9DZl2bSE6QxHYVtVAwVRoztQd4I+/s9dTbuYRQJteSq9sYDyjhoES1blb/EZDq+yNepyQ1sMvtLg7qGNarny6YtOa3De4Spxsuayd1as5KAy9shLrAAhXs2vwVnkhrO2PquY3tbEyrjNiobBF7A+14OYBdGLveM2PFBhyseY2crkd0H1fkc3Zyjvze3hK25UqadLd2k8w7mbMY5BV23iSlWEwwcoeQcoY4CgugHu7ETeXVxY24qY448J63c1qpIcMne3YwsjXABfLvG2e2+VPvjwTrerFrXpUUh7c+w28CUbjPc0p/gMJ3MbruLT8Z14tnlyVyOnez1nJbQTmEVo1RHFkahdHtMVW/HEmtnUe7JNLUOfatshB3KW40/NM4w6feDkwsr6TSdYdwb0b4wFf1U3nmO2yLJyWzGttRPK5URCIzmhIiNzi6PY0GbSNx6u2T6jR655OYmdW3L012YnxGWVSx3pR7yOjjyKqFzq52YN9kZwzLOktQmgPH0HOPRargQm4W36uS9iqL7NeuvkEzq+FiC8YiLLXmHXyd1Op+uKzUo+BtnDzWyXWFqpzPn8oimhH9OuOh0v47sUqHk7bXaWr1G8gEvRVJ4va3vCDkGx2yh7yv5prCFscIjse2Ti6ZTOaJFgzqpPRlfs+1QLVsyL/RQWi6dE7Y2UwmtyfVhQY2kUqXlXqvsU8Qhyq3SOBCLybVv5xXi9J7tHXWkvx722WG4VrdLs8dLRE2WPJEiMdcc/LC4Z+ztWMiDLh/PrTRxmp6E7abDBJ/dqlUaj3uLo1eoCiOjaO42Yg2XrIAMuNku7E26sxG2sb2FlzJY7nNEfmmFHekyp5DXNkcRs1aoXDRU2sXV/qZYy7hd44spIgmKOUh7O9HOSeg0MEOzniRuvN4oSeTUiaDi0MCoUkShMQs7R/ylCkAKWLmV2WZmbW47Xu+xvtmemlDenleNfLg5G22QCP1i+tLqKnoxb0WxUhS9YVEusiFQkjMtg0WvyxFVSL2T8t1RlkVAVvyWV7vLTuOkkfaRreg5e3zssiWZdCfktOqNfW6t+kZu2Z2iLqoOdq4bjVI0bl2OSnbdMmWVXKiJLbVuL8oBddnq5dbgOL4Nr/uNbV+3rFI56iI2/OKsBc7hWF2mRmwLIeyqYLRc4u5d5hulPE7Kxwg7Ncc6TuK9a9KxcgkZZkJu7SYWo2sr0uLAeCsV9oPddnkZT4gdiWQpBJckGpwoFY9qf5P3u7A6XOxzHcEro4B3hpKjZe5fU7Ngdkyru8trvdFI56yVnSphCrkYTtmxtNZwcrhuFzu/jiJ2t6NPA8fQg+iojoAZgnAp93eatJn7epX7RNYR5XJjNiET056itGiHaml8WYg64og9fbntZRwuV6zar40NlhINkUo7tYBltFTJ/V1JvGvore70SYkzCSDaNK0EKIzYTGyEMniEa+ftcizwlr41sX0rSUU5iiqiIjwccBlIvD0rXKusOPvsHrvU0u4mZaiRccRptzVMP0tNUay2l300nveJsXd0jPSsjjmaeOmw/Rk5YEnHJKeKsid5jUSM3IiTg1VJnbkKvDFk/1Ieyit/2iT+wpKC+GoOTtHfKVOnryC9UM3QqO1RUC/amVN34gVGKzK0bzbJIlHkdo5pyEIsW3f1bkxkEDJ7dhqXOFWbHVontI2Ih0piDVbv/MxaeZjcmVZ17B1451np/SCwqu+FulfmzQVPmRp0/62H61ydTDU3ZBamMSW/1o6ulG7Txk87kAbr6w4z19ywzthmL+8sTNoPMH/XCnGIBMytDCwbvdq39Z2mWguVC06LqT6yE6cPguO3bcg1FnEVG/lCO0p/G6zTKTIi3hKJI+jpBc1EB2e/z4Kr2mILZ585zMVf8PiJc4QVjRajf1hj2oEpwpErTk7uH/WMyrs+jzgBDddkEez55bHtnfTWtt2h4+53OCTwCDFwGKYNo4dDu0sui7K/k24haD18pmnpHqxzB5UaRuCnuo+ORbdnC730J9edjLbK8XNU8WMRMnnHharn6Ud35S5bjlneDugVPaEyrx9XG686VZc2YXZ2JS0mPzzqG9Q6NMk2z1D4Eqs13S13g6wHaTfgqJCrwTpIvQsW3lGQzO6CXueFU8DHRaDZdrVQ+ZA5hsvc8j03s3ZGuiK8SFpqHt3r4FCzTsAA3vcLiuuplc0bVrWAm4DI4LwR8OvRg+GuEa7lutlebheMq2Nh8MOQ4Zt7O6ijBA/shg7v44LacOeduIqmZZa5WqgqnNdxmwiNYFbkhe2BCBV2AClirEwddgyp8hgSUVn8XMu5158IRTi6J5sjibiQia7GU0Ex+20pRrTKFE1Iw9HOW9pGPpCsgm+NCyKWAnOMOrcL8epyCtZb4SQFTt3X+07trz49HbaUZu4NITv0uO8xHsGvdiuiJ5EthtDH2DxcBHt5Gj1pcdgv+MWNYIadfxVwTA2G9eZ8OsLT2MGrgVqDuaeTs6EiYfRoEjEar5aW3k6cox+bSjJsn/KM666X7qf7fcSbDD4qsHYRVgc1LGEKDw7hcAFDA9Oxjdaa5Jq4FSeW3Jj96ei1AXqXbyvlbpmwIXbk2tvUx9EFx1d3uu9WjOVouRBeGWE0EtaBqftN5sZ7TpjkZXnPp5gcaMAfI8yissr0VH8TqO5WILY8rA/IEWW92FbT3rtXGG1utj5xKdlsOKcK7rNhIyjxyFe6hNJ364p7GF/L574f7sqmrqRGhKcO5bEN3UptxuFx4E1InNzbSTQlqRQxY0qaRmHH8FKivntalIp61ynq1hdw5+Mtj/siNwrKEGhh6CyIO92vQ0fh2eA+mLej2bF3BWMWA+3h236Xmj7CsKQprdrigJ15AvMUJ+ubqrWXBd1LhCGpd9SphkbY4timRsnuHBzsgd1PXVqvg/PKy5q7XKwrObiLYzCGG0MEWVUeC3+kqFBbVp1gtes+2vYZC47bi6aQImXZU/hgm4dlRwmjvOz2CzgXmQPTyEt8iVDoegxvmNOcJgkzq37hnVL6huzW9M7qYHjKJZ9UKCrxvKC8rxe0JGHURsXzYJfdMQlHxXCxMb2rb4bZxF4pbeuPfdbT+/uBarGNrUQ2TNo1sm7WQb9G1qp62ZRn/O4uYP2c73TRrgBAyxRt8kzFg3231GnVK2Ek3bEo2aqRRh/37LrwsIBl16ekEYdk8jZgwnb5SCi7EtbJIxgol1hF+opC0XmjhTK36Q+UQMuBhVDhCXGP7VDXXSLSpILnU8Jus1FghHNkX9b0elQqpthSOrqbivWBtqz9ekkbLVZptOjhkt47NhOuBV21gpb2bSlY4fVUrKSiEUTn1l8YTMCUy95zJjNy8u1wpxDm1sFM2ChRx5kGrG+kBOebtNUW+2RTBIUxYRf72AYT61sIRgg5qHdQrALFIZUsbjF+I60vSyJ5nDnJVEhCzF74gjDsHBeNsK2Hymh0pyhmnQQL1l3XZKeXe5VlXz68PJ70vnxGEYoiP7zMjwXebu7/D+4Kh1Ncvr4JxGmM+vDyv3eb8nnL8P0h4ONWv297nx/aP//Ltv7tw0vtxsCu5+3kJu3CtxuU/+m27Md/8o7xLGR8Pr2en1ze2/dHJa0dPu5rx7nXNW09vjZF2r3tcLpm/luW5vXtEcPLw8WsnJ9X/ODS/Nl93PV/bYtXL27KovFf5j84mZ/J+YDQ2vePYf1ujzeCSMZu84pT5Ktfl7PTbw+m5ru485Oplz/+H+ETKaa3JwAA -->
