---
name: "rar-cowork-cookbook-teams-update-measure-and-analyze-procurement-spend"
description: "Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend", "rar_sha256": "f1e6ec7cf2c7167a61368a364584720a63915cd4a9ee3f78f5f3ab1fc9664977", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_and_analyze_procurement_spend_agent.py` and in the RCI capsule.

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

Measure and analyze procurement spend Teams Channel Update — Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 f1e6ec7cf2c7167a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_and_analyze_procurement_spend_agent.py` first:

```bash
python3 teams_update_measure_and_analyze_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_and_analyze_procurement_spend_agent.py   # or on stdin
python3 teams_update_measure_and_analyze_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure and analyze procurement spend Teams Channel Update — Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend',
    "version": '2.0.1',
    "display_name": 'Measure and analyze procurement spend Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-measure-and-analyze-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bdf27a411f8d5dca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/measure-and-analyze-procurement-spend'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-measure-and-analyze-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateMeasureAndAnalyzeProcurementSpend(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureAndAnalyzeProcurementSpend'
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
    print(TeamsUpdateMeasureAndAnalyzeProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebObyJbnV9Hc/sOuln1ZxeIXFTEIJCQkFgkESOWKW+z7IjYBNfXdJ5Hka1fXez1d0R0x2NcXyMyzn985mfj3F6ttwqJ6+fKielY+4600jUKvmlm5O2OLW1El4FeR2OBn5hR5U0V22xRV/fLpxfVqp4rKJipysJyrLL+pZ9ZM86ysnjmhledeOiuLupkV+SzzrLqtvDtdK7fSYfRmZVU44F3m5c2sLj0wUjdW09azW9SEYNYsyhuvspwm6rwZ41rl/Ya1KnfmF9Xs2kZOMgMSWYH3CuTxeisrU69++fLLr59eInD/8uX3Fye1avDq5S7WqXStxhMfsjC5yzwkUb4Lok5yAGKplQdgVTkA6+TgufQqwDMDr1zPnz2fPtZe6n+a/fu/JzerCuqfvnzNZ8/r68v059jmsyb0Zk1h1Y3nzhyrtOwojZrhdcakN2uoZ5XXtFU+Ga4GquTB62Pld0pFOft5Gvv4YPIaeM3Hry8FEMGaTP/15acZMMbXl6qd7l8nKuXHn17T4uZVH3/6Tqdu7dhzmokYkPr17fn8JAsmfp8a+XeuPwOqDyfb3teXH5Sbrofck55g5ctrXET5xwdh4NbOy63c8T7+9K/IOqHnJGlUN/8lur88CIee5QKdnoL/9Olu5F9n86dC7zT/NdsSuPXvaAKmf2P3afY01L+ifbf/fyCdRrlXv1v8n5L7ZwvmP89++Ze6/WcLPs38ry+cl4I8qSw79b7Mfn9TlRX7ywf3+8sPv/4BSP8/yahFWzl3Cm+ZlUe+Vzdvb798qO+vP/z6y4e2BLEGsuqtrdJ/RvOf2fXO508WfM76+Oe1gP8pT/Lils/eI332e1H+r+qP15lupZH7/X39ZfZjvkzXfDYp8Y3pwwQ/5EwNZP3Bjj+9/AHwIgfatM59GGT5v/3bTIycqqgLv5mpTtE2M+DgJsq8SXgtjOoZ+DvlduUBu9YRMOxzHoj/ycOTxIU/++1/O3cY/ew8YRRqJiR6a+9Q9PbExTeAi29PXHz7ARff7rj42+tMA5yKKgoiMGd2ZBTlaw5gDwAnkKKsvNqrOoAv9tB4nwEyfZ5uAHzOfvv7zN7udF/L4bc7WEcPBDuy2wm96jb1XicLGKGXP/V1AFJ7vee0gGVaOEA+PwIw/AlYpi5SgNjNZK06idJ05kYVME1RDXfawKJfJmK//fabbdXh1/wBt9jsUVhqCEx4F2f2+TNQ1E+jIGy+5p4TFrMPv//xYfZ/Zv/ZqjvxiYcCysDTX0BCQZWlGci/dtIbuBI4H4DL3V+///E0NyCTg0oIvBv5kfdYDOI38dxvtlc3zGd0QcxsD9gc2Dsri6oBGD6LmtfZ1p+9ywuYTkMTyodTQXS9ydJe7gyAqgXUebdkXoBaCIK09odPs7b27lx/syvrLmIGgMBqfpuJrAJqSpGCfyYx75PA4iKPgPnfI+PxHhCpPtSz5TcSrzNpithZaVVWGVbWk4dvPfwCasm35YC4Ncu929d8Kqb3ELmnz8M8YBKwjPN06efJ56BDyABWuPU33vc51lT5tHsFrL7m9TM1rGpyhQNKBWAatJE7FYx/PEOqDos2de/2A5JOlJ5ecJ9euceg+F/qKR79CPvsRx4dwOxri8IIPvv/3LRMSjA8f1zxjLbiZitJO54fxp1arYnDozsD/cJ98T2RvvcQ3xDoGxB/zdMIREo1/OMx8+6S55wHuAHBXYAexzt9EA/AuBPde7hO4VdVU6BbX/NviP8J2OYOb8AaILdB7E8h943hNPpN0hAk8PT8vfrf3VtNlpsSZla2dgrCxfc817YmG4TVlHJPT4DY9ab0u4WRE/5JqxmgDkIE0J9cEgF3gapwN51UADVBtvlVkX2fHk09FZDCbR0gLehlvdeZAbJmipwapCpojKY5wAof7qSAl4GNgYjvFq5Dq3wIM7W/TwGtyRdFNgXPDx54Dn6P87ssk/iAqgVCDdjyNiGx6/UPz77L+fQVEDabMvO+6M/ufuo6+7E0/eNrfpfxHfxBwqdTVf/BODMQgCCap6id8KoGmJN5zwACkXAv4K+PGvwo8u+yfPlLz//x720L7lX19GfPfZmFTVPWXyDoUQm/FcJXgBYQiJGo9OpHUfz8qFOfn3n3GXD7/My7zz/k3ed73v2J08NwX2Z/T9o/kXiG+ZcZ8gq/wtPQPnK8KY6fFzAO+3l5/oxPo1/zo/fd68/QmNA3HUAVfi9F36aAehRUXjBNfpSmeqpoN1BE71gM/PI1f4+MZ95MaBRMdbQufsjne00Gfn648b1kgKG8Abzdqct77IfSSfzae/mSt2n66SW3Mu/v74OmKgFCGdhm2kwBJ4Aeqom8+9N7PzU9/Hk3eE84gBRu8WXKu0+zqff9NHtvYz/Nvm0s7ju3vAU7q1+mFnpiCaaCX+9z37eatvcCNnbNUE56PHZLU+f27Kj/KsSUblPYeFPlL97zd+L4FyLgJgi86q9E5PuNlT5BBID9VMej5lvq10BOF3RFn2bAkyAlQZYB8GzBgr+yAXwqD1QAgMKTut/t912t4qHLH3czNI8t5+8v38Dk6YNnewmmg6z9XE8lEwJRCxiC50d8gbH/gcbzSREAImhzAEkf8QjPIR0fdUiEIC0CwQjKwgh8QeEkClsERiMLx8Ut2vMwn6T8hY9ZNuI7NEHgNEkCeo+4fZs6hWiS0oN9D6xCHRcj0MUCpxEStWjXwknLcmGKImHSd0HN+L40AWj6VP2h6mTX9x54MtHTAr+/2AQOZm7wess8Lhaidcs2IPsY7udVOu97qA7ahVEIkpcs5/pwlVvK3DIZ5+3hqN7qKGssEpACLTOYzU60ll0Rz4OOVOfEBfWM/U7UJScOHP6qSppDymNN7kVqXq8ZbUlsDbWJCD3ZZDsIVVHoZAhFfBDyDDmZQWrv9v2imGt81MjIuJH1yJvv9PVlBylkZc+Ffnfx9LUr7IU1EYn7syqEns3RQrtDcl1Px9IK4LLwpV2q7Up6d1IFIqnnW1czrEtknaq+aWwhtMLdXneumy0i5zFCQp52GS51HlOGlqK0B/XsTkLrdBWILsxCQFNkZxrIwrJNQ1yvDLE5XxRH6tZnrbql53Rc0qkcLdLWxIql4BAnHN4u5WsSNEbpbbAha/R9brUq4hXXtUhVO3axrzx2D5/szLumtXRe+/tULyVtOGbegb0OnWYnbsePnQlfydKF4uzUngZtcSh0Q9hRaUHcOpEY80OUJoCApcUVsQoXhzgRUp/di6ZuRH6V++LWYgmsFBq2OK4yZ2FyF5WSxtLr+v0WzmD8LAywTidQtdxYLdhDspSPWPp1VztDE6WXpErqTd8Tt2191jsY2VTGvjVCW1mlS7fOIg3Kbliqgu0FDQoMzt0obQEfL5x5Ui1V36yxJYFlV6xKt01nL3CR23L62N2qrW3mNFtt7DBouubWg5t0WKZjThjqJV7u7TFasejWPJVHTXZNJOqlsEupm3GUMONy2m0FxzlDTWGLvZWHxQK3nH4TK9gaLkt2PpLsOuzoM46wKyYlrzyPl6S2hv3Ksa9ketYRPVyQ0uUW1Fo3LMSRt/hYYtd1Je/UDAG01rJ/1qXazU86HcE6utaqipsf60XuQOu+6c7IXFC9iOzC3GdkLB/iFXwqCQhiRMvXKmx+9gveLGjvGpGmskyQJbot8R3aq8R1N9TwOUmujX7Vz8lms9na67BO3BSPT3C5uYroBuvplbyrUwEOTnsUgKB08NYYvFJOlAQzdicWlS3A7Ol0ZeMbs5W316jM2FjlbioyiMSRZzVJ2zbZtg3S1am/mFImb1Y3x6PHVl/jMkTujkZlheJ1LWD7MDJ7fBsGp7m/XHXgZyMQvT5PXBWpuputY9ncK5vklDUIPy4sN3avzVF2fRKgmbKTFueFvtM45Yov+NHQMSGt/ZLilKFIVNsehGtdJrIsoFsH6a2DrWLkBoJUERrwnVoR1yOFzBsk1VL1chWWtldzOWqFJ++2IfyzkdBupe2tXbzqO5p0NrQqmGtP5iU1YiGxNYy40W24r+imPK8ihE/XR8pVLdY0Kl04qRV+TQ/oqUvSjUEew5Kl4qrkRmKT33TvVJLS2ShRHA8yilhD6ytpNaG8zTFMjvSd1F5L+iCyUVBHYYjxOESzJpow9WHhqbptMXvatrUt1bZDteHcbWWpKhEYbSUS577KLeOkDqms48a8l+KNKBF6LrbLdbC5QSvkcoVzbKzdFUx0fSGP/BwTpPbQqwt8mZjGOfGYDqVDB4GKtNavdIE5Dkcla8RHx3WJeUzQdyi1tcKOnZ9W1sVekBQ/HuZUvChh7EwbUWHJ1FrCexyGT+tIKvwtsiHUVKGiAEaUnj5QbIaxiDDYabepemiFbeNdV87rm1hGttLkUiJw3KbgNCZwCunaBiYtRPwxjm7XsOdxgT3VYhwJCdKgEGIfWw7XVtL2sOkt/XAsy8DmRMowIkHcBxgXMCqcwnGjiKjOHYp9VjFx3i59eX3RTuLZPzINYmyaPivHJsxr4xIZLow0CTbCc7/jevIQlctxO+qy3KEweRhuYooJsWcrB3gDFzdZMbrktqCalUxkazp0md1KjFwl7VQoXWN+t+/mHpZQGnFU1vtbacmypZNDKbMeY0KraM1lrTfUt+sh5WkTYPd4rRpvjyvtJV1FKK7uC0FH2LjDNvWtMyXIa6m5aozXqNja8CElrKA+XTO7X15Bgyon5c0+VkxzUIpmdx4KovTH8JytL5nashAhpoeITszsiF5lotykyX43ckStLh3Hgq/tlU9s/MbPY649WmlzA3AuVTusPqSXyqv0amH5zLI8WrJ09Ah2iBNkrqwoTbVF24nqw1kpusvWcrOaSEeH63zMOeLlvLEX1Dlbyb55phIxP8ustdKLw5ASpmjQyWqBenTfCu3WWF9K0S87Ojnj60aJeGI+yJttcqGh7qa50to63pYc0THmaKPw7qirl+XOWdu9LnhoFtlbfXTNboforWocMlDOshi3kD4wD7o0MuGuWlyJGG8pHSBO5nMuL9HHk7JeJhXM8kyOS8eo9SJ4NDx7j85TplkmaAsvs4JMQZGkr1vDke1Lu62Z82G9Gql8XgHIyOABTXZRX/FLhNLq4BJi0tzn1VhYxqyOb1mPU0b52B40FEXzmE93ZrVB9zaErTt5WAspP1bMkYWl6qqxGutyohVbS3jM6kukwCeYF5FDRu1OiB1ZWAkfEponUjSKkit1kwdrdxow7YYF81V6Odd9qKn4ATsLiwg1SqMoCrhKeFqbD7u0jg48IyW9TcZjc5knYrQ9pYF2XUJ0Okc1TzpKNC8fo8ViF4jMgYrIsxnc8PFqolVRiFUpFExIQ8Rck6AFG8Sr4mgiLHYGUL6d1+qWcFVzVHnSjveXy9w1NirpH699yov5Ck3pOeZJLH6LVWlzk0vPjR0zSBhHSLgLLl6ZEGurVFKW1JEtVZsRt8tILirJ1OBF2S+r/SpUe8bmsrTgdukliwM6yHerNV4g2/VG93K2WGPNWBRXnUSROKMbbFeKVeFd10PpqPScDS5sArc10gkqc+uFVbLeaFcvOqwJjQ6SyuTKo8DliQhas0pmVpLNlKdtD4e4NKicCZUSEQop0sDEiUWt0WGKCuzmS18WvZsspLigwpoVcmjM2+Ha5y9DnO4WYcCGMtVvVTFdCp5FcMiCWJE4LvImslzoRyDh5gxRbrLbOcO5G41IGt0bg5S4CvrhJQZDRbuW0DKmyj5uDqmKumYZn6/dTpX0jD7E7k0p+aZ3q7KrkasVWGvrerbZiK0d0GRQowXzx3FD9YJS7NeDfeINYjU6pnFzIWJQo4LceHILwyRySQaDSkZKj0xsfyZGEdqc9NV+qCOJWJiimqXbk1aoeOnqTDS2xEEOAmKn1WVU5Uoacgko8BTOEMs4hrpObs8IX3k5RBZL+XgWIMqqrQWRVl2TCBlfJfH2inhpdQXgtc+umr8SKK4TGKkKUlJzzuvjeliNy7V7VE/7g6KdVRb0O1RpWBimbFlywaMyQ6a2CqxbIafhhNq7UeNL0Fa6jmme4+vmNviJJiQJbdlytMZ6LIKS8Lhd0fsFg86rJOvjkqhArC1okd3IKZh84hqNOWcF3YAassK4NMtonFrGym5rzYslwZE8czbkhe6k8twhfTOUChXbBtsK1Y3Q24k21lkhSK+r6QfS5XJmtbFW417iFhbTUXtx3Fbt8qi7I1RUXFkShO7sjrXomHv7OHiKau4iKlBPMs+Q5yW3NNbyStTXdX+uRCHllASnxmQHtzlmUd1JVU68DTMrit1WSs8EpFI5ubM02WS7MwQeMgCsiCdTL47hETU8KVjsrflYnMQxgOMhLtsbsZMo4Kk68W86klydPI7bOXGNY17bbAqCdOchbi1XfAyTJqK69cG06tzjMx6C1wqnZBGZcRsyNws/dzwfH3qc3pBeFyNa4YK6h1mxapHVzTFdH933vgI6zS4cSnjfOhsWq7pQTi5yqO8QmXYK0myutaluwJYCB+22z2QZo14rZ+8KyHK+jiVCRQxEkkWRiUxkO5bQ4K2WGA8hTZDjAQ9yvtH1RQfawaO0HZnVweKJHR6SQjpauHJGaA2JOUTK6ZLjsh52KG4DBXi3MFsCqRXurFwMLD8IxkmhCC52BjMzPbITvHgcSAUDF7k2abbnWLC/h3SFsl0T18hrXkq+yfNDXSE7gShJRtVW1OZw8ta5KBUbme0XAxN7O+o0P4ulENxksbvoZ02NlsURXixYZRVfuSGjGHvpnGKwPSJkd2GXpV4vsBvw/T5oHchFpU2EMwhSCbq4QkDzbND4GDf8hdtI3SCEKcXMYYLvsrF1OH4NOZIksfOaDlqZGqzluS8juk2UiCJ3ly7ZzzXvMs8pq1g5GLqy/PmBpmGeKy51LQQKdtKjuCcEKbHJ/KrQrk5UEIpQGLdmDXPZBZkXRN24xGN/SblLTKvIXKh3LWYFrrMEvYhy1nX0bFs9lPb2Qsv1m8Zc6Q7hWjmhb3RMd6mD3rTTdue3jTme2dV8Pff3h21Y5duIOwrzxAuNPWy2RodeMzUK8K2oEPQKLqoirTwbIfA08RtGiTPDceb6MRCCvlhhLrmkLsKcEfEFnmMbw/FlhoIr3rxFVbTVIbPooUrOzQ67xUtYQRg/4nQNV8jVKCPLJeOd0MOeWkVa2x1OBoiTM7eW16RHgU5IccNOWw0LaiPccleH2BziSYd0zNZkx5Xr7elcOe7GVcJH8AnauZ3i+lZxEpKgMy+LUJnjF5v3q6vk5sjYVcsOiw51ODab9CAuobhYYv1NyrmDguPOMas3zCXf2P5W5sjYTOzaw1sGIGOA6htM5dx9G0tIVWcuQZZkl6KdE9yQfaef44DA4BymW2Mp8RSz24SSSVyDkWbJ1SBy1yXJ5Tgmx0iR9pQXK0N08nWHLm+0oOwQVEZu8WZRkMRgyR7VoB1e3+yFjygES7g6NiKHbT8wEOZvoBJWdozS5qGGxTiVddgwlhQCb+O9vUZpiJdayCUGUVHsZuAgSKi28/UBI50taOzSCg+2vKW07Fo+cGZ4reSyBTt08xgsMkRbRM1Gk0wf1qMNnELxAeYOqpY0GtY71BxF2y2gbs0XSy5dUDl6MR2jpQzQnKNmr6mN5BWieJpz87C3RGcj8ks4ZTlxXOr9IiQ2bqZeCduRWmMkbJsmLLvZjNrNuN7WoXWM3ZjMuhPh3UJK2SxpA1E8XqGXSMYVzJoMWW9fHaRFt8yO69Mc5vFMOoiEgzC57IcHFF04XsppHpLvb7bi3HLeuHlKu6hEDuoWyE5cpo5V8/QcbeZH1jb3mbyG6ltDxm5ADNBiqDuHO6x66BYJGOgQkIuTzbedcIj1DjUyeE4s8gN1K2lKVhi/CLfSejFQZ9EV4B28Z7SUDg/VWCTcVdmGFAzl9gY++S7WDxvNNLB2XAwu6MTnATSQKZ/JasEwzM8/v3x6mY60nwfT/40v1dPZ4P/YEeXjNPHbR6z7sbRnuV/uvL78d4T89dNL5URAxMdRbZ22wfMY8z8c1H7++x9DJnrD4wPx9D2ub76d+jdgszbpEOVuWzfV8FYXaXs/PP70Yrf19N8x6rfnIfnLXfGsnE7cf1T0+9FrU7yV1mTu+0fOzHOjx/D0GDzPsj+9uANwaeTUbxixePOqctL8+XUFKIy+wq/Iyx//FwlMpdZ6JgAA -->
