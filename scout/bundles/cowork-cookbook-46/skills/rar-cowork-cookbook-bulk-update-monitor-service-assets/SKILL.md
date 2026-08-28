---
name: "rar-cowork-cookbook-bulk-update-monitor-service-assets"
description: "Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_service_assets", "rar_sha256": "d7c5f9e9f9f758283b9e51e97713e1cebddfecf324a4c8aef019d8494f406930", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Bulk Field Update — Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 d7c5f9e9f9f75828…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_service_assets_agent.py` first:

```bash
python3 bulk_update_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_service_assets_agent.py   # or on stdin
python3 bulk_update_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Bulk Field Update — Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_service_assets',
    "version": '2.0.1',
    "display_name": 'Monitor service assets Bulk Field Update',
    "description": 'Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77eaeda621d19829',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMonitorServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorServiceAssets'
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
    print(BulkUpdateMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjVpPuX2FqPtgeqksg9n7DEVcgISGxCQRIcjva7CBWsQo8/u9zkFTV9tjvvOMbN+Kqu7qFOCeXJzOfzIPq1xe7baKievn8ovt2Dq3tNI0jv4Ls3IO4oi+qBPxXJA74gdwib6rYaZuiql9eXzy/dqu4bOIiB9sXZZnGfg3ZkNOmCRTEfupBbenZjQ/ZblXUNZQVeQz2QrVfdbELPq5rv6mhyneLyquhoCoyoBeK87JtoDSum1eoj5sI8qrhU9XmUFn5Xez3kOMHReUDc7Isbt6AJf7NzsrUr18+//Tz60sM3r98/vXFTYECYBkL7DHuhkgPA/SH/sVdPdie2nkI1pUDQCIH16VfAQUZ+MjzA+h59X3tp8Er9B//kfR2FdY/fP6SQ8/Xl5fpjwYsbCIfagq7bnwPcu3SduI0boY3aJH29jB52rRVPmFUAyDz8O2x85ukooR+nO59/1DyFvrN919eCmCCPcH85eUHCOD35QWgAd6/TVLK7394S4ver77/4ZucunUuvttMwoDVb1+f10+xYOG3pXFw1/ojkPoIqON/efmdc9PrYffkJ9j58nYp4vz7h+CyKjo/t3PX//6HfybWjXw3mcL5v5L700Nw5Nse8Olp+A+vd5B/huCnQx8y/7naEoT173gClr+re4WeQP0z2Xf8/5voNM5B+r8j/pfi/moD/CP00z/17X/a8AoFX16Wfhp3IDuc1P8M/fpVV1fcT9953z787uffgOh/KUYv2sq9S/ia2Xkc+HXz9etP39X3j7/7+afv2hLkmm9nX9sq/SuZf4XrXc8fEHyu+v6Pe4F+I0/yos+hj0yHfi3Kf6t+e4NMO429b5/Xn6Hf18v0gqHJiXelDwh+VzM1sPV3OP7w8htgiBx407r326DK//3fISmeKKoIGkh3C8A+IMBNnPmT8YcoriHwd6ptQEB+VccA2Oc6kP9ThCeLiwD65f+4d8r85D4pczZx4dcHC3590t/XJ/19fdDfL2/QAUguqjiMczuFtIWqfsnt0M+bSSvgvGk94BNnaPxPgIk+TW8ASUK//GvhX+9y3srhlzuhxw+G0jhhYqe6Tf23yUMr8vOnPy7gX//muy1QkRYusCeIAbG+As/rIu0Au01o1EmcppAXA+YGOoe7bIDY50nYL7/84th19CV/0CkGPZpEPQMLPsyBPn0CjgVpHEbNl9x3owL67tffvoP+E/qfdt2FTzpU4N0zHsDCra7IEKivNgPLQKhAcAF53OPx629PeIGYHHQ1EL04mLrUtBnkZ+J771jrm8WnOUG+NxfQRIqqARwNgRYDCQH0YS9QOt2aWDwq6gby/NLPPT93ByDVBu58IJkXDVSDJKyD4RVqa/+u9Rensu8mZqDQ7eYXSOJU0DOKFPwzmXlfBDaDeAL4PzLh8TkQUn1XQ+y7iDdInjISKu3KLqPKfuoI7EdcQK943w6E21Du91/yqT36E1T38njAAxYBZNxnSD9NMb+3VxDY+l33fY09dbbDvcNVX/L6mfp25d+7ODBlgMI29qaG8I9nStVR0YJRYMIPWDpJekbBe0blnoPSX88GU++G+Pss8Wjh0Jd2jqA49P9t3JiMXazX2mq9OKyW0Eo+aKcHiNN4NIH9mKhA34fAvkfBfJsF3pnknVC/5GkMMqIa/vFYeYf+ueZBUm0FkNIW2l0+iDsAcZJ7T8spzarqjsOX/J25XwEod5oCkQE1DHJ8Sq13hdPdd0sjUKjT9bcu/kRnqmiQelDZOilIi8D3Pcd2E2BVNZXWMwYgR/2pzPoodqM/eAUB6SAVgHwIGBED1AG736GTC+AmqKo7+h/L4ykswAqvdYG1YP703yALVMeUITUIABhwpjUAhe/uoqDMBxgDEz8QriO7fBgzjaxPA+0pFkU25cTvIvC8+S2f77ZM5gOpNsgggGU/Mazn3x6R/bDzGStgbDZV4H3TH8P99BX6fYv5x5f8buMHqYPCTqfu/DtwIFBQWX1n0omXasAtmf9MIJAJ90b89uilj2b9YcvnP83p3/+9Uf7eHY0/Ru4zFDVNWX+ezR4d7b2hvYEqmIEciUu/vje3T4+a+/Qstk/PYvv0KLY/SH4A9Rn6e9b9QcQzrT9D6Bvyhky3RKBsytvnC4DBfWJPn/Dp7pdc879F+ZkKE6umA+imHy3mfQnoM2Hlh9PiR8upp07Vg+Z451gQhy/5RyY86wRQeB5O/bEufle/914L4voI20crALfyBuj2puks9KeTSzqZX/svn/M2TV9fcjvz/zcnlonvQbICNKaDDigcMO00sX+/+ph8pos/ntHuJQW4wCs+T5X1Ck1T6iv0MXC+Qu9HgPupKm/BGeinadidVIKl4L+PtR8HQMd/AYeuZignyx/nmmnGes6+fzZiKihgsetPPbz4qNBJ45+EgDdh6Fd/FqLc39jpkybqxp46cty8F3cN7PTAfPMKgdiBogN1BOixBRv+rAboqfxrC1qfN7n7Db9vbhUPX367w9A8Doe/vrzTxTMGz0EQLAd1+amemt8M5ClQCK4fGQXu/V+MiE8JgOLAgDKdSimXCBifCZiAIug5jTmMT6A+Q1Eo5qOu73he4LsBNsdt3KVtP0BQxqNxBg9whGSwyaJHZn599DQg0kcCH2PQueth5JwgcAal5jbj2Thl2x5C0xRCBR7oAt+2JoAfn64+XJtw/JhWJ0ieHv/64pA4WLnBa2HxeHEzxrRJTHTkyIErMljUFyZpqCKZe+j8St4wsooU+SLLWbU5UEfNXe5bPRF0W0hjrtmJqL87qYge1Al8w5Y1J+7kdNtSyoggo60vtN7dLFpslihXbiGwV0Yqk+bA7drd+oZUgo2apXZUr51mq7J7Pbh7zNe34vZIMbDm3bLWL830LKy8DR6CnJMH6tKnYYUWQcrrxVyzRL64sJVwUKKa6q+aXTaKJjhHm1gZ2bjRzta24xeYlaGrkrUzgxPmJGW0W1xlyVN95GG3OzSwHwy5cqRgBl7jMXYlCoVrTDMsz6neHMiNUNWrq7Gbo7y4kc7kWfdxs90OptkOiLhl9KVp6GuRMiXMtfmDaczYiCvaKyKkeCsiYW2KgEu4myGotLNb4bttKPSjJTWSqBn+Hk9Oplk2UsnZ8K2tdFkGYOywXG8KM3Bp0SWlIXP5xXjZ9fpBXNBDufP03tJjS7vs4Gg17BNH7aTz6nqKvLj2xNFWTvCCWG/FOjQMROTmc2vfz612Sc9N8TyTszo+5ycVTuLrJtcj8ypUhDeY4gKOztmBnq+Jdonvb6cEDa/zw96WTz66IxL8YKDDaJdi7TAng9XmFUJHen+M8PwSpvq6FZI+PCneZUGmWYxdUlXuSoJAllvZGDtMFKtjznDVxmnDJm+QflNtSy85B2c4qwvhkiGNkJRmxSHndd4kKGrXI18RvrDJD+ZxxaWnA14KM7mopNs2jwoCP7s3LFIxHrlqS06kOD7q0NMpp3eKM+5X7k2fr1VhtnaO5qjcdnXnjlfnkLHBOmiQFX0geE2J3Lmep3M5SlEmzlHv/pOapt/XDC/Nlo7XRluak2YrnM4ug65IgWB5u9WB2dwusaOOdTvjA2kZ48YO7brARddHpCqu8961NyOSUNXO5l0xbNFSSqKWjhQ6RuK1q55SpZ/Z6tjRA+8P1lBSi1gh7X25OQUu6fS8OPfPu9ORN/hzTCLaEmO3/lJg63Dk6tW4l26nDN94i2gRtd2Kz9nDQudHVbpdR5WPT4q2pmeJlfEILBzHUYzmS6e+eAougITnKJzat5ZaaMdomZT7XFKOFzjPYudM7Rwz6mh7c5qTt+NYsT7T0fLFapijFGu7im5IpUJL82ZXIm4vQvfabmjHKmUL5F2kL4bLEG7Jao+w5mUDl1aAtxIhykyJhxRlXeJIznax0RecTxa34Rgf7ZEUO73XE2zYnPtIIpt2HagztLoKJa2o/u52jmeyZFmX5nxGhgtsDMYWr7f6bsThuW1xpROg0UpkTCXl5iabytiB832VPS42Yx1FcAEHLH/TVwgS2RunA0e80bjQulMmZ+m2gOFQ0LdaujNUenkeBDwWyaXn5Juxy7Hd/GS6tCtaiWAm8zjFtXPHzdcrWsvEFXpbNOC8mWiludYWPJsgQmcImjfLl9f9MTseBnyfdYc1TXl8aThNtq0Dst6f7djPo64byWYsbi7MZqalIfV+E4o6dRXPqi3LVx10yguJb1KKmaE9vKFwyfEkbuk6IbXTzUVT47Cs7YM154JaYfuerbfXeObqMO6glcQWViEkGuB/STZXHJ+fYfHs9TvHXVWbbbvG/eA4UKdDaZjzuD0N6uF8bs94iCdcFEZ7M9p5ZyHB4Mte3qM5fRSQcMUuk4SN9bjpmcW8dIoSwwkaVXpW3BmadojSkL/eBidYueV4jgxJ0Llk36WZvru0kbmbqVznygpMOPskNGuvroX1WK6sG4i3atln3bZXZZ4fKZRuR5rxDSLe66JU2nTboYyRpOudB5/H3Yht2V7YjRXSbPEZ7K24vsXJS4PwnHDdjyNxMOLjgAy+mtB+MIOxLTES+9luF/bmzYdtKkkWC7g/kcYgL7PWGBqhvBgxbinX26GXm26D8nrcNSeWR3ZVdgzla3HVPNPSDUTVAyW8rDROAQmJXPFNIPksdlCX1WJL9mo8SPsjsXfs6FBeDpd1k+f5KTX2MHlmcSbt5X1GunGCYPXgurhS7sOdPVsEVCGu6i2qObmsZOLJlr3MGbAtv+99BNYWdMjtxZhJq9w+I5XcREvOPzNntorZC7eL1gHT3byK3+axfPVNylsOln5y9q0TDaHO6eV+sK2dt6FOs417qfWAo2+IFZYVqobpOLAxeRJi4iycLMlkz3mKCZqZb6iVJ8H1eq1HnNgcMANACLKOkFamXtSKgWvXBcF0xKE8FU3hSsKal47tLuKM/jzo25G3luZY7omZjO/ta7BNV5m5MxhtmcjzxTXc00sWL48FSL80o+lO2BOhY24Zt+SUc2rpRzte57J9dWIpdOYspwaXIG9dRxp2FhIl5/HUr7q4Tgi6gZFMAI2LyBC9FK5gGGMkbB+ODcY360g4VtjYOD7oIkpmltc0M/bVqWM25tWIDCLD+/VqWVxkl7y2Pu7hXsuJmHIw17vz7FCkW1ziV0Il0kblCTEI14zAFuxmxGtu3JuiWxAFT/f2alUZ+0KPtCze4GfeJPeCsr8kgWyzDCaRqTpq6f6iLsY2C2buak0ZM7vLV70r8Yd1vFCPMjnPRVRBytwwSzxLcB+e+UFpMbO5hC8SWzUiKuFm5K1ZspKndGN3bcSDxiftrF06W68aznXkLUtUjRynO9J9hXRCqCE77EgF84Wg6jwXLS2bHojIOe8ULa+XxPq0lpo9zdlLWhVlWEtQOZHPodiZV/6A4aVeHZTEVUv8Ilpr2WhN5LhFCkWmvFznUqVZiWjCyF06AJyqHrkaNs9s8mIBMJW22NaiEYu9yJEsaQieg/nNTQJ3z/Fz/BpG42igUioqnKEUoTsYIbY14o2mSjmzxwnyuHOsPNAtJ+EJieZLh+mjdlOWynbdxvj6sLymy1zbajsNiUrhTIp5z1oiJwjZlkPmdDb0KysxzdFdDZsTWXtJGUvwyfUOrVg54TmpkfMpCFNb9YXlpcmMWTnGzbA4WWNJSdtVpBT14JfpNpXzlZcXVwKrI2yfXSXGxI4WKGfOW6DwWT6RaVRg1FrBRQE+XkN9TOaNoViIMbtWcYKPG1tpU0RGjxvAGMkBOR661smMqwPr4SU8ng+rIe0TMAjs+jO/QHFqsT8JeKd7hpIu3LkRRbetNfarfcvT+JqKFgVaqVZb4AvR8pmq6H3DLhqjUqMVsY6woBB9kapzSWsuY4h6K5Q1G9xor/tkr5HVtmU3e1XC2ZO+3DbbAWHVpBsFgkDV5ZbnJW81nDXzSh92l0x0bLrn20I/m0vj0Gslk/rkWs9iDUMCL5b842Zroisy7OX1me/PN8Yi9SKpaY/sCNHQWbWGj+fGJbx6Tzq7YUyF4LhhqavGcyl7M8ZYuGriiTM0qadOZWcFi9NIx7lazWF2S7MlOquJo+WNSwVD8XjHS71wIZnESqjV1oNxedEwM1PtALj2mTXPc86kk+gmcUcG9NkixVyjBHMbqglrB8R3N16jbSTUsJKnRrZuTVRf8staYu3eW8eXwQWsXt0yxgqt3drZDrazzstG7YhtfMWVq8HSiy1S1xW2PYRU1sUeexZaDV+4K89fgIoMb7pnx1uCL8/4mUnlhtxG2m3NHlRS0im/Lue7NUUFa2xf+sq6xAdpvF0Hct4VxmqP8lvX0miUddYwamUUnRJyri7RubTeYXYODkQFHfAxg/scfM3nlMGo1UCZawaEvN14LFphi5YpvFz1jlQ6yIx2nt+6qlpziIk0mxZbhwiOagZpU/taUJZIgEstW52NqhBzr7aawm/z+XW+rejxygnZ6qJc1iyuLVxnth4XQaxVO+WomeYVna1nl+NGYjVWcNImvNTXQA4NLz6isr1VjWzWzHF3rlzaUMAYD0zy5tyWo6BTqN1A270y9J1+welUScXuNO8xC8c3OUnNYPqiwmHBpdY6Z9BxtsIQQvFJhuJzktnrTKpQqUyoJ9sWvDmpX3qX2cjsptcOLOPStBUgfLDan2ACA8O1kA4LBCddepFlG2STSE6CcQKeE9KMJjdRnpkknjoSw/fy9TpsxwJX/f427604O/e7TXvkqfGS76R+p5/WA5/y9SYwTucu09GAsVkySAOMpZNZ2JFwTLL+TQyZDlFDmtpRVSLCcLuH9blSLHiX2QcMPKhlu+i9pVwCJ1s7tnU3L7qN1rVmERCoSeazaoP5UuyO5awrhLRYFXXoqV3fKjB1HumxyYR2tBmvYE+31fHEN7fzxYaZlPSpW2eOduPhiiErtXeTsEDFMYdg5XrFK2zudEadCY16k414pQjWdi7kiAZO7XMBBmM2kVFXNRIWSxeN/a5sBQveHo5X3Pet04Z0WZyIths10k/UXrRviqqEx5UeNJtU3GwCN7BZGlmyVqh18ZrBDT0ITJz21WMyZMbosmSxTCzbnsNzrT2AyVpY9BkuL8Prxcvm3CEPqTG4xj1ImtX12jg5scRhM2Bto8d4dZxjSwucbxgvdjL84sw9HCF37TlnAxmXh/ZkDjeK2Fm7FTqQKr2mYaLrIqWJ0cHHlDZbH1t2GW9kDNl2YRXgvcfgo+nB3GZFdH6fmD1akWfi1sqWr9yY7rQYQos5G15DMn1Nbg6HdrhiZZZ2TG43w3JptK4XK2Jlc4GW0SvuhPYL4yhzKu9HnndsYm2xTHFY2xSUctHqy432F0zsbLtrGSBqLR1sJ1iKvsAW3hwuapFlCKfpWiWQ3ZakcNw/8v6sj3wG3ixVhgjm8n5WgOltdlE2VdUgQR8sG66yGpsqlsTSbairU+0OLt5iuDqr2+CEjCRdkes5FjazQOOGRURoRMzZEns4oSZlwudZvFn11+6kFSRfUZXQRTAj0ic/snXuxO90WMwpmjYJVtvJFoYlbtvi9OHgDTaFnsVloAVLU5gBVunbA6XulstCQ4K9oGpGsd3aF2eVHWp3Xq7LtqEsQty1DYPVpY8qZI7XxgXjjItCUqMSlAgRsrivLvGysmuRIlg0W4KKqSLOFy97nujYTOMN2FjTmXxASBddZOsg2s9tQvbTpd7ZY4rziY8vYxGXunlTSfysxc2dxKaz62LFkG1habBzFAuFmNW9jM1OYTzMTkM9w+1QvTQpqrUXXdsNuBxkARdx14BOjS2MjgrcRIfKdf0FtZ/ovnLm4W21PKj7kFVmqMGpZLwHEVyK2AEWAHXDMFGMmY+quUtt1FhqG5xmZ0rlBII9gNPG4scfX15fpofRz0fKf+O74ukZ3/+zR42Pp4LvXy/dHyf7tvf5ruvz3zHq59eXyo2BSY9HqnXahs/Hj//tgeqnf/21xLR/eHwFO30Tdmven783djj9EtFLnHtt3VTD17pI2/tD3VeAYD39QkP99fnw+uXuWFY293sfjkyyny40xdfnr2K8TL9zMH3D43vxY810GT6fM7++eAMIU+zWXzGS+OpX5eTt87sO4OT8DXlDX377L+AHJISsJQAA -->
