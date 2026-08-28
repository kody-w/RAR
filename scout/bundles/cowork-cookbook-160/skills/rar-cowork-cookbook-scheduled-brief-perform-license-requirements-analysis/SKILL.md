---
name: "rar-cowork-cookbook-scheduled-brief-perform-license-requirements-analysis"
description: "Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis", "rar_sha256": "a8bbfc4daf8d456c3a9a41179084102fed1b845ef7f236aadd7f9b02c25fbc8d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_license_requirements_analysis_agent.py` and in the RCI capsule.

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

Perform license requirements analysis Scheduled Email Brief — Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_license_requirements_analysis_agent.py` and embedded as the fenced Python below (sha256 a8bbfc4daf8d456c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_license_requirements_analysis_agent.py` first:

```bash
python3 scheduled_brief_perform_license_requirements_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_license_requirements_analysis_agent.py   # or on stdin
python3 scheduled_brief_perform_license_requirements_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform license requirements analysis Scheduled Email Brief — Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis',
    "version": '2.0.1',
    "display_name": 'Perform license requirements analysis Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-license-requirements-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5bd46b873664530e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/perform-license-requirements-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-perform-license-requirements-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefPerformLicenseRequirementsAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformLicenseRequirementsAnalysis'
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
    print(ScheduledBriefPerformLicenseRequirementsAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjWJLuX2FiHqpqyAyB2ES2ldlFQoAkFgkBQqpsi2Lf90WguvXf70FSRGZ1dc9M98zDVWZYCPDju3/u5xC/vVhdGxb1y5eXo2flEG+laRR6NWTlLrQqrkWdgF9FYoMfyCnyto7sri3q5uXTi+s1Th2VbVTk03In9NwutezUg7KizqM8+GzXkedDXmZFKdR0WWbV0Q3ch0qv9os6g9LI8fLGg2qv6qLay7y8bYBkKx2bqIEACdSG09OmLPImmjgX19yr/wIB0VGQey7UFlDd5ZALJIwQoL96XpKOr0A7b7CyMvWaly+//PXTSwS+v3z57cVJrab5pq3nLicV9w99xIc66nfaME9lAMPUygOwshyBv3Jw/TQC3HKBkc+rHxsv9T9B//EfydWqg+anL19z6Pn5+jL9U4G2k1FtYTUtMMCxSsuO0qgdXyEmvVpjA+xtuzoHjoAa4O48eH2s/MapKKGfp2c/PoS8Bl7749eXAqhgTcH4+vLT5IqvL8Az4PvrxKX88afXtLh69Y8/fePTdHbsOe3EDGj9+va8frIFhN9II/8u9WfA9RF22/v68p1x0+eh92QnWPnyGhdR/uODcVkXvZdbueP9+NM/YgsC4iRp1LT/Lb6/PBiHnuUCm56K//Tp7uS/QvDToA+e/1hsCcL6z1gCyN/FfYKejvpHvO/+/xvWaZR7zYfH/y67v7cA/hn65R/a9p8t+AT5X19YL416kB2ggr5Av70d9+vVLz+4327+8NffAev/ks2x6GrnzuEts/LI95r27e2XH5r77R/++ssPXQlyzbOyt65O/x7Pv+fXu5w/ePBJ9eMf1wL5ep7kAACgj0yHfivKf6t/f4UMK43cb/ebL9D39TJ9YGgy4l3owwXf1UwDdP3Ojz+9/A4wIwfWdM79Majyf/93SIqcumgKv4WOTtG1E/S0UeZNymshQCzw/wFYwK8PvHrQgfyfIjxpXPjQr//HuQPrZ+cJrLPmHY3e7oj59gSTtyc+vn2Pj2/v+PjrK6QBYUUdBRG4BanMfv81twJANClSAtj06h5AjD223mfA7/P0BYpy6Nd/Sd7bnfVrOf56bw7RA8fU1WbCsAZwe538cAq9/Gm1A/qJN3hOB6SmhQNU9CMAyJ8mQC/SHmDg5LMmidIUcoE4B/SV8c4b+PXLxOzXX3+1rSb8mj9AF4MeDaeZAYIPdaDPn4GtfhoFYfs195ywgH747fcfoP8L/Wer7swnGXvQEJ5RAxpuj4oMgSrsHr1oSgEAMfeo/fb70+OADWhCEIhx5EfeYzHI4sRz391/FJjPc4KEbA+4Fbg8K4u6nRpf1L5CGx/60BcInR5NWB8WTQv6Wunlrpc7I+BqAXM+PJkXLdSAVG388RPUNd5d6q92bd1VzAAcWO2vkLTag85SpO99cSICi4s8Au7/SI7HfcCk/qGBlu8sXiF5yluotGqrDGvrKcO3HnEBHeV9OWBuQbl3/ZpPbfWeJvciergHEAHPOM+Qfp5iDiYH0Pxzt3mXfaexpv6n3ftg/RWk3aNArHoKhQMaBhAadJE7tY2/PFOqCYsude/+8x7DwTMK7jMq9xzc/7fGi48RAFrfB5T7JAB97eYIikP/X00zk00Mz6trntHWLLSWNfX88PU0kU0xeQxxYIh4igHyvg0W77D0js5f8zQCiVOPf3lQ3iP0pHkgXlcDZVRGvfMH6QF8PfG9Z++UjXU95b31NX9vA59AQtwxDwQQlHrysOVd4PT0XdMQ1PN0/W0kuEe7dqfCBxkKlZ0NHAn5nufalpMAreqpAp9xAansTdV4DSMn/INVEOAOMgbwh4ASEXA98O7ddXIBzARx8usi+0YeTYMW0MLtHKAtGHm9V+gEimiKQAMqF0xLEw3wwg93VlDmAR8DFT883IRW+VBmmpKfClpTLIoM5Pb3EXg+/Jb2d10m9QFXy7Va4MvrhM2uNzwi+6HnM1ZA2Wwq1PuiP4b7aSv0fb/6y9f8ruNHOwD1/8jmb86BQN1lzR1wJ/hqAARl3keePrr666MxPzr/hy5f/rQ1+PGf2z3cW63+x8h9gcK2LZsvs9mjPb53x1cAHjOQI1HpNd865aMaPz9r7/Oz9j5/X3uf32vvD8IevvsC/XMK/4HFM9O/QOgr8opMj+47B+Cg5wf4Z/V5ef6MT0+/5qr3LfDP7JjwGNS4PX40p3cS0KGC2gsm4kezaqYedwVt9Y7OIDRf84/keJYOAP88mDprU3xX0vcuDUL9iORHEwGP8hbIdqfpL/CmvdLTey9f8i5NP73kVub9a3ukqXeAjAb+mTZboLpAfNrIu199zFrTxR/3jve6A4DhFl+m8vsETXPxJ+hjxP0EvW867ju7vAO7rl+m8XoSCUjBrw/aj42p7b2AjV87lpMtj53UNNU9p+0/KzFVHdDY8aZ5oPgo40nin5iAL0Hg1X9moty/WOkTS5rWmrp71L4jwHv+foJANEFlgmIDGNqBBX8WA+Q809mdzP3mv29mFQ9bfr+7oX1sR397eceUZwyeoycgB8X7uZka6QxkLhAIrh85Bp797wylT6YAGsH8A7haC9v2Hdy1/IWLE6SDWbSFoyhFIwscRea+56L2Aic8n/LnGGlZrkv5tI3MnTnh287CBfwe6fs2jRDRpKiH+B5Go3PHxcg5QeA0Ss0t2rVwCixHFgsKoXwXdI9vSxOAq0/rH9ZOrv2YjycvPZ3w24tN4oBSwJsN8/isZrRhkXPKVkMbrknvfDFnGzvSq/6km2N2UQfsNDKXAnHErc3tKEa4bGLrVO2u2HKjkGVYMDN1C48aJfgKu4IjTnGPosjISGNnOZveiHScOYsgWK3PvSEmCKFfEiXlCcPa6vW8dasC2+3GNhFrpUUNa6HJ56rWFCOqFRndprjBVygnzmZw2t02nSxFZ6R0iHlfxny/qyyEPp3j4wwR86KPegdfRVZ8avlCTNBWziUUrZtC2KTGqca2G11NVbRON46zPQV7wqqctuFxgt8isJdvF7RipihdIbg3o6qZ5B56ZlcPysFgQ36sWytDZfMk4KK2TvPNifcRVpypnWmEFSpub8dYc465SB1koZOPhyuhMMWarLrikBCjn984ojpKYeOqp1056OcUZVgqNq2Ru/aphWSHoqgNo2ydkr8QsugWt0wxwoZA6V1H+l4kc06VYulqnoRSpm9F8hDvySEguXWXImmQpQSzFbjdXJ0TY8U3Zd065MmbOSq+vHVH02OCbVEtByt0Ko+nr3s0zU6XVlJx0kqBBmWus0p7LI2dQJxHvEbs5NRIuSzLYgxny2wbn7cdgvL1SexO4WW/TrdOk0UaneHzxuBmdStuj/qS9EoE3yRh3VxWRa3YFY/2st6b/MlWzNtQ8AdH3DvZyTT7PcnPFUxa2qa9HJWTZhGbcX6jb2LalQOnVuaWpco4ive3Y1Sbl0o+l7WVi+qaqw/1LRHQdkl0or7gjH1sZ9LissC9Kk3EkgpWDEZLjhOu1GyBsoKut2W82N/MusIy4HgjvGD7S5D22n6EJZa3eW1YcQug7lKxxY7M9k11/5kdI1tOhdN+0ZX2EYc1+Qov4ZnhzDjCW8GLkDB7kr8Wwwxe2gmZxxjp+IXJIXZe3RTEPZSS20aityo7vavipl7xW4IvjSrUVXV+RfnhYiusd3KO0eUiH8mQgdXLCrul9kab7wqzMw9uUzO3DTP6BHk+cklLhJassea55tkLo4UDp6vKTT8evKhsVPO4CdQTnUhLd7k7t9HYiZKjyAHeXm6dwZ0FcxbHrNHWsnHZ8RtRdYlVYrsHVAQ/XFhQYkpiqhiLJOveiD6v7Au3rV3VgQv/qBzaI2zqFD6jeqRu4/NNORnZgsVE85IvUmOwKHFx2exi3bkM7SWhDYTwuXWs7K1NQdv8KNy2fmTmnSBohqBqV4lCIuVi58dONLe8sc03nDIi7W55GyOpQm3MN9AYWZKGPV8judzX46z11F3RD9emMwMBIEuEuY3o5alPo+IxbdUS1DljJEEyd3EkZXHW6DeE4SO6btbmWgy10dqO4Y5mb3hYDziXdPV6cK3g6NOqOBQkghezThH1Uq1UzkQF/KBdq6Y5JvMMOyZXMWB8RwiiOTveWDMI+dzbWXKeMtvrNdd3w3g0zlcYGIXeanF3avLthTyddZhh0/nGvopHxdnbJsUsUDetj7abVcreVQq9VRUdx+bkttzwwB9ME+G3TX2NFd/BZL8CwGv1lkwLF29kBXnRjku4Wgf+nlrpida79KaB5dYNkxmzr4e11NNH3i6tmHKYzbioo1CtLqczEEtQHbJjUtgVikrokcJhYsGfb490ReQaCnOsdLUciWHOWT3abCeY1x3MHw6bgtsRB42lg0rTCgbNNmNnyuZy66Q97nRK0wYAkMzltdn5S9FZCqLV1vFFtw4yo5+QSr2F4qpUZbE6zrvFTdXk6rhG5KvBhRgmisUquZXZEa2TjjD2LrXXBL3f481tLVF1TYldXs79vUng6hFmsPPN7LoewevmGCcZLdnxhRIYAudTlETblbBHm6RrO+9s+tpKyDcoJpCoj+E2NqMXPUXXFAUvSmqMuw22PM1XRIn2u/y8vbBCkTgbF4nHU2acdG1vjNVFIg/DzqFAI9d2O0m+4ubBqgiPAei7NWTzwqkbYrcYSILJ+CKyqD3CcSl5TMG4cFAqluNKjTcFY52RfLxqb+KxZM6NJ6ontyX2K4dNjg1Dc1UtXq9RipRWLy09rZlZW/Sqn3MR7ywpFj3t5sdxVVtcOJzNc1oX1HhAL9WJTfpF4ibr2QpD7CONpiW3spvzVuOv8zNJaOdgNIbqmi8jd+3D9e4E70R8t+3zorObk3q+kdaKPSp6GavRcMJczAMTR4euMYlbJeSxbzB/OG1YcS5mZnLbjYtdbUm5Xqaori0v9JW57iWj5CtqJ3j1VmSKzQrH63Vna4aMi1W3xlK3wrYifLJWtazraB3xVMFVzqIojQZ1I8f0rUXJZr6Y8p6h6sO4TGyE14MS5w/L8355utR7OaH8JHSYsTKr9W2jKKZxQavN/CxX22KpRDt7qe79k18qsFC2UlyuNu0wBIq/djY7xmsBHCHFcR0eB1HmuOSwx5VByrTVapZrVrUx7e289RdGupDmJVFuYlM8JuystgZF3WwPLblXV+tb3m/dW5MtLC9eCuQaDcekWICEyWn+mGDRsaqkw+1wI2W/j4bD6QzvkBZRnduWt0Rb4mfaKSgQYX3arIXDTkUv6XEINhIPUKsQ4ri04fU63XB8UJPbGT3YF3ivDCQuCxtFp9NEaoNFRdBCrnFadZqLRSVdAjop1Bns+eIuvjG4YBlo5bDdQZl1uJY5Z9LF8plmLbBIrF3ayfID1V/IgTuCCMIp2tHejKHgOFjgABgIrLkSS1i9RoGcBqPExsyu0/GFMF/v0m3DoISkDpyIwk5ubAW5PKd6utJ6oiKYRq8OSGaCafaQtku+PFRkneAGq8yyAxOVee9FmLVahqCcYua8Sw8NKjbdPjl7gSTG/SklyoKFo1Beo+2x3njNQF+D0YxDVWH7WkIBOijrtWSDaWqDoPSaIUGUZjq/OCbRHLEOBCuNGRJ4I17ONobGbhUtkv2j1Gz4oPJhzcI38xQArLYVTuNy0YFxTDtvr9Uh7xP8zKC7UKmKm2WKhWN58/VcsaRzWcDC2lHtNe/IubfGU4+BB4WktqpBeotyVchNT56o1SDbhoEPW7iOLsoZ2aQt0XoynS5GfVZnpLPb5AtkTabYkGJhMQ/oCvfh7Un2L6lRXkYcrra1p/iGIaq0FttKR+kGe4avkU+cBuFC07d+bMZ9S6wWwLxr3strE3ayQzpX8XHJ5PI15A6wrhuXIycorqgLG9WhyiuHrEpz5oHtxrJqTwvsih1ZPRpiANdpRZBJ3cfV8pR5h7Kk7VrnDjqHpxbKxsSSTvCx5K+M5hZKsJFxg7QDmM+G3aYStCg6HrerfOeeCOJyxrzNHClMYWMh8pB0MHHMCMtEuFnkSOeT4SzUViI4Fg8vTpFUmouq+Uq8YXgmEqdAVmZsg6Oy0LYbDjdkQyjzoExq9uKF5x07cr4UFAdbX6NsmjXu0tsM+WUt+Vq7WJEWU58UinNUZeFg/incFEeUCcR6bpxCb5PGuG3FNuVVmsOd7UON1oy4YA80z2xhYptdOAdRuTN6EzQ22JYhiIiEFBJH8GDbJjbzdCy7ZGBsdqk27FAUTc5wt92CMkVGJFglwaVZvkMyDMORXpcEg18tmCW5jQxqPlxdeIXkB/RQWktpbe6Vkl6LHgl0Y0I3XhSLSzjyaBuExSXSjjNFOta7OoexJjq7ip9SaK4rEnHDGE8RBzzlTEdAQErsAtxrdjB5aEGTOet4WRIBz1ZhPF4UOrh5lEEKEz7AxVXZq/OxJm466dqjxVEnXsM8c2ntFrPYvp1N4yq5MCEtmLPtzXvWvwxLThdPVDKY81yvWlbDZeW6vp6OPtORTLSrHUfJsiNsxCh1QlVC7p3djsNINdNyHN4YK2lGOWC021m0RHW1vyUX8zVXOGuOjS/XqsN3VwLH3cHa+TrhUm4c0yIPAGW5bK8uAvp7lUouVp8tYehuba8gThPYBGLyOD7zFRqzXNqME8m/9f1svuuvy5Q3L9YM7nw8W/RjjRl7bTfr15fZxexVrWCxdZiooquqOJ+r+OFAilRsrIyBHWI4RJFoxVyqWZKmcnbY8gomSgeC8QNPHzLN2cSJMl4wDulFsPWhMQW+kNvkTNVS7tXFQmBz/4ga8Y47uHO6Vw40roViMl924Vm9LHNaqGwiXArIcFQ8cU5e8uN+obIS7S4bJLt1c/F0C2Cb6tsVfBRk0Bfk7WWHy55A7qW95S5cXN4dWNW+FXa1oRSORdyyMDEZ6Ruipm0YjamW3zGdVar0UpovOThjxzm8xCu2FTBU0giLcKsBPXDdmkNDQ7hkbW3DJtenG9c8SavbfKZ3OBlj4nyvwPpNWCqHgIBJzJeDjYZr3KJlomXvRBt0bc8ZOlqYhei2viwiKb8cg7NJkXJ4wIDVC/OGDSQzcxJPutjDQBjz5TqWD9m+o12e9cMWuyjrOUzdcirac6tr2qzFa3T0UEfxybzH+j6I2PUeY+jT8sRKOtX7YKwkQN9eXcQzc2M82+MzNjxsbA7hjPMsJxjZNdoVt17MdOOatKwe1AvFWaP9DQOjUQSsrmZ5uXSjON6exX2pzG2qA6MCezmI2LzR1VmESeeWdlWqITs3v8gwznKLAldRh2V6OmJOvcDMdZn1Y/jKW1dHzRw3XXiLrRpjadVkY8h0/OpKWWFd0o3cHwjKgFVFdueIjXpivrmQzYgq6uBQcYt3Qs7etsGaI2aHYVmjODXHJZZc4qywmCsxXWXq1Y9pXN3tu8pLyl7TRsSNfOe6nAXzFquldFjYdN/J19vNTftZ6Z5A+db92tGYPX27zQBsjweZpB2l94Vg3fadyiK0U4kGWpN26Z9J24+xYJvFJtWs/Zl8TYS9SAmZHfe+WkYXZsALYlzV16WGowbm3yR/Ho7Irp9LyFlEwZjXbNh2N+Pz4JTD1JnvI4KGu9Q5IHaBOgDhN/RKo7iyqw1PJHTLHnBTX2h6o4n8nsGK87xbL+Vl4G6Z4OYg83N39kLhElZkhrBi2ZJznPaUjggRfMZZwfLMJxqmw1QM9u4N4QlxAN+srGc6v/BUht6sjGuw5+hi5cyCaxDV/U7z2CzgHcWJNE4YC5t1qr0Tl7UVpziHdVc2FnG57Zi2SGc9ceakNHWOjkDTpulvI9sUI4WbtaWd89iyTGca6nk4H52F/V7Mxa1IUkI0hOpsd+CLWYTcctPeU+Z4cGZ1euUVJo7Ds7uvVuuVLCcDtwNbGHcND1xKqwQnZPFCd3x1WCyGW6Jk17DXMKo4dyhOc/BppW/QcFUwDPPzzy+fXqaT7ef59P/sLfZ0PPi/dkr5OFB8f6N1P5wGw8WXu6wv/0M9//rppXYioOXjzLZJu+B5mPk3J7af/6WXIxPL8fEKeXpFN7TvbwFaK5j+eOolyt2uaevxrSnS7n6Q/OnF7prpzzaat+eB+cvd/KycTt//xlxwx3KzKI+m17xvbfH2OMf2XqY/sJjeQHlu9O0yeB5xf3pxRxDmyGneMJJ48+py8sPzxQswf/6KvKIvv/8/SmQlw78mAAA= -->
