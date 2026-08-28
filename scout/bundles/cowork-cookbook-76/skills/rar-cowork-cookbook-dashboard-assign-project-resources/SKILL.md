---
name: "rar-cowork-cookbook-dashboard-assign-project-resources"
description: "Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_project_resources", "rar_sha256": "59d93ab9d9048da7c79f3125a9319d3596e3b34db9e4bc207e001dfe94414cb6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_assign_project_resources`. The original RAPP
agent is preserved byte-for-byte in `dashboard_assign_project_resources_agent.py` and in the RCI capsule.

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

Assign project resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 59d93ab9d9048da7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_project_resources_agent.py` first:

```bash
python3 dashboard_assign_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_project_resources_agent.py   # or on stdin
python3 dashboard_assign_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign project resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_project_resources',
    "version": '2.0.1',
    "display_name": 'Assign project resources Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-assign-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a42b638f485b14e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/assign-project-resources'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-assign-project-resources', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAssignProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignProjectResources'
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
    print(DashboardAssignProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZOjVpbvv8LL+VDlpirFjqiOjhiEEEISEmIRApejzL6IfRXy+H9/F0mZZbfb0+MX78OoojIFnHv28zvnXvKXF7tro6J++fKi+nYOCXaaxpFfQ3buQVwxFPUF/CouDvgPuUXe1rHTtUXdvHx68fzGreOyjYscLJfrwutcv4FsqPHT4PNEbMe570Fx3vq17bZx70NrTdpBnt1ETmHXHhQUQFLTxGEOlXWR+G4L1X5TdPXE6DNUlH7egPVAmxFy6mJo/PoTlBfQEqdIyHYBVQPlvu8BKc4ItZEP9bE/+PUrUM+/2lmZ+s3Llx9/+vQSg+8vX355cVMgD6i7fNOBvYuXH9KVN+FgfWrnISAsR+CfHFyXfg3UzcAtzw+g59XHydZP0N/+dhnsOmx++PI1h56fry/TP6XL73q1hd20QE3XLm0nTuN2fIXYdLDHBljcdnV+dxxwbx6+PlZ+51SU0D+mZx8fQl5Dv/349QU4p7Yn5399+QECfvz6UnfT99eJS/nxh9e0AJ74+MN3Pk3n3F38j3uEXr89r59sAeF30ji4S/0H4PoIs+N/ffmNcdPnofdkJ1j58poUcf7xwRjEsvdzO3f9jz/8GVs38t1LGjft/4jvjw/GkW97wKan4j98ujv5Jwh+GvTO88/FliCsf8USQP4m7hP0dNSf8b77/59Yp6AEmneP/0t2/2oB/A/oxz+17b9b8AkKvr4s/RQUW207qf8F+uWbKvPcjx+87zc//PQrYP1v2aj3Wpg4fMvsPA78pv327ccPjxL58NOPH7oS5JpvZ9+6Ov1XPP+VX+9yfufBJ9XH368F8vX8khdDDr1nOvRLUf6f+tdX6GSnsff9fvMF+m29TB8Ymox4E/pwwW9qpgG6/saPP7z8CiAiB9Z07v0xqPL/+A9Iit26aIqghVS36AA2dXkbZ/6kvBbFAJmae23XPvBrEwPHPumeWDZpXATQz//p3oEUQOIDSGfvAPjtAX7fngu+vYPfz6+QBjgXdRzGuZ1CCivLX3M79PN2kloCQr/u77DX+p8BEn2evkxQ+fO/Z/7tzue1HH++w3z8QCiFEyd0arrUf50sNCI/f9rjgs7gX323AyLSwgX6BDFA1k93sE4BrLeTN5pLnKaQF9dAWFGPd97AY18mZj///LMD9PqaP+AUhx6to5kBgnd1oM+fgWFBGodR+zX33aiAPvzy6wfov6D/btWd+SRDBvY+4wE03KiHPQTqq8sA2dREAPza3j0ev/z6dC9gk4NeB6IXB7H/WAzy8+J7b75W1+xnjKQgxwc+Bv7NyqJuAUZDcfsKiQH0ri8QOj2aUDwqmhbyfNC7PD93p7ZkA3PePZkXLdSAJGyC8RPUNf5d6s9Obd9VzECh2+3PkMTJoGcUKfgxqXknAouLPAbuf8+Ex33ApP7QQIs3Fq/QfspIqLRru4xq+ykjsB9xmXruczlgboMGOnzNp/7oT666l8fDPYAIeMZ9hvTzFHMwA2QAC7zmTfadxp46m3bvcPXXvHmmvl1PoXBBKwBCwy72pobw92dKNVHRpd7df0DTe+d+RMF7RuWeg+yfzQbiP88U7/0c+tphCEpA/7vmkbsxgqDwAqvxS4jfa4r5cPKk1xSMxxwG5oK7EveC+j4rvCHNG+B+zdMYZEw9/v1BeQ/Nk+YBYl0NdFBYBXqzu77zvaftlIZ1PSW8/TV/Q/ZPwFF3GAORAzUOamBKvTeB09M3TSPgrun6e5e/hxm4DyQGSE2o7JwUpE0AHOHY7gVoVU+l9wwMyGF/KsMhit3od1ZBgDtIFcAfAkrEoJgA+t9dty+AmaDqgrrIvpPH0+xUPuLsQWBq9V8hA1TPlEENKFkwAE00wAsf7qygzAc+Biq+e7iJ7PKhzDToPhW0p1gUGUjq30bg+fB7vt91mdQHXG3PboEvhwmBPf/6iOy7ns9YAWWzqULvi34f7qet0G9b0N+/5ncd30EfFH46de/fOAcCmZw1d6SdcKsB2JP5zwQCmXBP3NdHr30083ddvvxhuv/41zYA9+6p/z5yX6Cobcvmy2z26HhvDe8VoMYM5Ehc+s335vf5UWmfn5X2+b3Sfsf54agv0F/T7ncsnmn9BUJfkVdkerSLXX/K2+cHOIP7vDA/E9PTr7nif4/yMxUm1E3HqajfWtAbCehDYe2HE/GjJTVTJxtA87xjMIjD1/w9E551AiA+D6f+2RS/qd97LwZxfXjhvVWAR3kLZHvT9Bb609YmndRv/JcveZemn15yO/P/R1uaqSGAbAXumLZCwO9gHGpj/371PhpNF7/f2t1rCoCBV3yZSusTNI2xn6D3ifQT9LZHuO+78g5skn6cpuFJJCAFv95p3/eNjv8CtmXtWE6qPzY+0xD2HI7/qMRUUUDjO8RObetZopPEPzABX8LQr//I5HD/YqdPnGhae2rZcftW3Q3Q0wMD0CcIBA9UHSgkgI8dWPBHMUBO7Vcd6I3eZO53/303q3jY8uvdDe1j9/jLyxtePGPwnBQBOSjMz83UHWcgUYFAcP1IKfDs/2GGfHIAGAcmGMCCZDwGtx3wEyHmnk27NBPgKEbaDI4yHk4ylI87OOE5jE84LobQPoKgXuAzBIESrkMBfg/O36YhIJ608pHAxxkUcz2cwkiSYFAasxnPJmjb9pD5nEbowANt4PvSCwDIp6kP0yY/vo+zk0ueFv/y4lAEoFwTjcg+PtyMOdkURjtK5MA15ZvWeSY6sV6p3r4r7OHsKUi+9LhLaMlekbMrumRd9bTX1qK1NFreXvTFMXBFeDyT+a6+brxW7FZtKGjx5nYrB5KZHbzCFENhg1a7k0tukRptkLA6hVVLJaKS1bi4Rddjudmdwxynme6E01x+ptDkKmXGbBaItY9iVcuZ1K3WxLTd86RinDs9ttYCKWUEujtpGxglVloZVooNX3N5D1+7leLs3GIzXk803Gfn843zQ766ncVQL+dH+lQhq4604u28HPbLkpn1t3gm5yU2O+S0fDthRBMcZ6Yxjupp5HqBAiqoad4mbHIyssqYi7u1VO1zWEQJ1DQ6teHxArkJG5XBtfEW6ZnDXQgu1KqKilj2XF4DaYsidluLW8xstonUqpdsJQgkvSu95WnB29SqMoxt5ltqRQ0dutu7jlaRp9vyJB/pei21bknkbGhtV/xtPcdVnsQNdzSPrWkezA3qHzllbI749sRRtuHsOmN0qnw5yDmYPObCUT2uAtohk6W1Hc7MPDo5aVZr/EXW9EgzujF1YnTL06KLRpRXHTjXyLxCXXrHQECsRsSWjrc/mqeKIU31pJCWriSWzKAgY4qsRY30shHYmayPDa8eUUw+6Kc1hkaMNpxoCsmFWea64/KyqGzc6TIaxTIR9yxP2rWwlGzHuXKysHM4G/FQutKmYR4TJ1GtJUHc5mp9QLEwPO9m3Dw+bczE4XEyk5JxM3pbW66y0+YsBdRY3HyOhAcyKbkhh3liwwnr9LYVDL1klht6RsltdWut08lPSGdjm4mZO6vRqiRkz4/8rjCs/VknW00nPQ0ZAUgVY5v4TsPMc4P0F5wvEX4UzrgFmpBabHPHVmNCdQ0QcDY/rDHp6gkre43XPTfbUMt+e95gelMlyG2z54OdXl3NShRhKV4rJq0st4arJlbAaAQOn5YApEm1Czfr/X6jo9s1LuRoRAa38+okmWPWu2t1m6VqR0g6mxpzXdHIRUHEXrNplK2yLiwRF7kOJNY6VTQRISQsdLXDlbolLlfBh742/AxPjPYw7uqkiUkRq13pbDY5J2zG8WDOq9Usv5SetR7OsCrDRwHtDDatTTyQZqiPMpedfeE0MkiZI9wjpzOWN300Jlp7FBMUu5xOtnbrpI0w99GosOzLlRFXeSUkZBcXF6a0b+sbto4r/aLOU9HhDMFM9CIbmB3c81vsEDjVMsPUWMRCJ3ZEc0dedc6PzlU7KucSYRJP6+0Lje6o6iLtiqTUPDSJfb9YgPthulPG7WzT60aiM9FcOVoRTHI34tBv9U0uee7YGBftsN/I1RKjF9F2DOi84ytdFU4yw1EZh3LZjm936IFkdmCDljHWQkzai9BvFmVvkGbbZ3uesjSLR8eFZ7lWaeVnqWnKYGun+caKVIrUZIX1N22zD0GSS8GtxfR202F2aTIXO8RPKp1c5RKVc349rLdcMxKDSFPZiOu4L5frAxWdWxhflrKTMAPlwaDwZj7P5U0Zxrh63larsravTFAOcMMPMJmK/vxii+hA45e+FnIlR04mzc0lUcSPrKm4uSP0faYQCqfdiHSreeM8kHlsv082DDbTCMqtbrh1UxbDMS222y0np4ssHx3meFgOoSSgtLUN2XSrskqpEZLnyeuMIbuLma1XBTsswcRw5Yt9vbW3a50PbdzKxuFApGwSyBLGL+P81NvkgNNJ0keGie5W1wxxGKPOx73W191ZN6yx8i82daNRCqjLUC5CNKwj6Gm7QJm5T/AFvO1Rn8S66/WwWBilrEkI4c5sUh0wgkzgweDETu1nspDAUi/3aAHPumoHH1YJcdytnGNlh1mL9RUjqVsWHkxKHzfLTHBhpFiKZYp0FrrItxg+zsrMdG+euz6zakl2w8nlrsY+P620AhXnIUWz4aWI7bHsUVnHx/x0Rvt15W3W5Wl7Wqf7fC6kWmVnNS02h7VmHAfseNsfxIwKtOYWK66wYtQ5r8J0MctDmI7RqvVMbZvS+mqPRfbcqLs0VMJAHwJWlfYqfCkzMJ7fJIQO1zvdyhh6cU0WgrNT5rNAtU7e3JkHm+zGInCbbM4yv6nV/QrftodQPSxp50zQZuAPoG5PHXxdygsnlGprcdlEhmDkRN/aQtdpu7EJqg1mqqHgVsfNYS8n2uW0uBHLnlNk65DWlblhmysH5z5AJk9fHeMYlkwDJROdY/cKmTXXdkQOMtqBFE0HWlm36mmLhCQvBJmwMI42YXGMee2auaG1MCfAqzqVxeU2uWknI9drwYpu4o2JrcXteMmci3IT4RMG2j0VxlLpmsvE2hdk6C+wqzis6iFhr86NP/C7g5cUmnZpwp4kKeTK0dYBpZxM6lny5Kvx5jQShaL2h9GI+M3Qjgcllobc6pgyF6njnloI+rXj0pNBL1rK40tZ6TaMWFTb/qhJN/YojJi7ZYLDfLdcXQWeNngfE/zTfq7Xq4uuHhfhdlfEEluuxSMmZ9mWOa92Kg6LG+64Pa4dysHhaxWIOa2xpNDmYEI5Vsv05t8qYTkH3eu091YXjz9qV5oivB54h+iGhXpYydIMWyBm2GJIfFgWS1fQwDzl0PQSpcbuRFeOkwWr2BL0KjdwfJEJwlEJr2yZoFWNIOZKQcXj1lzaFiqhXi2qg0wMsFGFmoMcEk4PtIwJLpamtck53N5ge3dZ4Nr2dJRTZ4XMFbTmhFIv1BVmcUnin6swLLVaMWAfqfsUdGaQfzfnpMn7+aIJ2XBczdHZ1S4yU9lY164s5pyr4+6GcCKkFOMRpEIFCmnJUwpLNtyoJ+cNEq9Pm1ImEnREOhO7BdKloVln3DA7NWeypSGLqnts0cGJ2Msq32/sjhMXOpqy88V4zetE4MvLyLncZeOQhxW79YuMyCTlEqlJdcXU7HoLb+d5InYJtxpCjcYOknwFQ6KkpBvE1m8FY9gCu1vblwMqXcvKqwci38oS3CjnMKlpdU6TB0vNkWi2UxZ0sUfaPhn79apZ1AcLdk9SvBOGtSmcA2FPRxSZ2Al3yasMS5PWM+SLKakuWZtJ49/22by5eTy1ItKrEUkg0Q4bJXYlcRjjPajRhUGXnL3Aq0Q6iXpGW1bYssheaJbVoNrMbqB9UphbvE37oTA7RQi5O+/5wt46nLOL2vJ4Ko/ceFpqkcwLrZaIui2yMyykj6E/GBWY+5BusWzZytL31FHnGJXKyt1hXlAzq+UPCzURtX7PDOKSpbfykr/eDtIY4m7tys3FJUvsSGksjJINJQ7R5ZbTm3pQk6Kj1MZNeXdYc45Lk+u1GrGUZ/Dhiiv02X5bmViB9exusLS6wVdcRCfCOZc2LqOFCz1k/JOP9qWee91t06qcyTuEO8du20zpb9xp1zArdD8TfCfMCzfkjbbL3DJ0l3iLAEAsVygGc86Fb5dLNtnM0O2tZ4+Daxq2Qp2pS33pQzALIKsFPV+YF9G9EcIiqmpJCY2t4GxG0L5PG2yGNmZycnOP57qEznRYyJZ+fECcEWdtC2ChF4N7t1xF/F2BxBonxi4TdRkfJTHexjpSzyWsZtu0wdJbja27GFXOxHndh17r4XrrhiG3HByM1nPNgW+5dauiK4wtRqTfr7x4AdCzHFZ4Bs8IdrbdK7iHklbr32YmDuaGXj0zpMv1Ru8YNGjvXZS0dIpxABQxlNBIbXnUVb33um1ZonZZIkc7lmJC3sih4SbnsaT58x50AOOKWwe7ILIbmMliOxJRa4x9XmRXszl2PddcsL1gg9qPfi/Tcd33c8UEU9HOWfUXxvWJFu47F0uo4QpnMlPoywWD+M1OoDeXfn86RQlh87fDre0xgmuOZxJZyw6HS5Yvo7GsDJQ8mzn1bhYuBqkadLoNZtfjLLcV7Jy7BYxVO0NP8UvZs9T1XK1dOyrmS8VM60Wzgs1GNYaBPJPR7hJxR0ecbcp8r+jC4YCLUsgsglA1rrDmi8vwMFqzFXJe9Rl6s/NAYlaUbKLZqTsh/jKiQddVzHmkH9rzhR6TnMsW5T70CoM3jtbsOB5gyUgIN+WaFe36M8qbLQkn34WH2XjSuquKcDg20vSxBtl17ppENdRsqfDzWx5R135JL1KV9Xewt3CVtTUOURHQp+5wKz1yF1D4rF5V0W4MffiSGKzdjAtKmC1NYt3WBwQoq+yMmqb15TUWEVO4plItX9tAHs0WLtKGogeZdzxPvaZrlKG5LCCsmGX7m0SXxJqbmVaHDkKyR1mwz7j4MV4a3FXwsOuM9j1eWkasOUs2GLn0+O1mDA5n3tTaQSEQ3D7sxMjcLboxamlhtTaNKMYz0lKZMQW1Hsl7bkibVX2MxgPqpjJjSuvkSq1MI5zpC1gsjwKFK7nZsq6xFriMoxbicafT/Di44441o6JSerI99nWz580s6YfrgaerhbSdSfRx6cw9JDVozrnuLyRlq2Z5HIwYI4/7ijkw7ULOVG4OJwnXeyuTFoO6EmDQwCjYVXxCl3Syi4hjt23n9QKRk+UJbIDcZTZfC9Z5afQFge/BwHDN5JY+cjw3OE7S1kq3z4+Z5dDidIpszDo4NRHLjm4adt4iht4jm37FgmrmUDAge8yxWAR67QJUler1XHDTOXUQxmB9pdjDpslgsINS/SFelf5c3BOhEOEOSYXdhsZmRc90wb7tCLo49zgcBJizYAOmz2G0Wl9YB20klbFu65MxI5ue7G1+0bp7PBCs/Zhgm67bCOc1FYQzeISZMOL3MD7ft1bMMDixu4Jd7np/PCvh1tvGM7O7rXGayBY6ffKlRUVbIz1wfTUz88HOWGOhXnYVDB+y3B8Q5UJWM0aLkPyc2U6QHg70wdzPaIwq5oIsMdwqaIhCPEQ7BYy/+xUXJgvNmO+k9fHaAkjv2yvpwjnt3E4ERTeabNK8yS5smVrT27NF2lGJUMF6PJ49SZMbrZfWG9bQWG9ohFXZ8K5cjOF4CbaOvtyzEuGS/EWQWxXr9Yvs1oXWKjedVCipGUa/rX3L8df9ORfijrt1pMHNuEQP0Nh26k5eBWXq4AKzGGgm2SLesOdAMZ9OB9Q2NsbaTuIa1tmVNiM3qYTBHiVXIYmfwUzML3Zr7mr7iCBebHXHc3XDyEgIi52eri/6wfatHcq6gR8bZJIgnIe4nrDRKDxB1rMeA7PQYntk2ZdPL9Op8/Ps+C+8NJ7O8v6/HSk+Tv/e3iPdj4192/tyl/Xlryj106eX2o2BSo+j0ybtwucx4z8dnH7+9+8fpvXj413s9Mrr2r4dtLd2OP050UsMBoCmrcdvTZF298PbTy9O10x/2dB8ex5Sv9wNy8r7ifebyMfNuw1tMVEG8fT8/kYy873Ybv3nZfg8TAaLRxCj2G2+4RT5za/LydTnGw1gIfaKvKIvv/5fyZrpNcglAAA= -->
