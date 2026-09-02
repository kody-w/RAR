---
name: "rar-cowork-cookbook-report-schedule-frontline-workers"
description: "Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_frontline_workers", "rar_sha256": "792a6ed2d24f91e395f0a3f7cc85359400b5fbfccd0a7e7f7793b74c834ac300", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_schedule_frontline_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-schedule-frontline-workers:7b0f5bbba1973d5f3c6344605c3b2658c4d8b4cb27151299b35032c937cf1999", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_schedule_frontline_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_schedule_frontline_workers_agent.py` is
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

Schedule frontline workers Summary Report — Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-frontline-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 792a6ed2d24f91e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_frontline_workers_agent.py` first:

```bash
python3 report_schedule_frontline_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_schedule_frontline_workers_agent.py   # or on stdin
python3 report_schedule_frontline_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule frontline workers Summary Report — Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-frontline-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_schedule_frontline_workers',
    "version": '2.0.0',
    "display_name": 'Schedule frontline workers Summary Report',
    "description": 'Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-schedule-frontline-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-schedule-frontline-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '251e8099fda9fa54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/schedule-frontline-workers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-schedule-frontline-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.429, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ReportScheduleFrontlineWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScheduleFrontlineWorkers'
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
    print(ReportScheduleFrontlineWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebPiRrbnV9Hc94ftx61C+1IdHTFCYpOEEAgkwNVxrSW17yvI4+8+KeDeKj+3u9sRE0NFXbRknv38zslMfn2x2ibIq5cvLzqwMmRpJUkYgAqxMhcR8j6vYviVxzb8jzh51lSh3TZ5Vb+8vrigdqqwaMI8g9NnbZi4NWIhdVO1TtNWwEXqNk2t6oZUoMirBsk9pHYC4LYJQLwKEkvCDCAjD1DBmU4TdmFzQ/qwCZAmb6ykfkWaCmQu/B7lsStgxW7eZ/VnyB5crbRIQP3y5ed/vL6E8Prly68vTmLV8NHL/s5Sf7JbvHMzH8zg9MTKfDiuuEH1M3hfgMrLqxQ+coGHPO9+rEHivSL//d9xb1V+/dOXrxny/Hx9Gf/t2wxpAgDFteoGauxYhWWHCVTjM8InvXWrofLQGNnTMmHmf37M/EYpL5C/j+9+fDD57IPmx68vORTBGm379eUnJK8gv6odrz+PVIoff/qc5D2ofvzpG526tSPgNCMxKPXnt+f9kywc+G1o6N25/h1SfXjRBl9fvlNu/DzkHvWEM18+R3mY/fggXFR5BzIrc8CPP/0ZWWh4J07CuvmP6P78IBwAy4U6PQX/6fVu5H8gk6dCHzT/nG0B3fpXNIHD39m9Ik9D/Rntu/3/B+kxpuoPi/9Tcv9swuTvyM9/qtu/mvCKeF9fRJCEHYwOOwFfkF/fdG0u/PyD++3hD//4DZL+t2T0vK2cO4W31MpCD9TN29vPP9T3xz/84+cf2gLGGrDSt7ZK/hnNf2bXO5/fWfA56sffz4X8j1mcwWRGPiId+TUv/lf122fEsJLQ/fa8/oJ8ny/jZ4KMSrwzfZjgu5ypoazf2fGnl98gQmQPZBpfwyz/r/9CNqFT5XXuNYju5G2DQAc3YQpG4Q9BWCOHZ1L/ostrRfmcur8g8OmY7hAirDZpkGVlhQkC82H0+KgBhLhf/rdzx81PzhM3pw/4e3vHvrcP7Ht7Yt8vn5FDAPnmVeiHmZUge17TEMsHWTNyvMcGxNJP3cgUChQ+QGcvrEfAqSHNvyG//Fsub3eCn4vbqMbXDPrFgm9dpAEpnGlVYXJDrBGn7FsDPkF4hVhS5UliW06MjH/a4vNoGzMA2dNiDiwZ4AqctgFIkjtQci+EkPwKnV7nSQdxcbRjHYdJgrhhBY2Uw3IwYjm09ZeR2C+//GJbdfA1ewAxgTxqSj2FAz4ERj59KirgJaEfNF8z4AQ58sOvv/2A/B/kX826Ex95aLAk3A0GgzlBJH2rIjAz2xQOq5ExLCDs3D33628PT4zSZbAIwnwKvRDcJ0Nq38Jg1ODhnnffQJ1HEcdCduf0e7shfQDtgoQNtBbM8fr1azaSyOHQqg9r8G7Ex+SH6d+d/eAz+qR+2hD6CTo3vY+9R+DoTCev3M/I2kM+LPUsu6NHg7xuYNAWsJaCzLnBmVbzzYVZ3iA1zJvau70ibQ1VHSn/YkPSo3FSCE5W8wuyETRY5/IE/hkNdGcPZ+dZODr+Ga2Px5BI9QOMsdk7ic+ICqA1kcKqrCKorBrcx3nWIyJgfXufD4lbSAZ6ZKzoYPTRPaPvkaf/efegP1uNR91HvrY4ipHI/9+mZBSRXy738yV/mIvIXD3sz494GjunUb1HszXSg93FIzm+dQzv4PIOu1+zJIQ+qG5/e4z07iH0GPOdPnt+f6c/JnN1pxs2MBBGz1bVGLzW1+wd36HIY1DXI1TBfI3H7M8/GI5v3yUNYFKO999qPfKIsVFpGL1I0dpJ6CAeAO490JugGtPoaXgYFWA0LYx7J/idVgikDq0P6SNQiBCGJ7Td3XQqTAfYHz1i+2N4OHZQUAq3daC0MF/AZ8QcwxeGYI3YALZB4xhohR/upJAUQBtDET8sXAdW8RBm7GafAlqjL/LUasD3Hni+hKE4FhLI7yPPIFXLtRpoyx46AabR9eHZDzmfvoLCpmPM3yf93t1PXZHvC9HfxlyDMn7DetiAjzX8O+NAgK7S+h5sMDbjGmZzCp4BBCPhXq4/Pyruo6R/yPLlDy38j3+ty7/X0OPvPfcFCZqmqL9Mp486917mPjt5CkudExagfpa8T++Z9ekjsz49M+t3hB92+oL8NeF+R+IZ1V8Q7DP6GR1fKaEDxrB9fqAthE+z8ydyfPs124NvTn5GwghjEFrt20c1eR8CS4pfAX8c/Kgu9ViUelgH76B2rw4fgfBME4iZmT+Wwjr/Ln1HnUa3Prz2Ab7wVTbCuju2cD4YlzfJKH4NXr5kbZK8vmRWCv6TZc0IsDBWxxu4GoJ5A1uiJgT3u4/2aLz5/ertnlEQCtz8y5hYsJjBVvYV+ehKX5H3dcJ96ZW1cKH089gRjyzhUPj1MfZjaWiDF7gya27FKPlj8TM2Ys8G+Y9CjPkEJXbAWK7zjwQdOf6BCLzwfVD9kcj2fmElT5SoG2ssgeFHSXgPyVcE+g7mHEwjiI4tnPBHNpBPBcoWFl13VPeb/b6plT90+e1uhuaxgvz15R0txutHB/CIGzjhP2/TRpu+l9e3kbI1zr83U3cT31vQN6heOJbR7175Y0/w9ojDly8Qa8Dry2jIKoR99XBfMb88xIF6fGteR+GsCuYsbAumMI0gJVisi1GHGCLedwzGx6F7Hz9efPmTjvdfpP8XxkY9yrZtC+MYwqU8wqEJkqRRyiFsnKZYh3RZm3RsnMEoDOc4m6BQAnc4gnE8jOM4KMVIPbWeUkyx0QdQ/g9D//U2/OVBANYLnKIhBYbDLRq4uIuTHocBgqM81CI8xnFYiqA4EkVtyrM9x3FRiwGMxzAcYTOkwxKk5RDo3YDPPvAh1dt7z/3ulQcMvEHkTMNRZtyyHNZhMNLlGIt2AIHahAMwHHMZAqAUR3gsC0g4/2Pq0zOj4x6Kj0ELW0DYgHUjn1+fnh4DkSbhyBVZr/nHR5hyhsWYjL0PbK6iwflymq7t8FjebEuJbAlgK9O113wqgqFe5Meqnqs3aY6pzj7aouvK3KjCip5puO7ZzsTicz2zdSWzZrOUbBzcbgkl9iiKZIzZfuGzTS17cjpfXkHJrY91sK/Hwn40Gxy3rman0r2ALQu8mnnelF547mm9bsBmgxOlFKmqcpLTqX2wDoY6FO3kdDtsIps+XGrliOq4dSTPR7AxtsqmdrtTe66rnTkdGpPGtIXvaFV4dU5UyG0JCpsMLOd2CkNrOIyD8yyNw2bdE0WYlHFmndTTRpGNdGlxpOw3dFCxGylyDHdmsKoexGasaRecCU/z9VSjjSFddwfh1oLdJLPC4pheQladqQBbiBF/3hjKdu9ZuwWG+4MqGbYkXFz3bBs6szqjS+3iOsok68rkTOTtPpFSoT6oR2p1CnkKxazbelADJzhkCSZKaLSunIUyA9qs2LbJIJ0ZCl/uRLkR1XwjoK14avODdApbp8JuO8bw7NvBL6aLbdVtUp/ClOM6tT3FTgLXUMskL4TKjLdRNEH9JpB7xaZy0axPnSJbO0kzmyOJG5OmnS3cktPWu3pGAolkpGNQhdsNpRK3PmhOykm5Elk6YCxLz+KwPRNVkmAMMQkWUUPw5kDjjlheGy+WzIYjW6EgxBoLlU24KhPb3AVzmcVMujRYuIQf6DYdfL2+NmEydf1ykxrZLWCwg5xVC21yzdFupk/PgolG5wGt6sNtucIGeWGaBSdK2ZTQTkYi4Grp7dFNndV9fevCYYulIR9ehBN6lU/77fawazd4UDuToEquWR5mjG0VmOT566xSVqylkfOjNYkvqS9op+l5DQbW8LxomK7I7UywF0SV6VOJClrTLkSssW6bLN8VgsHWVrX0b+cMi9dkRWmo3nPhcRC5nADTw9robk4452eLAqsLfbvjKHTI5cMNW1+KaD7v8etZCRctr7tLX1FncX5gDzMJ71Ny5a7DdaVkIXrZL1RrUtaGkfmBuloPLmCLE09rM4Wigiu7Hoh9ILOxfQC60hNBQgvNbSOBo2yKG24orVawKbnvUS+y9YbfblQaQps34ym5FcNh0k1Sne8q0eDySiGtdedAJKCkRsitbaP2VyhqTi8DzI95uVY7kFtayVa7gittv8excsnusnOy13VSdqKaS3QzaTd+sg4JtjvyPGhX1Ky0TumRmUwlp5sni1NPZSfZ0djAyglXrrZpYmduj2b7ebtZaHasw7Q5TiQpXQiKS+J1cKTm4LhdpcwRlPhsI81W5eyAa12p+ym9d27sNdm1eubVCmiEY3CJpjQoVvE8TnwvPqDra1eW+QVvmdOGYushRYm1qHP1zMjiG05xJeMU4ZVYnvv90vWJ/Wl22V7ifLY/CxeMkNpzwXZqY/rdpvYWvdpsW43CmXyfT/BzSk3XxCwpJRIsJ1NV2HR7gWLFTRFSOelvYT6hR0bS4Bo627X+RKCdlbHiGDRnV3Su9VsjGtrz2nSNmcjCLs7llX51jdNltmnEDgKm1S4cpyH7gb/4YbiYn5KQM3FZmIg+c4ZVcWAEaQDGhjpcylOFsUusbhfb8lq5SWTsLVsGa5WUN7vJks+4XSGxKecfhag3/J4Q/UWv88XquvTXu4YwKftibunzvuTXua638nyeY+SCLvFASBzjkolB7hdHu0+yOBBk9wywC2lz0ZXwJSFt9vRht2UWAU1LqcOcCjwOjnnmqrak3qbakHBe5ns5upcywusnpX4QWQ2Uhlxzwg6EoU9ygqdF2bDjGZmJ8AVG1tIpDVkvrMgJ0Aoim25Tx5suKfGqT+VlNcNKirXx65qXMH+PFpGlbRxSYNfS1mAVGFa8EqjcdYmRcpiuAa9bopFU7ELZ2FIpijG2dlCGDGEFoPeF4pVb36aiXcKumPPhplv4ET1uSyFgzlfUUnlG1LbBtgBNP4g3suKtLNrM13h2uO2iSKuMXRlJW3HqqGWzOTE7WyjtjVrfsOWluzq4Hvhkzl4XPT+fW7NGO9VhlB8VTxRFSi/pebNe9uuUPuDV1us22Jzc9Pvq1KDbVjcnWLXuwXktx5bGLhdtpm/NVXRiibM/Wcfy4dROJHGTWrtNdtjHaiqnpj/fWVrDSJV22EXW4TYsZtP6mqt15VkBs9kPG9HRd9oFYGq72cTAIidVs8RmrRBcF7zU6EQznyuzkDrP/X2+OZmGGHGVn2PCRCglOTwWjLBYV+hCX0f1BmYoqPM1cbFtlA3ETKjNLPZPJCUbhVNmZ0kTLoLdbXiR2d80F3QJrIGYMTOJWSwNdh+nV0MiSobZY4d+R1wb6XCiRW0N+64NtmpidDHRfDxZnxQbLWyAJRNDqW571Thp4lnjTIN2ws0lZXqT53Njy2CxnBdc7jb1Kr51ilBNor18QC8Cvz9dXL/am0s56pYUXwgAGwxa0Dtpa8rMWS3Do8CkyjyOwULQV8tkP2znvqGp+5CrVjiToRFtz1VejbMV04jMpfcYpZn7jrgYrkv+VPlsios4qO3smGBH7LiAPXucg+nE8SpTncbmbiX1l7XPoCpBq4E4q13NjaJctZVqhoaTzrDJS3XzzJDMDqVn4QQMuOWhcK58dMbarrF3fDRZH+W5eql6nBCrtdFvyn5qyuRNmWuLsPck6tINm0kRBVW/LH2IYgVKUFaRuDzpDdTSrNfn/WKPnShf3rqDk+hysuXEcxKZ9WTRG5gIVx9piYcDO3fPojBnKMXTJb5P/TRb05fBCJetblfVfHJp5XztsH1nUAubl0+Sb+jzC22Qc/oyUyZoyu5RmibkyzI77UzbX1Ew5YqBugbMaq87Do5Jdu6j/hHL+CZc1+dLWLg+xfanUI0ESbC3krto60aIJhqMbjrtt6aektTKPcRJb5nJil5MrinA52DVyOmKnBERHsJFRbPxMMm0DH4TXVBQXvQ+YyvdaRa3XZPNOapUJKIOmF3aytzcEru174rbXmc7k3PMjXRtLss+SvniNCci1aCpCS3YnG7qyyj1rlicZi3t76TTOfNupcWVRCNlWVCRPE8wx+DcXkJ0D7r5cWtHzWwWRiF3vuVeuZ6a+jwr6fCc4qWS2lt+65/WHHMwAl1u2GV4sHlq5hLeTmnVAl2sALM+8MbpuN0dXZir0s7QF8N+3/lrVkKNftnvdli+3eXyHML0TXD3tz2201JjXsb7vHNuBcqSmEvyhE7VVlDDFLXs+CRbRrnrDW4VWcNBjc7p7XLpGzKqw5NWp7axmOsao9LdRDH8QNtMNK6LG8VxCRnKOa89fSrc4rN/vvlWebolxio7MPgsxU9uYS/EYbkh5GCgQdebIk+2LhPubzd3UuHLZAEJZgEpHLvDpm9hAZNbjj9p2hwQ1nU5L5aL09nOJs58wypACIxqZ1zqM36s5bNv4UvrOL3t05lqB35ObbPGzs3LkU/ogXc2ot8vwCHgg+vF3Ai4nIibeI0qhk6i2ek87QxfNK4OygsyPyQn8uDvsz23ndS9kF743bHcnbhzq/XXrWv4IbVYSKTCRWpFy8HOquaJJm8thi/zlo0lY2A0/tqxQ7Ga5TgswsfjEJZr/+qerkejnp1MNNP4xAUyC1sPm6ZxQWKKQ2xHMdDKATirmZfajCsDJWDL3tDc3GUanHf1aV5l59VlihtbzPW6s+nWHkkLJCnQVkDYkWg5Vhm6M5BX622EeuSmnVWXc9MvhhY1izNofbwkpIqzxTnsCZaFvDn04TXvpg3nc2d/SdkglOsk49Sy1/Yud+XzTjDZwTtOvNmy4jvLqE0uPHBEJF3P8pbhBxvHcEB1ulQp7pW4pF5CHCAltJ9uc4rIm2FBpHS/8ll2502xhJpeefZiGKudRHcMu5teUacp4IJfa+nBtCSOkGxTHjCUZ7i5u4ovE4ULTf1inph0E2Dm9HxY5nFNJysMVm404JseL+aHVarR8+MOxEQb0aKfethldR06hVJvTbalqeVCtDH5aK+8HWBy0Th2vCNmp4wtCiJRNuvDuqTmhpSuOlS9eJGJtttqlRw0JpbEWGM5umWZiF2HIdcOEAgmp5N9MpzAS9VrZu0GYy07maXGmulyDbmcrfeMWhBYjzJAnzcHxmquQ6OwzXK6nHIkSe5ZsmpLkvOXZz8EXFS43OJKEJfWq91NsMCZU9T4ipAXWHLGN1jjAdgjwVVDSfnHE1il4pCtnEElhnaBTvrhvJ954cUccPXS9oMbmdpS6RahdTvQvBkvhrlNKBp7MH1nDUR+JTQaUZ/qpAuPya1ZZU0y20YicPI4WvWlyewUC99qEHvm+uSmKCaQJ+SkFylyKajnKZir0z6PqYk1IznQreMo1QgfFLwcEipzsBdNdOvpNd+fzgvRLyM3xWfXA+leNEyvpw0+FxqzOaARO5W7XJU3leA1N2JloiuXc+t9ygz2za1RWm4v2d5Wz+oNRh1c81HlYTvHbjRsclj60nXBtgmxGyC2bbo8tTMxXKkEKnWB4uW9y5GD4U7E1ZzqQJ8laJMRV7tk+6IkVk3jLGAdL5VDZ3F11fgxw3Ryd8Oig10yV1fG8jOdXB3zENK4n6FuN+NT3uHDkMnbPkKVrGDO8Y6nTI2NKSU56l08WUW9fzxcVM5QQK4FoX2wyb199VURdIUi9B4wGZsR4MpSacOJskr606lZDqfsRlLTRplQxYqbVcsuo68c1jIEsbxit+zYlEyO1pOJSSxOJsvVPqNV3CScTpXLgpA8AuZcinFrQr4GWnwCcwiES21hWLYwXU01pxZj29BSGXU3hMskp74zF9OllC/9OJnRbRcW1LRdHHeo1a62JCdyVJpeqaBrBqB4nLpZzDqD2J31kssSPkA3jJbzyzNaS2QsN+FBJbbKLjrSKzDL1hcaLpwAnjIxJ2iFJa1MXo4m9AoFIJ+7mUhOZIFswgurq1RA+bMzREIBJU28nw0gkiN5Pyka/YhrQ3A76rsz7OIsUd9xclsAbCUOCn+9ZqsM5zrYlPBwaQ9V9jdZs/O7TkcZXTvolBswKpdKNWfP51WHbyptssxFkkncY5aj8blusZOR4fmuzKbXXWvbFFFZPXVttx7vnMUaqk80M/24jFtqJqhRUaJiv7hiehJnYWZaU3O1Qv1Da5FDFDtMp4VOW5PsYsqrVb+ZqLy84/mX15f72ezLFwylaPT1Zdznf+7W/6W9Xn8Ii7cnKYJB2deX/3cbkY9NwfeTvPvWPbDcL3fuX/6ClP94famcEEr02B6uk9Z/bj7+j83WT/92B3icfnucLo9Hjtfm/aSjsfz7DnWYubDZq25vdZ609/1paOm2Hn9fUr89jwle7mqlxXjm8OA4kgVVFzrgrcnfnj+KeRl//TGeogE3tBrwvPWfm/mvL+4NOix06jeCpt5AVYx6Pg+Uxk3Z8UTp5bf/C083GJYrJwAA -->
