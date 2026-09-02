---
name: "rar-cowork-cookbook-adaptive-card-evaluate-supplier-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_evaluate_supplier_performance", "rar_sha256": "8040f20bd863cae186d15d0f2f3d0fe4122224d2190d30f62acec477a731e119", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_evaluate_supplier_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-evaluate-supplier-performance:7a5453d4a43b2b0bd28ce61e6b3d0a73ce76d18085669ddca246adb023fe4a32", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_evaluate_supplier_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_evaluate_supplier_performance_agent.py` is
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

Evaluate supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 8040f20bd863cae1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_evaluate_supplier_performance_agent.py` first:

```bash
python3 adaptive_card_evaluate_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_evaluate_supplier_performance_agent.py   # or on stdin
python3 adaptive_card_evaluate_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_evaluate_supplier_performance',
    "version": '2.0.0',
    "display_name": 'Evaluate supplier performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-evaluate-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '484c89491902034d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/evaluate-supplier-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-evaluate-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardEvaluateSupplierPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEvaluateSupplierPerformance'
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
    print(AdaptiveCardEvaluateSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjSJbuX2FiHrJqFBnsW7S12UULEkggECAJKssi2UFiE5uAuvXfryMpIjOnunqmeubhkhYRLO5nP9857p6/PdlNHeXl0+uT5tsZtLSTJI78ErIzD5rl17w8gz/52QE/kJtndRk7TZ2X1dPzk+dXbhkXdZxnYLpS5l7j+hVkQ6XfVLaT+BDn2eBz60Mzu/QgUdvKUJXZRRXlNZQHkN/aSWPXPlQ1RZHEgGvhl0Fepnbmgpe1XTcVBJ4hP3V8z4uzEIozyLOryMkBweoZfLDjBPwFY3TfTqsXIJbf2WmR+NXT6y+/Pj/F4P7p9bcnN7Er8OrpXaRRosWDv/Zgr3zjDugkdhaCCUUP7JOB54ds4JXnB++S/lT5SfAM/cd/nK92GVY/v37JoMf15Wn8t2syqI58qM7tqvY9yLUL24mTuO5fIC652n0FzFU3ZTYargLmzcKX+8xvlPIC+vv47ac7k5fQr3/68pQDEezR+F+efh4N8OWpbMb7l5FK8dPPL0l+9cuffv5Gp2qck+/WIzEg9cvb4/lBFgz8NjQOblz/Dqje3ez4X56+U2687nKPeoKZTy+nPM5+uhMuyrz1s9GOP/38Z2TdyHfPSVzV/y26v9wJR77tAZ0egv/8fDPyr9DkodAHzT9nWwC3/hVNwPB3ds/Qw1B/Rvtm//9EOokzkBPvFv+H5P7RhMnfoV/+VLd/NuEZCr48zf0EhHg55uAr9Nubpixmv3zyvr389OvvgPR/SUbLm9K9UXgDSREHflW/vf3yqbq9/vTrL5+aAsQayLu3pkz+Ec1/ZNcbnx8s+Bj1049zAX8jO2f5NYM+Ih36LS/+rfz9BdrbSex9e1+9Qt/ny3hNoFGJd6Z3E3yXMxWQ9Ts7/vz0O4CKDGjTuLfPIMv//d8hKXbLvMqDGtLcvKkh4OA6Tv1ReD2KK0h/JPVXbS1sNi+p9xUCb8d0BxBhN0kNLUsAUBDIh9HjowYA9r7+H/cGrJ/dB7DC9gOU3lyASm/vsPj2Dotv38Hi1xdIj4AEeRmHcWYn0I5TFMgO/aweed+ipGrSz+3IHogW3+FnNxNG6KmaxP8b9PUv8Hu7kX4p+lG1LxnwlQ0c6EG1nxZ5aZdx0kP2iF1OX/ufAfYCfCnzJHFs9wyNv5riZbTXIfKzhxVdUGf8zncbgPxJ7gIdghjg9TMIhCpPQLWoR9tW5zhJIC8ugeHysr8VJGD/15HY169fHVAFvmR3cMaheyGqYDDgQ2Do8+ei9IMkDqP6S+a7UQ59+u33T9D/hf7ZrBvxkYcC6sXNdCDAk3vtAtnapGBYBY2hAqDo5s3ffr/7ZJQuAzUM5FgcxP5tMqD2LTRGDe6OevcS0HkU0S8fnH60G3SNgF2guAbWAnlfPX/JRhI5GFpe48p/N+J98t30726/8xl9Uj1sCPwUlHl6G3uLytGZbl56L5AQQB+WAuoCv9ajR6O8qkEgF37m+Znbg5l2/c2FGajhFcilKuifoaYCqo6UvzqA9GicFACWXX+FpJkCal+egF+jgW7swew8i0fHP+L2/hoQKT+BGJu+k3iBZL8duwK7tIuotCv/Ni6w7xEBat77fEDchjL/Co3l3h99dMvyW+Qt/mmXod27jB87lS8NhqAE9P9HSzPqwC2Xu8WS0xdzaCHrO/MecGM/Nup/b+FAS3GjfMueb23GOyK9Y/WXLImBk8r+b/eRwS3G7mPu+NeUIIB23O5Gf8z28kY3rkGkjK4vyzG67S/Ze1F4BgYCfqpGfAMJfR7hIf9gOH59lzQCio7P3xoE6B6EY3KA8IaKxkliFwp837tlQh2VY549HALCxh+tDBLDjX7QCgLUQUgA+hAQIgbxCwrHzXQyyJfRzLfg/xgej21XcfevB4GE8l+gwxjfIEYryPFB7zSOAVb4dCMFpT6wMRDxw8JVZBd3YcYe+SGgPfoiT8cA+M4Dj48gVsfqA/h9JCKgCrC4Bra8AieAPOvunv2Q8+ErIGw6JsVt0o/ufugKfV+9/jYmI5DxW1kAbf0tfL8ZByB4mVY3UAIl+VyBdE/9RwCBSLjV+Jd7mb73AR+yvP5hYfDTX1s73Aqv8aPnXqGorovqFYbvxfG9Nr64eQqDGIkLv/qok5/HuvX5Pdc+v+fa5+9y7QcWd4u9Qn9NzB9IPOL7FUJfkBdk/LSJXX8M4McFrDL7PDU/E+PXL9nO/+buR0yMiAdQ2Ok/Cs/7EFB9wtIPx8H3QlSN9esKSuYN/26F5CMkHgkD4DULx6pZ5d8l8qjT6OC7/z5wGnzKxgrgjR1g6I/LpGQUv/KfXrMmSZ6fMjv1/9LyaARlEL7ALOPyCqQSMH4d+7enjzZrfPhxmXhLMoAOXv465hoogKAlfoY+uttn6H29cVvLZQ1YcP0ydtYjSzAU/PkY+7EGdfwnsNSr+2JU4b6IGhu6R6P9RyHGFAMSA2ivRlnec3bk+Aci4CYM/fKPRLa3Gzt5AAfA9rFsgmr9SPcKyOmBfgtAejumIcgsYLsGTPgjG8Cn9C8NKNTeqO43+31TK7/r8vvNDPV9Jfrb0zuAjPf3ruEeQGDCv9LkjdZ9L85vt68jpVsrdjP2ral9A4rGYxH+7lM4dhRv99B8egVA5D8/jSYtY9CpD7fF+NNdMKDRt3YYUACQ8rkamwoYZBagBEp9MWpzBnD4HYPxdezdxo83r3/aQ/83sOGVtkmCxD3CJnAHcxDHwxjXp1CfcnAPsWnc9WnKQxmEISmK9TzXxgjK9hwEwwOfsHEMyDN6N7Uf8sDo6BegyYfx/yct/tOdFCgwGEkBWgxCIAEGpGQo3LV9lAGykR54FQBpgUAoBi7Cw1AW8XAkoDDb9V2CpoEiqI+i7Ejv0Vne5Xt77+LfPXVHizcAtWk8So/Ztsu4NEp4LG1Tro8jDrAJiqEejfsIyeIBw/gEmP8x9eGt0Zl3E4whDZpK0NK1I5/fHt4fw5QiwMgVUQnc/ZrB7N6m8I3TRcfJQAWmcGIFUdvlW4yyEd7I4nhN05W23eFrp9dC1+IWVW+i3Ea48uJGsgdfjZh8R54zMtvQ8S5pZGRby0QinGZ0QXsu3G69zpTCdIp4FTakiT+jgFekOFnv86gv3LweOmW6AUUGtS5eselzcrMPC7qTMJuBYUb0E+1SL6iFZVGHXDaZQbJO6Imo2+Ow9hhEbPfS0YjzhPZYERPhQe7m5sHWykG2JFKjM7/j8hm7U+fHpUOc9LSdevDFnauUHzgVvB2s3m+Gks2sng0ynAgq1rCvu+1h38/aJYVdTlqS1Se5uwjDfuNL/Cn1FgPM7yM3wfNLrhGG5pzOhU+LuBNrZyGRr4ZOXbSLRi57hpQHgaQ3q+lFPfApT6/O/PVgFL3Gndaz3VFNPH259eyEv1yypXFp3M1FOx0dxA5h8mqtkZrlLzbJO023i8/6ND51yg6P/I5MJGxxEeStI/IusZh55q5xc/4QeKlAyrLeMcveP2ytueSqvEN4ljK3ZsyeFeRuTx3tuthGtnZeU+zBcAy1UFvHi8BKsFwpslksiyWZz1nXWy7kao3NTU82nf0Spc0zder7qJfPML5PEoAu+kUuuYMUTfxCUTVv2YhEH1eTJl/tGVRjaoushsZ3Q0SKZ6tNmZQknZmW6XgIX02qTMAlrI3Ncjlhs9TM9mi8rhbN/nCmlt0OpxLMsOrIrI4+T+8tTQxl12wGKUgFrsYueX8pkMLrgljRNWIxsOfBmfGR0svdVjDcY5WbVpyhi4M+qSaTcurVxt5eHBk8ifnYao5WnNO7605Qm4hk+wRTr7uEIZl9hYIfhDp4R++6K8qrTldnHhE3hXmklytCWPXc+cCehTg64DprkisdQwN/6LrQzcz20GuEJPIJ3E0ED0HORYyUCmxpQsn6yUFWzr0SrSPG2AomGjmLy3Y5P0yJqXDCgimzUbnlITv2iadGLXrBrwBv5u18t5Ty0hHxmbM1bDrsuWAt5Uxxtnd+b+ImKcQGly2JnVktp9PerGMrJ4aIcaaoQGfBrLpuW1pr0lMaeDohamt4JxPtOfA2qLLaYFLS8/G+OzFxCmfni2etuqOv45NspjqxKtpYg/cws3KUdo5Zs7OLo6ahlCi/Z8tyQ7jcML1Ektsg8aXUvKBLBPx0CLen2qQ4O5layCAz+NTcB35Bxh2IIeF84Xd7Zndlz3oVhkaYJbDHlrt1pWcTOlxZWU7JigJHvVhFYYvbZ23gJ6V79ijPM5ECJ3X3upldBKG2VbL30Tbzt0KWbEV5YzSRQPLBGS83XeHz3HyTztxcUtTJpOBir0OHTbe2ZGJtTXbK0dpbaxX2T2td3K2txYAKqMBf9tJBNOjjhlg0jUWZ6EKKtwfe6YUN7KeHzlEkZ8t0aS+W59llI6KGlR6lqhKtTtbo9KIWnttVIdEuEGx53ct0o5AULRwQ3JG2xiFFkxkbTdt2gBVSCmOfG5RSumxFlpnWHrnEdUobfKCAEs7mc6YgYdiGuQmi0LU2TQXXi+dLXarE1tHw9By03FZK1TWeCUqfXuSo284jnMaMqSuZjuBS8vSKL1SJ8jN63bZL3eyWFpWjC12LJ36rItsyWJ5x8jhJmbTHVe46MyNN4wx1dUidHqfCLIsrU3L6vuG4ZG2ou3ogrt5eiVNabDWzzlYHDj/ZoRNbC1teEPstI1xtnE05Q9K9ao+CxeoMESq0qdYKQRAB2k21jrHgZR5jXs5hygQnvY7M1gWll63cZgUQzLkSwI/hESk21Kakg70o7qpjcEm6mu1VN56xmt/QWTSwRSgDDKB5tl9zgh8MJDHRgZNJmAlmmynB+IFSmvsuxtfLMMTWHXMgU5Blm+mp0O2thOpZmkyvs+S4JjNjqU7bypz0S8Ml2XBxJPbqho0Eg+8Vp4nX2S7T+1MZztZaUhxyRZD6eX+azi3uREYBql72/rlD1XzDbeT1oJ6yhETI/YLGCma627ozdHAizZo6qkxvVAauBjc9uxq5MCaOcF1Vm1UjojqtXvRtill2uyYI+bCM2iKb9FMknKvyZHIu0wOAxy1ChG5reGl3mU8BQGxWu5ZxhXpz2NXwJqGt0HFSpJon3uIys8MtDlahUV64G1anL061ipbavA1Tn5xIoq1JjqWeuyjdiZqYelVyTFQ4PSHXI6eL+/MOR3LVLojLbGGKQ3XROlQ2KjV0TM/ntxv37F8l9UhM+NxEJ6feuAiEKwqHGVrtmaM8B/fiHuV3iKYl3FUvlujMvnL9/ERvss1WBvHRu4qkweplcbE4m/L2q/1lv6voOlMyHjlz631I1TnoiWjf4XfLAz49b3Treg6vc0Gm3frid8R037VWfMyXJUAJd2AcY0Gy7uB0uZZgnZse6MryTvsZkuioXcTVih32Wb0wTyieswtBjby0NPlDN1nQg6CLjr1ag9LBnxA6742Y0Y3drtp5YSEmnAEXBneYK30kynHBn1feojnM9TwR8n3cC+IQ7fhFj/X8rl/0J7ZGlD7PjBa2F4UgMfOe8oKJyUvLU10vvbnWX/dSoU5FF2/ta8g6RlrrSaYcVQ9nYN/Hm4XaU8XKKIQtyQEcoHR1tyqJpe9l5dkX/OSIUoU39+l0V7W71pIKR6mPkSIjC/W0q+bSsTSP87wLl4bPVYtl5uBFvzG1vRkMU6PYh0utiLZC3hwLzDNyCSHjfZ6FboGznV5GJWYxq2G+PIs2qsXCap+smynhd+k82RYLh8T1ZmuW5z1/PLKJIbFHdK2H/FxwrngwLWfu7JQeOco8XRK6koWsu0zXQ7VXTZpM7UIXJtxi63D1WegQ1hQRbX0kRZmIRQxtEBThsn1mTn1d4W0DrgizQyapIKNXxwgHLdsvsqa3l0aSzJldJ2VldlnsLmYnaXtRKLZ8lqtB61hH6hTG5kDpyVqhV9YszOT5Du9OJwkTgn6qt5Z5hXe5GxjlZcivXWbblTHjgi279i/7eMPUhYBkoNdkBjuauxno5zGwBkvx2WThoCsh1GMv2k98maJlc37SWTHCpNLmS59LmlOiayvVg3tNi2t18JdNguCH46lbD2d2uy4ytPSTtd/sq/S68qzFYTlUZiSv1XK3RUmdmk15epPM19EkTypLMA792jZTsSjTQS6n61w02yZEnMwKJHsRKISXXlyEKFerZX5Zu8mSpYzqIpxVkVqLl1mmbqvzBcEUjWmnGjkP1MhIj12+jg9CtGByd1vrQ7ItbTt1D1sFc/bz0Ci0Bd0H7kxAPdlac3y3tJcLPkhpAEXSdmLokq8XMn1YOotzBbubIDbMq1Nsut48DjYi1miWVeyMnxedramqMNUn+wsZrk82PUWmkdToS1w6xpI1UbtkIIOQprhhDWNMbWYUs2lk24j3YuyEHK5ciqmXio1lXZalMxHqZYLKU0491GHqFaE7x2tksNJCTnB/Ridz9mTq0iDC5/mC0ZxlvyOzZVGe9UZ1Q2LOFdSUsWeK2E/XYTMfJqbAz+UzgQyJjeA2nbr6ZbK6nDhLZdmVMat9VV0FCEMjvDQzTkchlLvUpWcd05w0AVn34rBbzUxtqWyCpTAXA8JKDlNnM6C4MCnTkkCa1RRlUGcz1fb18egspLCabSp4T2OJOjmwkrjD+0yJgbOdRNmisb2lDsSBcFYtvHQJdklT7a4uiRIsMJP0hCWwv5qd0BKnmslV2eRu6Q9eHhIHr/IXVEgQs5ld0GiHy1txv2vSvdE1x6m3YpaZADMANusBQzYgHJzDae8YvWouFmBxsiymho4kfd7C8oRjrR1F6fps08rkZCmf6EvKiqG5ivhWx0+Z3C68+IjKNq8YKVwjhIttT00o4N5xX1/oWrJn14mH7RMSvVrnk5/qOc0d6ZODTSqekleCBHteEFSmsub9ZeKV7MQMCErTcIYuT/jexSmRREQmFYeEmMIsF+qqgPMwuhEUZSbP11PHCSQRVzVNn4dUqPLT6fSKVep6PvAsV/ArUibCLVeKGXM8XzaeVDbDurOoDeeQaOq1O8SfRnPawMKLd73Ix03mdMNWUERvztFq7lnTI8ubDoHCStRzoHBvWWZXrJhN1DYNV8KCoGT9POfbpEbR+WTXGDWZ2Gq/N9fBypYJ5eCxjbnkhSnT8gh/ReggNmWdtutuqDewbMNLmDVZQ/CN5RHrZHN62Qir1KGORw6pRczDh4UOuufAvvrSzh84TCrOViOX5OSYtMmqVrbMTMRgw3CDLb2tTx58XmBX1SDWHsZqolmdYZPUipCemjZmuQk5E0rzlFAdLB7bbLsIOXk4zTuSp0XHTKJtWVypMgyK6+o038Rmw3MDPHW0LuowUOETcncwa0YjUTZfDarE21N7AjAw2nUDbMw70HBF2jIPUM7TZoeojbAGE/VVEl1VMWyus2KKe5RlblfhXKqji3gavE5Z72k3kvDVsCG2erQlzoNY1RhYzwerQEyaK+Yere02TlLr6mwsfdyYdlu/73N9OvWDHR0d86piGRlFN4HoHGCvWdTubLVIUbAUo1szMBF3bl4RbyI34nCYR+tTVB8nlLMlOp6gV1gbzlYzQFtMsQGfDTkrwaxA+6ntw/0kMRFJ1shGF6+efN6wSwfoEtEcV26poNqyok2ju3CnKmcTvuzOSpouVlNMxgspn1AWpV8YbLXeYlv2Gq/aXq7g4ASWJxP0qh4GZ9NMqB2NwukRBk5bwQ4J15uoV2VKwRS/J8NN2dK4LXXs7HToD3SJSj3r0TJ+WLBKzyqID4tBQHHxiikpHmM6e9KaS2JY9acTxyPmLNPyFvOqjk0mcrjfIicg4ZFW9j7nsUeaY+cIO/At1WxW+ITZd/NdFSTOeSEds1lgzT22sDqrxtJiWBqxnEV+FGeIj2xXahJOwushLFQrLpaTjbRSybq3tLYmSXeSlc6wBzBVn3CTXpiLqaNQK1o4WqQd7hBXOeV5eTmLNCnj6fzM8eeed1datNZnK7nfXpioVRzjJIcS4SaL81JJNKw1zoqW5Zk9pHk/IK7V7RncI5u6mgdtICya2dAmhxl82BimWcgyCvP9amIfWLRV+y1s9mfMnEuLrmVy8WhdBMvxLxNeEtXWaLMqRQKbOHLMUCShsuK8Urw6a5S/Et05UyO1mm6Pw3rWIpGYGv7OJUuSr5xzzdL2SjAmlVXJJwxbr0x8wvVa4S0227XKcU/PT7eT4KdXFKER7PlpPCp4bPj/i7vE4RAXbw+iYKHHPj/9721X3rcO3w8Ib9v/vu293ri//kvy/vr8VLoxkO2+xVwlTfjYrPxP27Sf/8Iu8kiov590j6ebXf1+lFLb4W2/O868pqrL/q3Kk+a22w380FTj/3+p3h7HD083VdNiPMv4QbVvW6t1/lbYo83jbDyy870YSPR4DB/HBM9PXg8cGrvVG06Rb35ZjDo/zqzGDd3x0Orp9/8HEyL9Iu4nAAA= -->
