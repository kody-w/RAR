---
name: "rar-cowork-cookbook-scheduled-brief-manage-formulas"
description: "Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_formulas", "rar_sha256": "d3fd0240ac47c540ed2236161b30ffd9afcd0c2c1206aec780acf838f9929b17", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_formulas_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-formulas:8c5d40420669a8b3ee5cd599ea77cd2acbce95989761666636d73c4d68b12f82", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_formulas`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_formulas_agent.py` is
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

Manage formulas Scheduled Email Brief — Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 d3fd0240ac47c540…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_formulas_agent.py` first:

```bash
python3 scheduled_brief_manage_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_formulas_agent.py   # or on stdin
python3 scheduled_brief_manage_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage formulas Scheduled Email Brief — Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_formulas',
    "version": '2.0.0',
    "display_name": 'Manage formulas Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e393035e21427f17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-formulas'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-manage-formulas', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageFormulas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFormulas'
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
    print(ScheduledBriefManageFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e5Oi2LbnV2Hy/lHdl6yUh7zyxIkYRVRAQRBR6erI4rFBlJe8oae/+2zUzKo63X3P6YiJGCsqE2Ht9V6/tfYmf3uyq/KU5k+vT1tgJ8jCjqLwBHLETjyET5s0v8Bf6cWB/xE3Tco8dKoyzYun5ycPFG4eZmWYJsNy9wS8KrKdCCBxmidhEnx28hD4CIjtMEKKKo7tPOzhfSS2EzsAiJ/mMVxRDBdIeQJIDoosTYpw4JE2Ccj/gUAhYZAADylTJK8SxIO8OgTSNwBcou4F6gFaO84iUDy9/vLr81MIr59ef3tyIePim17Amw7KrG+S5w/BcHFkJwGkyjrohQR+z0A+qAVveVD1x7efChD5z8h///elsfOg+Pn1S4I8Pl+ehn861GwwoEztooTKunZmO2EUlt0LMokauyugbWWVJwViIwV0YhK83Fd+45RmyD+HZz/dhbwEoPzpy1MKVbAHF395+nkw+8sT9AK8fhm4ZD/9/BKlDch/+vkbn6JyzsAtB2ZQ65e3x/cHW0j4jTT0b1L/Cbneg+mAL0/fGTd87noPdsKVTy/nNEx+ujPO8rQGiZ244Kef/4otdL57icKi/I/4/nJnfAK2B216KP7z883JvyLow6APnn8tNoNh/TuWQPJ3cc/Iw1F/xfvm/39hHYUJKD48/qfs/mwB+k/kl7+07X9a8Iz4X55mIAprmB2wWl6R3962G4H/5ZP37eanX3+HrP8tm21a5e6Nwxusy9AHRfn29sun4nb706+/fKoymGvAjt+qPPoznn/m15ucHzz4oPrpx7VQ/i65JLDYkY9MR35Ls/+V//6CmHYUet/uF6/I9/UyfFBkMOJd6N0F39VMAXX9zo8/P/0O8SGB1lTu7TGs8v/6L2QdunlapH6JbN20KgeYKcMYDMobp7BAjEdRf93K4mr1EntfEXh3KHcIEXYVlcgiHxAO1sMQ8cGC1Ee+/m/3Bp+f3Qd8jop3JHq74eLbHQXf3lHw6wtinKDUNA+DMLEjRJ9sNgikSMpB3i0zIIh+rgeRUJ3wDjk6Lw5wU0DG/0C+/hsZbzd2L1k3mPAlgTGxwxu4gjhLcwjPEFvtAaOcrgSfIbBCHMnTKHJs94IMP6rsZfDL/gSSh7dc2DVAC9yqBEiUulBvP4Rg/DyAeRrVEBMHHxaXMIoQL8yhg9K8u7UX6OfXgdnXr18duzh9Se4gTCL3tlKMIMGHwsjnz1kO/CgMTuWXBLinFPn02++fkP+D/E+rbswHGRvYDB4tBmoobVUFgVVZxZCsQIaUgJBzi9pvv9/jMGgHGxACayn0Q3BbDLl9S4HBgntw3iMDbR5UBPlD0o9+Q5oT9AsSltBbsL6L5y/JwCKFpHkTFuDdiffFd9e/h/ouZ4hJ8fAhjJOfp/GN9pZ9QzDdNPdeENFHPjwFzYVxLYeIntKihAmbgcQDidvBlXb5LYRJWiIFrJnC756RqoCmDpy/OpD14JwYApNdfkXW/Ab2uDR678YDEVydJuEQ+Eeu3m9DJvknmGPTdxYviAKgN5HMzu3slNsFuNH59j0jYG97Xw+Z20gCGmTo5WCI0a2ab5m3/pfR4aO9I8JtzLh1eeRLRWD4GPn/NJMMek4WC11YTAxhhgiKoR/vSTVMUION96ELjgcPMUN9f4wM7+jyjrtfkiiEgci7f9wp/Vse3WnuWFblUBl9ot/4DxWd3/iGJcyGIbx5PmSw/SV5B/hn6GAYi2LAKli0l7st7wKHp++anmBlDt+/NXvknmhDAcAURrLKiUIX8QHwbtlenvKhlh4RgKkBhrqCye+efrAKgdxh2CF/BCoRwhyF3r25ToE1MUTkluAf5OEwQkEtvMqF2sKiAS/IfshhGIECcQCcgwYa6IVPN1ZIDKCPoYofHi5OdnZXZphqHwraQyzS2C7B9xF4PIT5OHQSKO+j2CBX27NL6MsGBgHWUnuP7Ieej1hBZeMh8W+Lfgz3w1bk+070j6HgoI7f4B4O4re8/eYciNJ5XNyAB7bXSwFLOgYfeXrv1y/3lnvv6R+6vP5hlP/p7037tya6+zFyr8ipLLPidTS6N7r3PvfipvEI5kiYgeJbz7vX3ed7lX1+r7If2N699Ir8PdV+YPHI6VcEf8FesOHRKnTBkLSPD/QE/3l6/Dwenn5JdPAtxI88GJAMVrPTfTSUdxLYVYIcBAPxvcEUQ19qYCu84dqtQXykwaNIIGwmwdANi/S74h1sGoJ6j9kH/sJHyYDs3jDBBWDY20SD+gV4ek2qKHp+SuwY/Ps9zYCwME+hL4aNEKwZOA+VIbh9+5iNhi8/7uBu1QRhwEtfh6KC3QzOsc/Ix0j6jLxvEm67rqSCu6RfhnF4EAlJ4a8P2o/toQOe4Kas7LJB7/vOZ5jCHtPxH5UYaglq7IKhX6cfxTlI/AMTeBEEIP8jE/V2YUcPhChKe+iBsPU+6vo9K58RGDlYb7CEYGJWcMEfxUA5ObhWsOt6g7nf/PfNrPRuy+83N5T37eNvT+9IMVzfR4B71gy8/8MpbfDoe3e9PbVvq4dZ6ubg2/T5Bo0Lhy763aNgGAne7jn49ApRBjw/DW7MQzhS97et8tNdGWjFt7kVcoB48bkYpoIRLCHICfbqbLDgArHuOwHD7dC70Q8Xr3897P554b+yLuWNsTGB0TRnsw4JAOV6FMcBm2Fcj7BdxwUcxbEcQ+M0/JC0x5Du2KNZByd8loA6DCJi+6HDCB/8D7X/cPLfnb+f7sthlyAoetj/k76HEWPMdseMS40x4BEECZXBHRLzfY+zfdfDXMLFoQ02cBkWUvosyfocR3AOzgz8HiPgXae393H7PSL38n+DeBmHg8aEbbusy+Bjj2Ns2gUk5pAuwAkcmg4wiiN9lgVjuP5j6SMqQ9DuZg/pCqc/OHvVg5zfHlEeUpAeQ8rluBAn9w8/4kybJhhHPzloToOjdRiJTri7RqS9Mg17pV5pY+bxl8DaeGkymXuXUM3kSzYr1ifGDheBQQkJM90UJUutmU7cZR0WsvsQ0ouJdOktlolUjrXkIOQxrbI6arfd4kpFX1qbNTLryhiqyeeqEknJ+BJnuLliuaKq+2O4Xnc7IitavM7yxUbOxtkVIxd4ck1Gc9eZWFt2N9/ZnSlbWmXsMazrl/uqu7ihadq1W7WHhQlv7IKT3RXNCL9mHdE458sx6SnaS3qMAYcNURonBgUOi+I8G9hngZIOstwtIXbi8mFPclJ5lfXpscNPF64hUMzByeM10rs1m2GHddah7Ek5LPJ0bHuBluE7T4uU/jJS906/w6TZnA7TXd8V4iqZBzKqiVNOX1l2JV1USY5M2zkstLg6GIm9ss/YztmUjp6jOZb21kG2LFpTdMnILquY1s4buj8boRlcI/fYVUddvUh8Rx1Uo8HbleuQ++6QJ5uJvO06UppH04lJ2QWfqZwyC/zRalL0tu2cJXXP11XiaSKH09ku9U/Valt1VbtvoZvw3l22bdeKzlQv4jFlN9wVX0lNnOXtBd8aFkm0l8zP9hm1MIN62WyWpnxRjpqEK1bnCXgu0Qmdkb0lV77X0DtdmEV9SDBMvUvaRZ6ssrO3OV1bJw3IvRRzCXMJmG0TQmdUq+nFBuj2YF57Rc/Nqb3DPSnI9gIq4j7RmPGxNBrM5RRw7NqIa7l5Lh1m/Wx+yonjOJnJwGh2hdtsiXgj+opfMbQdkqY5PxzRuNuz680ybwq9sNJAPGwDpsCwfRV0TpV0tlInuwhN18oUjAxmgU6n6MglhVE99UHDBqQaCbtkNN7kywnt+yuOW67X54IyKfxcgwu2J8fZWCbaLX2Vu4KwZGkO8t0VT93CQIv9otX103khVTBnQcmSWCctKiuntl7DV9xSPpwvPOpd0Vm4mQGzmJ5lmeg8Oz05zXE3FRbYTt/hhJ7Nx6sFtfDEcGKsrnpjNkK27WTZLvpmHM9Cvd5QO+vkbTrTZSuM3dVJOD5xghH5uojVbUJzZSdLQJgSDowTcbItUrCVkcjy5NJu3dDBg5rbCEqbjjFZmfuR13h2kaOGfKwP88U68huUdDrpWmSFqkiE6OKtNbYJTDgJebPpyVmL4Tpmg+kcDfVdX12N+fa6zYAMBwV3FxHR4rw8jFYUL29SDgtJN52unY3f53NKuIajJX+lrGBUXHf7PnMdjMjRsrSFHKazaRUT3sizgmkzKdKuuYt7K17vrqP0LNb7YLzjcXUn0cGRmzF0yEr1HKtygdoZQUaOw0O+j0RdG6F5qmd6nu02hLgRpgCGVWIOFpypUVen2kM3FWtnolhbWfXUyCO6Y+Fl0eaorGLB3pyd7tjmib0TkgXcluKHdD0GxqyAKLaUTxh/JJKczez+kLVlz25lX93NaktRaB/vjIUoimov96sz74DAGnH6EefErDZlPCcn5oSrNs4MJtLFmqI7slDXaE+ux8LFCpwpHsVJwLGTcedNV74bbGQ3LZdCpS560E+s8jqTlkm+NFfGaeJktB92vsvH5ISWOrgzWybtSCBFXw6zzuzIrIM4k2yERRQamsfPUktzpPV500h83K3Wx71x0RpeyObThW9oM7s82yTnXdvz8VgFko2l1zGux3mzwpWCh1ux/mjOplgpzj2PisOLs8tE0hof6vZM+vmWv5zLKJnXPM5WAa5yZEtve9WYdeeCpVFwoGiuXuGL40VwDGk/pntn09mmNTe6xE0U6zLiAysMNRa1UTDfzKspTpCbYnXWtZMcLn2yHDOocKCLJde3HFs5/SjTYOZ3p5S1rEN9LcaSOF0XvBqtVzoln9Wc52e4e40NNVCb3vf1+XLulppw0OyKApOoCrO5coAKiJzMSjQ1oePYxsNVPV8HjAR0nBaoyZIa2ou1PrnzKZpr3a4ZZSEHq+bELi0WZ/ML9GFY4J7WHJTF9hgENSGJpoqrMw5M2UNbEoUdlU2Z6NFVIGHbsPJNCX81o3Ai6sf9OgN02J1ZrlsL/XnprC1XcbVjm56peN0s7Q2dyb0trbB4VcdC7RT2FhiTfIKWS3mqZddoNqeOqequXN8J/XB2WtjKknD83XkxiVYLmIRulM3nG2W7tyiv2xuHFm0uvX/iwzBow1m/6yNta07w9c4gzexKXPi0T66j3NpTlq0dA5m13cw9rDeyKLpUepybLu437FJReEnMDl2r5zM9mkwMy8b5fSD6U5E1+4t7oQ3OAsvLCqSTo6kGm6k/J82rYYV4zjsLL7BdPjyic2cNI3uwqY0+P8lSGBCsxDNVuwSMeZb2Qp2JgltsHc2dBzO2vzhrAWJFBh20jeiWm+6ZsgV9drLtzIouErEambgdiSfVIpRpNqWlHrbvjGZK7LzcSTUfKftxcOHUq5CIo1212+2iwymEyLzVYNNpOLspMLNrJBWITrFgp7a2m862sqKetPkUt6IteRKnBr7V6qDlcBe9KIaWpVPvwowYDSW6DTq222wpti4baYLcANOr+ygVKVxyTGy3MA45JS/rUZJ0be2zZ/6YoUknqtysABm9HiunzAsB558dcKyiQ9Q5nnGF7XN9EGlTpwl0jNf8bGvPLv1Fpg8k2E9EfrvgTxOCXl8pn7FkVU+KGbWwp+tSG60lndvkJrG94EqsWJO4sS+L1HbdzJSSo7pao1qUTxeZltL5ZWwuVbYysum2BsGcoV310FGmfsLHlCkrPJoZ4+lkfaqnXtcVyupy7McHXdns1GnFO5nQ2mNvvtYpKfRjI4smW18MdsTUkvVcuOqzax0bIAWut4oU34DTntLwbAW2WMSN17KfZaqMl+uWbGyQWZaYi+HeXFPGWvPked4eT02nxavzvnUYUZOnFgnTDg9JbVyUqRS6hOX3RrlaHcMmFVjHHYsNzU3qEM71fOxgGWfMJ1ZxxMpk3tnENW/DraltLfVYiFHJlZbCRexYGI3NKwi4bsno/ZivezwXrF49OuJyuyxsdFtkGgwjVyx99HJJr2pLnHMIIyTOaiKD6hvdU1FKtwyrHqO8OvXMwtAOvEGH56NOK6muCnB8JD2x1VT8kmK71mzXW6y/iJVXjCf0tDuTda7WIrbIAcOS6XShH5UR6yZXio7zurzyILKbuKOTfSZjqUzJ+HVCNjwnjDttdkzFEFsquwUq40ozyrVCKMyZROlStj73kZq7blGsauFg47NgBzvuuPM9XjK8MpdnTkM463BboR4nUrPZ+HRk08sV4rUp0Wmd8YftabZGR3rhUkq9oY1VEx5z35hNe8tcdPNJt9vEcmWrteaJgrFK4n27Y9vzpkt3aJJj86RRwQGQiSupI5cx9qc00PqmUPLY3J/AGiNXKs4f0NFOHW2xeRQJ8+QoJdfjcsfOfGFvxbru1WE1Hi2NZRBlOirtXSxbz+cLCmNXBRF1p1I7wkE3ELHZEduBvuD3c7DGr9ik1XpHNVZ05yk5N5qK+EEi9ckymKCRH4F2tSSXx30jwSbGS3Evu4wgUlqEBzp62ptgL44NOPQdMbENsLo/C9fuSo0gio98ljmvUhmARUvhrWceen4iLk5xFQojm61cWWXnEja+bOR4JkaEsKRJtV7WXs76QUW59pmDs0VMkTRpdpfyKCYVq85QZoZaHjlnqmlYLVfJOu6aYuYSh7UvXiVehq1YTVsimVxyMkhtb4H1hMXOlE4y5ANYut50wnkJvqv6A5VMhB1r8bbqHurTOqhGMTEFnWgTqt2Yh5hDD/iE5HRGb9xjcK4nJL5J+kBuVjDb+EO1HcWhoq5mOqMJDtpUWMSPpH1QbBIvcoBXzC2RzHTWPxlpxxBKoeCVqlOoPRr56cq/8MT62mGj0h3BVKhThjxsgIrWguNby8oydgYhXMIlXgUpu9zolabRKyac82Z3bq2RpnXGNJBNv4MJb4oz45z1jaCoG3EjH8lpIbTdkir6gCajOI4IJvLXo3mgxHSvkKm9mTZTOt9vr1ZznVUHnOmSpbyuZWAttlIUsUuwG0/LuD25s3jOuEqOT9CUCyqV7ezpsbVCrhL8kGVWdn1ZsQSw0GhtbvmopxYjkhHReAxnoTWxX0MlrlJ2btEVfvGZ6LrhPJPORzQ+Imdzfu/xCqcLxQSfX2YUhS7aZuMAP+bYViBWh7zUNgvxxEzKarV2lmRZO/1Roa8OzpwnsEHg50qJmYxZMr5olcElbYSRRydxI0ioFBK7oJ3gaivQoUnNQbtYYUm1r+NsrE8CZn08JLRy0shW3rOHGdnmE2Yb+Mu1OKZYeTYzps5WQhlsNu4MdleU1jghl4Tmq5PGzBdOE+YVnBt8+lQnft0c181MwZbXQG2tNHeYMaA24jkIZlMnmKF8tsLIxpWns7Q8XVczdHTUr9ey0s71mZrDGtByVx9Juas4a47ECfHknKRaIoxDeqVidx5i2kjmrgfYGXeZMDYOq3TUMH26R1GBJvKD1Ls07VroWFBF96BhMSqX6HmKbc4zExuvXSNml7x1mNn1cZUQ45KimWWVBTN5elQiHScckmdSz6UZOQExvWda70qKa2XLFIQ4rspA4pZOo0kBOZluXYxxt/QKxzxCEiaqeUaljY6aQk5tTmNOnAuE4Zsued2M9zFGoMKCPc40JqLkMZgyHWn5VDFyLB876AmobJw5hNicrVSf2Y6BPR1p3Ska8axy2DO556G8Pd+XR4X0/XbRWuR1tBdjqvTqxh9Rvls11wXroAJxuNR+oU86vRzrWTixWQXuKjxihe45dyl2V9/VU9q6MgRfByiWs/Y+sHn+OL/a6CohadpsZ3p2PkCYA5VyQTubiXEy7PYLIkSnV6PKT/NTmGAAUzfaOUCDBgSpZoUWXL7eaEzZzXXDacuO8AzHr52tl6KOH7b7Cbvarlep78Ipxogn0EPsJozLvEn9y3J/VIPJvhIk6OLJIWYXlmAa1BZurvBJn/U7/mih85nlXFp6p0jM3q2nBddPXQtuhDhSsQKfHYFSDdZ1aARJRWOjXjRsyptiNRfPK9dx5/sDszEThsf0ictCwMXkvbJfzs9hju7EuTGKskiFHY3YFLzrn5NmKfPOkm9ogC2ki205wkQi0CjVRsJ+iS8vO2D7rdlVKpN3vqrRjrOgSAB62G/P2JJZadiKU2RtMnl6frq9on16xTGKIZ+fhrP+x4n93zjxDfowe3swIhmceX76f3ckeT8efH+Tdzu+B7b3epP++h/r+OvzU+6GUJ/7EXERVcHjEPJfjlw//5tT4GFxd3+9PLxubMv39xylHdzOqMPEq4oy796KNKpuJ9TQx1Ux/HFJ8fZ4TfB0MynOyseR8Hcm3N9ChEHyVqbD6WuYg6fhL0CGF2nAC+3y/WvwONOH9B2MWOgWbyRNvYE8G4x9vFUaTmiH10pPv/9f1viqIjYnAAA= -->
