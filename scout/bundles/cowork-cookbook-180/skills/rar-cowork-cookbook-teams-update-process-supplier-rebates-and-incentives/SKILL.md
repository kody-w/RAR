---
name: "rar-cowork-cookbook-teams-update-process-supplier-rebates-and-incentives"
description: "Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives", "rar_sha256": "a48cc02c5e33a51d644c4ce6c87b17c7fa617afe03ab6879149b73963656fafd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_supplier_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Process supplier rebates and incentives Teams Channel Update — Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_supplier_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 a48cc02c5e33a51d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_supplier_rebates_and_incentives_agent.py` first:

```bash
python3 teams_update_process_supplier_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_supplier_rebates_and_incentives_agent.py   # or on stdin
python3 teams_update_process_supplier_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier rebates and incentives Teams Channel Update — Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives',
    "version": '2.0.1',
    "display_name": 'Process supplier rebates and incentives Teams Channel Update',
    "description": 'Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-supplier-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c878686ae633e54f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-rebates-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-process-supplier-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateProcessSupplierRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessSupplierRebatesAndIncentives'
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
    print(TeamsUpdateProcessSupplierRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bObWJbmv8K8/iEzG9uIXbiiIoZFAiQBktgk0hVOdpDYxCKWnPzf5yLp2ZmdVT1d1R0x8rOfEPee5TvnfOdc5F/f3K5Nyvrt85seugUkulmWJmENuUUA8WVf1lfwq7x64C/kl0Vbp17XlnXz9uEtCBu/Tqs2LQuwXajdqG0gFzJCN28gP3GLIsygqmxaqCygqi79sGmgpquqLAUK6tBz27B5KEoLPyza9A4um9Ztuwbq0zYBt8CdNqxdf74HsYFbPd7wbh1AUVlDty71rxCwyY3DT8CicHDzKgubt88//+3DWwrev33+9c3P3AZ89PYwzKwCoHb/tEZ/GXN82sIWgfzNEiAuc4sY7KtGgFABrquwBlpz8FEQRtDr6scmzKIP0L//+7V367j56fOXAnq9vrzNf45dAbVJCLWl27RhAPlu5XpplrbjJ4jNendsABZtVxczeA1wpog/PXd+l1RW0F/nez8+lXyKw/bHL28lMMGd4f/y9hME4PjyVnfz+0+zlOrHnz5lZR/WP/70XU7TeZfQb2dhwOpPX1/XL7Fg4felafTQ+lcg9RloL/zy9jvn5tfT7tlPsPPt06VMix+fgkG472HhAjR//OkfifWT0L9madP+l+T+/BSchG4AfHoZ/tOHB8h/g+CXQ99k/mO1FQjrP+MJWP6u7gP0AuofyX7g/x9EZ2kB8vod8b8r7u9tgP8K/fwPffvPNnyAoi9vQpiBJK5dLws/Q79+1fcr/ucfgu8f/vC334Do/6cYvexq/yHha+4WaRQ27devP//QPD7+4W8//9BVINdAXX3t6uzvyfx7uD70/AHB16of/7gX6DeLa1H2BfQt06Ffy+p/1b99giw3S4Pvnzefod/Xy/yCodmJd6VPCH5XMw2w9Xc4/vT2G2CMAnjT+Y/boMr/7d8gJfXrsimjFtL9smshEOA2zcPZeCNJGwj8zLVdhwDXJgXAvtaB/J8jPFtcRtAv/9t/UOlH/0WlSDtz0dfuQUZfX9z49Z0bv7648Svgxq/fufGXT5ABdJV1GqeFm0FHdr//UgDqK9rZjqoOm7C+A4bxxjb8CLjp4/wGUCj0y7+i7utD8qdq/OXF0Q9Pj7w8M1jTZeGnGQU7CYuXzz7g63AI/Q4ozUofWBilgIw/AHSaMgO83c6INdc0y6AgrQE8ZT0+ZANUP8/CfvnlF89tki/Fk3Jx6NlgGgQs+GYO9PEjcDXK0jhpvxShn5TQD7/+9gP0f6D/bNdD+KxjD5rBK2bAwo2uqRCowS4Hy0A4QQIAgnnE7NffXoADMQVoWCDCaZSGz80gh69h8I6+LrEfMZKCvBCgDhDPq7JuAY9DafsJkiPom71A6XxrZvpkboxBWIVFEBb+CKS6wJ1vSBZlCzUgUZto/AB1TfjQ+otXuw8Tc0AGbvsLpPB70FfKDPwzm/lYBDaXRQrg/5Ybz8+BkPqHBuLeRXyC1Dlrocqt3Sqp3ZeOyH3GBfST9+1AuAsVYf+lmFtqOEP1KKEnPGARQMZ/hfTjHHMwKeSAL4LmXfdjjTt3P+PRBesvRfMqD7eeQ+GDdgGUxl0azE3jL6+UapKyy4IHfsDSWdIrCsErKo8c3P8XZ4vnZMK/JpPnJAB96bAFSkD/38eX2RFWFI8rkTVWArRSjeP5CfA8ds2BeE5qYG54bH4U0/dZ4p2J3gn5S5GlIFvq8S/PlY+wvNY8Sa6rAYpH9viQD3ICODXLfaTsnIJ1PSe7+6V4Z/4PAJ0HzQE8QH2D/J/T7l3hfPfd0gQU8Xz9fQp4hBi4DeACaQlVnZeBlInCMPDcGYOknsvuFQuQv+Fcgn2S+skfvIKAdJAmQP4clBQEDHSHB3RqCdwEFRfVZf59eTrPVsCKoPOBtWCuDT9BNqicOXsaUK5gQJrXABR+eIiC8hBgDEz8hnCTuNXTmHkUfhnozrEo8zl9fheB183vuf6wZTYfSHVBsgEs+5mPg3B4Rvabna9YAWPzuTofm/4Y7pev0O9b1F++FA8bv7UAUPTZ3N1/Bw4EEjB/punMWQ3gnTx8JRDIhEcj//Tsxc9m/82Wz3+a/3/8544Ij+5q/jFyn6GkbavmM4I8O+J7Q/wEGAMBOZJWYfNsjh+f3erjq/I+vlfex1flfQTqP36vvD/oekL3Gfrn7P2DiFeif4bQT4tPi/nWLgW6AD6vF4CH/8idPxLz3S/FMfwe91dyzBycjaAbf2tI70tAV4rrMJ4XPxtUM/e1HrTSByODyHwpvuXGq3JmRornbtqUv6voB/2ASD8D+a1xgFtFC3QH87z3PBtls/lN+Pa56LLsw1vh5uG/ciaauwVIZ4DOfLQCwQHzVJuGj6tvs9V88cfT4aPoAFsE5ee59j5A8xz8Afo20n6A3g8Zj3Nc0YFT1s/zOD2rBEvBr29rvx09vfANHPPasZo9eZ6c5inuNV3/2Yi55N6JfO5prxqeNf5JCHgTx2H9ZyHa442bvYgEEP7cz9P2vfwbYGcApqMPEIglKEtQaYBAO7Dhz2qAnjoEXQAw8ezud/y+u1U+ffntAUP7PH7++vZOKK8YvEZNsBxU7sdmbp0IyFugEFw/Mwzc+x8ZQl8yAS2CgQcIdYml7y8wnwxx3CXRgCIIn/BDyl/SHkr7dORSKO1G4QJ3PWpJMyjBeDTOUDhFUpEbBUDeM3e/zjNDOtsZLqIQZ1DMD3AKI0mCQWnMZQKXoF03WCyX9IKOAtA5vm+9Ak59Of90dkb22zw8g/TC4Nc3jyLASoloZPb54hHGcimM9o6JB9dUeHZOiOylNoViY1JzASrpvleuroLGYKnPWpguU9ebftX6UWpddiFE5xg+O8z1jqt5yImZtgnSxk4PVbIrpk027Zmls41TfnG+6xulcs9hl467w+0ITjC2fq2dDbEFc9+tRg7ovSZNP8fXlFnnnV+vhIW5le+S5NHw7khZvsUL+FrOi60MRl0lWy/P9NLT7RorS+/kYn2ysbaZsU3Uk6iPpYwUSjmuD60B+AA1buTKsm+kpa3LYL+7jlHhXEnt5BDICou0EznBa6Kztqmvs0eU2NiWX5twdetRcLY7u4em4oepi517ZsZ13HqZxcWZlhOZdspLXfWpVY9ueL68UmVn6bVmLCnnHhxIld9iXVyvF/1NGdGt4d80dNpbPGaX/IiO9SKvz/Jlv1mfnFN1wTQraUiL2XaU0DTBDR35YM9aZc6NF8HiFaTWVG1j86k1VDvzRKyF8ULLhkut7DM4f5mkbSOl7PMEPmw6vwxXpU/uBUdZqozSnc6Z6Aamrxhmt14yChU7fW251QHZpXqmX2pcrs5O6IruVoBzLt+05027QNe1vev0xNmvsrXf5KlB55O11pfIrd1tTIWjwmpByNekbjbsZnfJyZgxBqsmF4WN5Et/FK7izcG9NsNqxj90JEafQUR9RR9ly4mdyIGz5nq+dItGTrjWHUIj96l7vU6dNtoNbAN73bUvF7JOEDLcyoI6uNnFMjGtO9/7QkgJs7/7m0vL9xKu+NdKEPQBF3Zbk+GUZdQWC3RFdbdtNzUUf0ku5yJaj04enXV5IdvjcTAzjDZydTNR0qbBNMNDwd81FSjdgFSS5t7VYd9uMDiKY7zM93GDCAayHgvf5ZYrDIkZxZ9qhrlFVYbGfuHeNWwiQnWXJTK8VZtVXqXLMlR1/XjiyV2rG2m6QfMe2wqYch6F1N5f1Ju85DLessOKZvWOSs0uG2IC21/3UcNMZp/vKm/iF3qumJnM8RYrHVHJrMTeTG110EY5Y6uuWYl3zmD1bCeXVYorq8sZ5MoSyex8jSIyPqHeccgK9UByvRkegvXlrKQ0xcqrqxvESze8GX67jBb+cMea0CFvNnYcV5MtIVXh4tHGnO4TfN8ztGojVz9eb+UajVLBo7d0vsCkBXlMsGqlj964uTWby0laTaLmEnddODNEEsbO/kbt0guNRmYUnaJhlZ2v285dSbXCuFVQGou9nx3aYDKmqL+uyIZRbKEeN9a608j1WHJIsDVFdFu3lG/BmdnejEFcm8NOVS5E4OAX3VQP2yStjxpfIpvbIqeDcMcZN8ehYjgQJoJrtiilnu0KIyS2XFJmlB6DNjrcxZ03kcdbtYJRHZFF+Hi0Hf3g1c0AXwd6lHK53u8UtOPXrdrestw+0UKSaFdzu7GCeHc65aHiolMmbyvaMNO5rH1HTO5st0T7Qyub7ITCdutUC5chKq2wRay5wUudDK6TJmBqJtiO76wC0kj2nSfe25V6606txgjbuxomOXwilstFTKMSE5d7CzFh0/Qy3Cg9tbSYaaqHBdsxE6ZUHSiEeN0vvVtyvKrmeacwTnY87+RzBTjJxvf91e/TPMo3xwvFFEY2SkLdn3llNZ7zy+RNILu2Qi9ShzVrbamjfme4Drv2nKcdM70xzc2WX1eSn2yrtjTZnTCMhBuwG3Mt7NLu5t4OEm7sVslaM33Z6tes4+uyQxW5JyfZWRWtKVng0h60lOmWc2hlhlv73shBYRMknF40QxpWXUIyDGIs6H2xFr3VSr+o9oGJ1ASXsm0aRDkzNsF0aXjjqMO3NBFwGN1KKr73g249SNpAIQhyB7kzMDIT8rsdczydRnJZ7hP1YHVGGEZ1elV49TBglahLqsxkTmJbZo2eqa2hmeym6HATv8IX2/C59VUs8yJWtmfMCixmiPVIDrt+s7mVeVMHawPV4gq1LyfWS9Rs6ZggqGpP2ivXtnNrXxT7Y33b0c3VX+uafwHtwd7csjVHHUFbYLako9lRYV6Oa8NTzgJRbzteq9TYKgwmpLDs0Dk7O61sfNjfBj3eYutdiFnTZaPDhev3EprvQ1Doyrm3liOmSSdmm+dUniT34NQVp64TRqYbHNnQkJK/yIUeqdvN5XYIde8e0rRIpHQuJnp4PGFBS0zKOqPFnTweF+RS2ZmJ7LrmHpadYcU27C12bBy/WLnFbYjVibP3gZ3X7nlHBKpQWi66FcrDRs/2hgYrbjPuuE1a+laD+uvlKRLHEssjORA59GDSW/bqLTg2rgjRBoI426n36pWMronW965NraZSHXe3K4WuTF+1hVJf95fNtroQcrDat4ZfX5nVcXXJVXbqi2Pcr7q6SVTU1X171ej9sFqzWegsNj0fHqVauhurXXslg5Zyx6V4BvV0dar1xhYQKzsX8k28dsy65LbnCW+6Ndov2b1+uDC7snd0G65Mv2BE/XpKw9tNOUzClnL6/EKLSn4qKjPbJFNOctPRc1K01VuLH1ZcnHcxEmt1E5s+tz0Ap+7M2Qx2ERFfN+xN4fc6gvs2ph8HnICHkpS3hZImZ1+64vxhKZ7EQC9IQTtMCEzBenYn8DhZ4bVZSkFxkfyJauTLbTGAgHqtpqhtQU5OsFMZzZXvx5jMzeqOkejxJLLmkejZ0cDvdbpYrW1MZkVXgPttSG9R/RJH9IE65L3hLcYTa568ntCoU+Wmw65Xtnl0sU7cRq8vnBO4BirYjexmeiWfnMVNU8mA0vksbNceSR870txkgRAcOsu44PfmnLKKeEDSjtxZ4k4/bjVuMRTnkvdN3N8sh54w4yO5FfbGZjHGw/7a7ypWaeW10MoJGg2bu+locC1KQ3pcq1O3jKORLPeH03ThFCPdhbrSxGLKMuW0JnRwKPRLV9ccDlFQbH3iHa5T2RXlZ/xB3JvC2hLlsamO6JmWvTN5IK28apyj1zm34Gwk2UJYrNANNt68RZhvc3YSnKtG88PatdDltKFys1Mw/4iBcVUKEdrZnmFzm+QlL+EHowIJfgq1iytgp2RF1KvJuhGXkdu06bHb1aEaWdb2GGZDi4AO2bfeit8g11bfjjSeYZmTIzdzN+zShvdHQvf1y5pY6aXbl/5GTg2NMvLY8LZH0Nq9Ws74XVZpx4bYBELhkCgq2aQ73UtBwjI2KU4LEuEWqLP3pXNIqNIBP2Qusz2Bue0sLi0bYw0soaaMH2PdqTSUVZYZ5sR3reCcoZQut8TgN1xx80xyOHt4x7aLG2hLt1gdzBxejTfStZW1PB60M5L4yzN2nnKp549XI946IToUHDvRdO4BvmpuS2O5xFTkuj3WZePtdjo37P2TmK8E3hRaFz6LJdzGob8ydkV6GxbL4bIfSxMujguWivfUrjCG7lpE+VRVB5OQHSIEbWRbHU57FjXo+5GZ7qhYauPGZHmeblYGozHbkLvvJm2q+JY7GuGEZK5AZhOlN2R5kLWd2srLXYNZY9WlA0sJcbkQzgsznGK+WQdBvS7XaZKPfn4aKj24Bwi3YUHLunAhywrKaXsZkcPJiTwRA5XtmClZ3SLP6snl+WqdveMx90OlZw6uNh5MH19XRbbeBXfMqAnDpx0RCb26H/eSz/qhsZdwt29coW5xSkrK1cHfW21kbbCBC26Uzy/6aRmTxHmZ4AFe0gHFCAx9GeA9LknlFKDLoGulFvHhnSUZnnvi8GCBWPf1CONr+CQU6BX3z6J697wUjGAB37W3diRVrHDK5mSzrlBycXPtOHPFYlZId9TuXBOYgme1JZno0F/Nk1KJjqgYRHKQBwSDZXhlohXJcHboofAd8w5nVpZEL1GCBZocyYHOl4euosg7LQnUQqBGkuLpveFhKu5X+JJC1wlBNXQ01fFdFruDlMBrG93dz1hP2z0pSTSOLJHkDrMVl2FiAU7ByApHKS2kGNqSSDRmii34CXqNsG6pJFbEnl1gW4o/HcPlJjY6UVT2mKTpssxda9i2TRRlrwQ4dwzClYNZUhdJtY+1A7Ip/BNPtObijiu0cynbY9o1Y0B1l97XWqK2dKW0hMIiw2VF9qfteqPsAr5PRz6iOBUHtHBPRnN5zwJlhK9IP4rkSPFOsj8x0TVgKxjHI3O9rP3eo+VFdq1iFFMUGOkauid7x4/FJVMcTqsjFvGDK8Goe2noU+jicIuQg1uCo+z2PrJoLNZKHBoScZJYsiXhhHZuO7cNMXTvn9Na4TGiGZooxJi9ukRvN7U+aQJ5OdU3TanaKOirAubPMbtbohoWcqf9kHqJz612/iFVsVWNyow+5SCfmoiRlMzm+4TwSMprDzi3C5fFhA7gAOqvQtWhhoFYASY3uG2OpE01sQvCC+5TAug6D3FfIytbvsdJqJ9MZbrBWkQtFksEmXrlgIQcfOUb8eDhDuaA4WR37pe93W9i1s8ZpZHYuMf78zYdkD0luvTlvNpuaFi5JBtKcfkTsqVjLyrAcXFY0+Gmxfe6Pq0l0Z8KxOUaHPaaeLsaD6ekJfoLcs1tWKSoi+fcfa9beAyx2lnOKFC9yEW4xra+xjXnsxZJQawwKcGvKFoahF7ww4axEjzvhSRuRCzGKNO7RIuqa9urcTdAj2Mw1LsqrU6j8GYMdleL0vC0uHB3PuN6o4arkotKcEyUWaWWluvwsiQ0ewylhOKxTZN3two5ugOr1sFSbombSNY2vewAM8GULze44yHUybxHnYsPtnw4jQRJt15CyhIjUhIOFz0TRJiHn4i2PInY5RTwkbwT8WhiHFYqRQzhcGS0xn1yVcGYwd3vlQXLPHe90FSay1zdo+uLhTs4iRP35uLWQdpKvHqKSGsp4Fl02fXCgTXYSscHH0GKtJDtTe/C5IrJUKTID7ifa4yt93vsNFj6Xg37pWx2Uxon1CqQGp5dmCKvCAqebMBIqd64m+tFasePlBcx9PZ0uVQtuVufhV6V465ipoIKtbO71CSYBBrcVYtI3mUYDus6EcLd5aBWFyYZ1mZohqQYHBRCGcIiN+LIxmglzEIjZ1a7U4t2B2C8vJHwEC0s5EJblFzu7iqteXHkLTGx9fOMwlPYhr2cAavhKGjIw1VLGnO4L29VVx+OW4xUl56vg/EtUlq1YphJ4y52gffEkutSOcazYtfHw6I43A+lHUT1chWRoq6Vy5SeDNjwIy5k6ESSHTWqo0KqW0UbJmYN+gHBx/A2Ztm3D2/zY+zXw+j/1rfU89PA/7GHks/nh+9fXj0eRYdu8Pmh6/N/z8y/fXir/RQY+XxA22Rd/Hp0+R8ez378V74GmSWOzy+I5+/ihvb9eX/rxvN/i3pLi6Br2nr82pRZ93ho/OHN65r5v2Q07868PZzPq/lJ+++d/f7AtS2/Vu4M+eMLzjwM0uft+TJ+PcP+8BaMILCp33wFuH4N62r2/fW9CnAZ+7T4hL799n8BnAcqMYImAAA= -->
