---
name: "rar-cowork-cookbook-teams-update-measure-frontline-worker-service-performance"
description: "Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_frontline_worker_service_performance", "rar_sha256": "3cff8310166325fc90e325811565a0d6dd797291d51532d4e91478e6f69f5bf2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_measure_frontline_worker_service_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-measure-frontline-worker-service-performance:3f1c8e7cba07c0d1efa00c3eca4734b900ba9e090d86f4507a4dbf5ec6cdd747", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_measure_frontline_worker_service_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_measure_frontline_worker_service_performance_agent.py` is
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

Measure frontline worker service performance Teams Channel Update — Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 3cff8310166325fc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_frontline_worker_service_performance_agent.py` first:

```bash
python3 teams_update_measure_frontline_worker_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_frontline_worker_service_performance_agent.py   # or on stdin
python3 teams_update_measure_frontline_worker_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure frontline worker service performance Teams Channel Update — Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_frontline_worker_service_performance',
    "version": '2.0.0',
    "display_name": 'Measure frontline worker service performance Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-measure-frontline-worker-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d5ee7c0d142cc81',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/measure-frontline-worker-service-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-measure-frontline-worker-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMeasureFrontlineWorkerServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureFrontlineWorkerServicePerformance'
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
    print(TeamsUpdateMeasureFrontlineWorkerServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSLLlX2Hifcisp8gAhAARffqcQWgBgUASixCVdSLZQaxih5r67+NIisjMV9Vvpnv6wyhPRiBwNze7ZnbNHI/fn8y6CrLi6fVJds0U2phxHAZuAZmpAzFZmxUR+JVFFvgP2VlaFaFVV1lRPj0/OW5pF2FehVkKpi8L06tKyIQU10xKyA7MNHVjKM/KCspSKHHNsi5cyCuAkDhMXWiUDRYq3aIJbRfK3cLLisRMwXVZmVVdQm1YBUARKEwrtzDtKmxciHbM/HbBmIUDgRnQtQ7tCAKKmb77AtRyOzPJY7d8ev31t+enEFw/vf7+ZMdmCW493bRTc8es3N1dpfW7RqebQvJdn/13dYDM2Ex9MDnvAVYp+P5QFtxyXO9d9c+lG3vP0H/+Z9SahV/+8vo1hR6fr0/jv2OdQlXgQlVmlpXrQLaZm1YYh1X/AtFxa/YlVLhVXaQjjCWwKPVf7jO/S8py6O/js8/3RV58t/r89SkDKpijI74+/QIBTL4+FfV4/TJKyT//8hJnrVt8/uW7nLK2Lq5djcKA1i9vj+8PsWDg96Ghd1v170Dq3eWW+/XpB+PGz13v0U4w8+nlkoXp57vgvMgaNx1x/PzLPxJrB64dxWFZ/V/J/fUuOHBNB9j0UPyX5xvIv0GTh0EfMv/xsjlw6z9jCRj+vtwz9ADqH8m+4f9fRI9BVn4g/pfi/mrC5O/Qr//Qtv9uwjPkfX1aujFIl8K0YvcV+v1N3q+YXz85329++u0PIPr/KEbO6sK+SXgDSRF6blm9vf36qbzd/vTbr5/qHMQaSK63uoj/SuZf4Xpb5ycEH6M+/zwXrK+mUZq1KfQR6dDvWf4/ij9eIM2MQ+f7/fIV+jFfxs8EGo14X/QOwQ85UwJdf8Dxl6c/AG2kwJravj0GWf4f/wHtQrvIysyrINnO6goCDq7CxB2VV4KwhJRHUn+TeU4QXhLnGwTujukOKMKs4wraFGYICLHIRo+PFmQe9O1/2jeS/WI/SBauRoJ6q28M9fZgzbcP1ny7s+bbgzXffmDNby+QEgB9siL0w9SMoSO930OAFNNq1OQWM2WdfGlGZYCi4Z2Mjgw3ElFZx+7foG//8upvt4Ve8n40+2sK/GiCCQ5UuUmeFWYRxj1kjrxm9ZX7BXA04J4ii2PLBOQ9/qjzlxHLU+CmD4RtQP1u59p15UJxZgOLvBDw+jMIkjKLQQmoRtzLKIxjyAkLAGpW9LfCBXzzOgr79u2bZZbB1/RO3Bh0L1glDAZ8KAx9+ZIXrheHflB9TV07yKBPv//xCfpf0H836yZ8XGMP6soNSBD8MbSVJRECmVwnYFgJjWEEaOrm6d//uHto1C4FhQ/kX+iF7m0ykPY9bEYL7m579xmweVTRLR4r/Ywb1AYAFyisAFqAE8rnr+koIgNDizYs3XcQ75Pv0L8HwX2d0SflA0PgJ+Dv5Db2FrGjM+2scF4gzoM+kALmAr/eCn4wlnjHzd3UcVO7BzPN6rsL06yCSpBnpdc/Q3UJTB0lf7OA6BGcBJCZWX2Ddswe1MUsBj9GgG7Lg9lZGo6Of0Tx/TYQUnwCMbZ4F/ECiS5AE8rNwsyDwizd2zjPvEcEqIfv84FwE0rdFhrbAnf00Y0BbpG3+2c6lHuTwzyanHs/AX2tpwg6g/7/6IRGk+jN5rja0MpqCa1E5Xi+x9/Yxo1w3Ds/0H3cJt+S6XtH8k5e77T+NY1D4LOi/9t9pHcLufuYO1UCmxzAOceb/DH5i5vcsAKBM0ZCUYzBbn5N3+vHM4AIuK0cqRDkdzSyRfax4Pj0XdMAJPH4/XsvAd1jcswVEO1QXltxaEOe6zq3xKiCYky7h0NAFLljCoI8sYOfrIKAdBAhQP7omRB4DdSYG3QiSB/Qf91z4WN4OHZoQAuntoG2IL/cF+g0hjsI2RKyXNBmjWMACp9uooCzAcZAxQ+Ey8DM78qMrfVDQXP0RZaMMfSDBx4PQeiOhQqs95GXQKoJIg5g2QIngLTr7p790PPhK6BsMubIbdLP7n7YCv1Y6P425ibQ8XvNALuBsUf4ARxA6AUI6pFgQOxGJcj+xH0EEIiEWzvwcq/o95bhQ5fXP+0nPv9zW45bjVZ/9twrFFRVXr7C8L2OvpfRFztLYBAjYe6W95L65V7UvjzS78tH+n25p9+XR/p9+SH9flrwjt8r9M8p/ZOIR7S/QugL8oKMjwSw4hjOjw/AiPmyOH+ZjU+/pkf3u/MfETLSIaBoq/+oSu9DQGnyC9cfB9+rVDkWtxbU0xs53qrMR4A80mfkJn8sqWX2Q1qPNo3uvnvzg8TBo3QsD87YOt73WvGofuk+vaZ1HD8/pWbi/st7rJG9QWADiMb9Gkgy4IgqdG/fPnq18cvP+85b+gHecLLXMQtBpQR99TP00SI/Q++bltvmMK3Bru3XsT0flwRDwa+PsR+bWst9AnvHqs9Hc+47sbErfHTrf1ZiTD6gse2OvUD2kc3jin8SAi583y3+LES6XZjxg1IA9Y/1FZT1BxGUQE8HtGnPEHAoSFCQcwC7Gkz48zJgncIF9QBw8mjud/y+m5XdbfnjBkN1387+/vROLeP1vb24BxOY8P/eG45Yv9f0t9vTUe6tg7tBf+uT34DZ4Vi7f3jkj43I2z1on14BYbnPTyPAoNTF4XDb6z/d1QT2fe+wgQRAPV/KsReBQc4BSaBDyEfbIkCbPyww3g6d2/jx4vWv2/J/hUNeMQ+15y5pWyZC2oiDAisRxMZc25yR2MyiEMQyKRehEGdOeDMcIc2ZY3m4axO245AzEmg3ej4xH9rB6OgzYNeHY/59e4inu2BQpKY4ASRjtufNMRRBCQKb4p5NIS74PUdRnMBNxCGAghQ5pVAHR3Fs6sxcCp2Rc5fwCMrDLW86yns0q3dt3943Bu9evHPMG6DrJBxtmZqmPbdJdOZQpEnYLoZYmO2iU9QhMRfBKcybz90ZmP8x9eHJ0dF3QMbgB33qaN64zu+PyBgDmpiBkeys5Oj7h4EpzYSnpHUMhImOTLoOngU1fsq2oueu7SJWRaez/Y0pCkuFn+XqjMG2sXVAj8rWRjL8upGCJUWn5HbviSSDb9VzoeTLi7+5yqJik9JQw7hxPfjMytrHylHMbbnnG45AyEhGEQ29ynmgsad41Wu8Jk8FMxQHeN/x/Rk55tPawPtMwfBTXmz1GWk4XueKvJCUl5wXOXalGck6U2snmPfMKYlT7dIJpxpFhORQu+g1OcpEX8ZKvDXm/iQto2ytZD52UWf1UUPzWhMCk1V6SkrxqSMp2tTdd04iaBMbDiRBO2XRqiKu83XB5yhyioke8QrHNqMyl7vL9WLAYbVI10pSXJn1Vdx1+Kms/Hk107Zpn0t0toqv/Fbm57g4GOEk0HZa6RynvDGoZw3XTrtdxJ3qJN416govYjl2Vq28PkfxEDjrCYpSoiXUhpEo1kTX9E1sXww+NziGL8s5667x1dQmVmodI3EoT5KqlcXo6B7Yyzqqusaxtm5ke7RNanEaKsdBnmvakO7ERKCbIuZhQcxDaZPnOgOfEuWwI9BrfMiaGBZO8VG0Irksa940+eUkWaSLzlpUUpKJJmX21Vagkb43t/tS37RXI630fFCLhcuG7ilcc2bBKCEzw+vM0uaoTFUGXuL6XvIN2kpEgjAcl1IiCXTMBDO1seXKrjcnbqNNvcrYJrtZVUjcQTgEPnAutl17m2JVi2WxZobOE9ca48vWauHBZ+bC6Xl7KkDXqcYDO1khts7ULLleO9mUm+PLKOVmxkk6GxbPcvvUIetJklWobjjJPi9jb7no8DkfTXftYWXlqhEbShch1lCecpk85sk0UMb/8fSi6FcBJUkpSWblfkWm+1bVp7rY7smZjs2ls6Wv3CMBk/T+6ikFNjl7GaFn2F6rnXYdyIZnrU7ztWzmzjqxEtnd4ptcux7V43HS4ivcsBbLwJ2h274nfJHB7URjqVMfDX6BktPoUkSGW62kJbwP0ezccHxVhdv12Uyy0D9kIbHL5mlkHV3+WC+S4ypbb1E/nJ0ZgpFzK453J+Pgiv65glP7um+dptcc56K6847gQZiEea9nlSFEnibjQqtSVos4ee945xSnSb71cPyqTo1+AycWjNGU1UUF0QYY4VFs4HnMVPfjWpmV5wZk6nW2U4q5m5FnJNyilcFdS07D2NWwkTbtTrxw8YFe7OfyHG5nhFkSpjvhJzFGkjIRrnlNPS6PKmpcM1SortIFW9uCoRvreqYwTiKFjQeXoRqruH65bFcV04B9rFA3ulRtediUFW0wL6ew0Vje8RHJwGd+VCzOudpH9rWRd9qamFNyZiwTxsrk/WEyyQLG7Rwh6yRDm618eCXDVhdIPEyG9ZpXTV7T4QWZrDC+4JlKqJyo170DyGh8nV+qaNNsGV5CpwjhZ7SVB1KkWdutFgiploACJw0xzRWFJ/fLGJva7pZxt7UoBoI5y5ZpQeQbxcqx+ELKV0VXlciUqEk8Z3yEIehFrE61lbtyUDKAeyqLd+h1yLCVq5OcaGM9vGOnM20xgSvNVMjmXKyOi0jzplJF2M3E97zVoYdRzpnEgOe5RSpMp2vpovNld9oSAwgk+3DpnTS7Nl7HzAKmotXrwTbsidccMiPTE7VdBeGpVgwnI2fHBXKNmAutiHSPDJPLRk/P7amLLLfcxLzSHtWBzJZqdUr8Y7BTYbakaV44ldddqy2Pi0A9zbbmOm6YdXVoeY0pJSfPo44LbLZgrhPJRXHHVyOlHGyRr0h+bQ0GcSYwA1ufuuVedjxLLClpWHdO2i22dHGhzTqZwZew1PdeMu25RmQze4moBj8MHTXZiovWaipJN7GUpWGZpA5EDW8bT5ng7UTGdw0pxEs7M+kK0YfespHAP2UbCRXMA56lu4vEh9fcFVJdNphwM4cRPl2liB1Q7cqUzbBz6B4LB/OU92YkyxQVavLaEY3NFE2vW1MhYnM6M+hG3lzDKzc9T7J4n7LXMyDF1tyy8hKopR+GxK7KCbkjYrYelkihLrzaosOhT0+H+XV5uVyuihvn3UHXxaIka5Uycpc9LqdL/HDUNwvfZKW8nPU7WxGlmViFu4mx2dpma9jtVCq0SvBYUZl1WMRturhRJTdFhjgb2qmWtufskMQmt0Sr9irbNQnrEbnS3RZhlD6ZdNR+Yfm74rww6pMkiIvAzLb7vT+fzLRoU/JI0uPB8oxmIHBOC2enKroRE0m4mJHass9jVovDQlqwulBR4aw12629rRRNWV8tsAmDYxx0EFfVpI5ZvM165jzsRGcht/xk4c/VIbKjRKFMiUX59LCfF87BpL31CrvK5GqgpSKxAk7dTZjwWPaYtpg38qyvIy6cAVBmc4X2mwUh9gorX/jDhdFbLnIZBE8Pui/ggyNbQeXHJuVRJ6zsbLauQ+t4Rn1hak1PKBfw5zqYiseEJnBStGMHKxF6Nz8kMJ9dizUKK1mwJXaoWK1iS5tdyhWmdqGYdnI2nBwtcDecpMWsQ3uJdVoLqLZdRYezGhLcJSO5mKWP9O4UWa2+ZmVswm2ZA68sPGSASaHKdnOitAIENF0KOvWTko0x+UBttkwlq6gSB0nF2cESg+EC3+qWkS5EOd9gZ9bxL6w3CNn2Ysx6j2Is1OXqiw4aF0I3iP1p1xxjM+mreGrhB30jqUeuXcwF8ooGBMMvA5a2hEUz201p1S76MzvhqlXQLlcIwq5UXZhTkqnQVt8WGaLZfTPlfX2jHUy1qTcOJ6PXQAO72qu2YzsnPK1iKV9b+F5xe0nnr3vnkKDK5dgMqzl9TNJFWBmGvrmEB15aIx175JEWHdJhucxlbR1xuwkPSs7GaP3FcI6jfHU6rEJW24t7IkR7pD5PLfnIGYm6j5YTPd6TzCaztrJ9LMxjUNDzKhVXm4YRBxWN6b6b0b6+m29rtWdsPtpODGlNZpqnXl0kN3qVI2pnJda2fW69DttoqU2Z7Imdrc9LONjKThkmThr4jK9dp7lQZudrQQ67NFtbV7M6ByXunE4UivRqN89igyJ7dnoYAgM435WGEz1Nr8eZkqEVAcAPHHJ1sVVkrs6vVzWiisI8SQTYZnBDq6izgmvqU4BOjVpFdNDXayuKH6JzIPCHc3qI0eOMWSwKsQ3EwxzRloa8ZiWyUJecYjdmy1wX8AVuik21QEFblLbVlh74MlcmbD6pXXx/JrqNttgNR4OyClmU1fU8NlFawReUOuvjTUcrSiaFnDjXEH07caRQVQ77VKOTSF7u1TofetAD2wsjVyfiAeWscCvOhdjqMlAMlG2IX6w1NhwjLN3tw9WFSZRcjJDNYVU3TY03a5npi04YhjPm6uXFOlpEwSqLxdLTN+F62avLiieszbm70vvDWinSqAh2zux4wRHCO5wT2hlanWsuGNYPNeqspjm/Y3bzZmsY7DkTsIBBF+gUVqfzTulKZiswreLRyN7wGaupjbVcmbxcmKSQiQyHLSmmxNvZbrOZTiNXa7W4L7DjOXIW/omip+KaLQm6DnTd7MzFOTPKdKHjfc5MJ3AUbwqfyDqPpo3QiY2qyoS6dnyYjjnuerRbdE81pl1zoPkX7GzgWTZzc9EyOF6ywllOHWXSoiLM4ZwKi6hY2+/ZYZ5W7CU4nPbC0JSuqKC66HB+v2yLDdqk5NFBPIO8XrYTSVlkF4ZtJjQxJTXCIsH2da563H5BUFcc9kj2SDaDUZJ4UzYBWU7216J3XFLovGU0VEKzYxdY0QSSSVyYLC6c4lyRenWtyMNaUHzVL6PJ4swxrgb4xRFFjVqyTpoXBXHmZjovEKtEkFSdDHi6g6vJaXJO26NBLHVJF/Fyb/qRza4vXdu6pNnis5lDmoKn4s6CSi+UsHJwe7GuWqck1wbFm/Bw8kvQnEek65Rrg9732URst/CxIiVkQ8Asx3mp5zXI2mtZcZe3CFnZcOdQbnapGwnrJu4ZyXv4IKfJstm6Wbi4JpdWXIeDHyN6I9ArKuwuLMx029WKRjp4a0mb0D/ZTiIbQU/DdFld7GR+YDkvGmAhcyX3DOBQ5gOiZ72PaSfSu/jnvdMX51MZqctCIyQ7Jtt0U21Lttx022TjtculV29s0P4ftLWH7Yst56HpTgCM4gUAm5VetcF8n1rWeu5XJoXHptVf/Q3nnd0WNliU9GV0uY0vu2ByDsvI3R+l+uLZzRFW8gbdw6c9aorq1kROw4QxbIYnd2xUzdkOYc1Tk9jJNZ6S+qXyBSnrLKaRBtHSh7IWPFM0pXrOdCA11Lkjk3V+seBoh7YHdcZ7U2rZncMdvCKmqt/RCHIOveOR5KXuJCCXetfA58N24TtZsp1MlrYqcjLMasjcXvhHDGWDDava9Xrh6xkpbyfDdJ0dYjjY2NVcxlHKb1L/bKLL9UzepZuSbbAzJjTYbLU6B82ZJXypM6KlneIEoKeLTy9FhU4QBimQobX5xZKrgquwnMNnpcdOU04NBoqY0FHmgHiYb5MjNXFJlBACK9im26miZ4DRE6YjaCeewOyeDfnrKlN0IcPbdJ6VVCmi1aZWEhwdZgPeZud8cJaqby/m7UzEOrBbWy5gfHJe7mY13Uk1MQ/nPH7B0ms57Su63ixakveta1UuGyUmtYkiiSImWZTL65xBbPpZfSQojC5QypWXO++w4oc6tTbeIfd4u+OyZb/z+hzZx8d+oszcvewexQhDlT1B7eTAxJrl0uUWmYNSHm2tqRlZedc4wAKQ5bMFig8pjB8OXUjDpLeHM3XP03tfCC8YPltZgAqOsFtTDF0TbMWxk/qMOf4Si9Rpo5Fz2oW9jpMmOiJU8NqYXIlttGT7S5Lxmb/eM4RECEZB4oDpruK12TCoXU4belUQTWfMN3mR7JfrzoP3itKcTY6w0ebYzqpDNOlNMkKHsN90U9TdVMIBRyMVV2YSsVlnYWu3Z1Y+cLueN+fCbn/oqtZQmqrD7UlKWgNKEGS+8boph9JM6yLe9FwPPbpkK3Sy9/2aPKcNB4M8kemypJ223KyrcmU3IDn7eqImCCvSu5mNr6LNvpKnjRrt7TRLTWBY3yFno4vmZGP6uss2AuIc9YWB2cXCo0eywkURhddhM28rsjiD7hY2+mBlL8/VxctjxTlFF61qVVybX2k+h3ukTzF9N7CUbHuXqt3w9GUZmE4jL1eyKPYBnZHeIeLhkIudI74eknS+NZjLhUoTlrMnvdMILBUjUkdSa5htAeY679P00/PT7RD66RVFKAR7fhoPIh7HCf+W987+EOZvjyUwEqeen/59LznvLxzfjyZvxwuu6bzeVn/9N2j/2/NTYYdA0/sr7DKu/ccLz//y4vfLv/yWehTb34/jxzPXrno/0qlM//Z2HTRjdVkV/VuZxfXt3TrwWF2Of8BTvj2OPp5uMCT5eI7yo9mj8Id9Vfb2+Nujp/GPbMbDRNcJ72PGr/7jmOL5yemB+0O7fMMI/M0t8hGFx/nZ+Jp4PEB7+uN/A+hs2uS/KAAA -->
