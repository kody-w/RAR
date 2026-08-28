---
name: "rar-cowork-cookbook-configure-track-project-fees"
description: "Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_project_fees", "rar_sha256": "97dae94ae66e2a55ebe42c4794dfa0721a2557e1594718b7711c184ecdc04bc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `configure_track_project_fees_agent.py` and in the RCI capsule.

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

Track project fees Configuration Bulk Setup — Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 97dae94ae66e2a55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_project_fees_agent.py` first:

```bash
python3 configure_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_project_fees_agent.py   # or on stdin
python3 configure_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Configuration Bulk Setup — Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_project_fees',
    "version": '2.0.0',
    "display_name": 'Track project fees Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94e234b33eb0c408',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureTrackProjectFees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackProjectFees'
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
    print(ConfigureTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZObSJb/KmztH3av7EIIBMITE7EICQECgTh00O5wcySHuC8h6O3vvomkKre3Z2ZnIjZiZVeUgJfvfr/3MqnfXuy2CfPq5cuLDuwM2dhJEoWgQuzMQ9i8y6sY/spjB/4gbp41VeS0TV7VL59ePFC7VVQ0UZ7B5UxRJBGoERtx2uRO60dBW9njY8QN7SwASJMjTWW7MVJU+QW4DeIDuMKv8hTKQ6KsaBtkfXNBgvhRAj4hXdSEyNVOIu/BZlSqypPEGXnUbVHkVfMKNQE3Oy0SUL98+fmXTy8R/P7y5bcXN7FreOuFfaoCjFG2+hDNQclwZQL1giRFD52QwesCVH5epfCWB3zkefWxBon/CfmP/4g7uwrqn758zZDn5+vL+E9rM6QJR/vsugEe4tqF7URJ1PSvCJN0dl8jFWjaKhvdU0MfZsHrY+V3TnmB/HV89vEh5DUAzcevLzlU4W7715efkLyC8qp2/P46cik+/vSa5B2oPv70nU/dOnfXQmZQ69dvz+snW0j4nTTy71L/Crk+YumAry9/MG78PPQe7YQrX14veZR9fDCGMbyCzM5c8PGnv8fWDYEbJ1Hd/FN8f34wDoHtQZueiv/06e7kX5DJ06B3nn9fbAHD+q9YAsnfxH1Cno76e7zv/v8frJMog3n85vG/ye5vLZj8Ffn579r2jxZ8QvyvLyuQRFeYHU4CviC/fdPVNfvzB+/7zQ+//A5Z/69s9Lyt3DuHb6mdRT6om2/ffv5Q329/+OXnD20Bcw3Y6be2Sv4Wz7/l17ucHzz4pPr441oo38ziLO8y5D3Tkd/y4t+q31+Rw1j43+/XX5A/1sv4mSCjEW9CHy74Q83UUNc/+PGnl98hOGTQmta9P4ZV/u//jsiRW+V17jeI7uYQgGCAmygFo/JGGNUI/D/WdgWgX+sIOvZJ98SwUePcR379T/eOlp/dJ1qibwgIvt0x79uT/tuIeb++IgbkmVdREGV2gmiMqn7N7ABkzSivqEANqitEEqdvwGeIQZ/HLxAhkV//Edtvdw6vRf/rHSqjBypprDAiUt0m4HW06hiC7GmDC2EX3IDbQuZJ7toP4K0/QWvrPLlCRBs9UMdRkiBeVEE5edU/YLjNvozMfv31V8euw6/ZA0Jx5NETahQSvKuDfP4MTfKTKAibrxlwwxz58NvvH5D/Qv7RqjvzUYYKcfwZA6ihqCs7BNZUm0IyGB4YUAgY9xj89vvTsZBNBpsYjFjkj01pXAxzMgbem5d1nvk8m5OIA6B3oWfTsZdAXEai5hURfORdXyh0fDQid5jXDeKBAmQeyNwecrWhOe+ezPIGqWHi1X7/CWlrcJf6q1PZdxVTWNx28ysisyrsE3kyNsPq2Tfg4jyLoPvfc+BxHzKpPtTI8o3FK7IbsxAp7Mouwsp+yvDtR1xgf3hbDpnbSAa6r9nYDcHoqntJPNwDiaBn3GdIP48xhw07hfXv1W+y7zT22M2Me1ervmb1M93tagyFC+EfCg1a2J1hE/jLM6XqMG8T7+4/qOnI6RkF7xmVew4afx4D2B8mhuU4ROgQNArkazubYgTy/zZgjPoym4223jDGeoWsd4Z2fvhxHIhGfz9mKNjuEZhMj5r5PgK8Acgbjn7NkggmRdX/5UF59/6T5oFNsLg9CAnanT8MPfTjyPeemWOmVdXdD1+zN8D+BJ1yRydoAixjmOajJ94Ejk/fNA1hrY7X35v3PZKVN5oOsw8pWieBmQH95t2d0ITVWF3PGMA0BWOldWHkhj9YhUDuMBsgfwQqEcF6gaB+d90uh2bCwrpH4Z08GkciqIXXulBbOHGCV+QIC2RMkhpWJZxrRhrohQ93VkgKoI+hiu8erkO7eCgzDqlPBe0xFnkK8/aPEXg+/J7Sd11G9SFXG8Ye+rIb4dUDt0dk3/V8xgoqm45FeF/0Y7iftiJ/7Cx/+ZrddXxHdFjbydiU/+AcBNZUWt9TboSmGsJLCp4JBDPh3n9fHy300aPfdfnyp8n84782vN+bovlj5L4gYdMU9RcUfTSytz72CoEBhTkSFaD+3tM+38vs87PMPo9l9gPPh4u+IP+aXj+weCb0FwR7nb5Ox0dS5IIxY58f6Ab28/L8mRiffs008D2+zyQYITXpYRN97y9vJLDJBBUIRuJHv6nHNtXBzngHWBiBr9l7Djwr5IExsDnW+R8q995oYUQfAXvvA/BR1kDZ3jiOBWDcpSSj+jV4+ZK1SfLpJbNT8L/sTkachxkKHTHuZ6Cz4WTTROB+9T7ljBc/bsXudQQBwMu/jOX0CRkn0k/I+3D5CXkb9++bp6yF+52fx8F2FAlJ4a932vd9ngNe4N6q6YtR6cceZpynnnPun5UYqwhq7IKxd+fvZTlK/BMT+CUIQPVnJsr9i508saFu7LETR81bRddQT68dkRyGDVYaLB6IiS1c8GcxUE4Fyha2PG8097v/vpuVP2z5/e6G5rER/O3lDSOeMXgOfZAcFuPnemx6KExRKBBeP5IJPvuXxsHnWohocCSBi2nKswFN2IAkwcyez4EDiJlLUDTh+faUmmGQbk4BbE4TFLZwKArDXGxBANdzp4TjUpDfIx2/jV09GvWZ2ba7cCmM8GjKJl2ATx3cBdgM8ygcTOc07i8WgICueV8aQzh8GvkwavTg+2Q6OuNp628vDklASp6oBebxYVH6YDsn1bmF/GRI6JtmzPd6fBFqD1N0DHhboapBZM1UUXKMtRPmjB/oHLEmQsYVxOxgs2dUqBbdlTRUKsQAy0m9TvpGZAJxuxsA3pATtWqCNaNfGvIgV7GmpQVtmnnKmYntplkfJrhZbGdYvzgdvdM5lg7ekZsos9NpcRDN497WOGndiMt6qp+rVJ8cSqHPvSZu9Uo+yqFLSpNim0mYdGDPRyWRDddWqsSJjqlJeJt5muUXzeJCWT3eALe1m263KuYLIC0o+STOqN31tsuqZuKioSI1erFeJxBFBNCUlll4jmuwyVa0bb3Wj254ttC97GNmUAWNk5hlq81T6KekzS4Juy7lkDE33oE/FmbGTdyaqgt3fuiPN4w7lydOi06i3oSNaM9PUegYNru3sYO9viyGXjvM9t1158K7vZTqXnxA94N/2hbePI+hVomSespUyxrvVoQ7qEuFV5gTxJLUunO5OmtOZJVHA/MsermKTpuJ0AgC2y6UOg0XBdjQ3fU0VF6z0AnbTjo/ybOYVxI9PG4pDPTr9Ogdb5tq2HX7lU2gVmxFlb1yvN2+xMp5TOj721w7SmKcoVY0rTDPJSu9OySCn5WawhbMmWIPqjTdz6ZZ6ZeZs4u38wW+yjV3j54UaXdNacNfO6nblrvpZENxNQQu22qbLD3fwtmauOSJlMwqEbWMEq1TMcHqimL725W8iNpUzPcc2t+4o75JFbbKwmLggIy6JzYk5PzqCvoGLS6XWNjLpzY/wxmgEU6XyZlujjK1KctaUi45oePFhfCPXITFfsdy0xzQ+jqZF/1+jdH79bTI1bzOTlZKtEpMZmo3XGrjRNhqF3vnyeGcRcVgoIS8NUrPR4clHdUnrQVlTbazVvemzvo4WRswbw6qnQvnLHaTtBQ1jneWncOFV0IWrdt2k0wwrgIaIUkCfmZjdA9zbL4KM20WZPiAcwZ7jtKry+tldyTESXcQbFLO7VgYolq/tUtcE/dbp1KWRmd260Lvt9tzM4TLml9TAPTUiSWvQWXNd8V5bijr5doRrttNJAf7M4Va5Xw1U/tzsqtpwzk3slNuNxMTxLhoc25SYZRKX3Un0m5o7ES+eOMbv64mhn6++slG4fwOtZ1eLOsiU/n1sFFsopXtHisUl7uC3FZJchsZ5LRAN8psPzsKYLux9q1rzvvqsJCylCJPxuo6s5yUETPvkvcWOtls034jT+gDk+UJ6bhTCSMBVhY+SSSFc8yneXW9xKGHDSnYMXoyqbJj4Wy1vkQLcFWPvnBgs7o2NsIMLLGJNrnh3LSt1jfTCHRjYTh0Sa6FAp3YglZoVWiqU6nIxaInt2tvV3OD6SsyQVSakGRNcL6GO+4Y6y1FyKY47RNWqGLWJuPhNiitZ1k6Ft+kq7kKPYtf7fd+eNL3c2kWrDYL1E+qo+1tWkVttoVJa8edgOGkVZ03q4vK1yU5CJcuAIaF00YuUqJ1PekRLtIaPZsvUDz243LA65ZILixNsWdFlOMSxdo01p0bheUpf2pDmotDzTpyutykRG467GGjdOoGaMdpx1ZDQHMHFBV4Rrjhy8i82odDj/ph0K/SRJLnp6JcpN0QzN2ltEwJhViKrWnl6PKa5NusGdbWUbqKN/0ksmADW211bvrjzPIi9rLfJ4zQTys9nm5IPb/dzs7+wimEy8bL07okHHGe9vnZxGvMOzvhbcCXkrxNLrsi5IakIhP+MG3T0z4fgmGh8R4NLk5CelnVo0rEnvZxtbY9GltsEj8y3QQXL37F7+cUL+St7xn7cKAt2CyoLN3gcSfOe24Cq89Ts9pSs/JCmL40nVoTOkfD3d5qYgAAFSVTVtknZKGw3E6mEys8JlqFncmtocQ7MW3xeBqTUXpxd1y8ydNToOjn9OAdZoYZsXsfTOm1GzuybYulOSHM7cnbbj2QOHHVmsdEtlzPXIklU7qDKaK7+YWYl7eM6Gdsw3PpdCUlpnU+87upRRAZdH9/mkRiM1MtQokIODQaLr+cFkewywTpaOOLacya4VxmIEzl/YEqpK0q4QJhHGW7vmFdfVtGZaSmyglWD63VyakhFVHfeYcoMHl7bRdsgHGeG6+vVggpdjeGlNo4EPPL2qBgMbgMwQztVcgljYOd6BTblDkJ5fORO97OnVhrMuPTuieewRGL2osxQR2lPl1rf3UJyXButZt5kzqlGZG52LgTQuy4riSiBve89qCJxBpfHtUdSCr7LBK1jHEDelqs5ls7VOJbeT7ehgOpRatzttyeDsbulPjcsF/ErUmRUU6KJZucu/oCmAOzvjKTfpv0W8OzyFpd0etiugklfr/h+JuG2fGMKMPlaepHQsxvV6w9OfrGjnLxrcXr60YYOpX1NgJjbNvZGT9UYuSzibRbw8hdKQVjuyTe0cqGNvftzEjO5raSphZeDbqWxmaSq/TxELlRbpPU9Bisi4sKBz22sG9Lsl9f8p3JqQvDpJVynQnEKdiy1Q26vi6aVaRePAGdeUm0JwXFSFbeEroMzGXMFNfx3kojUliVlMCtGCOWj0k1HDleRyeCyO63zXI1tXFwkw4SfzrU1OaSZeW+08V4AJ6rr7QGFInMYB2e9lPVQ1U8q4rb1p1w23hdrZwpQVHX8KTU3lEx8NzzqGGJlZPWkEoLD2EP1eXMnCRYSys6SxnxYrkOOtr3JmtxPz0zwnllnzc4yztwdFF3ARAuptiUnBKSak7UuAWj5p+xmLUuZ7HR4oMs5hmtZP0kzBJnzWwP3hLz7CIAK9/emxfsKvmK7eHb0C1yLWHnpqLa6K0Xll25mpBU3OytQFznZ94gvSgQJ4bXZQO/CnWFj3OZljNju1ovDKaNmc6NvGSRGIOImooMkijtz5Io7frNIgJsV6CEZqzmrBFdnL3cBzwpz0ojIXR/W8IJ21aMtUR2oTWk7XG+j6aMzYRlfG6H7YabKQ1vsQ6vbPQYVy+2QjiW2vA2T4hGuWYP2Kwvqyl90znGWNnT3YyL7GlZzVMDcxvXiolLXRxOk5vTMVZaHJfH0rZWgi+uFPEwsRrC2eUrq22dEL1Yx8qWtqaN+bSzxAzPNirXsTB8m+DOqV8b6BYXKunaMukxteizcEpP3JkT50RMJPytE5o9puwJ9ibHntlwzOnoJpqxOaHL7fq0Kd1V0yXMSkwD3Nb4hAskQxw6dGscQxxTwM2lgTYLFzBTTDjjb13Y9vNoH4haiVV4Fi1x8Rbru4qpnT3Y7Kt9ZeKracMzp8KUMw4i4c1tTfuqRd2tXahNxcwUMOTGRfRuXbIjZ1nO8tx5P4DtnJRIbSizgiktSzLJAU7ispdd5+JJT1idXvCWFp1Ve6tLHUTcq35d9uJx02FMbqqbbQmG8yYN9b1kVvx1CGSL1GCxd/5eDULXutSayhngouBcbGzjZC9MeipOYgiDNWAq0/Gdg0ERy5202Qo7ZWCVKY4vc9Y/H61UP++Wmr+zlt114a71XtYqgeD7nROSp3lcJXCGi4LJBjY87qJpjsIo9cGa1cfg1G88sbf8TVY01VUTj+VZKWUuZ9jpTM5xg4ooqXLxvXhkF7EhbwzUaTdG1PUFeybN/oIpfGAcZgp7SbGdsMgJqS5Td4gPwqI6VRdTuQ3BLlpVJUWew3i9d1UGA7R4RFPbPcj4VgvM65zlvVMjueTCpBfXbsJR4q1Uqe1VbQ4N1hZZ12CLbLZIl3DruYhPKXEdcpdqFtY0IGZ0A9aTIQ+2+2MEp4OhUcKDsklye5fW3cw+MoG2viRWfcVPdgHAzb76Vl5fzpmRhaydOnGryWzrh2hKwWEtzk6UxDJ026o6utxlJ7cLuN01mYT4jY+7BaB7Mq2Wq9JTqz1GrarKyWcyipvNPGi8EmwuMl6T1BBxVbxcuGFSK1R2u86wWNVupIGiTiWhwbKXy26K5qh/c9HraTU7XD1hMsk3qCU1oWEuZ+w1ViRtvSQ2mea6+oJnbbUKNtEwCb1pxDJGlTkhH65s2VOUc9gzKLMoVvKm03nBSwdldXFn5fnktF59W2hCzR+tlj5phMIdsyQvUncbUMkcLIp5l/GeKEse20U9eyUlAr8I0TXsYlJNvGmnwJ0F7JA9yVrhLiPR2OPFCY77JrcoFG8y6LsC9kiaC93h6hX4DQ+mBbObV0rY5pd6wkXTXVMdeHF2XWAV7UzwSxXy26B2iiXNyEdxPUnVrlWWQzk0PI6t9blNNyWYaxwrLLGbxVuzpnCAQ1aHtX9K5dWwQY8t0Uc4Ndkpk73ELxUjKGYULomRJC2MRAhXEXfxIoHmJLOmI7Uqssm8TQ+dvlINQzboCUcU1j5RQCXeKDUwml5lFYGZLLYXfqPNav103V8v4nXYDMcsurbXWqwJenmstSu7MYlD7KFYgIKrQbhatKEC9RAcgqFVcLw7dECTWD7VZwzP8CoVzDqXXa18JSglfoHmYlXu6n2UXYleWSc5W6+vC25qzCjVK6xImi2MSgEpl25leX5VJiZlXX3e6ox5xlwd6xbyC02maQyjNzMjJXE6x6lOMPuh5rFAZtGLC3e75tLad7uJIjGWw8H9FD07MXhYyse6weKpIHBdN+OdfeP6TZhQ/JXF+mJetKACjWbOV9dDfChIVZJM78qhgACWwgSZCrdgOr1T6HbFTALA3FD5kqO2GLt8ToF1H1EQGMUKyxdhds5wWfCJXeVthp3rb3yHblzZamczNGibJepieG/uGZTuBhzgq8hUSX6qXXs/ij1nRuNLIoilHVlUqa92er+eDVnGOfUMxwkJXWhxQMxV1xtkiyK92t/XtqAs8mLBnBe7g4UthhV6slj6VB0d+VAS88Ail8ebH3mLncGojMj6mOfzw4C7WyErp1azvTmkNo8bXLj4Bzh+d+QCjdRj1W5CPZm5JqPuh3oRMPYl6LQQ7qYFuFPvGmZnGA7WdJuD4aBXTV+43g7FzhVsw4XJTdXJeWKE+OoUEhNcbttqD6NOub6iM40rnDp3u25ktVYF8tIHJ2EolxmTOtOF7vJUn9mXaTVzqdhswATtGdmyljt6ul5M24Xv89k6aBedO29ZOh3O9rw/nyogkc68hf1nvprTuJGwe3LTGxu0j1KqWRKVE+O38LZlyAKdXqysba3pzo1JlOcDebpc84vp3F9vtrG919jImk3qTqOm+gHj4xOw1Z6+EColDgp/1tQtpfG8VAaKhi6WqozuzkpXMAzz15dPL+Pp9POM+Z96Zzye/P2fHUA+zgrf3jHdj5eB7X25y/ryz6nzy6eXyo2gMo/D1Tppg+dx5P84Wv38j95KjCv7x+vX8RXYrXk7fm/sYPx7oZco89q6qfpvdZ6094PdTy9OW49/wFB/ex5gv9yNSYvxNPxd2OPmXfEmHyn9aHweZeN7HeBFdgOel8HzoPnTiwfzKY3c+htOzr+BqhiNfL7nGM9oxxcdL7//N6wHaPmUJQAA -->
