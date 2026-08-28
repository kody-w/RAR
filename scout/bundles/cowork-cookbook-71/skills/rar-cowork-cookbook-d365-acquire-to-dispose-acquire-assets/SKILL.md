---
name: "rar-cowork-cookbook-d365-acquire-to-dispose-acquire-assets"
description: "A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose_acquire_assets", "rar_sha256": "2c0950f3725fad108aaaa71def9e121cfbebbb96b23061659182c4be362eec7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose_acquire_assets`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_acquire_assets_agent.py` and in the RCI capsule.

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

D365 Acquire assets Expert — A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_acquire_assets_agent.py` and embedded as the fenced Python below (sha256 2c0950f3725fad10…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_acquire_assets_agent.py` first:

```bash
python3 d365_acquire_to_dispose_acquire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_acquire_assets_agent.py   # or on stdin
python3 d365_acquire_to_dispose_acquire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire assets Expert — A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose_acquire_assets',
    "version": '2.0.0',
    "display_name": 'D365 Acquire assets Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-acquire-to-dispose-acquire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87f438f8ab12d9b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose-acquire-assets', 'uses_skills': {'custom': ['d365-acquire-to-dispose-acquire-assets'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AcquireToDisposeAcquireAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDisposeAcquireAssets'
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
    print(D365AcquireToDisposeAcquireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816+ZOjSLLmv8LmM9uqfqpKgRAIamzMFgFCAnSAAAFdbVUcwSHuSxL06/99A0mZ1T0983Z6bX9Y1ZECIjzcP3f/3CPIX1+cro2K+uXLyxE4OSI4aRpHoEac3EfY4lrUCfxRJC78h3hF3tax27VF3bx8evFB49Vx2cZFDqczCNfnThZ7DYKTBLL6n0d2i4BbCeoWabyiBD7SFkgbAYTxqi6uAeI0DWgbxKmBg3x0kBRcQPp5hjSd6xeZE+dIEbyPhVP9uCmLBvyEfIaKXEDdINgMkXGkrAsPQFHNK9QJ3JysTEHz8uXnXz69xPD7y5dfX7wUrgV15KBmT4lawT3kPa+ZuzJQQurkIRxa9hCWHF5DA4KizuAtHwTI8+pjA9LgE/Kf/5lcnTpsfvryNUeen68v4x+1y++2toXTtNB0zykdN07jtn9FmPTq9A1Sg7arc2g/0kBU8/D1MfOHpKJE/j4++/hY5DUE7cevLxDJ2hkx//ryE1LUcL26G7+/jlLKjz+9psUV1B9/+iEHAnoGXjsKg1q/fnteP8XCgT+GxsF91b9DqQ/vuuDry++MGz8PvUc74cyX13MR5x8fgqEnLiB3cg98/OlfifUi4CVp3LT/ltyfH4Ij4PjQpqfiP326g/wLMnka9C7zXy9bQrf+FUvg8LflPiFPoP6V7Dv+/yA6jXPQvCP+T8X9swmTvyM//0vb/rsJn5Dg6wsH0hgmhuOm4Avy67fjgWd//uD/uPnhl9+g6P+jmGPR1d5dwrfMyeMANO23bz9/aO63P/zy84euhLEGnOxbV6f/TOY/w/W+zh8QfI76+Me5cH09T/LiCtP/LdKRX4vyf9S/vSKGk8b+j/vNF+T3+TJ+JshoxNuiDwh+lzMN1PV3OP708hskiRxa03n3xzDL/+M/kG3s1UVTBC1y9IquRaCD2zgDo/JaFDcI/Dvmdg1GFoohsM9xMP5HD48aQ+r6/r+8O39+9p78OfUh/XxzHnzzrS2+PRnt/daDEL+/IhqUXtRxGOdOiqjM4fA1d0KQt+PKZQ0aUF8gp7h9Cz5DNvo8fkEgX37/9xb4dpf1Wvbf7ywfP5hKZTcjSzVdCl5HS08RyJ92ebAwgBvwOrhMWnhQpyCGHPsJItAU6QWy3IhKk8RpClm6hhAUdX+XDZH7Mgr7/v276zTR1/xBqzjyqBzNFA54Vwf5/BkaF6RxGLVfc+BFBfLh198+IP+F/Hez7sLHNQ7QuqdfoIbicb+DpSXsMjgMugw6GZLI3S+//vaEGIrJYamDXoyDGDwmwzhNgP+G93HNfJ4RJOICiDPEOCuLuoVcjcTtK7IJkHd94aLjo5HNo6JpER+UIPdB7vVQqgPNeUcyL2A9hMHYBP0npGvAfdXvbu3cVcxgwjvtd2TLHmDtKNKx8NXPWgInF3kM4X+Phsd9KKT+0CDLNxGvyG6MTKR0aqeMaue5RuA8/AJrxtt0KNxBcnD9mo+VEoxQ3dPkAQ8cBJHxni79PPocVt4McoLfvK19H+OMFU67V7r6a948UwDWdYjKvVT3SNjF/lgY/vYMqSYqutS/4wc1HSU9veA/vXKPwbFe/2O7wD9aiq/dDMXmyP8HXceoKCMIKi8wGs8h/E5TrQeAY780Av1osWDtR2AUPZLlRz/wxiZvpPo1T2MYDXX/t8fIO+zPMQ+i6mpolcqod/lQYwjgKPcekmOI1fUYzM7X/I29P0Ev36kKegXmb/IA5W3B8embphFM0vH6RyW/u7D2x2yGYYeUnZvCkAgA8F3HS6BW9ZhWT2/A+AQjftco9qI/WIVA6TAMoHwEKhFDB0CGv0O3K6CZMKOCush+DI/H/ghq4Xce1BY2pOAVOcHMGKOjgekIm5xxDEThw10UkgGIMVTxHeEmcsqHMmMP+1TQGX0B3dyC33vg+fBHLN91GdWHUh3faSGW15FhfXB7ePZdz6evoLJj7Dy89Ed3P21Ffl9m/vY1v+v4TuowqdOxQv8OHAQmU9bcWXTkpAbySgaeAQQj4V6MXx/19FGw33X58qfG/eNf6+3vFVL/o+e+IFHbls2X6fRR1d6K2itkhCmMkbgEzb3AfX4Wm89t8fmZPO+3Hrn3B+kPsL4gf03DP4h4hvYXBHtFX9HxkRx7YIzd5wcCwn5eWp/n49OvuQp+ePoZDiOrpj2sqO8l5m0IrDNhDcJx8KPkNGOlusLieOdY6Iuv+Xs0PHMFUngejvWxKX6Xw/daC337cN17KYCP8hau7Y9dWgjGTUw6qt+Aly95l6afXiC/gX9z8zJSPoxZCMi47YH5MxJhDO5X703QePHHvds9s0ayK76MCfYJGRvWT8h77/kJedsN3PdYeQe3Qz+Pfe+4JBwKf7yPfd8YuuAFbsHavhyVf2xxxnbr2Qb/WYkxr56sOurylqjjin8SAr+EIaj/LGR//+KkT7ZoWmcsyvF7vWignj5scT4h0H0w92A6QZbs4IQ/LwPXqcEdX3809wd+P8wqHrb8doehfewTf315Y42nD549IRwO0/NzM9a/KQxVuCC8fgQVfPZ/2S0+pUC2g30KFDPzUJpAA3wxIwLHx1DKgZ8FBveuNMBmmBe4wHVdmnRnOEpiJEFj1MybuwAnZwB4CwfKewTot7HUx6NmM8fxKG+BzX164ZAewFEX90Zh/gIHKEHjAUWBOQTpfWoCqfJp7sO8Ecv3xnWE5Wn1ry8uOYcj1/Nmwzw+7JQ2HHK+cG+ROalJYDUJk4qqmLo9gaUnUh3MuhWK0Ldov+WFK+8n8b7cpse1WHKLtPRlkV33y0N2DCq/sxm9NHBXUgo06nabXEwGAicnHhmGLGMfDtNLz+LO8SJhqaSezVN6dHIXrdVVdjPx6SSyZ9eS7jx3doyFE0bRFZBRwt/O1ie/4qWkXknNqWgmnDGXhsTxbCA69m57LrtmbqhN55HOaTDmnuboXbq0z7vsJHaRk9rF5DCTQdA4oh4rTLlW5oJITYKcoOgDng50efQvZjlMk8MG7zhW3Z+Mnr0I5Kxqj2nazgzJsHijSi8sexuksz2NBHx3WtUNp9olJ3Z7LaXjbuEdk2Hu+qFCYLqvZOqQTPecmV0ltOSM1IoAJiy9VSoxIBEEYiGXPmdE65Xg8p3RoNfUwKxoei4d2uy7zlhoPhrNZFMC4lwyNukq7fMYcBeWOp/3diPpiuP1mjRleLbKbkpF9IpZLU5em1yO2wMzMfrjQrEFcalc5FosXNFkL3IqLawGc1yf41M5DC7aPhQCBxOkZD2bEpFek1g/nAStii42M5X46MZZbJeg6/NJxrIInHjMAIJvzUl1ItS6apKLY8+nDMgrcGLBxiHWZ0kayHnou4Mh90OaDXOPspbJRCmxuF8QuX6c1wq2oo/d5VZY+CWWWqFv8plORdnKPbtLKV22u7ix/IltZM5CV4eUDoFxMmOLOwlyc13fWoHobrpgrA6pW0mUSrmmAol3AuZKIk6jTJyyt4xKubWud8XNORBnDLOHtiIrpaHzhlI8bdcTWwi9oN3YVSIf9ERz011zzQy7IhspAafjueYvHpnl+0NBTuXQzG/5YbZfX/VDI0vtsFEJye04Qr3tL3gWTfL8tOy9mHYmQ7hNJHMhz2O0V/pMPjZTKi3ii1EZFgrcTcZn65vqgrNgeMezZe24RWjFok3h15RmNIG0lCrWt1mrOlwZ7LyNuookh776x3Lphoa8bKIm7M+9oparhXj2uSTeKKxfg5V3tdG1GM/Eaiamy3m2jDFi3S5XztrELrUmY8SZT+JyOin0kh+OwWGTZVrRc1HKV/pZr/ypVnn9pcCpXRDk+MThm32JYof5YVvL+SAX3jYwbloXHAy8T72g7OPVTblOB/codY2YCGt+cLbOHEcr3Ezkys4nclhWSRT0x/68oKK+qJTDBHeicpDybgnKaB8Qi76Zl3IT+Va17WUpljeWfMNidnpsDTfJ0KHMBMr1sHJQTMPYWJTDp52txDTo0u1uKI57zRT3bLw96VFycPsld+Lz0A+S63RvVURqhduzt7pM+9Uct49iMsU32FLeRGJVTjdqqKwFQw3r3J90Lkv0jWYyoaHOrtypiNPcLs02ErYCaWs33uiXvujZpZ2Z26Ypj0dHqYvK36/Om3C6neFsH7RLfkeQU+nU3Bw/aKbJ+YjWjKk3BzrQ5g3oiMESfN+utVtoDM4BaBg/yRoThjSHdtclmlHTiXPoJ5u1PMmTMwX8qcDPbPtotv5JG6hwjcWHS3ppT0dD2Fgnq5/T3EWNLUMhGGpHXfGGOQEvr6XLJVvO1Y02s1LpHEyo4MBnO/4sGrNWQ2FhGxb2AJaLa8pvNozc6QKqyRdCMINDgtvrKKWuAi9uAd/iJY7xuOHGFXE78uDIsNedpHbiyq423M5wmfx62ulD1kdMaSkuMUuzJrJre6OL0Q3V6oRNzgVe7jjZ7uNTPwPZ3jn5t7Lb2L1WL+jGLGdOJ2/7jahIJzSSBhdHHcNZaVTu1YZdTFnG9+Li5E+CaaypsbMgb9FshwlKNAwENZXh//Mmn3JzyliT6TQWvZuKS0J0rIecqM+bLtSuq4MhMiHR5ofdnm0qw5Mz42jTxmy/ow+1mq6zQN+v5nwt5f3hXJPe4VLG4KIQC/+sr9QE34QJaTMNX3KaG2gV0FtV2deWmOPi1GCrlSKtnEal98fdpVWroqQnvUt7Ymc5t/UikomIp5sdZ65qw3SvzXHlO+kho2stEuplNRjtfs2do95idH4XteZpN5MpX6xZaRZF4qFkNrGybW/6TvO4Srq415VDulliS9FUOacb1Gir5LrbTHnYpxz8iMMYJZLP7uKAo0bMxHGnx06WJZY1xVi1PQ3TS3A4nduQmVeKyOOTCLLldMUER2ZDJ8MJlFXWcFNZJqanedsf0fQcttqZxGivmKGcv72W21N4awldCWZUkZ001jBW+lbPlwwvk8uEybbblsnAddXjsS/O2jVHkxddvEqZspqYqYpJ0ckF3nWwbp6op5urF8wcsqcvWFydpSGKV5E3P1ZuxcNImVCY5W3EWmbs2KKsNN8Oet1roYlOaKeIvAa2oZ0vmFdDuYgnzOipmlG3k9q2BWZosXDLcGqnpTVftRwRoei1O2b6ljVwmj3zeNHze+qoG1ojmvVGkzg5kBzFbGAFrGbr4qTsUJW0doukXOnNSdUkM9xvz7K7SbmNWh1maT9xz/4Rp4sjGi7CHV4G007WVH7uni/y1WNIjTwpicD1bZy3tF2eSrfo4uJKglpWaJyaArAVmN7xy7VeKnuCUSc3Rx3Oay3xKFI70pRqry8L4kiaNrkddqczezuU/qE102CLLk1OnXOCWevakrdF4dgzJ4nGduhstmpk2A3YYaWXV+jg65pXzJqi9xVAbSqSlSHzbjiJad2y5u3FIRX0jTKrIl4BsmRsuatfV2yyL+cugWtdZ8uJIbhmmyrbhYkJKrNaMS5uBruatZfCfrZCJ2tNQsW5RUY7zhMyPCtJ3nbKPWfx2m3LZgrHHWXGjBK+Ho7ujdN2tVV2DgBLd8bs0uEI1odakLd+Jt8iGIARI6DbSXkw5upBqpoiD/fUZGZlu1WiCQQ4WlxaskIsxyW+qUQvmVtORiqyjfOMik+GWGo2IF5tL5vbccrEVZDIS61Ai1zsGz3cgpMteBUGW4hdeUTNvU41tzri3OkRzcmNjdZoFDA0aycHfJdT/fQgNMtct+G+CR2mQp0MfZLRTaSvpzSx20iRfLBXrZxrJbPoD5kYe4YbXPY7iac8dHsm9pN+Uy+zgyqYSUjvhUMp75k59OTG1y8Ys9UMKc5EzULbZieYB7JhpNDf0AvcLm7spEQdElxJwohQWl6vyMLh1eW+vpa2rkchGxpnrT0kUqdxTOLMRHYvLY76VmQqTVZQaimkSmzpO0rTY0KRZrhYc+czkaHMnJC20Z7K8TW7M88nEJLeLl2GN9OOlNQjI1yp6vPREC9k0SuJmy9ElzqeRYlkKSvjGzSJdp1FDevCZHyhPipetOrhHtzY2jpsywRvW6W9yyoNmN9Se2DMg04yLnPIU7PVSF3E3a639bBaCrP1Ydf0ZbKauQ4KCwdmoRkvp8IgsoKrxTmpC2t/duA0CStWsV+IQqWG+3RLHhv7Sm55EmsSYPSVRKwXK0HZLkOBZk675aqZM8ncFIfCWlFRfvQct0+PdkmTexHTlpgadsUki87RqRU2cmdDi/eKeNpSidhs837WejkXGQKvJkbCxcGMmaVFodONXqRTNTQtI+kcxk2Ww/KCYdJmQU9x3pJb9YTSfqL07HW5733zcjS4m9v3GTeRSMqYquz2hi5O4gbiGblBEVwIk5l3EtXjk4XuajRwyOjgl/5ivlh37J7ufXytHhbJIHaNv5AGbCCyrbRkdZCBAnVu2txRy0ITMy52F/vZ8prVCzvziDYjqnVbGlUdu3VGqaIyWJiITgC/Pa8uKM7mZzaoC5SLFwMIVj1L4ya4hqwG2pa/UME+nKfTHBNddmoV0/EkEvZa3XVL+tEew/hhJ4Q4fvYTAvgeaW/wtsCF+XxyPtG44/va7ZodBtPEF4I5Z5ta4m7lFCe76dllT23uWwCtZwtFnqR7sNwzF13eK2iDsu0N+Gy/HJiL1oXH2VWTApRrEkWZ+OZ035StwhRztKFUzlV7hhAvW+GqhQm4OWfKm986V8kJvMnURmp7uu+4vDj4U9k4XRh9WRv93psvBjGhtM1gr05iJgRX4xacT5u9LJuNCPBDAjYHzEVlGheCiBPz5rLouDnRRn7a8/jeTQ8oFlahDg6orQdoTdJXyYrWxyELTFNtu90Za6PCxHfohbrVlDvBzjf9TMCAbPhA4fhYPTTDrJtxHkbgPmywNMIh/OqGKauYZwvYh2bWrM1t3ZygFTZZXMW1jC3VW7/wMA8Aqss71gqXwwQrJ8EyzHFJLr2ltQBKv4xFHKYFX1yWB88PJthcXTKLZhtoielFHWvoRJfLMbWcFRvKc1Vu1dcZc5WxjQvoqyqIkmVg2ImfArEhqDl3gwkWsI6+8c5+cDtPwVlFDd6KLhaHWStLqDl3Ye124MQtYeEhGXHDm3KDX7cbwM27SXU7T7rrOq2wJkgWZzqlVqKSbjfUdeHvat6fYbN+6ba7XCQ1rTjbubeKUdOUiBiX15d5yS/OplwQV3mgTpPJnJztTHHhkYSlgrm+tWwz8GadkEyxxqLtQN9N9mumzP2rYPezxSSAbaIMTlLv8xuWKNZ+g8nuerBW+9tikL2qc/y8wiv0pEXnapDK/V7OPe9iJNR8b00YxcxpcbsC6cU/htdDsQ63Abbp14PB37rDElzF1MT0C7k6CVdankXpZc5g/SLQm9U1APuFuyjzIVh3FdTqPOTmRBryfGoR03Y9Ia5rmlsIl41325C4n1OSxSoFVt86hyIyU147Dm0bpYe77frSmweq2Eymx0lI59tTUCyX3fY2L4iera9LjV7t28P2SuP7bYiRWD7wTidYaxAajblYB5x+5a6skvumeUvQ6YyNRXKnTYk9px0P27SbrKxFezprx/ICm1VjnhdKRecrZonu3MOGEYq5zluO3bHcDt/KykpfLADIuZKcoTjoMtKiJ4ebs1mfuD6eDCvcOxWiD1ufCcsSZexQZ5qIiA2LWmzFh9d2F2opJcAdPDfR3FAsoKh0k9xUqhJui1QlE5+lq/3xLDO3KId79FYkyhaG0n5vr7xVSB8bebLLLv6QXHFzftpMhyMKsIqNcFowZgNXiVRASVXQoHnYdJi5WqMFU+XTXpPc1hvwC2Hfur3JWMUO9eRVSYdWtixX/EY0XbJRuUbVZemwqTzUu11k3b3k9HGr3KbHwTDXu/oshFOKccyM5HCmZBjm7y+fXsZz5+fp8V98NTye5f0/O1J8nP69vVG6Hx0Dx/9yX+vLX1Xsl08vtRdDtR5HqE3ahc+jxn84QP38772NGGX0jzev40uwW/t27N464fhrRC9x7ndNW/ffmiLt7ge5n17crhl/n6H59jywfrkbmJXtt/tbcHhZtBGo4c8/W/Yy/srB+HIH+LHTvl2Gz7PlTy/+84XmtxEYUJejxc9XHKMzxnccL7/9b9dzsk+4JQAA -->
