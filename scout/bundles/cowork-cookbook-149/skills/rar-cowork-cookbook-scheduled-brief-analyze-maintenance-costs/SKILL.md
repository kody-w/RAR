---
name: "rar-cowork-cookbook-scheduled-brief-analyze-maintenance-costs"
description: "Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_maintenance_costs", "rar_sha256": "a675d65b56c4f9df54eb2259b34b44f63de31b48779f1851d2d1203e74b4d0b0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_maintenance_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-maintenance-costs:3b060603ace8d8a72808be72647a7ec912243050f2d2388a3124835311a3d000", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_maintenance_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_maintenance_costs_agent.py` is
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

Analyze maintenance costs Scheduled Email Brief — Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 a675d65b56c4f9df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_maintenance_costs_agent.py` first:

```bash
python3 scheduled_brief_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_maintenance_costs_agent.py   # or on stdin
python3 scheduled_brief_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Scheduled Email Brief — Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_maintenance_costs',
    "version": '2.0.0',
    "display_name": 'Analyze maintenance costs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e471e47b543643f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefAnalyzeMaintenanceCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeMaintenanceCosts'
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
    print(ScheduledBriefAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxrbnV2Hq/WH70d3sW99wxCC0ICSBhCSQ5HZUsySL2HeBx999EklV3X6+fu/6xkSMKrpLwMmzn985SdZvL1ZTB1n58vllD6wUWVhxHAagRKzURaSsy8oI/soiG/5DnCyty9Bu6qysXj68uKByyjCvwywdlzsBcJvYsmOAJFmZhqn/0S5D4CEgscIYqZokscpwgPchcyvuB0hnhWkNUit1AGRe1RXiZSVSBwApQZVnaRWO3LIuBeU/ECgu9FPgInWGlE2KuJBrj0D6DoAo7j9BjcDNSvIYVC+ff/n1w0sIv798/u3Fia2q+qYhcCejWuJDh803FaRRA8gltlIfkuc9dEwKr3NQQrUSeMuF1jyvfqxA7H1A/vM/o84q/eqnz19S5Pn58jL+6FDF0ZI6s6oaau1YuWWHcVj3nxAx7qy+gkbWTZlWiIVU0K+p/+mx8hunLEd+Hp/9+BDyyQf1j19eMqiCNXr9y8tPo/1fXqA74PdPI5f8x58+xVkHyh9/+sanauwrcOqRGdT60+vz+skWEn4jDb271J8h10d8bfDl5Tvjxs9D79FOuPLl0zUL0x8fjPMyax/O/PGnv2ILo+BEcVjV/xLfXx6MA2C50Kan4j99uDv5VwR9GvTO86/F5jCsf8cSSP4m7gPydNRf8b77/7+wjsMUVO8e/6fs/tkC9Gfkl7+07b9b8AHxvrxMQRy2MDtg2XxGfnvdb2fSLz+4327+8OvvkPX/yGafNaVz5/CaWGnogap+ff3lh+p++4dff/mhyWGuASt5bcr4n/H8Z369y/mDB59UP/5xLZR/TKMUVj3ynunIb1n+v8rfPyGGFYfut/vVZ+T7ehk/KDIa8Sb04YLvaqaCun7nx59efodAkUJrGuf+GFb5f/wHsgmdMqsyr0b2TtbUI97UYQJG5Q9BWCGHZ1F/3a+W6/WnxP2KwLtjuUOIsJq4RhblCHqwHsaIjxZkHvL1fzt3RP3oPBEVq94g6fUOla9PYHz9Dhhf78D49RNyCKD8rAz9EBIhurjdIpYP0nqUfM8RiLAf21E4VCx8gI8uLUfgqaCIfyBf/2Vpr3fGn/J+NOtLCuMEKUbkBUmelRDFIfBaI27ZfQ0+QtSF2FJmcWxbToSM/zX5p9FXZgDSpwcd2FzADThNDZA4c6AFXgiR+sOI9FncQpwc/VpFYRwjblhCp2Vlf+9C0PefR2Zfv361rSr4kj6AmUIe3afCIMG7wsjHj3kJvDj0g/pLCpwgQ3747fcfkP+D/Her7sxHGVvYKZ79B2qo7DUVgZXaJJCsQsY0gTB0j+Rvvz8iMmoHuxMC6yv0QnBfDLl9S4vRgkeY3mIEbR5VBOVT0h/9hnQB9AsS1tBbsOarD1/SkUUGScsurMCbEx+LH65/C/pDzhiT6ulDGCevzJI77T0jx2A6Wel+QpYe8u4paC6Maz1GNIDxh0mcg9QFqdPDlVb9LYRpViMVrKPK6z8gTQVNHTl/tSHr0TkJBCur/opspC3se1n81qpHIrg6S8Mx8M+sfdyGTMofYI5N3lh8QlQAvYnkVmnlQWlV4E7nWY+MgP3ubT1kbiEp6JCx0YMxRvcKv2ee+JcTxvsUgMzuc8l9GEC+NCRO0Mj/9yHmrvtioc8W4mE2RWbqQT8/Em0cvka7H/MaHCOeYsbqfx8t3lDoDZ+/pHEIg1P2/3hQevfcetA8MK8poTK6qN/5j1Ve3vmGNcyQMeRlOWa19SV9awQfoNNhfKoR02AhRw9b3gSOT980DWC1jtffhgLkkXxjUcC0RvLGjkMH8QBw7xVQB+VYX89YwHQBY63BgnCCP1iFQO4wFSB/BCoRQo9D795dp8I6GWNzT/p38nActaAWbuNAbWEhgU+IOeY1jECF2ADOSyMN9MIPd1ZIAqCPoYrvHq4CK38oMw7ETwWtMRZZYtXg+wg8H8IcHTsOlPdegJCr5Vo19GUHgwDr6/aI7Luez1hBZcecekTpj+F+2op837H+MRYh1PFbM4Az/D2DvzkHIneZVHcwgm04qmCZJ+A9Tx99/dOjNT96/7sun/+0C/jx720U7s32+MfIfUaCus6rzxj2aIhv/fCTkyUYzJEwB9W33viowI/Pevv4Xb19vNfbHwQ8/PUZ+XtK/oHFM7s/I8Qn/BM+PlqHDhjT9/mBPpE+Ts4f6fHpl1QH34L9zIgR52Bd2/17u3kjgT3HL4E/Ej/aTzV2rQ42yjvq3dvHe0I8ywWCauqPvbLKvivj0aYxvI/ovaMzfJSOuO+OM58Pxm1RPKpfgZfPaRPHH15SKwF/Yzs0AjFMXeiUcTMFywiOUnUI7lfvY9V48cf94L3AIDK42eexzmDTgyPwB+R9mv2AvO0v7ju3tIEbrF/GSXoUCUnhr3fa982mDV7gxq7u89GAx6ZpHOCeg/WflRjLC2rsgLGtZ+/1Okr8ExP4xfdB+Wcm2v2LFT9Bo6qtsVXCDv0s9bdE/YDAEMIShFUFwbKBC/4sBsopQdHA5uyO5n7z3zezsoctv9/dUD92nr+9vIHH+P0xKTzSZ+T9t8e60bdv7fh1lGDd+YzD193V9xH2FZoZjm33u0f+OEO8PtLy5TOEIPDhZXRoGcK5fLhvvF8eakF7vg2/kAMEk4/VOEZgsKogJ9jc89GWCALhdwLG26F7px+/fP7rifl/QoXPlI2z8IeyHMC7vMWRPM7bgCNZmrM44AgESdIUzuAe6ZIUz1sUQdI8xVAEYVEujo9KjsIS66kNRowxgXa8O/7fH+dfHoxgWyEZFnKyWI5xWcZmWIf2BNdjaGCTJCPYFG3TtMdSLqAIm+Y5TvAIniFc0iVInAIcfOzi9t2hzznyod3r28z+FqUHSkDpSRKOupOW5fAOR9CuwFmsAyjcphxAkITLUQBnBMrjeUDD9e9Ln5EaA/lwwJjMcISEA1w7yvntGfkxQVkaUsp0tRQfHwkTDMs2MVsP1mgZo7cbVvkNc8pUmWQ01OgLrWHb3UQ1+z2zovPjWfGifV1YdKk4m4wpFlq4ZSWsWnNxekldJczXbr70ptl5cejV4UKeEu/CWKssCfpTlYcCs9mbbLrWc7MflMPyuiAroDC1odLmKgAnUxpmCmeYK0wuBw6dzS+RSS684ph7MLuLMgzjuhGoldmiMwZfg/4kwGKcV/EqNMrjLVdPs4FgzUKmY8e08cY5KVddJc2l753S3VSoDeV027PgsKExDBsuDPDSdU9j84vrtemVtPc3YC/9W+rOluThbB/ROmE6TDeSfR8VUcNOYjSjtnZ/tYiorpXMVS2irOVrKsXLs5OKx4Wtmri6v7DultySx9nWGOZnqjpd9748UwmL3EUsXgnH8nIJrQisjKLA8VzKVVc7UJJj7yxGvS0bVvYKoeB5mOGGaRfywl4r1BVuB07abVbkW+V0mZs7KWBuwlHJ9kxcKCxNaWraspIsNS6v2ztRVPe8VmzU5DRpy8mSbS1brkNrDidoBaUW4OAU83JO541qb66NUewhrTsTMTMdZkE1N3v7MJRTMiOrVNonbbLWFTX17IV5DWAniG1T4j2Rd/HVjliIqSOky/5gVqfGLmpPjRSYrdNsH0my0pAn0BI3iUvt2nfbOuvKtaIayaU1UNrR8HoZ5Ibd45dFAo4GcamG+YXYmbFqks7KCLahdsKqyTxZStCeUxAMMVi1mpw0FymCSTuzhETTzjelByvikKxMMkenTEkR3trZJ9a+4LRpuwaLbSLw5oW80MEy3cecEqkoCHob0IM1cMtyGqdELmEbwZBahVzuOhqNAi9svWCCiWJ5QoPN0TqwW24q37z+YKOOd5bl/rA9NkK08HvvzEWAnQ1m7qreuYokvW8tzkgy/yDke7W44dKiquhY7TrWWYs5bpIRMCxST/kNH5jHDPBs3i1gUsbW+TA/1qnPzvsppZfadT5tlSja81dduS3U26afxcvrujGi83rmmn3RnKshiPBrcmnai24H7im/8cyER6WACisFFsrtFEWLU5SeV8R227vNIZniUUjbaWNfjOXJVTQtqiVqK+vXaED7LcqxR7bXjlJ0NNiCEDforWHq+ipAWA3x/TJzs4jQj3VxSNwwKc+m66bWRDlWHYbh0wlKGUfN069sqA9rrnJNYh8Uh0hbqIa3PworllrVYNl7U25RyMWBjylnyWn2do3qNz4pChZWnOBM2oIoTiCikslWwfptae2sZKpb1S7aiVQRGzpnWvxpT872RolflQvwNvtilsRBZE2n5HZb2Nl21sTEJV4nTnjA4pinPHNnykO76G74jjvjVK+q0fRCQH1pDNjpDK30/Ebu++nW9gPQ2ys+IFKioekDI89staxEa5o6PE6cT5pxOstqRlRHvhqiaMnd1urtuDoJ1BXNEs4o58IgLJMkB1EGoV12pbmth3M8WK9qqV/xuSBqanfilPUlI7hDe7Xa9rhnMc8LbANLrkzXr3qqmdKVMpu4Rs2ynbFqLV3Y72YMO2+dVi80pXG0HXUs1noh5fbW3NIauZ+AdcjNFIFfyZslk+aJk6HXPLo5N59Nd/g6zQecuHATa7nFxcbHd2K7SqheSbzj3Jd2iQiLfmGIx3wPJCXZEVO45ZxTg8tM4rNI+IuINWrHgsqJCRuTxrZwhPOxXFzslSEUJrDm1UGOPHd5POXdpi2rRXRwY25+NWru2FqkYwKXx/Zdoae51l7mON+sS4H3oqjy7WRDuBNCwBp6lgkL6JSY1JlOmyhuvtUv2VLAqlWQ1t1W5nJnHcKaLXYYygccmgcCym8ZWeY6j8xaby4b80QGqH31o+OK8HU8L/db7bJe9WFSxKcVQxK6rdlrn17bkqwH0VZULtKqaVbT4IapMtXRHuYHR3Owg7y3I/E8rYPT/nhVmdUmH+bakZmbxgktorWyPt72k0OxKDkw3KphihmotpciLl3KlJEud4ukFtOC0frFiZs7q1za4YEWB8zlShobsqHrIdcI89QrRqWWOq4rLFVMJr61mHGANdd+u+cS89IlQqzBHfNy5fSHqs42yvKKdklP2bt0w7TlyUmuRTw4u4CqgkSn0L06MZ12XwVpZa9OGnYhmZQOaDMJD0Ll+bUc1R0P82d/ic/6LFizrSEIhwsOPR2Lq8paKmG9PZwTVV/vZpvg4K0uJcl3g77a2VLKVIZNXjdXZbrZ5cLGJAInm6pRVMyNXXtaevPhAMz4uGa5rKzzvc93Ve2Imj5rRQasFBYyucT1dirQw2oCm0AmnmUK1OuIpMPBzw4bf6vvc0uz5O0UPZ4SYbM7usvLdKbxSnee6hOUy7yjMUuXS/xYWF2Hz0UVXGhlWIA9xZOidc7d2tu0DbcxaJaNkmOpFpP5sOtBPlPECa4x8aaTDxPApUcQdthOiiW7rw8qujyAVNcOvV24llXo146Yb7Lz4cAPq3V4cs9EEBwiRsd29jwmid6fgwjfnxb+FL2t8nCycyYTp2fZlLNwYekts0QRk9DDrrXDqaVEU7STHm8OP90tlF3WcL13wc/T4rAo7SIss0Um8sIGxwYCo8lu12zk2F5xIreJLtxlSfnkpLleaFXRXCJgefek1Jha8tg5pJND4VnkVg9j0cZvw+QiWgZGEh0r9Vd9Jq63ertBD41xWvHmBAvVW0QubW0xQ/cMIXinWvJV5UisIjQzTXmWU3qsaNeC6Y39TL1kxuxUsPEw4QGzmoQREc6ZjZTq1HIOikxNULiFWVDeeYil5XmqLbjI4vFuUutdk1h51q2cI+Vc+FvHHH2dWYntQakGn9pG3foiberlfKouAwK7Ka17xntM6izxtC7VbsE3YIXHPN0NIhOe/Hq9UyNRFq0a3VuzWXudSsbal8tggV83sb6arXCiS/cDvtzSZX0QDHyrK30uG0MW1z0Qo+vGocNaXPLXQyZttNZ3LxCLegcGnZgrx8lcTXSuWkVGbbbJZKOe10o3zxduq5a3NhIS1pcMqdysmh22b+BurefZ28QZFngnbOMibtP1yjQFd28rLZqtVwtCUwuWux62kyAMZlhvBvLFGHrQV2tPXc1RoqMm6g0obUmpgZzP/fNm5pzWMjHFdlodL/dOIdS7cyAMcSqyzgwOZGHNMtN9084d5XydOmF3benLVsU3iuzJuK6vZzD4gl2a0/1xzscXQjwwU8GhV/Fi8HUhbzbLqXSx7BDTIl/JC3kIw8NeEVPNNlniTFNgWePFaVZZiXo7BexsnySsuZnT4WZz3kxdPmON9UK+LW65fiES+oZeHXA7sIaB57vE83ISHBOKvSxj+hisKLzrHFLVq2C3iafcvo20TDSl2TCNg0TI+cl12y8dND3Q88aXz6cbFTnHKwgOdalHuHLJ9rLKKdm5XTg22bNXm/MK1zn7IdmH0lDNrsP2ylpiS+HVoBSNMDm45TSvuummwo6lJq2vE12v87S2k31uBqu1PM0Wk+68KpddZ/q1prDDXtkNiqRKhNaszZhL5mgYWNXa9EWt20glthEl6ixnwtUW4+Wy0J2MSElG1WaKew6P50t8CCA007V11qYrwzltloNVJY1HXU766SYzK/SYtheRPysdHaXe5USV19Uy28hb11NtYud6QWGxM9ghjlKioZdDaxUiUIEbHnOSj5iT3hs8ipKgzWiraDRyQbZDz15uNZhwnHMies1FGbc84+S0thcoF5ircJ9SdrVgXbhbdtdqRs4pnVOn0tUHjavRJivZbRJsKfdqyEdC7yQIp5eVPTme8KsmtlhDQK372a5iJ+UmJ1HKire9KE5uEr3aOjU9k+AOtZWWFkD3t1uHloRL88Gkxt2K0zDfKZmU7TvebS4+Q+JeJFHLA85dW3NCVbbjlSvncBUuGAaMFBMn6NwNcswSsFARJlbatKC7oRBrld5n9ulqWs/NDDrJhPtLNYyzGDe9+W7GpXo4CEFRheHMZDDl3Ji9rzluszrfehETnfrgJPwxdWw43JaRu0DtUwkH125zyjCJdEFsKqwmg8EoM3KnBUMhtNpuSts+iCDQBmf9op8E+cgxQbm99QbE/5qcsf2W16+O4Orm7GBgcrzerbxawLWJt6LWsntZRBURafl1uj3JpcZrzuK01Kt2Ts5vM6ENb6x8w61pxJ4YUKM1xt7YSO/prGmPgr+wxRAMU8Y+7dg6J68yEypWDVCCps8hI05IOhsqTINz0rrHV6G2Lq8iz1QbQl4cUaygjwI33+izObo82e05NOmYujnBUXF2mkrOUpystcGccQ25ZYhEWk9o0Vd5QYMx8QNXOzFsnsoASNqiwpZ0tZfFRPXiqQ2rchJYm1U7XLqYi9dpJYvAMsKSXdSSzHAGjWLWpOPBNhuupEz623xSTEoKAk1q+3SobdYbYyYZPsngyjwTInPJTANw9JT4kNmJ6tBN7OmNc6GOKO2SIk/5DC8Qy+p2pBLu0qnH6qZDH8YbKeSEYSkvVldtNuc4bbPC1nEEgqaOqP5MAaxJduhEmgMvIs5Xsb2lItmkS3Oxkdtr0i1MwtF1T2ApFh2IAJebtp2GE0dVcxL3MY0625P1Gm+dBLWwmGkpOncC36LMea+dGnoOSpdWNrepeC4AfnB8dkNQ5TAL/e3yhlVyxsOJwUkzFj0TM+1wMGZUWdPeAtfQ2YI/T3dcLZQ7bzG1vdqT5wFO0pc2aTh3ztG75cy+0RfaswNiLdcLbkExace4LiqgFW1XxiJZUa64Xa7Jg7N1nauceiSmc0IsYLdw4/FttraBJAgpvl3O5VhWdyfdX3mLomWTQUY5mgyOsmFtpgXLFBy9ahNsJndWIpqTfbQtUHRDc5MO13mioMVDTJKnGJw2jSuY1m07Xw+3vaSC82Je7JhbJ06m2gABwdLkCTSk9KNhOki4SGgB1V26hVfW0OOw2biBHLWGtBZn+tZ1WW973OjDkXa1K7cuAD9v+WsIpxzx1MwmdOOKVIIuZjPDZXa2fyaWA9z3S84FnV/taXgW+ibWCFk5xlTVDTD96jVWchCueHF5vJkGs+48yrDaeTO1GFfBmynfOnxKrzctOikPw6SH2RjHTmxcHLh7NtXCY44iMRXM25nlGMy+WddkqjYTaKDg2IeK2x0D2CObHRt2+A1s6RU6a/v9UVGZHNPITTQArjok6o7IqdtAkNLpzKI7PukyuMkII1EUf/755cPL/Rz45TOBcwT+4WU8Mni++P+33hf7Q5i/PllSHCV8ePl/9/Ly8SLx7ZDwfgwALPfzXfrnf0PbXz+8lE4INXu8aq7ixn++uPwvL2w//stvk0c2/eOEezzdvNVvhym15d/feoep21R12b9WWdzc33nDCDTV+Dcv1evzCOLlbmaS189Xy9+ZBe9Yzv1c4LXOXt2wyrMKvIx/mjKe3MGuDAH5eek/Tww+vLg9jGjoVK8Uy7yCMh8Nfx5ejW94x9Orl9//L6gcazLiJwAA -->
