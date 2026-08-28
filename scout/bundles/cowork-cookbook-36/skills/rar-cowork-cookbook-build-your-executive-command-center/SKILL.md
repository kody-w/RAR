---
name: "rar-cowork-cookbook-build-your-executive-command-center"
description: "Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_your_executive_command_center", "rar_sha256": "af8aeed741ed798fd57883e1bf37d69798d8fd72c9ccc9770dba85ab95ee81f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_your_executive_command_center`. The original RAPP
agent is preserved byte-for-byte in `build_your_executive_command_center_agent.py` and in the RCI capsule.

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

Build your executive command center — Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-your-executive-command-center
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_your_executive_command_center_agent.py` and embedded as the fenced Python below (sha256 af8aeed741ed798f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_your_executive_command_center_agent.py` first:

```bash
python3 build_your_executive_command_center_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_your_executive_command_center_agent.py   # or on stdin
python3 build_your_executive_command_center_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build your executive command center — Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-your-executive-command-center
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_your_executive_command_center',
    "version": '2.0.0',
    "display_name": 'Build your executive command center',
    "description": 'Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'build-your-executive-command-center',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-your-executive-command-center',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a01b3152482f58b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/build-personal-insight-dashboards'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-your-executive-command-center', 'uses_skills': {'custom': [], 'ootb': ['Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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


class BuildYourExecutiveCommandCenter(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildYourExecutiveCommandCenter'
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
    print(BuildYourExecutiveCommandCenter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjRrrmX2HO/WD7UlWITUB1dMQghJAQArEIAa6OMjtI7IsAefzfJ5FUp+zr7jvtiYkY1XIEZD75rs/7ZnJ+fXP7Limbt89veugWkOBmWZqEDeQWAcSVQ9lcwY/y6oF/kF8WXZN6fVc27duHtyBs/SaturQs5umd23RQeAubCQrcCboW5ZAWMRSOrt9lEzQA1BDqSigq/b6FPkJDChbuOwiAlGBRMLRLmrKPEyjM3TRrP0B5GHbgPvg2S+MnbtfOAEAGt4j7zO1CKO2gqeybNsyiT0AksFheZWH79vnnf3x4S8H3t8+/vvmZ24Jbb6s+zQIbDOfH0O+79BZyZZ4DbC4surAB8zMADAZWExCtANdV2ERlk4NbQRhBr6sf59U+QP/5n9fBbeL2p89fCuj1+fI2/9H6AugyK+u2XQgkdyvXS7O0mz5BbDa4Uws1Ydc3RQu5UAvUKeJPz5nfkcoK+vv87MfnIp/isPvxy1sJRHBng395+wkqG7Be08/fP80o1Y8/fcrKIWx+/Ok7Ttt7l9DvZrDZRl9f1y9YMPD70DR6rPp3gPp0rRd+efudcvPnKfesJ5j59ulSpsWPT+CqKW9h4RZ++ONP/wrWT0L/mqVt92/h/vwETkI3ADq9BP/pw8PI/4Dgl0LvmP962Qq49a9oAoZ/W+4D9DLUv8J+2P+/QINgDtt3i/9TuH82Af479PO/1O2/m/ABir68rcMMBHTjeln4Gfr1q37kuZ9/CL7f/OEfvwHo/yOMDtLDfyB8BZmRRmHbff368w/t4/YP//j5h74CsRa6+de+yf4Z5j+z62OdP1jwNerHP84F65+KmTgK6D3SoV/L6n80v32CTDdLg+/328/Q7/Nl/sDQrMS3RZ8m+F3OtEDW39nxp7ffAEUUQJvefzwGWf4f/wEdUsBHbRl1kO7P9AQc3KV5OAtvJGkLgb9zbjcz07UpMOxrHIj/2cOzxGUE/fI//Qd5fvRf5Il4M/l8ncnqa/iNfr76T/756j8I6JdPkAGgyyaN08LNII09Hr8UbgwezstWTdiGzQ0Qijd14UdARR/nL1BaQL/8G+hfH0CfqumXB52mT47SuN3MT22fhZ9mHc9JWLw08kE9eIKFUFb6QKAoBdz6AejeltkN8Ntsj/aaZhkUpA1QvgTcP2MDm32ewX755RfPbZMvxZNQcehZMFoEDHgXB/r4EWgWZWmcdF+K0E9K6Idff/sB+l/QfzfrAT6vcQTc/vIIkFDUFRkCGdbnYBhwFnAvoI+HR3797WVfAFOACgf8l0Zp+JwMIvQaBt+MrW/Zjxi5hLwQGBkYOK/KZq5EoNx8gnYR9C4vWHR+NPN4UrYdFIRVWARh4U8A1QXqvFuyKEGlA2HYRtMHqG/Dx6q/eI37EDH/Ole3X6ADdwRVo8zmMte8qgiYXBYpMP97KDzvA5DmhxZafYP4BMlzTEKV27hV0rivNSL36RdQLb5NB+AuVITDl2KukOFsqkeCPM0DBgHL+C+Xfpx9Dr0iqf229mOMO9c241Hjmi9F+wp+t5ld4ZePRiDu02AuCX97hVQLKn4WPOwHJJ2RXl4IXl55xOCjTj/qOvQezN9EgJ7BDH3psQVKQP//u45ZYFYQNF5gDX4N8bKh2U9Dzu3SbPBnhwWqPxCieSbN947gG598o9UvRZaCqGimvz1HPsz/GvOkqr4B1tJY7YEPfA+MMeM+QnMOtaaZg9r9Unzjb6AI9CAr4B2QxyDOZ32+LTg//SZpApJ1vv5eyx+ubILZFCD8oKr3MhAaURgGnutfZ9vN6fVyBojTcE61IUn95A9aQQAdeAjgQ0CIFFgUcPzDdHIJ1AReiJoy/z48nTskIEXQ+0Da2YefoDPwxBwlLUhL0ObMY4AVfnhAAacBGwMR3y3cJm71FGZuYV8CurMvynx24e888Hr4PaYfssziA1Q3cDtgy2Gm2SAcn559l/PlKyBsPmfhY9If3f3SFfp9ofnbl+Ih4zuzg+TO5hr9O+NAIMjz9hGCMze1gF/y8BVAIBIe5fjTs6I+S/a7LJ//1Lf/+Nda+0eNPP3Rc5+hpOuq9jOCPOvat7L2CaQlAmIkrcL2WeI+zpnx8T1vP77y9uMzb/8A/bTUZ+ivifcHiFdcf4bQT4tPi/mRlIKVgDleH2AN7uPK/kjMT78UWvjdza9YmKkVMIU3vdeZb0NAsYmbMJ4HP+tOO5crQCnFg2iBI74U76HwShTAF0U8F8m2/F0CPwoucOzTb+/1ADwqZpYK5iYtDucdTDaL34Zvn4s+yz68FW4e/ls7l5n1QbgCc8w7HpA6oOvp0vBx9d4BzRd/3LU9kgqwQVB+nnPrAzR3qx+g98bzA/RtK/DYXhU92Av9PDe985JgKPjxPvZ9S+iFb2D31U3VLPpzfzP3Wq8e+M9CzCkFJPbD9sG033J0XvFPIOBLHAON/wSiPL642Yso2rkwtDNTv9K7BXIGoMv5MFcLkHYgk4ABezDhz8uAdZqw7kEBDGZ1v9vvu1rlU5ffHmbonpvEX9++EcbLB6+GEAwHmfmxnUsgAgIVLAiunyEFnv3ftIovCMByoE8BGG5Eu4CUKQIF/zF0FJAUTeMh6kU4FSwZcCsANynMZ3zfZyhqAfibJl2PIcOQRiMc4D1j87FOOouFua5P+xRKBAzlLv0QX3i4H6IYGlB4uCAZPKLpkAAWep96BRT50vWp22zI9651tslL5V/fvCUBRm6Jdsc+PxzCmC5lU56ceAy1jOL6QtMLpnZFYWElnuwE633gsIeF66yu3ZDmybUSuwOmSFydyqvjzd6xsCbCg0FJhVXtJ2ndRZY+nNe6K2qTepNgZNuHgX6pxZKR1qamE1hVYxvg56nrNpaea/nNcTLpIppyXZ5vCLLM8YszSaW2vDamQG6lixe3d+/UZ2h8bZeenSq9WVdmedmkdiOZ6b4m0fYudjtsPOfLfVz7WC336CQGmrtsRWXc1NWqRcY0Ar2K7+rx3ju32YQl5+m0YLHGyc5jyoeXBR0eLXJAjgWKItWCiBCvHsPOvm1qrc24ydtpbXsWunxAT7UkOF26N7LTiKo+MpyJo+idzwC4QGt5VUnhTY6MYCzV1qzyFZffza6xpJG4qZuUDJfJKts1ApnSrr4ipOY8xSUZV/hC7a5CMrLDpTvnm50lSg3vOkPhLc4X1Z8s0CItb26hZHqW5Xqn1gfcVJzkkoROe1aSg1RF4smpgqucmvfgKlZ6ah3Y1jtj56Y4snud0IrdJluxAynlfWmIRZL7a8qJUMFlCnsy0LihSGwhHP3s3kaxxiQBekZrrW5FfzEOfkRPHME1tpwwaNKcmrORycYWF+trPt3Q3Fjg1bkihSy+bYfjNthfZVsV8aMzyTzabKh8WeN3Zx9GwbA8afv0dE8xirqdilFoCqm6BHgCj14himbu3TaEeSCCtNNUgwvPCxJPOD1D3fa+achwty34c+3E3ZkPD9dIWZg50d6Hkw8f+tN9NMeJMaXd6UIJm+SG2kTB7hXvft77o45hxx2ihH2DOSlq6GbhYL4jDQMNd6kj0+LuKlpTtbxmImlM5abKSNIowD/wk5l8cndANtV0O2XwKg1T7zYWUaxoDWVhrJvTWyZOvWM1MJHR3FkirAXsfrN6FDPQyynGs2O6dPtRzEVpR3riWSdrv90xrbXe9NlOrcndStsMLLyzWZE0d6vd/l6R+jVIkHuFsyc8W55W95wrRc7Y26645IxAiKVAu5bqwdCkUZWnw3LFaXfT3jXnOC+z6ow6hqn4glgSV0+CTde2DLqxjrJ8vAiwfkiiSQ+Oo3S70AZpw2MW8r2eb7vrhLA0Stk1ydliiA88WwRSZij1BrkhI6zH+a6l0D43dincerCh2zdrIwgXdRfbWGqYGx32fYNWCU8HWSaXPDBrEuG1cIH7ujwxrCLtVUE+YKSAEv6A3Re64ljjliVvmjOQorTa76y+WlWNJ/PAysebtnOMxl8wtqssnJu/j/I8U7Vadw/mljRpVHQIPvVOyyvWuNjJME1Kc0GjjAEnZlx7z9hxuS1Q6WSFuh63G+Vop0fkdKe9qeGaLYE54UGUo13cO0WyRvTSJWtXCrx7cedwJVjEZUi3a/M6OCdKdKmQTEcs55caF1wzTTwiZ93dKsImt/puwyM9T5jTmk6Xq0JWqOjg3U383IhdO8p3ROuN48lI9jIDhxtrdeGnUnA8E1fHY8A6OKO1PJOmuCMu7wRnDHCPIBxWEGt7hUfl4FvBNrsP1W43YOtSWkUqc+CJieF3EX0NlTRut1eQfbbhqCdikdCx2eA33hgPFye3LsQ5Z41k2OUknZBwr5l3US0z4dTjpmxsqtYpbXGjlQcjc51wh27hi1Oqy8skXW1UCsdJVxNxBEGnBf2Z3DO54rOGwAqenqqlnVVZrQ6XnOIIf3td7S8q29MLycmlHV2sLFhAIrojdFXOz8hZXZ8X/dGcglyxFog+1GoRyK5BkbBfGAwVnoh0cKYDalwasmREUcvlSOj2LbM0fI7rlzJb2BZFp4O5xCPb74dW23DbaFp3+GJCblGB32oM6SWPgsXbeUUkwWbrS9PU+HIyqCpXuFdzZ2MXTEs2jnFgzvukpWx2OKBY6enqfu8n2EosQZ07qvxibHPC8/OEO98C3jzFiBEcaIonVv1A8ZwPG1h1ES5xgQh6shTW1O3u7lL/HOtgaN40RzPbSAfvWvLZwqJhU2+vmzTPDqfTzu2tGtT9mOAKrXNJJ+L7WNyzSK1dTVSiz5JSKRsF09xAwhYlth9Ld3nTtAPLkpvWnTKqLJdCjNuMVi328bgZkNJ26pOB3E8ZZhYXbH1IkWsXFSY8SclZ1LzcWxQnZY9kZZwndFLcXYZTVtmIeyqMrntW1wdTEROqwi6esV6TmHbMZA4nV7qRrdwy2l8br4wW67V+LWkgez/26yKv9uhJIuDSIEvuYu/aLorZkT/GlCCKy73qOXl3W48nmT3aDa6u9rdwci25G/k8XqdR6tju6TK5MB0JMnaz9htJ3yTbfoyBQRhHt0nPGfXR0gQu0zkDNOU3pxD73XGfG50spsIonBoLUZfhnUdDt6rq7Log2h6JOrxaZup1XfCUUC7i4OA0ghfTE4ybobu1MnVThIv0aPSFqEu4bMrnHVBc4EoToxx+FYm4JZ9jWsf3CsYt7cDLo5owd3y8EK6pttUOUbyTDU23Q3NkepLZ+Y5AL9j10kOY2KeuW2zwgo2wG336ctrqA2x5VE6p3To3AFPVXF7L0+mAIP1xkYXwoNjZPZBParDkUGa9sONcKTrnvuhbwEFLK7Kqij5QC9jW6dyoIxfD3RsIh1Ia+QuxLo5djRE7mVtzCYstdwJ5psy9ohXtmhS89aFXwxtfhlFBI7vRTdeb5KLWNi9X4ZR7+SleXu5VbqpUv7/U3X3lh5Q71FeTY5YYKQmNOZXxrQnG+uSiS3Jby/EgHERcdEHbqIY25/qXqjisTOFYXer4hm9UXgltq2pRZ+BylNfO+lUnsiu7JMkrUkuWpJOGg06ufvfj264Yun0E84eBkcXx3FX5ec8NCeD0CauQS6ScpB0vjXZYCbKw50ff5fa0wwmDoJd5XXPwhSW35qXNWv1swR1L2GlfU/7F8HnbjuIcVpbbtdHlJ6Sa0kN6aYV7TR32mclopsQ2w5ok0Q3oT25BI0XVXV557onD9QhXjbY/7U6tQvvng9zbl4UYnPelLxzAjidBMezuMdr5JG9tREOvecGkBc8pyNVYWEbUr85G4sFMa+rHRXCd+FMq1ye7AGSV0KtVfEkZAuHBltTGTpU4jW45XqM2dQYZ51bG4ewhzc7CxYtALVYRSNWjthgS0Nd0FdP2G7TRuj171ivQ65JsfVe4mF0EBLPo7f1QkzrgjnYZlo5eGse9gEo1B3huYbeyhKwLapSS0+4uEA2gVOKuB6KwCuLaOwRZC/MkKDPrW8IPRbscA38Z1dtjd7LSalUqS6P1O/6WnVWpD7j1rVFj8+BdVC5Z7IM0M/dOGy5chVZOe2rZgSChdwRCkserYrEbPvQEq9M3poMtb5xzivPVFrYOeZr6pnRrinJza+qqW6aupy1APyT1uKHQxGFFwUjENcpVn9BNQPTKqlgfNQp0MYO48aXNRlwwjb8s9iy/bQ+rYVDWK5NUeE7eqKPSHPabtXwl6D17AT06Q8lit12hqqqUcB6rmR5RitT3wRix2U4cduczL91t5bgdXPEc86aycdA7p40lhVfskBGAnu0N3aXWxCQ9fmSR09Kn781lV1gLz3XhZOdoJq8Sywar9h3eVDsjKrU+QNeT3ZCgi0/VEOwcLPy+3TKr23FbWaZHOXUAuvK6No7BNdh2w4JxEU4q7C1JK6YyBnJMnJk2BI3HVdnsmDSoCbEvdmWOe6UTFPwCc+gVaLgjoQgMv1E2pLdpTlTdTdHhkJfpHj8MZZoGvH/c3FaMbfAu58ZoaFJRYwxr/BTy/krYuvhOgot70a0iFNG7mGr1qL4E4ZbVGn/rKfdbbe3hFC7b41bLPdjq5HQFigW9vBQRhx+s0GvY8HIfIgTBcAvh13FmqjvYQRDzSDOi5IYMdqcOXcPwNZYxI2+l8CrA0u0l3SEbZrEPe2yPkd5ONiOas9D1JsZs2Dm153gnKAq+42x6RNQ4vdA5c7JU/3qHmxJWAsdqErOlMIudBi+86RebENZ4pLq1eV2X4dLHCzmky3FVyalX6qfzSUPUSYBBv0Qf1HUDn/EYQYqohAU4neLW7vUQn6QhDLLOmjbIHgENMqaUqyRgYpnCr0crWMVLQK56tPbRzWIkaF7EjkwKmie4n8yI8RAquYzSPk1h/nJm3XRaETRi2Mtt1yj3EHZSb9WgWLu98GYbC/gmDwoSKzryBlSTJ5gYDq3H2NTF6ZfhCOMTICZxf1gfcaVy5FUQpbtuIx5U2Wg1pawCxmo1mtlR2X2hRBxIBrJh6UjrJQETT1a9DEOB2C79FeEk8vaY6DY1SO4o42Fs8XqUW1fpKPQEDPiQELjOTkMePg5lQtGovCR9mAm3h6hnmfPKnNMvilhrRfIBz9mNz6ZqYIX5eT2qu4g8bDQbwUkuCUvM4TQYuZqLvOPllQTvghhs23HfslOyP+RI0YhB6uX2okDCdVt0eOsH8DK+J53fXhCu38DWkrgUTgdi+u51QyGVKqGh4ZqLiHx7Pm5Z7CBvo8s4Cu4AIjjwTGaiCXzTHI822Nyy0/W8dk6RhzaJt1D6c4ACOXOH8qmg0Ww3wS8Lc2C2G6Ne4fEQcUd2pTI7KYQZ2cNhTORV4XRB+JtWBdvCWV8Iht/yuRWZPFLK9qZY5MutQKtrtbhRVOxvcbTHYKqi0RRvbqRMUlQzHLLhQLQHBkfpJaCBNBhx+lIqtxZ3EYPe4yKjE4scu4XENvEaqfeJ/r5EohLsuHL1Pp2Y4eiP+a06DyNXtTE1JBrPkoRbUw5uRwS1VsOLm9CA65pcuh1qWCK0aKzdVSmKatg0RB9G1GjygQCqVn9Ug9CpfH2Bo9Vt4yc32cSRE8GetKprCtZYgI1LzArl0Il2LPkLzO/9MNk61z1juOqErm4wk0lg57ZDzLRelWp2kOpIr+DCyNljQtDHtO/qoYyu27OtxOy550WiD1grpwWHNw1S9yYbZe/V/cTZDrxZO+vUZvZKHjSKFZ8Dau1rnhYwNw/swAZmSROsTt2ZRTVYd85de1uxCjviFjN3Ggk8UFlwTzkVWxZfta56Sx09TdFktJc1gnKrE0LuN/cmOlLniVUidAK9EhsUuwXOlJJeDgvLVtVWViyvZ29KrfZXWqUuHrLyj3pyJpuLwmmLjuHXGdpsS4RmI29VFlRbsiz797cPb/OR8+vg+K+8F54P8v6fnSc+j/6+vUZ6HBqDDfDnx1qf/5JU//jw1vgpkOl5ctpmffw6ZPwv56Yf/433DzPA9HzhOr/zGrtvB+2dG8+/NfSWFkHfds30tS2z/nF4+wEYsZ1/gaH9+jqkfnuollfziXfZJQ/UWZL5NyaA2PP7VHDHDW6z6vP5aAqWil9HyMA9rtek/te0nlV7vcCYz1vnNxhvv/1v79/olZIlAAA= -->
