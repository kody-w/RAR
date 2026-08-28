---
name: "rar-cowork-cookbook-teams-update-define-environment-strategy"
description: "Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_environment_strategy", "rar_sha256": "58e4e2b1f3beaf1122e012545a58d540ef5bd7adea01b53967fef278c0a84c81", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_environment_strategy_agent.py` and in the RCI capsule.

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

Define environment strategy Teams Channel Update — Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-environment-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 58e4e2b1f3beaf11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_environment_strategy_agent.py` first:

```bash
python3 teams_update_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_environment_strategy_agent.py   # or on stdin
python3 teams_update_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Teams Channel Update — Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_environment_strategy',
    "version": '2.0.0',
    "display_name": 'Define environment strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddb62191c431f4bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineEnvironmentStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineEnvironmentStrategy'
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
    print(TeamsUpdateDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOjSLLmv8LL90NVP1Ul96EaG7OVAF0gkATi6mqr5gaJ+xT09v++gaTMqn49M296bc1WdaSACHePz90/9wjytxe7baK8evnyovh2Bq3tJIkjv4LszIPYvM+rK/iRXx3wD3LzrKlip23yqn759OL5tVvFRRPnGZjOVXbQ1JANqb6d1pAb2VnmJ1CR1w2UZ5DnB3HmQ37WxVWepX7WQHVT2Y0fDuCL3bQ11MdNBPRCcdb4le02cedDC88u7l9Yu/KgIK+gso3dKwTssEP/FVjh3+y0SPz65cvPv3x6icH3ly+/vbiJXYNbL3djzoUHFHF3C/jvBihP/UBIYmchGF0MAIsMXBd+BXSl4BawG3pefaz9JPgE/dd/XXu7CuufvnzNoOfn68v059RmUBP5UJPbdeN7kGsXthMncTO8Qoukt4caqvymrbIJJrD6OAtfHzO/S8oL6O/Ts48PJa+h33z8+pIDE+wJ6K8vP0EAhK8vVTt9f52kFB9/ek3y3q8+/vRdTt06F99tJmHA6tdvz+unWDDw+9A4uGv9O5D6cKnjf335YXHT52H3tE4w8+X1ksfZx4fgoso7P7Mz1//40z8T60a+e03iuvm35P78EBz5tgfW9DT8p093kH+BZs8Fvcv852oL4Na/shIw/E3dJ+gJ1D+Tfcf/v4lOQHzV74j/Q3H/aMLs79DP/3Rt/2rCJyj4+sL5CciPynYS/wv02zflwLM/f/C+3/zwy+9A9P8oRsnbyr1L+JbaWRz4dfPt288f6vvtD7/8/KEtQKyBbPrWVsk/kvmPcL3r+QOCz1Ef/zgX6D9n1yzvM+g90qHf8uI/qt9fIc1OYu/7/foL9GO+TJ8ZNC3iTekDgh9ypga2/oDjTy+/A57IwGpa9/4YZPl//ie0j90qr/OggRQ3bxsIOLiJU38yXo3iGgJ/p9yufIBrHQNgn+NA/E8enizOA+jX/+XeSfOz+yRNuJkY6Ft7p6BvDxb89gMLfntjwV9fIRXIz6s4jDM7gU6Lw+FrBkgOMCXQXVR+7VcdYBVnaPzPgI8+T18AWUK//rsqvt2lvRbDr3d6jx9sdWK3E1PVbeK/TqvVIz97rs0FbOzffLcFipLcBVYFMaDaTwCFOk8AKzcTMvU1ThLIiysAQ14Nd9kAvS+TsF9//dWx6+hr9qBWHHqUjBoGA97NgT5/BssLkjiMmq+Z70Y59OG33z9A/xv6V7PuwicdB0D1T98AC3eKLEEg19pp6cBtwNGASO6++e33J8hATAZqHPBkHMT+YzKI1avvvSGubBafMZKCHB8gDVBOi7xqAF9DcfMKbQPo3V6gdHo0MXo0lTrPL/zM8zN3AFJtsJx3JLMclDwQkHUwfILa2r9r/dWp7LuJKUh6u/kV2rMHUD/yBPw3mXkfBCbnWQzgf4+Hx30gpPpQQ8s3Ea+QNEUnVNiVXUSV/dQR2A+/gLrxNh0It6HM779mU8H0J6juqfKABwwCyLhPl36efA5qfwp4wavfdN/H2FOVU+/Vrvqa1c80sKvJFS4oC0Bp2MbeVBz+9gypOsrbxLvjByydJD294D29co9B7l90C4/+gn32F4/aDn1tMQQloP8vTchk8GK9PvHrhcpzEC+pJ/MB5NQwTUoePRboA+6T70nzvTd4Y5Y3gv2aJTGIimr422PkHf7nmAdptRVA67Q43eUD3wMgJ7n30JxCraqmoLa/Zm9M/gkgcqctgAHIYxDnU3i9KZyevlkagWSdrr9X9bsrwbKB80H4QUXrJCA0At/3HHvCIKqm9HriD+LUn1Ktj2I3+sOqAOgNCAcgf3JEDJwE2P4OnZSDZYLMCqo8/T48nnolYIXXusBa0JH6r5AOMmSKkhqkJWh4pjEAhQ93UVDqA4yBie8I15FdPIyZmtingfbkizydQuYHDzwffo/puy2T+UCqDQIMYNlPXOv5t4dn3+18+goYm05ZeJ/0R3c/1wr9WHL+9jW72/hO7yC5k6la/wAOBAIQxPDEphM31YBfUv8ZQCAS7oX59VFbH8X73ZYvf+rcP/615v5eLc9/9NwXKGqaov4Cw48K91bgXgEzwCBG4sKvH8Xu86MSfX5k2+cfsu3zW7b9Qf4Dri/QX7PxDyKewf0FQl+RV2R6JMauP0Xv8wMgYT8vzc/E9PRrdvK/+/oZEBO/JgOoru/F5m0IqDhh5YfT4Efxqaea1YMyeWdb4I2v2Xs8PLNlYp5wqpR1/kMW36su8O7Dee9FATzKGqDbm3q2x64mmcyv/ZcvWZskn14yO/X//d3MxP8gcAEm01YIJBHohJrYv1+9d0XTxR93cPf0Arzg5V+mLPsETR3sJ+i9Gf0EvW0P7vuurAX7o5+nRnhSCYaCH+9j37eHjv8CtmXNUEz2P/Y8U//17Iv/bMSUXMBi159qev6erZPGPwkBX8LQr/4sRL5/sZMnZQBqnyp03Lwleg3s9EC/8wkCHgQJCHIKUGULJvxZDdBT+YDvAedOy/2O3/dl5Y+1/H6HoXlsHH97eaOOpw+eTSIYDnL0cz0VQxhEK1AIrh9xBZ79X7ePTzmA9EDbAgSRjE/4mIMGuOPbAYpimI+gGEmQNsl4JIH4Ael4NNhh2QjqkPicogM/wGjGRWyGcBkUyHtE6bep8seTbZhtu4xLo4Q3p23K9XHEwV0fxVCPxn2EnOMBMyn1vk+9AsZ8LvixwAnN9052Aua57t9eHIoAIzdEvV08Piw812zapB0pcuY0FYTlhWGQeTFcM1s0dH+kNsdhOFo5ki5S3BbMdVIIeYpi1oo/FVZCLPsDsg1KPrC28zkpUrV8218HQo97qzCJ7kr6xlw+eO5w5Y+XHVUWLqWdDykqXrHZ2bgmzsoQlBLDiBxT1kMjo6N40BR7JqBbZlXBM3jbEHpdJJZpIPvbFs5HFuNj06BUZHAUvcLy3DFsbDVuDVlADaGQREMB5tft4lDQu/3NE85EijXXoTklWtlqXGhn6g0OMhqDZVXCNOk2bytpdpxFvijp28v6GCro1bBRqQQtl0jh+jqvdsfapHIsILR0NRjnhSpwuOCtRsHtOlPVxlLlNHUvrOSyKs6lGsKyHtz42i10e2iP3ToOW3ZAF7m+XqPXqggELZJMAi01rT0w6TltazEfaMNEsDYmk8yScKJTDKFxyfyqFOd8f4nH0duqmWeNxYkdNCWVdjd0zh3rAht7fG8XTmyVmDp3SdKUhxLf7UD0s2uXuUlcIc/3lyjoIlFE0oEa1KgonSWsx8HRpVBhZVYdSm8Vy0Id3u72uLRwNxt4H9ande84RcnpteF2rK2LgoBa0rXDpSgWrhZ+tnXlanLMXC36U8EZvNIrp41EL6msLPCxkJugIcjzZsshY4vTYmVkN7bKnCb0uoa4iXmkpctknlH6cIplWuljfo1s9WVo+7OToZWjdOoSIvQ9yVDMs83vXGbv6VfnSkjGeD5jcmt2fXaJiXPfuWTTsP0GqV01Xm+SsVzr54LmdllAB0UpNpameRfS2Tl9Xysde5PHVOFjT9jUlbDl07nt+olsaHPJN66Y08ml6JG2HROwWrPwcgnv3MOiD6IF0zM5Kq8Wegn30pjxFAynG2p5tDYkVY31llmqthPE0aXICoUq5aFOT+IOtYuzQOZubUu1vu5P4+2yLlpldT7Vq0Ncbw3NEdSW9Y1KVFxQ5sc06D2LcPrFsGbCwikY9nS9Li6LvS3lZbRDhlBRGbWJF8QJWyvSbFGl2zhKzueblZ0SecOPrs8SOFseLhV5g4sc47LVPiZJdSsrRikrWplxIhZWPal45mWfXsaDpGODfMTsi0Pp7K0llSizKngD97q3RlGX2fH25ubNxqAQqvimGwS1ZEcDwa6ObnFnz1H7E0HHGCLhNiuzGrGaU1E+c/Jydwgc+OiRSesJRDNGS2132a5Ow0JiABEIjT6nh3o/S3BFVIeYvzVzuNWDLXrWCUIzxJivUmMn3mZtY1sarCMt29kXJb5iC1Wiz7JFIDySr3LSEM7V5Sic/GbZ16vNvldXS43aZLfVVk3FwtN3A3lYqDDKd2u6OsWXGWk2QrIur8rh3JELayiUm2CLnsNseuzgW+5xZhHmqdse06pZ7deDgl3q/Q6JVWtbxTuTckfxoqduEaFCkaBGXhNXlXdLmt6IS4Q16axiCns0ilszMooQyGeutqSGCtCZut1uTXkUgADW8RcUPT+Z6HxbdJqAVnhuRvR5H3U0jN36DdmnNyo8yP2SvcICK5RNjZ45JAzWimn51FX2FW3tEXoxkIAGOGOpmUTIWLDmiLmUyyqiGTAT1os089c75VKuDXFO8epuZvM1mQRpNThcs5kvVjknbReR4LjbtTG7eOLJXWz17VBvOC68LhU3bsJkh5HO0FQ97TZCz9KsqUVqlArJEkWG2+7kXC8s45rXpRBrnIwgo3WVhJmstK4sE6R7PEeeO8o1wSLJ2UcwP5VdzLtZ7dbKDAMbzU6tUdewhqMi7hvz4khtQM7Pp4tBju0prYcgOm64U64HEnxYZOwY09SYYKuhz4/NFoE78dTTzEwVaQKWN0M8XtDQ3xpLBVkzTIGvTJevFwVWCMpaqudXK9KWRUK0nrbLQrEiDxWZ8oWOs0641Wt8JaBL67Iey7jo7atvzt2jrpw9GVnlbdbL28J0VlywEOGSU9I63ZerCFfUoR4dazlDrEb0QP07Yx51xlRhZxGdhFuYgZotJl7PqrZSV3tAn8sIP1NF03uZmtg5lhwbq9KzvF7lwSXaHm19tfEpfbwsSEpG6FCu9pZLnk8mGZZkJwdtUZ6lnSZeNm7Z4ppuz26wr7b6KNDWCl8qyyWqJMJMoG6DR+Ekjp9x/qBskTLosdmAWCwSWi0c3fyrL5eHZW1eGindwGxwPG21o87W1XqjlychjHzWy4usrVRN4ld1mzuhY+OCeNwIS5E7o3ufOBXMpiiuqr0KUY88KwHGbG1OTMphKDPB4kNlSS9oU2W45bY0wmifZNngVeIRM82VMGctjK1WqO7ZsZRy6tqOzZp3l9o+2B6y9VxwGjfJWSJhbqHl89We3dZzL7zlIID7Lol1e23mfIBZsd1nSDM/rCX2CJikU3CvFGPPE1XtINWR0AdUW53JtYlIaC5txaNszxPkoPFd7enLg7hLdgaRRpSH7OSTX/h5Hm07xDilbIoX+/6QHxTgWzavBzWN9XHZucfmJlLbLXbcYEF60ppc4fqFmYouEXj4oeAQZGcf7fzQYeNhHuox63nCmNutzxbcfiGI7YzC+NVIXW8lRYlbalEuDgd1fkBof7ar+VvRImJk8Bs9jgJ7tiOkqMgVfy5eMt9sE0MbHE9N5ym9N7aUdqKwGYUix10jrbe8I6OaNzuHrMhGi/wo+RneDiWqqKFDH6lj2qviedgszobTz2Tq3NrKTTyLzLolKyzLBG1tr0H9lq+74CyVJXehEnUJelBqGWdaPCeoAuerZCgvXUUOpWuh81tmLkNQt1a4aPeIchr3Hiac2eP+ouyGW0/ZZjxwPLzHDWFxpY4LQgV1dThzZZaqs9xzGzGRGmR93dOCqCxhMc7mkbrfq4OrOdQpycM+zhKebgexPV8SbjiNtdFFFH/Z7c12p/AYAngB2cKIsDqvjbPfiNGwzrMdZ2VpIyK35iLMtaBZ6xtipV3oaEHQlnagXGqXLYbMQpp0FdtIWaGpgtqNa9UE2GxphjzPcOp8Q0O2Fo/jjOTmOcnsNJKah3ur3WOx1AmY5J10e3t29fXNCwZViXNqU8rNFaEN44ztGZ6eaZza6DNSsnyrS4+cb501fryeY6k8m9kiQlVzzS03KypCj8yZFy0FVLKl4/AnlrTH0Gl54dIwDEVdLnJDdlh6uZKLKDPGcbYpytInsZ682X4sh9SNOs9K4RruyHKeL7KenV/74cgp1m5gVuFVhoXVrodFL+EZb7GzTtuCiYVErgKXCXfdVTVR7qo1Ak8Pncbt1FNd2Uv5ttYOWZzORm9BcSoTm/trVqoWcspmwtxg8qo5pAvfmvmOTg+aWSC6F12LI5O2Yqawy0RYxkWwP519nTiIrBUNo+Yi/vaWkbwcqFd46V45OsEbEmfVDpcRNLe3/J4ROZtMNLALDCmywHJ7jlMRZpvnll8uAWtYVLpEDwt8vKXW1TB8s2i1AJGWnT7Md7qLWIv1CkMRpgoRbSi64/bqReEe4/Je89WQKzV7j1I9ezuOlswdyKHZFXNYEtHNEj2Fh3ChR0yizz134yAwV4smXwBi5Ucy9Zzl4M5qRUAkpRqDzdrU08MmWm/Xycy0Ev1kHOBMuM0RufXaa00QjZHFgy8dNV1jyHBY5paYxIc0E3O2AwW+kYRxlkfsJqiXWI3QGIUL8I7o5yf3cqMMRp/hdpaNCuq1zOrq4VF/m9sw64zuRuv32ox2yxDR57W9pm5hsdJElU6GdSNL57OcKYjDjiGTzTgx9FJNJluKc7hK3IAdQNlQpmnyy1UgnFK145ltIIgw7S0OES9dNnuzpEc/WI69BBsBcpTXpEAsaCEZHWRjJnNVizl019FeupEuOZ2zEnxG3aHymsrUN2M7NJ1cs3XtIPlM6ndzy6NlZE3Bm60La0EAX60AWc/25YDAbR0QKdPVNG4cjjLcXsH20qgttVYxto43WnvNmc3hNByPlEjHCauNl5sFH8+DugxFLRioPvW2nHopxp6X5MP2IJj4EnDosCHrMaTwJE0TjE6CPbwKJYwaJTy3D8t+SYu6Ulp9ybUGSg/ZRtjfBN9aK7skYTj/TK6adChcDlvRruSgy1nnha3MDPbSvEUx3PKHmKEFqruK8wbEf7LXFLYYyaWJw9tZSnBLZI/pe2BEuStUktqi14BOysPc06gKplAY51as7nHaHOwcF+jqypHkbHXrD44fpHPmxmOiUTXHw3qb0IumFffOBm86ZzQlqnRQ+rIYbh16aaWULugNHWytJrzmPQ97VJb2/G62G7BzeGNR+cZT8Yok/dtaRLJW79IboSxCem8aGSVGCn4TMMbg8Ju4gJUw2OwFgmQEjhuXjrKLaIQjBpW51TeLyPANdgzkRa9Va6dP6Xa1OgTpLei4ELH3PSchmzKUb1ZdOTQxIw/bSxhySyfkZyygYbx3hSWXN1EpcjPYPJVl0x6T7kImzGp3rFwV5kRfctw5jmJC5ERSt8NUIy/J1F3FyBEW5i2+34TnkidUQ8zhXkQQfTbjKawydrRLUa41I3h56xqAe2acy6+52l+vu7xfMBnoilfDjEX8+ebQ3LIRTQ/eeFyf2d4RL1WJtRp+pKgTrvnkHpnjJa2VJ9OO8IjRek+8qpSMh6G67BZsSBRzZobwXUfXynaxrzYM618YStKHw+ZGca5iefOzOLugERWoTu45t4XEtnhLR+ahE71uPrgsY3gWTBhq17Y2vlhvj5sZTcKNEJHhet7PVriEj1oTtM66Ii1boWXcrC2P6dB013oG2K3AM72TGSHq1nAkJaTYzY7H/dXxedsM1x131iXDu8JZ4J2GfZnhvC2ndjsLK+LQCPB6la/DMF3aaReT81mbuEfEJkAdn22qS3Goo5ZsPKJOoqbsIvsqlszJNIv5puEuyJY45PtNLvBrMz118cghMu1GYG/OOG6TnTGcBtXYAvRG1Fp4YJELS21wOSgQMuQI/8ARRWUzu25Qu/1msRANlmcMPRRHeSPFQsHkErm3Qwshy+V+37FR3WDmXGCvc1rQQ8wno9m+DqnAU3V3Ax/wSiU4kUiIHX31dGbgsdY4eiJsRU62hpdaMhtRa9Y3/HFzkKtMYpOLFt1sIocTZXmGScVSqy7zLvQi24CgXw5heutrOWuWsbVOsduC9bpK4oPbKpqfyNUmzRidQS4XOu9ak3BEgcJ9bDdQ8AUxmAVKw0XHHIvFYvH3l08v0+H084j5L79Lnk77/p8dOj7OB99ePd2Pl33b+3LX9eWvm/bLp5fKjYFhj4PWOmnD53Hkfztm/fzvvriYpAyP17XTG7Nb83ZC39jh9CtIL3HmtWDw8K3Ok/Z+4PvpxWnr6Rch6m/Pg+2X+yLTYjol/3FR4NL20jiLp/ep35r82+Owebp/fx2Z+l78/TJ8nkN/evEG4LzYrb/hFPnNr4pp3c83ItOx7fRK5OX3/wNkMeOj6iUAAA== -->
