---
name: "rar-cowork-cookbook-dashboard-purge-and-archive-business-data"
description: "Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purge_and_archive_business_data", "rar_sha256": "85b59e79625b4aeba5f3010e6be87be6a30ca1a229bc03d1279abebc620cf620", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_purge_and_archive_business_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-purge-and-archive-business-data:b47ae539bb087f8f6a1a7b6beaa17dcf4232aaccf410cf832bbb2fb8dcf2135f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_purge_and_archive_business_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_purge_and_archive_business_data_agent.py` is
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

Purge and archive business data Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 85b59e79625b4aeb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purge_and_archive_business_data_agent.py` first:

```bash
python3 dashboard_purge_and_archive_business_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_purge_and_archive_business_data_agent.py   # or on stdin
python3 dashboard_purge_and_archive_business_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purge and archive business data Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_purge_and_archive_business_data',
    "version": '2.0.0',
    "display_name": 'Purge and archive business data Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-purge-and-archive-business-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b14a47f062b51d68',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/purge-and-archive-business-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-purge-and-archive-business-data', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardPurgeAndArchiveBusinessData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPurgeAndArchiveBusinessData'
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
    print(DashboardPurgeAndArchiveBusinessData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOj1rbmX6HzPti+ykpmEHXCEY3QgBAgBAgBLkcWM4hRDELg9n/vjZSZVT4+vmeIfmhVZCaCtdfwrXGz67cnp2vjsn76/KQFTgFtnCxL4qCGnMKHuLIv6xT8KVMX/EBeWbR14nZtWTdPz09+0Hh1UrVJWYDlSl36nRc0kAM1QRZ+moidpAh8KCnaoHa8NrkGEK9LIuQ7TeyWTu1DYVlDVVdHwV2eU3vxROR2DVjYNICwdaBPUFkFRQPYAKIBcuuyb4L6GSpKaIlTJOR43kRbBIEPhLkD1MYBdE2CPqhfgJbBzcmrLGiePv/y6/NTAq6fPv/25GVOA249Ld9VUSYt2MJnHzos3lRYAg0Ak8wpIkBdDQCrAnyvghqonoNbfhBCb99+nOx+hv77v9PeqaPmp89fCujt8+Vp+qd2xV25tnSaFujqOZXjJlnSDi8Qm/XO0EB10HZ1cQcRQF1EL4+V3ziVFfTz9OzHh5CXKGh//PIEEKqdyRFfnn6CAKZfnupuun6ZuFQ//vSSlQCOH3/6xqfp3HPgtRMzoPXL69v3N7aA8BtpEt6l/gy4PlzuBl+evjNu+jz0nuwEK59ezmVS/PhgXNXlNSicwgt+/Omv2Hpx4KVZ0rT/Et9fHozjwPGBTW+K//R8B/lXaPZm0AfPvxZbAbf+O5YA8ndxz9AbUH/F+47/37HOppD6QPwfsvtHC2Y/Q7/8pW3/04JnKPzytAwyEM+142bBZ+i3V01Zcb/84H+7+cOvvwPW/5SNVna1d+fwmjtFEgZN+/r6yw/N/fYPv/7yQ1eBWAuc/LWrs3/E8x/hepfzBwTfqH7841og/1ikRdkX0EekQ7+V1f+qf3+BDCdL/G/3m8/Q9/kyfWbQZMS70AcE3+VMA3T9Dsefnn4HdaIA1nTe/THI8v/6L0hKvLpsyrCFNK/sWgg4uE3yYFJej5MG0t+S+qu224riS+5/hcDdKd1BiXC6rIU2tZNkEMiHyeOTBWUIff3f3r3IgnL5KLLwR3F8vRfGV1AYX98K4+t7YXydCuPXF0iPgfyyTqKkcDJIZRUFcqKgaCfJ9xhpuvzTdRJ+L8N3bVRuOxWepsuCv0Ff/2Vpr3fGL9UwmfWlAH56FPc2yKuyduokGyBnqlvu0AafQNEFtaUus8x1vBSafnXVy4TVKQ6KNwQ90G+CW+B1bQBlpQcsCBNQqJ9BEDRlBvpAO+HapEmWQX5SA9DKerg3CoD954nZ169fXWDAl+JRmHHo0ZAaGBB8KAx9+lTVQZglUdx+KQIvLqEffvv9B+j/QP/TqjvzSYYCGsUdOBDcGSRoexn0qajLAdnUk4DPHf/uyd9+f3hk0q4AHRTkVxImwX0x4PYtLO6t7u6mdx8BmycVg/pN0h9xg/oY4AIlLUAL5Hzz/KWYWJSAtO6TJngH8bH4Af270x9yJp80bxgCP4V1md9p7xE5OdMra/8F2obQB1LAXODXdvJoXDYtCGLQhP2g8Kb+6rTfXFiULdSAPGrC4RnqGmDqxPmrC1hP4OSgWDntV0jiFND3ygz8mgC6iweryyKZHP8WtY/bgEn9A4ixxTuLF0gOAJpQ5dROFddOE9zpQucREaDfva8HzB0wCfTQ1OeDyUf3DL9HnvJP5ozt348pH7MB9KXDEJSA/r8ccSbT2M1GXW1YfbWEVrKuWo84nNSbYHlMeGDKuOtyT6pvk8d7kXov31+KLAG+q4e/PSjDe+g9aB4lsauBDiqrQu/m13e+SQsCaIqIup6C3vlSvPeJZ4AXcF8zlTyQ5+lUNcoPgdPTd01jgNr0/dvMAD1ic8IORD0A0s0SDwoBEPcEaeN6Sr83/4BoCqZUBPnixX+wCgLcQaQA/hBQIgFhDXrJHToZpBGYsx458UGeTJNY9XC3D4E8C16g0xT2IHQbyA3AODXRABR+uLOC8gBgDFT8QLiJneqhzDRCvynoTL4oc6cNvvfA20MQwlNDAvI+8hNwdaYA+VL0wAkg/W4Pz37o+eYroGw+5cp90R/d/WYr9H1D+9uUo0DHb70CTP3TLPAdOKCw13lzj1nQpdMGVIE8eAsgEAn3tv/y6NyP0eBDl89/2jf8+O9tLe69+PhHz32G4ratms8w/OiX7+3yxStzGMRIUgXNt9b56Z5wn4CgT28J9+k94T498PxOwAOvz9C/p+QfWLxF92cIfUFekOmRmHjBFL5vH4AJ92lhfSKmp18KNfjm7LeImMogKM0gt9+70TsJaElRHUQT8aM7NVNT60EfvRfFe3f5CIi3dAE1t4imVtqU36XxZNPk3of3Poo3eFRMbcGfRsIomDZN2aR+Ezx9Lrose34qnDz41zdLU5kGkQswmXZaIIvAoNUmwf3bx9A1ffnjBvKeX6Aw+OXnKc1ASwQD8jP0Mes+Q++7j/u2rujA9uuXac6eRAJS8OeD9mN36gZPYNfXDtWk/2NLNY13b2P3n5WYsgtofC+3UzN5S9dJ4p+YgIsoCuo/M9nfL5zsrWY0rTM1UtC/3zK9AXr6YP56hoAHQQaCpAK1sgML/iwGyKmDSwdatz+Z+w2/b2aVD1t+v8PQPvalvz29147p+jFHPKJn2rP+20PfhO17s36dJDgTn/todof6PuACHm0yNeXvHkXThPH6iMqnz6ACBc9PE6B1Aqb28b4rf3qoBez5NhoDDqCWfGqmIQMGSQU4gdZfTbakoA5+J2C6nfh3+uni81/P0/+sKHx2CdoJSJxxXWROh/OQclCHdik3cByU9r2QwHDMAa04JFDEC+c45rouFrpz8AhDcTIE2kyezZ03bWB08gmw4wP4/3zYf3owAl0FIynAaU66JBPQDIWRLuEErkOGOIIiAdB2TrsB5eCIB9THMMb1ENxHMZpx3MD1KAyoDn5N/N6mzId2r+8T/buXHkXiFdTXPJl0n0yfezRK+AztUF6AIy7uBSiG+jQeICSDh/N5QID1H0vfPDU58gHAFMxgwASjzXWS89ub56cApQhAyRPNln18OJgxHPpEu2rsMjUVWLYJb93keBlc149dwUb5jSevOH2Rklgy3xrdSh6EFSp7dmQjJX2SZI6nFgqmha4309hKKzaaGLvWIiUSD3M7XExDkiRoY6GuSzSQzajYDOTtVjh4lp0WlYUdqvNmRdZjRputzc2pIU9PcHhVkr0SrPNCu3Qe7LoiPRsMtM50zZKI+bC1zoVsrLNRlGY2z9ESRhhiZRRoZGKFvj4l8oJbakZ3cgqjjQWqP9arIoRpajd3xvPeOR063RJlbAgS3MpU3Tw0wRnx8tGe+cWI0EGxRGN7gMNCmVvN6FlCZ6xOuhKgmy6zXQzNW7V2jPNmR9K7qKJjmRQNY+eeopzZxMceRZmOdztBWyeC1FuH/HJr5IVHKmOWEh1tJ7aKjeR4XDkDLigXSRZnhpbzJXdCEcF1DpeTsxk0augMt/HPB4tBadaCDbLyNWNn5g7n2KvqtFhgm9maTG/WYCFXa7s3bcHUuMU+MI/VibtoJ9oEG5mrKQWLJqM0emuvBRaF66az3J3JdV5tYEOFOo57FuTLUU8LEuvbdnu2l1gbSAzO7p20RJem3Ic8b8RLl5MjjKdPG/nUBvsjdrzW2sVzdzB2XTjMDt1vh2ZBAJ3o6hDV2mZ/HAepznlUisNrwfku7N7Gcn/YVIXfYebpqgzr0x4PF/TejYd9vTEwNaNgLCG41AMor7Zmid8iu9x6rdgz9mWLD/Ne2V8QO2dRNaZdfYYlzWhfXIFXDPMiNUboX1VnLmyZ/mZpTC1pMapsCeOSS9sGu5FL8oyi4ejnVA0WFnNk6MblSM0EyT05W26dChJ21R2s0h2iYqozhVbJBq1a56iExd7gFczRakwI421RK/TcxQk+dWYpmUeaYsDWFtapQAorlEk8/tDt45DeCot0NiBZI+VIvSlHDpW0a1ZVjSMKSXg6Jk7TsnG9xATdkzb1st/56xZM4FoVCbCsiMa53Af+kVx6RKehxzGiNsOttUiR1ZY3R9p6y3iXVlyhedugsRuV17YDppaLdYPaFZ8ZuoNQEtkTeX2+pfl8pTZhuGd9OSI8qh70067PEM29mWnHGbHYD0y1myvHwmJpoQwEUjzejHlOaH54Zrr2tls39DkEhVsbrH0npqQwHmciKnIzMumWqOqfrVWyzOU0V+OjzJvI3AqU0+rAUkh5ApVrn1+6TMfjfH8281nqHBFpFWuX/sCXSJKxpy49e3FGw56xuCKnmersUzITvL2wojaX+VyoslxktCBtCwq4RjZh15NEvhJcrojn1RXLdgqb6i1/djUA9LYp6323S3xt1hSJZBxNvAzCgxwHREMe7Vys5okCH8dLt5v1kt6YNE0JYrbatSZ8iIi4wrWs9NHODlWbYZa5sBQljmnZdSb0FVpfxOvm1uPazpfKbmvXYt9k0gYt0oU4I7OmoZgsK1Y3d9cNNyT1OY6tKBixMMvfyF2YCKNNJb6+GK9j31Uym0TsKLmmv1ztUY64DmdLGNfrhhJQvsflBWXMAwUERLTimVkajzASzEF1W1gbyvOtnceToLrq20of0/w2rHmJyG2CXroS129WStr5J7jSsW3GyDpzjfk4RZs49y4tyiPENXex5a497pF2SyaXpj3vVyYcWf1FYDdLdTPo8pVY5ZFOEMGu9MWOO6wFaoup3LG64JSoyr3CWYeVygVGq6G3VbS0L8FFVFe5jeM5y8qavN2RI9vGVlrPvbVNeP44ElHFgVpKjf1SNWL6YF88Gq+wLD6CCiG7tj9nlBGlZqAdqNuNvtOEGzqDuzQtB+eK7jOsuwn7xcL397GdL2DYZRdlO+I83WzX6jEGYF9npDE7MTQ5S3kSVWCYqkfyAO92ZXzi6HmGtodeKBd6q53SvVvRfR+lC12svMHpLyxu9qEF0ngTI5xYrk8ebGn1wjvnlJVX9IXCyrxOt5RW1UapsEdH73OZD1idSXzn4l+ki2Ejp+WsRXU1gp0tns3r3YwK9/KlTGUEl9eJ5Eq9wWkUvluaKzsnx1U4ytEsuC1n7qV3Lx6hIeJiI835yssVlLnuhMwwe7mUajxhqgu/xAqCC1Iuj0xcrrR+JzVLeb+VRfRkN1Q/d3tCq1qvqwVk5veWWIkYvcF5EL84La9IzeTFU92mp70vwu6R9nS/9LaacWFEnUitflVZN4/KNQxPjvxKltw9WtzsuD/DI2+52zWB5hK94TeX1InIc2R3oKHs3KAqY3GNu3PRUkGuWofsUKylADno/jbb1n1fJuSOVEBBc6Sddbg2WnxLi+0qim7EanttJAFsxubEDq90G2va5TGJj3VankpRu1KDYyYNwgn25Ybe8sOuqgm55fDa92vDZ0/8LpeWbp9qfb61TL91uYrQzb4n1bJdjoVbkFlp9i4zgmEibtTMQWf4CW/t4WpwSKah9SK/XR2uPpLrEtmjpbwVDx0YPua+M8IqaVimoO8MbLzBeglmC+kmtpKxNGjWtx0wdVz1m3FgkFvdLuVTWsirFlsGh8zqsuQmpOwmmq3ClR+souN2LXAwz+PGSB1QOcnL9SxSaJfHbnVP7TtLxWRTWR65c7TO8IChL9za1yxUN46Gv16z/LWOMVLC4ZpeHFI8cNj1bXGrWpxcJXvecuhjfs0QCj8ptVx5FxyZdTZzEhNfFoO2uMpyuh/ParQwzKttHvu+zy8lu9ksNz0YXW5NXLBjvSSdeim1B76T1fkVjAtajh5zmVvd+H5n9NxxRzr7Ljkw7K3iTtdjeRHPQzay84DWFklhJAyVVzy/zKhdRNcMdjnZIp1Jh6UaSYR7zY3bVjrnLke5js36sU2pUu3t83zbRLcrupDd6ORtWQ9b2zu1zpPDss6RYn6gyZ0uum45bgVsfUKWM3MtUhLmWXsSPV737qbJtX6+FSg8NtWsLe2kCiKmGcy0PXMCZ3WCucaaeLHdyAZ7NBawVnrnC4kdMHk7ZPKCtYYOTG5n3VtZVlifknXU8YVR6bNiP2jlRnH3RaPvzLK/UI3AyaagzTzVTOoa1waa2dmlTJ6WTHdLlS4qDnJo1s5ePLEY1it2fFZQwVbra7FB+1GvxmFXU2Z0cm0U6eKDKJ0EfH4JEseH3bo6mnBC7IgdWhMF263qVXULuFWiNTue07bI2OVEuRocCztWIpgL0wGBbWqM9GY1XC9znJ6p11zdyHi5vzIWo9hor+42idPPBsI9nWTnyDaZhhB6vzByb80uLsfUdpaXhKNjZ3rdoTWri8HZ1QGvZH0sdrWD1OYKvt7abTzsEDvxM75bREeLVlmLOuS3fG8KrUvHKRfK+4FXy55s5SOIzKboYEIAyjtn2t70I+JTnSf44/bgM5TEVe1RY4/7WG+Ol2oUok21xRfZpqUdQuGDlRXM58W4EPs1zFNkRh9jA+zu6z43tkKkwtk4liVtO3i3RAYaQY/YvGSaTVc6bGwgFAkXi0gJ8NQyHEQ9haXQntRebjDkAqdniVNN7qZqvtK65dG22IgaWU9aRv060GO2u9knXsN22VJKt4hoOIRUmBaco9HSuHlItLsofBYSfGQUKt7BTc/l9vYgXo4mYXVXtqd8NbqS67VALJaxXNF8rDiXVarsJI7eVVmA+KlL+vvhOq7mLswXV4I5mCuCSi+XmpTVNWvYdaEq2EUshnO+0PZnZ4Efr23ldwuqHeq+xnfwkrDIg3dmSLPAQJ4VAdFtGjzf9/slRvuzKliu6W6ZzPgdGL3R3hMDjOf82/G0QJcHmrnR7V4wlK70j2hbqDY/3+BbWrr4GDoiCI9sFNOmDfcIhurZSp2Tm2o/1/v4UrbwiUmChl06cnlbY6d+tgzsZWv6ac8K/QL2aartBRjutK689MKswI0yWm4YJGjEDexL1/ZmgALurMZgaK8dsWgkBQSrTAm+6tPdfE0piijBoh+G85VyWTuLzHPhWRkS1OmEMXRdYGRoUkIlifO9cMsIbuazFn80ZuL1ctIEx3BPbIJirq3PoqjJzyziMASislS/yXgdDIXU0TsEx7E7O+I5V242r+JXUZDFFt/NSExk3YssymPpKPKwqEUz2qvjZeyOKD1kBWJHR2/Yp+NSpDZIPZwDc73uFctsh42eLOFg1D3/lq9V1QX4e9tQvDbtZXa4ojZZUMdbJa13PLXWFUxlWmKz3KpSS6byiLgqf0bPdYnjIhJSgyvpMHqGO1Cdr5Tg0pzgLHbiji9MwuUPTEvOXHxc6VYbdCg7txIzX7S2vh8Z18TnuRheNmTgbTemPCv92xz3FAt2yUPbrNANW9C1McfOi2vOmgOR3DbkuN2XWRAVpZowazqr5ztek1a8EJ9Jr3BzGTm0sDCQnjYqq4i/ZW3gBeqy14XwsOhofGx6PRfC8pyJ1/2cmM0XZLlh2xINV4o7lOo4R5kZwQSLJd+ELetrnJFdRazD1i6fxchBSKqe8xdYS7mWsmbj+bE3duMMtg479IRuNXicJ7MoLcGQNyNAL3O3DI5i/cK9ClcBG83yQub+OkHAlMekpsRHprbxhDpDQoIZ9iJssj7t16mdh363YjyO3+zryNLhXcOeF4hyXhoIIXl6Puc529Sdazjg/i0c0VzxlcPmmPSuCDyTdwZ+oMgWNwJSQhg8po1a7bPl9dbUHOIZ+1IMlov5ds6uF4jezvhSCSPcSlXW1pS5x+yyNGjTvXJGDp5m+8xxnKVMTIW6W3rujZW5Du/U2FKuon9lNs1mbvo23Jp60V2XKEi37RL25+EsO8yJOEDbxJQVO3FAvslXK4iNygpuTIfPOWJPYXzbFjZjXhETp8/bG72b3ciuwa4VdsOkah7RfayuWJK4bOnKlULGPxOy2lpzSzTQEcVLI1zPRqW/yex8k24VA52HisKAIQ6rjR7G+dK67tNub7vEHE2uSB2JoHwPfZMYoqmweOlh19VCXkS+YEWif8S8zgti3k53jO4cBnRxnTGZiI3IDjaiy6I8ZJJ4CbVqVug5q8TEXEnytu7LMOVP1j5iDXer33yHvUqEh20vxZDilXtc7s/Swc5SYiVne/KMlDsdbypnadP5khiGs8BgjB2Fc9hr95F0TfSo6BI0HLe6Q/oL5Mrk685zvXUdDgH4WZXDisgqLyuPjdsEt41hwtp2rcPk1pS6mZ8rDeeF56Lnd5zLcwgVIBshdXR3xQrYLC41eHXis81JC3ahXWOSF/oqM5orr6lrn7Z5sZ4patizi5pIODYpWZb9+een56f7KfLTZxShSeL5aTpReDsX+I/eJ0djUr2+scRpCn9++n/3cvPxovH9DPF+TBA4/ue79M//gba/Pj/VXgI0e7yKbrIuenux+XcvdD/9y2+bJzbD43x8Ovy8te9nLa0T3d+KJ6AbgilneG3KrLu/EwceeFfv7Yji6W5mXt3PO94lg2vHz5MiAdzr17Z8fZwZBE/T/2qZTvUCP/n2NXo7TgAMBuDOxGtecYp8DepqsvrtYGt6/TudbD39/n8BQXMgHzAoAAA= -->
