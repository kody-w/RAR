---
name: "rar-cowork-cookbook-ppt-exec-monitor-budget-to-actuals"
description: "Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_budget_to_actuals", "rar_sha256": "28731c646cf6942a17ba386f6c1dcbfb24a3a949331dfd9ce957e35098a2da05", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_monitor_budget_to_actuals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-monitor-budget-to-actuals:d4e86462cc6f305245562164502adfcfd136851032132203103acf610b415e0f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_monitor_budget_to_actuals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_monitor_budget_to_actuals_agent.py` is
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

Monitor budget to actuals Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 28731c646cf6942a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_budget_to_actuals_agent.py` first:

```bash
python3 ppt_exec_monitor_budget_to_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_budget_to_actuals_agent.py   # or on stdin
python3 ppt_exec_monitor_budget_to_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor budget to actuals Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_budget_to_actuals',
    "version": '2.0.0',
    "display_name": 'Monitor budget to actuals Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-budget-to-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0036591e7b1cfe2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-budget-to-actuals'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-monitor-budget-to-actuals', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecMonitorBudgetToActuals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorBudgetToActuals'
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
    print(PptExecMonitorBudgetToActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V66ZKjSJbuq3BjfmRVExnsIEVbmw1CEmgDIYGQVFkWyeIsYl8F1NS7X0dSRGZOV013XbtmQ1pksLif/XznuHv89mTWlZ8WT69Pe2AmiGhGUeCDAjETBxHSa1qE8FcaWvAHsdOkKgKrrtKifHp+ckBpF0FWBWkCp4sgAYVZgRJORUAL7LoKGvC5AKbTIdv0CoptGiQV4gA7RNIEidMkgIQQq3Y8UCFViph2VZtRiZSVWdXlM2QXZxGoAHINKh+xfbOoyptclRmFQeJ9zm4EkxQyfYHygNYcJpRPr7/8+vwUwPun19+e7Mgs4aunbVbNoFSbO9vJjauW8neecHZkJh4clnXQHAl8zkDhpkUMXznARR5PP5Ugcp+Rv/0tvJqFV/78+iVBHteXp+Hfrk6QygdQHbOsgIPYZmZaQRRU3QvCR1ezK5ECVHWRQE2gogVU4+U+8xulNEP+MXz76c7kBQr605enNBvMC2395elnBNrty1NRD/cvA5Xsp59fosHGP/38jU5ZWxdgVwMxKPXL2+P5QRYO/DY0cG9c/wGp3r1qgS9P3yk3XHe5Bz3hzKeXCzT+T3fCWZE2IDETG/z085+RtX3o9ygoq3+L7i93wj4MHqjTQ/Cfn29G/hVBHwp90Pxzthl061/RBA5/Z/eMPAz1Z7Rv9v9vpKMggRnwbvE/JPdHE9B/IL/8qW7/04RnxP3yNAURTLXCtCLwivz2tt/OhF8+Od9efvr1d0j6X5LZp3Vh3yi8xWYSuKCs3t5++VTeXn/69ZdPdQZjDZjxW11Ef0Tzj+x64/ODBR+jfvpxLuSvJ2GSXhPkI9KR39Ls/xS/vyAHMwqcb+/LV+T7fBkuFBmUeGd6N8F3OVNCWb+z489Pv0OASKA2tX37DLP8P/4D2QR2kZapWyF7O60rBDq4CmIwCK/5QYloj6T+ul8t1uuX2PmKwLdDukOIMOuoQsTCDCIE5sPg8UGD1EW+/qd9w9HP9gNHsSyr3gaEfHtg4NsdA9+q9O2BgV9fEM2HjNMi8ILEjJAdv90ipgcg3kGWt+Ao6/hzM3CFEgV31NkJiwFxyjoCf0e+/ms2bzeKL1k3KPIlgZ4xobsgwII4SwuzCKIOMQeksroKfIb4CtGkSKPIMiGGD//V2ctgHcMHycNm9gf6AyRKbSi6G0BMfoZuL9Oogcg4WLIMgyhCnKCAZkqL7obq0NqvA7GvX79aZul/Se5QTCH3KlNicMCHwMjnz1kB3Cjw/OpLAmw/RT799vsn5L+Q/2nWjfjAYwtrws1iMJwjZLlXZATmZh3DYSUyBAYEnpvvfvv97opBOljfEJhRgRuA22RI7VsgDBrc/fPuHKjzICIoHpx+tBty9aFdkKCC1oJZXj5/SQYSKRxaXIMSvBvxPvlu+ndv3/kMPikfNoR+cos0vo29xeDgTDstnBdk4SIfloLqQr8OVRTx03KoxRlIHJDYHZxpVt9cCGsqUsLMKd3uGalLqOpA+asFSQ/GiSE8mdVXZCNsYaVLo6F6F4/KB2fDcBsc/wjX+2tIpPgEY2zyTuIFkQG0JpKZhZn5hVmC2zjXvEcErHDv84fWAEnAFRlKOhh8dMvpW+Rt/rSLmL23IN83H9Oh+fhSkzhBI//LDcsgPS+Ku5nIa7MpMpO13ekeakObNWh+78xg64DA1uOeN9/aiXfkecfkL0kUQPcU3d/vI91bdN3H3HGuLmDo7Pjdjf6Q58WNblDBGBmcXhRDXJtfknfwf4Zmhx4qBxyDqRwOwJB+MBy+vkvqw3wdnr81Asg9/AbtYWAjWW1FgY24ADi3HKj8wczvnoABA4Zsgylh+z9ohUDqMBgg/cEDATQnLBA308kwU6BJ72H/MTwY2isohVPbUFqYSuAFMYbIhtFZIhaAPdIwBlrh040UEgNoYyjih4VL38zuwgyt70NAc/BFGsNg+d4Dj4/eI46cbykIqZqOWUFbXqETYIa1d89+yPnwFRQ2HtLhNulHdz90Rb6vUn8f0hDK+K0OwG59KPDfGQdidxHfow6W3rCEiR6DRwDBSLjV8pd7Ob7X+w9ZXv+p3//pry0JbgVW/9Fzr4hfVVn5imH3IvheA19grmAwRoIMlEM9/Dwk4OdHin2+p9jnKv38SLEfKN8N9Yr8Nel+IPEI61eEeMFf8OHTOrDBELePCxpD+Dw5faaHr1+SHfjm5UcoDBAHYdfqPirN+xBYbrwCeMPge+Uph4J1hTXyBni3yvERCY88gWCReEOZLNPv8nfQafDr3W0fwAw/JQPkO0OD54Fh7RMN4pfg6TWpo+j5KTFj8G+seQbshbEKjTGslGDewH6pCsDt6aN3Gh5+XOrdMgpCgZO+DokF6xzsc5+Rj5b1GXlfRNyWZUkNV1G/DO3ywBIOhb8+xn6sIy3wBFdtVZcNgt9XRkOX9uie/1mIIZ+gxDYYKnn6kaADx38iAm88DxT/TES53ZjRAyUgkA+QDYvyI7dLKKcDu6lnBLoO5hxMI4iO0Hp/wAbyKUBew3rsDOp+s983tdK7Lr/fzFDdl5e/Pb2jxXB/bw7uYTOsRv/9Fm4w6nvpfRtImwOBW6N1s/GtQX2D+gVDif3ukzf0C2/3OHx6hWADnp8GSxYB7Lr723L66S4PVORbawspQNj4XA4tAwbTCFKChTwblIC1zvmOwfA6cG7jh5vXP+qH/0X+vzo0GLE0S9o261I4Q9IMw5IESzM4aTqu7ToExY4YAqdIgiJJnIJ3pu2yBG7RBANwF4ox+DI2H2JgxOAFqMCHqf8fuvSnOwVYMkiGhSTIEUcRNhQTch7TpElwlkmNWJe1Cce2XIukTcoc02OKIhzXGdtgzHCAYvDxyCQdE2cGeo8u8S7W23tH/u6XOxC8QfCMg0Fo0jTtkc0RtDPmTNYGFG5RNiBIwuEogDNjyh2NAA3nf0x9+GZw3V3zIW5hgwjbs2bg89vD10MssjQcKdHlgr9fAjY+mJaBWTt/jRYR2rZY6dWMni4pR7btItI3Tmt7oilLk+7Q7uurwC0jSyVaw6C7PshPJo+lBXpt0D0gd2Cf+mrCgfnVVPhwkzikE7FufAjzIF/vBOKwSsnckJtoJYonnWaiDKykM3qsd7JuojO0O9S+Ray6w/rKsAtuUYzRZtNwyzDd2aSML7qjxmt7c0/QTU00nRhPV1USe6iTXnHysuxaLWZTdVfAltQ5lQa2NWdbxRYPjN0dF0Sx76d6LalgqrKua5V005/Zc9Mv0X7EnOs1R67Jc0Dx2VQVoAStSRzWJXlYS2Jh6IWyOfTdYaJRU+tqzTRTlycyuxGyxGhkGnUWu7Vx8nk+XYh2dQrOLUjmzGkcjad2menxuRzJogyI5UzZyEWn71lJ9iWJ1KqdqTZz4XxwT9PTcWpbqsnM274xLTcn8vGs05vNaJ6HZsguR4QEZDb07f6kp96IsYTQOCvzQnVWBzWPo7pl19aWuFzoTaKU1WhvrfeMvzue7Supl3NYsA/G+Jzj7XyKE4WHrfvlQnFMQljGFMsyp+NBg73QSo1wbeqoroGfywU5tVxZNQ/5mGH2u12llorWnI8ivZMoNMfLZumHfenvxfxK9yHlSqqcM4ABymhE2kWSqBtf7oWxPaprwJEiqVD2xNoWfrcpRALdRSZFBfQqscU2mRnnWXOc+Yfy0u0LhSA9z11jwsiss81VzDeNdYIySTE3a88HG9XrsGijlhzPy0A4975wTViDZoSZNOfWc9HMxtqcxuLmeKAUUs6t/WgclmVb9k03Fg/lVZ1Ziz2IzodzmGdyc1zKEvyZHnI2U7J+fDmbGwaNyXY8vbAzBm2BO1m5J+VQxGq40t2R5F8Ca9swNRrZ5SVgZgzRNK4eiRS3xDtqZ3SjIjX2kyUqZoeg1XfL8Xmu5CwZiGpJE0KHsReiGY0kfrZiZiW/LI5Ztq9zVWFIilb0Pbrh8SjMpykle3pBCvNO5qm9v1TTRSwcm5kFg2K32vfyflHEhZIykU5UYL1JpRkOi2hEwVXnpRh3SRaKBMNzs2Qp0RW5UyQ73AVHIBnb7dWv97V8TXTaSmpnd7hazlJRlpQnSev9xbNQcov2GG9n0qLd8+txFXgb9Eq4JuhQid+cxFKbypWYm7PLcnTayzh+mgbcQfHm9BnLnQRdB9llS4WUrrhHtdudrxMiL6winFjMmlosN/TRPXDC+cwwDb0zzixQmynHLHZzUp4TbDzdqgUM2mU+ZsGhNqnNpFZX2nxvbCjfXcf6wsOK6nixunmR7pZas187c3Y0X/FbbjVdG7MkdFxd6xU9ZyImW4SjfIedc8y0fbGXqGu1P66W2JTHFlNRXUmHg8pdHKV2NNacy/JqL5+502Td+3SGWYejZl18JdSV89LxNOPoA+UsF+vF6rjsTNEJEjwlhU4c7Tv8yMdkDIPPqn1Rs0pqt2RWRptucbHGNF9Tz7sNPenyUx1seUVTiEZoIFFZLE0ZkzzX8sYp6qJ1tHAbgZdSzmZRcbHcQ8dzRq/h04hHq6WwccYWqqatxDe1MbJzIXZacsKc1ENDtudZJ4dngF2dazcjY005kJzPjNxWtqZ1pK+IandG87K6KLPjnJ/RR3WCF7pIakuN9Q6p21pydaWFhbCfL4UFHunr82qeV8zRHu9FP9SnU7xYBMF8ISsX+WCZiW8b52TqN7x/FOqeL9eHVX+YA9oajzsIqpu4MjiNX6GHluXO5ImxzmTs436SKU3Dok7CdGM3mcajPLNjmNWYFB29ExaxB7PYSrQ+OYXOqlcnGJYv5l7VUxLnLWa7k0crqlhigATodDWOOmru7kapG231NKcc1OFOIc+j1xOrd8tpvNKX+mxWrJjDMtYMkaSxEM0mJzvTTrMjv8pyXgCUNLpu3SgAzWidVh7uZ50V8qdx5et7/VB0/EbWumkZidLppFGCS8zS89a0OnohyHjpXlB2Ke3CY7iQjU3E9Scs2MfqrPVyoM2ryZoI4wWcX3C2SNfHWTTRBMMX05Yrp1IdlSRZNokWmToZ76saFi18OTYSj9/S5tKXj6M4WCiHuvXDUXY5XwxiehKX52VhMw4sejKDjnpdu1wmfOVSaQeNHFcVEMWJbC30c7dZG4sQG+NKfSavCuEvwmZZjbQZEKhpG2mrntF2rWsD+ohPGhWLL6gqyGE3P7K6crmgUopWE73MQUfEprnYTZwSW5Ez1zBwURaSU5ZEvXmixhMpSlXVKFtnZWtb2ZytYp+hJmV+ylZXfnElLyVsM1L0EPZEMon7pQUo+lqFSyKP95NjsyfM4yojhR5X+i2peBtyt9tg9TaajKi8Ei65sKCi1lOcsOtZoq0oL1Yz5bJz1uCE+77bN45pTZan7Qj42UZFu64yMbmwiHKLHYRZHpmidzpW6wU7MxOt3pHyLubZiiqra5OSjQOUzTr2gWhsWWeWbXfhsp07EcmXm5A+8lAOnTfcLdtmfaAcQ0meV/Ha9qJTGe3b1dKboftFR66Wu25mX8aZ6pJ0yurYbrLQJrsMFpUxVpq4eOFgW9Pvuqux0UM+rDnW0q7ONNNWuZUHWVoJ9tZ1my3eu6hf8sF+zOl8fVUumzPqh7srt+jFcMzhMcm2Y7MsIgNNiH5btLa2PEiNxaWUNFU27cnTKnLT1Kt0tlPCzWwzgS2FZJlEuKCl6uSu5/a5ymdem2/Dsdn0GyaftEUrWq3jrdK+ilYsyRy3PDjRuj81NvnMd2JYwqiI7PUt5u6MsYYXRbwnJLURGTuvwgBt99VEhWA4p3qnXTpiJAns6ZIl/JxYu2B5tnw84/0On4C825NTvBcm+Epf4YF4HGcyfWFavNYJbVuGJcVbHcOs90mfTA1psR+ds4K8htORWpqHyNXziZ+s5rRwZOJGWs/ne5+vl+4xOq9EDd2I0zWb1MFpKe6J1ZaTzqvLrLGik3ae0+55f4opo1zjq16LZ8SSMlMqkw3joHpotwTkeV8YKUVEipEzasK0MhDq1ln3TZgV16Zd+uu1CBEhdPhG6RwDn1zH0aTFWSU/TiLPcUb0NV9Z1QLa6LzYnmrqUpTO9Ejq5FIZHUKNvOxwDACpudBTTxaUgOWUNphtMiGwN4ueESZdEjALNvNyfmUEmyg3yVBW/So6bkh7lnuXEuPUtljuyTOet+61UJIle/YuU//oGEteLsgqW/EwO9iFzPKJqgQljxueZlqNoPKhlNvQb+NqmUaXxWW6knwpBzoZWVaNiwWFWkIKAlk0E+bAeNEql6ebdqxserK1LbDPZ+7G4nVtA/pCDvGJBlDjSE2Kq3oxtm5GKmbQ7C7+uq6EeVOo3mEjx35pYfN9rQcpXofipR1aeIu4whwYLWiMGUuxMPFOY+y4aCxc6fqKgIUsEzbCdlQDcx44UQGwZG81GqFZveSsmoz3NobjxQ5ztadUNfLmcTYnqJVghY6zJgVJx/JDMpHYycSxMiky867aTXyhm6aKcD2J2YIfHdllMG8Nu+BLfUNavsrouVY1zbmd5HSdw6CViE1ZrrdLh3dUrFcmWbCf7dlwXivr4rTZJvhpefbPO3R+vsYz/0JgXTgPC2HTwcVIxKK51zsYdrFSG5Ai1V20CG+AvDvoxChIOw+2NP0hKTSijw6dmo6uET9eHeNr03m0wczpCee77uhM7S+67eZlSCmtzlHrFZEIgOtoxSobRqbqY03HK9pGncBaC23VW/aZmauLCYSFhBBrnI7Cjpaj46GR5TjxVspuNTo7zLjFw2lL4sSOk6XE4YNTsIicPqj5ZWW5dHU95oJaXi1VPkYbKq6ucy7fCjVvCSp5lUbJxaf4hkYzlhY5SWIb7ehfZyI1IftyPZY7QEqGkVzSXuYUsqM9keFdybY5FTCB1TunCw5QEcOIiMFaDzPz64yrXIyYYtvdnkwaZzz2jwQT6I6AEvnRGPPV2Ren+WorEHGkB0a0I8zFxTFJHT2JxTLFlwCj8cO05IVE0pJ4Ywfb63Z1oiYVXFlJTNmnLFWFcURyibvB5rycx+uKys3t5DphG8OrnWsub9f7Ma319aIRwNnYL/1oLNk6vWssgRgpnpS1Ildg2ATbjeQ2mk/PZ2LO2YtmWlVVjapbrmNmitFGK1lr1N2kOU+JxJaUyWWPGwtUnoDd9ljMDB+rDJpTIlK/YIWL2kYxa1Zri+3k0yTvF1JmjeRLCsiS241H7YxcH4tK3YppyPFkmcXnuio49DhvoplzPAoTpnfzHGxSBzu0GdUpp26xGk0VCrSw81fc0vZDiOqKXCy36cE8JOXOH5+2dbERDAGuiMwOwlFbd2IdJNsDzoyOV7e+Shdrv+sZfS2M17kgU6DMpjOqFLtxEqhoVl5Re3ItjE2SzanTORmDC8fUWog1OH2pcCn3lKyaEbV7XZHMaT6fMJdM8PGQLNTtMvJGoThrpxO9cHvUVxPdGgcKwC4LtgcX9GoxooPKRU+Bo7WZ15sYS4qlE1wuS3O9zSakxXgkqMas1/uVU0no1gYBRlwlQJmMeE4o7uLWk2kgrXFrtvXWLgsrLH0lHEVI5N6cXuwmLaRqbqGjgskpqS7KiTCx5conCI8SuVSzC44ubNjucNW4JtLU8KmAPPjmdp3ok2Z+RWdAFTx2sUIrnW8KrZZnqgidKW732Vlan7cXejyXZjFc52ywzDpZTTrGlzLtQay1KM/LVxxJWa4TYhbnElTbO/UeHXUkmKLSdDvmbGV5wtLo1I7nxqYpKRObGttGi/2Ucng5oagtXbOtVBXtuXIb/IgxzamlO2Vk1RuqzsDY2yzpgLv6Gjdv0spZBfU16amRR4vzIwfBnTRROu850sFKBTddeuyv0HVCkeSh5duM1q0Lrhxj053Lzji3IJcd6XMj3b0cDcHPGxxNZWdaUzTP49ZxVqrzRqfSSjX9WC0I+bI/pg5HlgxQQKvF5UHdiJml4kfCRS8tMZVK2pU69XgoYa23GluxeWPNH66FvbZOM8adBMQqG6UVSeSTmtqoZyakZ3KkMBd8sbK3ToBLjhVDSpGocbnV8xyNjoHFL915suttgt3GKtl2rJYBbrO16ZheGw09NqhYSLsZHUV2lOqlVYJWPBzRHMLGOG7tjmO4AlUnPVof+fGVd2xLSzle93fZqlbVy4nVquloYmcruwxHOtsfuQ1dN7XIXDyFda5gNPIiopHSLVeveseYrVSef3p+up3wPr0SOEuOnp+GE4HHvv5f2xb2+iB7e9CiOAqS+v+3Y3nfPXw/9btt8wPTeb1xf/0rYv76/FTYARTpvpVcRrX32Kb8b/uyn//1bvEwv7sfUw8HlG31fixSmd5tOztInLqsiu6tTKP6tpkNjV2Xw5+qlG+PQ4Wnm2JxNpxQvCsybNDe9skHFe5n6U/DH5IMZ27ACcwKPB69x9b/85PTQZ8FdvlGscwbKLJB0cfp02D/4fjp6ff/CwDoUIKGJwAA -->
