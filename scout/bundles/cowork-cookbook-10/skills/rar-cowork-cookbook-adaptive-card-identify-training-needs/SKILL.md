---
name: "rar-cowork-cookbook-adaptive-card-identify-training-needs"
description: "Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_training_needs", "rar_sha256": "86548793362e6cd5a5dea31587aab1d7b6bdecfd2fb2824c0fcd5737ca428cb9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 86548793362e6cd5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_training_needs_agent.py` first:

```bash
python3 adaptive_card_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_training_needs_agent.py   # or on stdin
python3 adaptive_card_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_training_needs',
    "version": '2.0.0',
    "display_name": 'Identify training needs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d6a8de63b2a71f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardIdentifyTrainingNeeds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyTrainingNeeds'
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
    print(AdaptiveCardIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e5Oi2JbvV3Fy/qjuoSrl/agTHXERAUEUERCxq6OaNygveWPf/u53o2ZW1/TpmdMTE3Gtykxxb9Z7/dZaG397cdomLqqXzy964OQz0UnTJA6qmZP7M67oi+oC/hQXF/zMvCJvqsRtm6KqXz6++EHtVUnZJEUObt9Vhd96QT1zZlXQ1o6bBjPWd8ByF8w4p/Jnsq5uZ3XulHVcNLMinCV+kDdJOM6ayknyJI9meRD49axunKatZ2FRzYLMDXx/Wkryme/UsVsAUvVHsOAkKfgL9hiBk9WvQKBgcLIyDeqXzz//8vElAe9fPv/24qVODT56eRNmkkV6cjaejLcTX0AhdfIIbC1HYJMcXJdBBaTIwEd+EM6eVz/UQRp+nP3Hf1x6p4rqHz9/yWfP15eX6d++zWdNHMyawqmbwJ95Tum4SZo04+uMTXtnrIGJmrbKJ2PVwKR59Pq48xulopz9NK398GDyGgXND19eCiCCMxn8y8uPk+pfXqp2ev86USl/+PE1Lfqg+uHHb3Tq1j0HXjMRA1K/fn1eP8mCjd+2JuGd60+A6sO1bvDl5Q/KTa+H3JOe4M6X13OR5D88CJdV0QW5k3vBDz/+FVkvDrxLmtTNv0T35wfhOHB8oNNT8B8/3o38ywx6KvRO86/ZlsCtf0cTsP2N3cfZ01B/Rftu//9EOk1ykAdvFv+n5P7ZDdBPs5//Urf/6oaPs/DLyzJIQXBXU959nv32Vd/x3M8f/G8ffvjld0D6vyWjF23l3Sl8zZw8CYO6+fr15w/1/eMPv/z8oS1BrIGM+9pW6T+j+c/seufznQWfu374/l7A38wvedHns/dIn/1WlP9W/f46Ozhp4n/7vP48+2O+TC9oNinxxvRhgj/kTA1k/YMdf3z5HYBEDrRpvfsyyPJ///fZJvGqoi7CZqZ7RdvMgIObJAsm4Y04qWfg/5TbVQDsWicTyj32gfifPDxJDKDt1//j3cHzk/cEz7nzhJ+vHsCfr2/Q9/UN+r7eoe/X15kBiBdVEiW5k8727G73JXcisHliXFZBHVQdgBR3bIJPAIw+TW8mbPz1X6L/9U7qtRx/vQN88sCpPSdNGFW3afA66WnFQf7UygM1IRgCrwVc0sIDIoUJQNiPQP+6SAGyN5NN6kuSpjM/qYABimq80wZ2+zwR+/XXX12A21/yB6his0fRqOdgw7s4s0+fgG5hmkRx8yUPvLiYffjt9w+z/zv7r+66E5947ADCP70CJLzXGZBlbQa2AYcBFwMIuXvlt9+fFgZkclDlgA+TMAkeN4MovQT+m7n1FfsJJciZGwAzAxNnZVE190LUvM6kcPYuL2A6LU1YHhd1M/ODMsiB+T1Q12IHqPNuyRyUvRqEYh2OH2dtHdy5/upOHgIiZiDdnebX2YbbgcpRpODXJOZ9E7i5yBNg/vdgeHwOiFQf6tnijcTrbDvF5ax0KqeMK+fJI3QefgEV4+12QNwB5bb/kk91MphMdU+Sh3nAJmAZ7+nST5PPQfXPACL49Rvv+x5nqm/Gvc5VX/L6mQBONbnCAwUBMI3axJ/Kwj+eIQWqf5v6d/sBSSdKTy/4T6/cY1D6i95Af/QG33cWX1oURvDZ/+8WZJKbFcU9L7IGv5zxW2NvP+w5dU6T3R/NFmgE7pTvufOtOXiDljeE/ZKnCQiOavzHY+fdC889D9RqK2C0Pbu/0wfyA3tOdO8ROkVcVU2x7XzJ36D8IzDNHbeAk0A6g3CfouyN4bT6JmkMFJ2uv5X1u0eBDUEMgCicla2bgggJgblcx7sAqaopy56uAOEaTPbt48SLv9NqBqiDqAD0Z0CIBOQNgPu76bYFUBOYOayK7Nv2ZGqWyodn/RloTYPXmQUSZQqWGmQn6HimPcAKH+6kZlkAbAxEfLdwHTvlQ5ipm30K6Ey+KDIQv3/0wHPxW2jfZZnEB1QBwjbAlv2Et34wPDz7LufTV0DYbErG+03fu/up6+yPNecfX/K7jO8QD3I8vQfuN+PMQG5l9R1UJ4iqAcxkwTOAQCTcK/Pro7g+qve7LJ//1ML/8Pe6/Hu5NL/33OdZ3DRl/Xk+f5S4twr3CgBiDmIkKYP6vdp9mqrRp7cs+/SWZZ/uWfYd8YetPs/+noDfkXhG9ucZ8gq/wtOSknjBFLrPF7AH92lhf8Kn1S/5Pvjm6Gc0TBibjqC8vhecty2g6kRVEE2bHwWonupWD0rlHXGBK77k78HwTBUA6Hk0Vcu6+EMK3ysvcO3Dc++FASzlDeDtTx1bFEwDTTqJXwcvn/M2TT++5E4W/IuDzFQAQMgCg0wjEEgf0AQ1SXC/em+Ipovvh7h7YgFE8IvPU359nE3N68fZex/6cfY2GdznrbwFo9HPUw88sQRbwZ/3ve8Tohu8gHGsGctJ+Me4M7Vez5b4z0JMaQUkBkBeT7K85enE8U9EwJsoCqo/E1Hvb5z0CRYAz6cSnTRvKV4DOX3Q8AAY76bUA9kEQLIFN/yZDeBTBdcW1EJ/Uveb/b6pVTx0+f1uhuYxM/728gYaTx88+0OwHWTnp3qqhnMQqoAhuH4EFVj7n3WOTyIA60DTAqjQJIHTFINhJBqQnk84hB84GELQlOO4iE+5pOsHXuijoYvSKO7BIdhEYZTn4CjtuQyg94jPr1PdTybBUMfxaI9CcJ+hHNILMNjFvABBATUsgAkGC2k6wIGN3m+9AKB8avvQbjLlexM7WeWp9G8vLomDnSu8ltjHi5szB4c6KW4TH5mK9Fl0P3eMcB+rJOqaQalu45rydR/dpCSW2ePZNln9UnIpJ9mRT2ItxfeBdIFsGcoIoV/Ipl8iOU/mPE1n19FiE7yjvIAkirVUiGdsdxBWFWJSZurrggKqqcldb/h1bfnWTrB0V7FSuvR0sjJ2txGm5wlJlxfDudaXtayfTwe5ipzbPF8NiNnEHJI7ZycTLC1lhoGyKJcf08PS3YvmCQxq3Gkrt3y03fuFtLged/RQ3o56RjXuUiMhaK0cYGiurjqGWe0GRj1WB2auDmq75a+X0sn680nYdsb6WK1AY75lruuDbI+wcWF6hEbkc5BWeiuJkEleLR2B6P32KF684TJfxJzTZHCZ4s3xtB7sHXE4CnZuMjzNVNwavxqObbuWFR/oyuKJc6qnByuDlYtcYTzZXGGUEQp4pS41RglPltUeOFE5bMTgaq+YkyxuaWWQvRJdC/p4GHearl5EzoOFmLsc0M6nCl/ZYqtoJSM2ceHGJHLmI6lk3Jj2bh5hwjH1U/SCrXS9PKo5kdtXvtoOS8+17Pa6dgbpIJKto5HqDj0t7GsToejNFJtTe1Iv8MY30+voyvPMrhzGwtQCrQV7XBFEakSVLqpyLlsF2dqhmZgo5MtIx3QrNZKldeSJ1Mkn6bl0sCmfXtVMudmTo3s8iUc0LIlburIt3rWuTWlvzga61scaPV0butssb+U11RdOLXseH1qwaeHNrTc9aNuatz6/JYSpSNoRZZVl2A6DyptenqQ8ATrHa6BBHsMcR4wvr4TSEuediZA2lFs3RLzlCRv763N73NVilihxLXZyOf2MXW6mELZpFsuuRIgwKuZJfIzw4LagIpnvfKco9A6eo6pMQ02GwTcm9nb7tR9QCOssZerc7ilpv10jmOXHZDas1kzV6I5ch7Vs1JXfx9lS3BpeLRZLTQz5NhWFrBZEhctSMoVXu3XhDZF33GvsSmrBzONaojZYVbCSuGWEJa2qFRhf50Xi8ns4qduL2O/NZi8Ycl2Oo5qrnipfcdqUW8F0V/mtyg1pi1nFnCdkHg84TV0V+UlCN93gt/piCScO7uaZe0qV3B9Q9cD0SnIoTgPThbf59tavmkPPXi5uJ+ByHOrYUbh24ZnlN0tbjgWkNbaYsaZNfXOhbS4h0W10wPFqfcghJWqc+RUmhg6zpXZpWXvmKHd2uhjF7ZpVtGh9IH0qdPob6bqSv1tvDRGbw9AGGq51NcBZe7Q7yjksa/KIMtvrHN2ddSNK0LZBWVtiFUy/5genPBK1vz7UlVRUamuNvuWUrLQXkmvJ3cjtbq0Df7sa6bsXHXLSeckrNUf7m1CFKr0cypLPmV0oLaHD+iCcDLfCIqi4UXHI79BAFNxRklyGLCNENxG/jNWLXpWyqRsDkmZwG9ESct56SkkSZ3V9AQ5v++HW+2y2k8l5FRcI6bleKGoaamXaKdgtA104LM4CfBJPBmEYwyo3GqWv0MTCgkrM/QpXvGJQgi4UqD6s9rvjVaIrbrVe9qVMcujtUiyKAtoMI18sMVQvjOVyDAzeO0VbRzick9VNABUCXuTCGCY4BCGniIepFhE1b6dDQUfgg9dXh2zsaGRhEG4h4ixV2DLL4YZyEKqud2N9p7F7++z0nqxyuiBbErJYb5srFrvoHu44T+MWa/vgO/AAF1yZHeUVrZq1MgyWJa2bksvG40Lok9CpaZXDCZpH4qUmBzTO3bZ2MEJuHhCkL1OpTOSGBZ3C3Y2AoG4VryUQ0uetiZMQiem6eWqOQ8VVG+ayYi91e9bo22LOFBvh3GDoSql3/KDFS0pZ0e12swvxItCNOZ0vkVqjzW6Mr/DJP3YgDGVpodecmm6oPSHnasVxHeJcj4Z8ZTCQMHGt2rpvePyRHZvrQoOC3R6HIna+RHOxueZya4h+wQXoflle85hiAxbMD7Fkq3SfQ8BDNlpQZa7stRCFt82GZbwuOK6L2och35vLWxGv+WyUtJIqpctRsAzrkLWbSqXoypDd1sWTWmUsnl7I8rAlwyA9DdrRR6411ZqMZzc7x40rWNuOitqXFGYGJr7q4iz31sfTucqDZCls0or1mTZZqPCpYgwPs+kMzs4wi9B6oQjpxkJkohh3HkUabuLGq5izhZC+hbK1kdcuKZbpUNi0vwUpqwdxvZbmplYIJpJsOmuVtTsnSh1ua5d5m6+RZmP2YCCL9rR7CGDJ1F22PLDOpbeZ48XlFwQ5Oq24lldky1npSGh1zZVjZkh8FPRows/5Xl2nuJIrJ0HNxRHeXsWt3phtEB0HH7mglzNR8MbNOwhcNa7liiRoGisYz7000oHXss1SwS8ye1zl1TndputRhkZr1JLtsur8XI6do5bT1NKxY9DqiwcIs471SByzxHFSB4nYxjme0PUgCe2e3OxjjsAVR22JOc8UiQI35/1BMcjzHg3h09oIyuu1HrS6R4Qxlo9IFinI7tpft9ylGc9tZClCFY3Nfj0sV5wIGcywLumFFiw4fnCK5bwhGmmenddn0VqSjNr09RrWDKpA/eV+7A8bt1gcPCy3+oh2zczX0NMpNSCYDqDW7U7knFE0aWn4J5Nr12qzgaAbvO8p5bi7IOQqV8ee2W6VC4RmCLZD7XaAr9XQLJGyiPa2s9HWCVOtKTfmeFRgF310YnZ5eDkklzyaw/Gm3Caitrhsi6LrcoI0LphuCaco1MRSy5od6ZUXGFQOk9SiShCrS4ErO0k5YwdzY16LY2ciCxxx2gOPM2GA6Get6zYMuxXZW9wSwlHsxu2pVsoEpB+7O9lQoQlVM5iLZZ4RpAvCjz152cKV4rzEo2N5EXOo3OKJjCAtDMMs6dw8tlPypJFDdbPrfUEZrLTKRnUZqUfr5oxS1xiqqWyWVazTl83kMaHfL9b+RTqww7XQriVNGsuLb6mjOixC1YQX5Xk9Stm43fb7OIaWngQV3lZFTwaUryXY5kxKreoejIK6YLZjkGISJqR805VXeV5DuZbjrU30Lay0EWarIXrcq2dnhbrRAiyMtHYwD+25b2XFlrt0URqmf2ZWlu4EVRWz507ezAUTo5KszW87eMvPOepaAJwxz3wZ60uSC7r1itMknupE39wJfI+a5dDvHLi/eK1b4zy1kCqyaCD64hKX/TkkuZxsAqwgcTvmtMFzTptdpTeBydaxjtjubSEkPhFhWOcaXqFafATfZNSXR53Q1vlBCS6C7HMww+I1Fcr1ehBlVK4hKdqwlbGPXFKzbqKh5FkwNn6v9MamRDYw6roEr7uBSh/pVJLZ3ArPIpzRFSr7y8vRa7jVshwcp9ek2MAPV9wASYCwmLbftMGKEpc3cTNf2wZB7XprydKpt7L2je4HKzRLWXndpajN7W5BYreQSGbHIKky7KpUjaezuCgcjTJHfZFlsGDTHnJjOKEJxGx7nRRu81L1+EPCJSNMBof1SUdMnhPXK9xeLiL7kiyhMIKlap8drCjjeJcgT7Z1qxrbcOTFlVIdbXFYDWhLl/D6VlBZmNELg7tIwiCL0OqW9xs1N+2+3bdWwPW44QRjYdCyxpfEnj26h03JYniGx0xKUHKX6Im6kA8ww1zsMVmz8Qgqk344D8exTxdavYHWq+LWXWrKKmVKduMwrMMOWbF0e61HDLodqCN7QuBrSLH0zgVpKWBEx0TBsScOlI8mS1CdB9woxb1kXZpVh60CGBdMkrRuRk1k8aiyG3VPUyZVVXlZ7LI6aG/oFZOhfvQS6bZRuESX4f1Ih7RVc17SL81VzV0dKqwX4fp8O0d2z6xObEgu1c5bzNfrrAIYp4dZ06iKsqf2vAvRLXrm5qYV1bvcT10wQAsnaQd6l+DWmQusBu1QtfbONzqdQ+Eln0uLC3GIy/kJmicEE1h52wXkiQlsBBpDVwcjGeid2Z3iCzKhgijAU9g8KhVfXcTkBsU+nJxZo51f8nQJs1yeG+d4A/fzyIsNL6PN3KOkHDrKpI+P3VGqhN5rFy2LHgJB3OPqKsASxDTWYO5CiU61GWKfrHSDx7T6WhcVlIDJq5cw/MaqN6BMtKgrRugx5GgezjypoPQ+WN7qpoW0jnAInVBsMuJWGMqdO9RmfFhcFqe6EfrNzTwa+bnfVzatKmZIkaS8nyPdvBV3mxOfYegY9EteB/3emXSPGtnIqIvdNobtBxCC43YyRAsUL2713EKYuTLC67g95twivYXXlRdusSW0QyEwCC+2+0iGKMRuirWBmy7i7Pmlh1+OTaklxCiVzlklTvPVsRTATDHG0LFEiQyXDm5KBFeZwAJtWQz5Pl8lGs4TCrnY7tTeF7kwFtCdyueeTwwsfh70+hBqoM/CO7JOsZu9WZ0Hans677AoKNmizGumayIlohM1UTZpxumF2GByE9fFZjuK3LUOgf+03HS9WJrPYQROG6lZKEzvw0h9w/xuEBSv3II81OcCthmKNuhXp7DmCFBQD1zOOQSzgnZeMtLbHjjSJcRTh7nx7sjGg3HFRX4+Vqw0+suiR3yV6+Sbs4ydruhW7elGeVbCnM6YBi9SqQb9B0kyFQgntbUZ5AgGm52PtYh7scTCR0IBzHmZwizdXt/Gq4gtgssxdMkFhjKozGuieaY24ZkjVCsR85LcYvLmGl9PlBH01K4EVLd4tIpXLsZG9WqHJOicsti929ZzpCqx/BinLm0PEhiIqhi+rlJeQTtc1pDQCZC5i586cx0TmC8xKwpaeK5/yjHOraE5RipzelH79Vqlq1bCjnDlITE/aj6ulQlr09vDCWHQFdQOzaoAhXdzuJJEQsF6l0BCRbtZ5HC6ubqSkLRaDb253+2veOCeUfmYWUe88RnHHUDe3Hx/jqiSwDs2TbA8s2wxnF1cN+dY2Xj5dpsr+arYoyeuM9HLptHceXfSmZrhQsQuIoeXDY6k+mtYwkS0xP3dGS8rh15TxALJlwUrVDEXKJUmEKCp3QsHqPSJjROdYOIabzYdN9QxsglSQ8+dW0oKeYsbSUXudu2+2iznHY7I9CINHJpnYOs67Dn3qFzVFPf6hrqFUTLOT2M9xy1NOteHVAvO+v464pvADNcxdw1B0TkxyK0d4sioaC9gKc2wSSt30Wjgz8ZBixYqhiLcjkw0qEjOFWZAYm3LEARdjcyPT/u2wark0jYws6B3p6WZVtyFZdmffnr5+DIdTT8PmP/eo+TpuO9/7dTxcUD49sjpfrgcOP7nO6/Pf1OuXz6+VF4CpHqcsdZpGz0PI//TCeunf+lpxURifDynnZ6RDc3bsXzjRNNXjl6S3G/rphq/1kXa3g96P76A3Jm++1B/fR5ov9zVy8rpdPw7de7XGWA3PUn92hRfH6fMwcv0HYXpAVDgJ98uo+cB9McXfwROS7z6K0YSX4OqnLR+PgeZjmynByEvv/8/QEfouOYlAAA= -->
