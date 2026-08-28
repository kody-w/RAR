---
name: "rar-cowork-cookbook-scheduled-brief-plan-fixed-assets"
description: "Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_fixed_assets", "rar_sha256": "0eeeec5fcdf94c85a2d18ec4ee67aa86c2604a7fbb27573ac483b7ca8aefe6db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_fixed_assets_agent.py` and in the RCI capsule.

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

Plan fixed assets Scheduled Email Brief — Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 0eeeec5fcdf94c85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_fixed_assets_agent.py` first:

```bash
python3 scheduled_brief_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_fixed_assets_agent.py   # or on stdin
python3 scheduled_brief_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Scheduled Email Brief — Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Plan fixed assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07817134cfef3a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefPlanFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanFixedAssets'
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
    print(ScheduledBriefPlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObWLbnV9Hk+8Ouh52A2N3REQMSAiGEJISQULnCZt93EEtNffe5SMp0VVf3666IiRjZGSng3LOf3zn3kr++mG0T5NXLl5eja2YzwUySMHCrmZk5s0Xe5VUMfuWxBX5mdp41VWi1TV7VL59eHLe2q7BowjybltuB67SJaSXuLM2rLMz8z1YVut7MTc0wmdVtmppVOIL7syIBorywd52ZWdduU8+8vJo1gTur3LrIszqcuORd5lZ/mwExoZ8B0iafVW02cwC3YQboO9eNk+EVaOL2Zlokbv3y5edfPr2E4PvLl19f7AQw/6GZ63CTOnsgezWJZu+SwWpwwwdkxQAckYHrwq2AOim45QDtn1cfazfxPs3++7/jzqz8+qcvX7PZ8/P1ZfqnAtUmC5rcrBugrW0WphUmYTO8ztikM4caGNe0VVbPzFkN/Jj5r4+VPzjlxezv07OPDyGvvtt8/PqSAxXMyctfX36a7P76AtwAvr9OXIqPP70meedWH3/6wadurci1m4kZ0Pr12/P6yRYQ/iANvbvUvwOuj3ha7teX3xk3fR56T3aClS+vUR5mHx+Miyq/uZmZ2e7Hn/4VW+B9O07CuvmP+P78YBy4pgNseir+06e7k3+ZQU+D3nn+a7FTjv0VSwD5m7hPs6ej/hXvu///gXUSZm797vF/yu6fLYD+Pvv5X9r2Py34NPO+vizdJLyB7ADl8mX267fjnl/8/MH5cfPDL78B1v+WzTFvK/vO4VtqZqHn1s23bz9/qO+3P/zy84e2ALnmmum3tkr+Gc9/5te7nD948En18Y9rgfxTFmeg2mfvmT77NS/+V/Xb60w3k9D5cb/+Mvt9vUwfaDYZ8Sb04YLf1UwNdP2dH396+Q0ARAasae37Y1Dl//Vfs21oV3mde83saOdtM+FME6bupLwWhPUM/H+gE/DrA5wedCD/pwhPGufe7Pv/tu+I+dl+IiZcv0HPtzsU3tPi2x34vj2A7/vrTAOM8yr0w8xMZiq733/NTN/NmkloAfDQrW4ATqyhcT8DIPo8fZmF2ez7v+X97c7mtRi+39E8fOCTulhP2FSDla+TfefAzZ7W2ACV3d61WyAhyW2gjhcCVP00oXKe3AC2Tb6o4zBJZk5YAcPzarjzBv76MjH7/v27ZdbB1+wBptjs0SFqGBC8qzP7/BnY5SWhHzRfM9cO8tmHX3/7MPs/s/9p1Z35JGMPrHtGA2goHXfKDFRXmwIyECgQWgAd92j8+tvTu4AN6CQzELvQC93HYpCdseu8ufoosp/nBDmzXOBi4N60yKtm6lRh8zpbe7N3fYHQ6dGE4UFeN6A5FW7muJk9AK4mMOfdk1nezGqQgrU3fJq1tXuX+t2qzLuKKShzs/k+2y72oGPkyVtzm4jA4jwLgfvfE+FxHzCpPtQz7o3F60yZ8nFWmJVZBJX5lOGZj7iATvG2HDA3Z5nbfc2m3uhOrroXx8M9gAh4xn6G9PMUc9DqQbfOnPpN9p3GnPqadu9v1desfia+WU2hsEEjAEL9NnSmdvC3Z0rVQd4mzt1/7qPDP6PgPKNyz8H9n+aB95494+/Tw711z762cwTFZ//fRo1JV1YQVF5gNX454xVNNR4+nEajydePaQo0/acYUC8/BoE3GHlD069ZEoKEqIa/PSjvnn/SPBCqrYAyKqve+YOwAx9OfO9ZOWVZVU35bH7N3mD7Ewj0HaNAYEAJxw9b3gROT980DUCdTtc/Wvg9ipUzFTTIvFnRWgnICs91Hcu0Y6BVNVXWMwYgRd2pyrogtIM/WDUD3EEmAP4zoEQIPA68e3edkgMzQUy8Kk9/kIfTYAS0cFobaAtmT/d1dgbFMUWgBhUJppuJBnjhw53VLHWBj4GK7x6uA7N4KDONq08FzSkWeQpy9vcReD78kc53XSb1AVfTMRvgy27CV8ftH5F91/MZK6BsOhXgfdEfw/20dfb7/vK3r9ldx3dIB3X9yNwfzpmBekrrO5BOsFQDaEnd9zx9dOHXRyN9dOp3Xb78aUb/+NfG+HtrPP0xcl9mQdMU9RcYfrSzt272CkABBjkSFm79o7M9Ku/zVGef73X2+VFnf2D88NOX2V9T7g8snln9ZYa+Iq/I9EgObXdK2+cH+GLxmTM+49PTr5nq/gjyMxMmTAX1bA3vDeaNBHQZv3L9ifjRcOqpT3WgNd4RFoTha/aeCM8yAQCe+VN3rPPfle+904KwPqL23gjAo6wBsp1pMvPdadOSTOrX7suXrE2STy+Zmbr/wWZlAnuQqsAZ0xYHlA0YdJrQvV+9Dz3TxR93Z/eCAkjg5F+muvp0x8VPs/dZ89Psbfq/76eyFmx/fp7m3EkkIAW/3mnft36W+wK2W81QTIo/tjTTePUce/+sxFROQGPbnRp4/l6fk8Q/MQFffN+t/sxkd/9iJk+QqBtzasdh81bab4n5aQZCB0oOVBEAxxYs+LMYIKdyyxb0PWcy94f/fpiVP2z57e6G5rEv/PXlDSyeMXjOgIAcVOXneup8MEhTIBBcPxIKPPvr0+GTAcA3MJwADogLPjbh2Y7H4DZNmHMHpV0bd12SMk2atOckgpuUZ1lziqAw08ZpzKJskzZB+yUdC/B75OW3qb+Hk1Iu4rkYg85tByPnBIEzKDU3GcfEAUMHoWkKoTwHtIAfS2MAjk9LH5ZNbnwfVCePPA3+9cUicUAp4vWafXwWMKObME5ZfSBCFwTqrx58uBwltSm2c1/vLq0+7kqDj5XzgB1cdkNJkn28tlHLDhdmFROitBBJbj8/epVCLQjp5MlXU+dPio3j4sWZOxm1V5BmddJU4lIHx2qvW8mhKapzWbtS0ugOfnbFBRpT+eHCXM3KPsEenIhnaVXktrZDN6dWgXcnvde1eWZiMXWBBJtZObaKWedKtaRznpjo1tT0fqu5SRlA8mWVMpuTaAorASvsiLOODOuR+5NjCXuJ2MkVxUC2d0F7s60qWtMdknFhbiHr84WeWpJ6PSrxfN4r1bVl9ohqxXayKarSv8KhPKZINWfUDRWaKy1trlRPU111FkQJ5zkBOzfLU+xexN5vEnl5SK/VmQhps+PwPi/PA5/t0KxsLFnR+KhXG/2couuTVDVzN9cic3lZt1d9fsSYS3NJo2OSpNc1tkVlTk1PcHfjETkzUhTszsp6fltzLE7MKRyR7AFdRY6VnZE9w4n+ZQdJDc6yQmEK+lkYqG5E/ME7N06G9soC0SMftsb9utXPaFhfsDOTHjATXevnVRuyVqkRqTpfZIZSMEhQ6dZZSyRNxJQ8Tocbk0mqP2+0sLY4dx+ATOfXm4zTWnOIr1vrLAN99Vs2nHCI6rt1eGXLTK93mFujvUBlchE5+4LsLFFaAmffVgOxdfF2rTYn6ohbguCe0ZXejicUPZyb/Tk1ZD0QI0kcGy5p5WO9KS99MmTQAt5dwopnGhs/1Ao0iqvtwSdvzqEc0b1h7/fMQG7aZL68KterK6u2YW0p+jbWfesb0SGx1rIAywfCCe1tWu0ETccE7RKTyICsZGbXLHhRpFcyrXEQv4TZIbLJU38M4ACgxDKD6dwjCjS0b6sFY1LYqDgJLTMbpl6lTUkbLRvHoUI0pmX4uHGAr62SR7EsbA90Rsc0xeyD+VAdO2yoKT9BhHMcVbHm2vVOjmvtuK2TOhdUyDap5bUz8iOpxOkxlhhpXZDreRcX/HWlOqNkhmV41jU9s1XrsJNKgtHldrUys8sYieNaydyUjqn1nL9JQqf0chaB/ofv0LXGUVzsw0sa7S1KiTOg5F6WR8dpL1syyeARKfp4a6/E9W0okXVLCXDcpzJGDunmwN4yCpRHWFinlKZ4RUAasiTRxbHQgwZGlhyD6aedp1akr44yVTpn9BiUWrwRFN1TTwmhIZvGXd+8JcaFYqHRGWavrZ21lyUKgy6lXIJBuu8E18eKhtTcfMtkHgs3V6m8KFLeH012hHWzHIcaxcukNuISIxbHkial5CQrm3GL8GLueqeV2vJhgl4TObJDDU4MmsIKXt5TrdAFyAE1EA+3sVglUKAv3kFWykN+X/Tusdf2lq+6A2kuA/SC7HBcI0TeUqqaN5eZTSOocdnpl4Oo5Gh9ov0xQtZUL2/60+aCYRFUppRerZiRWadp4cZ5aVqis+ApNVwhfrVpFsOGLgh2p3QXSpKvuUJpt5tzQYkdhYlwxaFeHcOI2OPLNS0tylxMmizTF5JGdtlaDffeVYgYekMQcl/kvLHS9V3nbVeDg/gr+rIiNhZFA7w+jG22JbgOxUaCWmlbfOHPzRSO7GSrQ+HFXwbL9drbLnQ3t21ITVeSqNLXcGvpXepL61MESoXPXcR0HJcWvcN6zvJGcVbQnBKPbD5czZhOxiRxWk4KSn1IrGt8GWrzRCCriyvQJK3ggqaUp9v5qnajCQULpF1SA3lkW02Oo0uveXu5hCAXS1byWggi5XJwPPhmH08ueFodqy2FZ2xYxlGhmou9Rx3zC2Yv+548c3h54AiGgW+LMSAYOi0xHQr2hOkGCy/Zn1Y65kKWFcQ8h/oBUkRHUTmhiaFq+rFibNLEm3SPIu6KURd5NRd8vvZXlzPD4Qy0xyA2wx2+PteWnRILwR8NPQ6Wo3sMFltGDXbOKVjNi4IsPXRr+CczkKF9Dll0R6N7T/elBTlot3zVCuqRuq3s46adS/TpwMc5rOyjRSQ25bVgei3THPLQ+sfb1RKyIuA678SJ7LCVzkySXzg3GXc05kvVzrJ9Wj0RfnTVTtc1t2QKJ2vmgWwM8DlDnQVoTHTA3WxyG+3rJdUfiTaQlp7dnloJ0phR6ZdIrfAZeYJ5SAybjj5gx+MV+INXZfKmM/RAIPtrvjIkX1gIeqbhCBEdNJ7F1ycN05sUS4WFePThqaAvdSmM21PGLDEkMFMu9esS7L4bED5+SWM6j28IqwZDups6LBu53fbAw/xAb3Rc8qsrSOczjexpYTwmx8BmsxCylMYRZFZ2z4cllx+D1XaEYsgUh2tab3bxOjQxgSVozckyrgMTBwDEtbvRpasxLAJhz5I8OsprGXI4Znto52N1xqRMpq8aNs9DxW2Ejj07FU/wbBRgMR3zmuTSCdJWPXRYrhYyUkUSuqbIWO095LqR3WtZlL3sCocgjAh9t2SzRkd7n0wlZVRlJpjr50zcsMjxcixYW9tXi+pscwsS3gwV0dqM7CFRXPi5r1QFCq9CtDNdZrePr7vNohj5/HjhiD2e7ri4z05Nc9ZPq2gvZjk0Ms5tv8FYvT/Q1fVsiE643FtrwV71W9bac4XStrV3lklCuRWwJyuhHF53BVMZjJCfuEoTtquYCzD4cuFyebOND2zNCPRY7FDdrnpDhNag2RlBjBsasbmMJN2a7uI6BLkuMcdyu5G0NpKPNnwZFmG8Nsdjuc50tGo53CHPi4QDGDoYXHrDknNwQtLRblErpPbxqfBr/nBLboTq72z+eLarNN2U3PLSi5iwVNzdiud3UL1BdtoOP7BUvQkP0cVkffEiKxmjWsRGk61rlR/PVqIULIwSGtQFqTCcMl6Yx1eWVXyk9xMFVw9CaufnwwZZMHRnlORpveorv1Xi/OD1BKO1Or/SpEUi6lXtN+F5GWvLFA+DhUhHWr7Ybm8db2aEMNijmaCocuIaLtKoXI7RQr/NVztFWEpdkvDOTSp7uIZSM17qi2q7bg/QceeV1dBRfW90AkJj+6WQ3hJxc24J+0itGqjcb4Rksy9JLNJuihtyPDScm9VVhNNa357h0lgzVtMuNiRx3KuNdTS68ah08YLbUUVEcmgOjE6k1vTO690BIuajn/DL8XKzzo4d5HU/7kwAf4JjqTd8kaW4GFNRaJ7alPTLnjxBrRD7ElFSOZuRK/La6RvlxoaWZhvbHT+cMBFyJPY4npQs4eN4kHf2uUHJsW9p1apOO+6M1pafR8gmUVbz2tiPS+MwHASKVJHwtN2HSjSEfeX0USHgjHkjLpdjsrgyUHYljpYXxuElOPKVpy250UCFYcUOp32zce3rzXd8XpOzZN4bdB/th/wEZRXOleyOuqhYbMeZV4xFoZ7w9RV3hUaWCuO2O1rJnIwozCtl42qHQxcuqJof4Z22cbnbsmvH/FgTquZGy+DWRXwBx9F2YWVLVS3KrLGS8/UYbKglmwvcYGxuUse6Yd2uyHHBHcbrbg/yupHnAQUUiwIyX599dtshixzOeQ5by+lyqS2SnC9Vu55n517YnSTHWBjGRb8E9I4nm/KgLDeqe6HXvVm3rYeppwMGY4eVs9LY3L9ELLyHWqo8z42TaggSCW3G6gYRY0yh0nZM894w6AG7DgeDMbfR8hoNjE5VBbFCGOhm+j5uV01OjZTIEQ5Pz2/bK9hahrjQ0nS7WFuWOtSR5/SWrq7VrOkqR2hOXZsIyH5J5Wja92qniJvEtmyyweZqVpV9GbXmbYsnK05Q00Ff0evhRszNcMMgI3/IMY7Eyzkzv23gc4CPDdvxZ1wG+zO8GS02x8G8iQWhsoPng74TRRXragvSQixzqf2uS5VsmVkucxCvPpi890t8bQcOFdArcn8Tc1iCYYg9wf6qXjlJBRMwvBqHRXJzbIaoSKhz1ZgjE+W0N8zmQC0RPYtNTaBUGewd16GEbaJVNnKrq8KvCwpS1VOTsCecskFWxRLEEVpKKHi1M2Apcy5XqObnN8ymkthoVFNpSWfTaoi9W54rXd/mzjLTCZfOV91FZKSt7Cy6coj2JCth43ruRUiJblpqy2Kxh48CQZJRvU4rps13vg1bVG4sIL09OWhsHsfzgVS3W7DLr6mO6K52IJTQxbjw2pxYZ7knqvVOK7yExEgKrsRSFeUwJPtxzl7rhURt94njLEmw3d166TopUVK8aEEox+zSCqPdSFMXjG4ro1zjbbtdjmk3nuzrUYSqQNvXRs8fLnjhtEy0skIDXpHiIekXOGYcvaOJVIoBBo4evqSGUIs+x2Ijgrl9uzghhJeVqe2g+Bo3RyQKx7W9MND5SbmtunzJIrjjOGMg306ti9sSkZ93t3xn8soIVRLG5OKyx5mw3RueyUKxkAutvZNSpV2GPN7V/ekgCUtz129rsU47Ibc3w8hsS2Xp9FnEIxS0k6MNGUHchRRIW/SittFDaU6P1k5t43Sz2+plE5xE63Y2yE4jkODGEn0gwkyt5TuUTgPtjO+ZeC5261M5NqnFGwIMNvomZAeG0TlAAHu19F5MYKxyLRI+i4ZLQvRmveqQeWadl3TlBEA7bxEMFlFBYgsfwmQQuMo5X9aEK3YqqBs/HPktFybUQemtPLqcb9vjhqUjEULcaKgEZfAigtDItZ1C+fXmWN1OKR173eAHIcIoMvUhRZh3vccMc8qiWex4826LEOv60IcxWIyq836zxmqs2/UphC0rWvJHr3CWh7bcWnuMCvCWRMWbgttQhJFLmNZigyZuTtauMQy52beAH1QHVcHghuJgk1RatEU342qnNnrfu5GfVjezhJaUehu9bnlgNbY4Yr0NQ20IUE/aLUbbLQYck/Hcai3PlaWraMr4utjzbb1c6tsDbhhCKHIj5zMS68t1pxiuwQXZ1d/cNItdEMtbj6Zyj2HSto9KNeeSfJnDiUXuxdOWwy44vDhSVejSEcMUxHoxdBy26PBz2107KNosNxxdKblg8FeEGiR255nNjSsWNnFTd2imaImYD2NUUSU1WlQXQTTNq/3ZweTugqBmlLbakXAK8hZtK5fEcHnrzdlKw9i5nFOJc8r0wmgM+9yWGHNgdRHSA5uiCMwgyihbOi3bH3jari4FdTBCqUjrw6YdkeAo4iEBhu+rhBewgMk21d5InoiQLenQNm0bCbq/xZeziStjihcsy/795dPLdAz9PEz+z18RT8d7/89OGR8Hgm+vle4Hya7pfLnL+vIXdPrl00tlh0Cjx1lqnbT+8+DxH05SP//btxHT8uHx3nV6/9U3b8fujelPfzb0EmZOWzfV8K3Ok/Z+mPvpxWrr6W8Y6m/PQ+uXu1lpMZ2A/4MZ4I5p30+SvzX5Nyesi7x2X6Y/NZje7bhOaDZvl/7zjPnTizOAOIV2/Q0jiW9uVUwGP19zADvnr8gr+vLb/wVQ8tH3oiUAAA== -->
