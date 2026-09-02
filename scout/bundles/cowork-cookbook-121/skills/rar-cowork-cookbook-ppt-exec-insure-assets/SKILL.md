---
name: "rar-cowork-cookbook-ppt-exec-insure-assets"
description: "Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_insure_assets", "rar_sha256": "92ac541bd331a15feee568f10b36ab98adb49aadee309b23d3a5ba05a3e83e28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_insure_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-insure-assets:9d66857c91fc9dfa833e8b2dcce324390e5a51d606612dfb3471b9d539353154", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_insure_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_insure_assets_agent.py` is
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

Insure assets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_insure_assets_agent.py` and embedded as the fenced Python below (sha256 92ac541bd331a15f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_insure_assets_agent.py` first:

```bash
python3 ppt_exec_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_insure_assets_agent.py   # or on stdin
python3 ppt_exec_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_insure_assets',
    "version": '2.0.0',
    "display_name": 'Insure assets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on insure assets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fe5acbb1d88b703',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecInsureAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecInsureAssets'
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
    print(PptExecInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxpbvV2Fq/rA9qi6xiK1vOOJJCIEkhFgEErgdZZZkkdjEKvDzd3+JVFXdPbbvnRsxEU8dXYUgz37O75xM6vcnp6mjvHz6/KQDJ0MEJ0niCJSIk/kIl3d5eYG/8osL/yNentVl7DZ1XlZPz08+qLwyLuo4zyC5ADJQOjWoICkCbsBr6rgFn0rg+D2i5B0olTzOasQH3gXJMyTOqqYEiFNVoK6QqnbqpnqGItIiATVAuriOEC9yyrq661I7ySXOwk/FnUmWQ0EvUAdwc0aC6unzL78+P8Xw+unz709eAtlCnZSi5qEm67uo+V0SpEmcLIQPix4ansHvBSiDvEzhLR8EyNu3HyuQBM/If/3XpXPKsPrp85cMeft8eRr/aU2G1BFA6typauAjnlM4bpzEdf+CzJPO6SukBHVTZlB/aF4JlX95UH7llBfIz+OzHx9CXkJQ//jlKS9GR0Kvfnn6CclLKK9sxuuXkUvx408vyejNH3/6yqdq3DPw6pEZ1Prl9e37G1u48OvSOLhL/RlyfcTPBV+evjFu/Dz0Hu2ElE8vZ+jyHx+MizJvQeZkHvjxp79j60Uwwklc1f8jvr88GEcwTaBNb4r/9Hx38q/I5M2gD55/L7aAYf13LIHL38U9I2+O+jved///N9ZJnMFcf/f4X7L7K4LJz8gvf2vbPyN4RoIvT0uQwKIqHTcBn5HfX3WF5375wf9684df/4Cs/yUbPW9K787hNXWyOABV/fr6yw/V/fYPv/7yQ1PAXANO+tqUyV/x/Cu/3uV858G3VT9+TwvlG9kly7sM+ch05Pe8+I/yjxfEdJLY/3q/+ox8Wy/jZ4KMRrwLfbjgm5qpoK7f+PGnpz8gLGTQmsa7P4ZV/p//iexir8yrPKgR3cubGoEBruMUjMoforhCDm9F/Zu+XUvSS+r/hsC7Y7lDiHCapEaE0okTBNbDGPHRgjxAfvs/3h0xP3lviDktivp1xMLXB9q9PtDutxfkEEFheRmHceYkiDZXFMQJAUQ2KOaeEFWTfmpHSVCL+IE0GrceUaZqEvAP5Le/Zv165/JS9KPCXzIYAQeGBcInSIu8dMo46SHkQkRy+xp8gugJUaPMk8R1ICqPP5riZfTCMQLZm2+8DzwHSJJ7UN0ghoj7DMNb5UkLEXD0WHWJkwTx4xK6Iy/7O2ZDr34emf3222+uU0VfsgfkEsijb1RTuOBDYeTTp6IEQRKHUf0lA16UIz/8/scPyP9F/hnVnfkoQ4H2370E0zZBNvpeRmANNilcVo29poYAc4/R73883D9qBzsWAisnDmJwJ4bcvgZ8tOARk/eAQJtHFUH5Jul7vyFdBP2CxDX0Fqzm6vlLNrLI4dKyiyvw7sQH8cP17xF+yBljUr35EMYpKPP0vvaea2Mwvbz0X5B1gHx4CpoL4zr2SCTKq7G7FiDzQeb1kNKpv4YQdkykghVSBf0z0lTQ1JHzby5kPTonhTDk1L8hO06BHS1P4I/RQXfxkDrP4jHwbyn6uA2ZlD/AHFu8s3hBZAC9iRRO6RRR6VTgvi5wHhkBO9k7PWTuIBnokLFhgzFG99q9Z976u7mAfx8kvh0hluMI8aXBUWyG/H8YO0Yt54Kg8cL8wC8RXj5o1iOlxgFptPAxU8FRAIGjxKM+vo4H70jyjrFfsiSGYSj7fzxWBvcseqx54BZU2IcYod35j/Vc3vnGNcyFMbhlOeav8yV7B/Nn6F4YiWrEJViylxEA8g+B49N3TSNYl+P3r40deaTZaD1MYKRo3CT2kAAA/57rdTS69t37MDHAWFUw9b3oO6sQyB0GHfK/ex26EwL+3XUyrAjo0kd6fyyPx3EJauE3HtQWlgx4QY5jBsMsrBAXwJlnXAO98MOdFZIC6GOo4oeHq8gpHsqMQ+ubgs4YizyFCfJtBN4ehm+5438tNcjV8Z0a+rKDQYCVdHtE9kPPt1hBZdMx7e9E34f7zVbk267zj7HcoI5fMR7O2WPD/sY5EKPL9JF1sJVeKljQKXhLIJgJ99788mivj/79ocvnP03qP/57w/y9YRrfR+4zEtV1UX2eTh9N7b2nvcBamcIciQtQjf3t01h0nx5l9elRVt9xezjnM/LvafQdi7dU/oxgL+gLOj6SYg+Mufr2gQ7gPi2sT7Px6ZdMA18j+xb+Eb4gpLr9Rxd5XwJbSViCcFz86CrV2Iw62P/uYHbvCh/Rf6sNCBBZOLbAKv+mZkebxlg+QvUBuvBRNsK5Pw5pIRh3LcmofgWePmdNkjw/ZU4K/na3MqIpzErognFnAysETjp1DO7fPqae8cv327F77cCi9/PPYwnBzgUn1GfkY9h8Rt7H//s2Kmvg/ueXcdAdRcKl8NfH2o+9ngue4C6r7otR3ceeZpyv3ubePysxVg7U2ANjb84/SnGU+Ccm8CIMQflnJvv7hZO84QGE7BGcYZt9q+IK6unDmegZgQGD1QULBuJgAwn+LAbKKcG1gR3WH8396r+vZuUPW/64u6F+bAx/f3rHhfH60e4fyTLuI//5IDY68r2Bvo7snJHoPi7d/XofJ1+hTfHYKL95FI5d//WRcU+fIZSA56fRe2UMZ+ThvuV9eugAlf86iEIOEBQ+VWPjn8KCgZxgOy5GxWEn878RMN6O/fv68eLzX02vf1Hdn1mfohiS9lgs8Fg/cBiCAIyL+54HCHxGsCggHRLzKZSiMNwPXGJGYy7rkwRLkARGzqDoMWap8yZ6io3ehkp/uPR/OEc/Pagg8OMkBclY3PHIGeb6BIE5GAl7FiApJsBQl6Acl2Uc352xDtxoAgJlXZzwCYd0HZR0oP4EwJmR39tM91Dl9X1+fvf/o7RfIQSm8ago7jge49HYzGdph4L2Q1EewHDMpwmAkiwRMAyYQfoP0rcYjCF6WDvmJBzn4DDVjnJ+f4vpmGfUDK4UZ9V6/vhwU9Z0KJx2tcidlBSwyIBSCeOKXnBaV5NLS52LvXzhDosLicfM2mx4ud/wmOxp5z26po87mROphYLrgUV7PV/omdXGzDEObWWdLeVsaA2a7DpT88XcdFL3eOaa+sA52YkxjkflUh8XLWbhOdEXttDanr0KKvLGTq2YXW2PRRMJDmNzW/WQtgsGxaYqOnPNXXZZpWzdCBkaCeb1pJ04TrTOg1UkW2zmWkU4dLOqPOpUlhxNfRt1xhl1MgljQSYxTHCaTrINPgWn6e3kDXCW1q2Ed+bx2U+LY1HIaR85qX00yv3OHHpzcSCWbufyB8eQo1WvcEV2bOUZ481U6WhF83m+TnfkHLdvIFuRFpuwy2NVGKl9ZXaCDLDN3hQdjN5G/iLtzjG9Ko9HQ7JVXDNxgTWARtWLITqdttMre62P2FZMbc50pINskM6B5pjequ2ddVQbtYimp118vV1Lk7oaZw6zlh6sfxxnBTE8CZN1TRv4sI0avThXZ2szIe01RLdTE29XhXRaTIhUV73evPKu3Jps3zXxBdPRY+TmoUDlTL2mrWMloBMnxEuTvvWX69lZqGo2oSpMvW5a3yzsSbLcZNr8IvvnW7aoJk0umj12Y/wNWZGBsg/tRZnKFGn7DXu67LfbCdzprNCpgGX2ZLOtXAkLVst+ZQ2NBHcH11ptbmphn9IrYRzbaBYC3zRwjzNTpcoCwuLOm7PNXK/g6hqmdZ3Se85X9/r0tuB1ttx5UX+4MKtruuObesmIg8g2k7QUzJ19BKKGJX6qpCxzWsexzEfbnleu+XVHndC0zPnxP3WWB79Ib0RvK9lsp+C3hF4tpuINO5PH1OG6WpqGwSZDqckknc5WMbWT0CA7AKzX84NXEQfOx9x1P4ljdSP2ZLk76vFCKVcRdhJQtU0yPsdPgzGph2zOc+FpXoQh5rAYp2H9+rRXp4uKM26hcGmSzufJauuDLttpltAbG44vLjPdr+RK22pi4a7NPE6t6pol5sFBZxo7n6XlGbtcmZVZ+cE+ZXfh0K4XakquRb7RN510yyhXvtF1wA8px7DD1Wk4l5TmbAI4h679/aqmsJYRmzmuN0oYr0+kG61PbBQzmJ9M9hcQyoGEbWoud4y0YyywR1FvcSy1fWhY7pTSLhM4q54VIjugOADBMbwMMLHV0jaP9eLQr5vdqkx5z5NaHTtvK4YhKmm68xXJRnuwuW7bG8E3ZniiCiokCsxvD3qLRzNVC2Nb5KhwRvQzwwBm3Ea2KWyoLbNpiLT0mevcmJc7TBVBRLK6v8ITcV3vSI+76AG7I1p3lXPW1Kth5scCtQymah2el+B6jbKlm3hV1p/3rnYJtwPeyadseTPPx7LBhhXn74pdzNHztGo4xhvco64Z9HBBdzSvJKvqfFnNkiFsODlnbq1C+PouJezr+dCr9VkNNjuWSrjucos3KJvwmM/v+eVWzoLVvj9Q242NljSLSgnR95OAXc4BjZ8cdWaLylHvtLkRlaKNc3JM2QO6sVy/ZLUuWQmzizxDl7J+agSua0tpUXez1Xq/rM8nghC9dSTj6JDIZxK0RB7gt1mGrRI3psBVWlqDtrA7tRf5UA0woc46t19MtnJ/XB68Bnf4y0KjYs/POHMbE66K4aKh5XN/ca233fq80pfZpTAFvDCzbWqr3aq7akJqm6SlC9u6zJZ2swf9xg7R6+loLi5drRi5nx1xkonD2hQLvoExmsKpc7rDaQ/fbsxLVHAmSrQzpmQOSybvSxPkwTJL5nFhMVwQ9MtFIvms1tNLVTXWBnOchZmCtpo2rYwTBQIxmyZzxm7iVRLUQz4VolDrONG5RGsDlYg4WjhCdOJuFyzSIEbTtZoGC+OwWHbcUY0vpcOAfYZOdhnK+EosSL4gbho1KlF8Za/3QraZs7f93PUPYdKIZHiodAc1+NzYhkbQX03xEO4Pgxjz5lls85mU6+tlmaQ6NpXadF8n8s09Y9u1rULnTglUWHqSXcu2v0+ug1/TieuVQlScuzOxVhe4w0bCiUnjtZK0t1vm5bV9Pt4IS9hfM/OKNyd5nzKzib3dDJPO6k81Ljd7rCiNOqTUg7g2jumuNMIL68nHlmy6BRatL+1myRgVQzbLuMdI2CqUGM+jW3srQWQWAn1oKdGSj+BKEAfdEXJ0tZwyPuhXV9ex7NyjCTFCXUOYbdfcwQBZQjiWdON6zNOXQnjzCENWBo8XrVMnazymm1IekoJgmMklYXm/SkA143G7PHRTYdVE2ErvVbmdDWedNPddXnOsSK9QYb7O0+BK994EpndkogseCLNwqfS+3VHplm4OczNT8jzJtuhJdqenFDjbQVqXVLCQd2pznCYczpZSfQHtxhau0XHVqXpT8qToJGWrOXM93dHtqbue26vYsAtbKfX6KATGUTk02UbnuMm2koHFWuVi6y5WXRGChD4Ji0u1mYC1W+0rzdl40irmigTE5wOt5sl5rjpn/3JzyOVQO5PL7rIzhZCk3Kkf+W6/nBabaqn186NiWPOgkTpXDL0hP+wL93q95rvUVZRDTaDTYNKJILyAfTDXacXel+KUV8VVc6DgOJZtLddViF5vji7l4Rp7lGJ7e2XdE0jNmVusDgJHNIUsTy5DmHLrueAsoef3HZavb4xChRPj2g220Z5ioxVrOri45744nxxZ5fbrY5HWksmmzF5gJlpYcgKvHYstsVvAluHyQpk1k6jWk/IUcPxWuAJZH0xXNydhQM2jtWaUQUxoXsQn2ZqyhiRdwe7S8AyEJiPUyO28NTeyu7j6Ub6d00tKW0oNmjEaT1KnrRtlnH50Q5ncMaviwA4Q+C6b/VrGaKfW/NpDVz0JsxTCp3Ljr+iMYYyovoSbLj9eNkVV+YtuGgQ5uTr4GrrQ1lQh+oc8uTlmo+y2brxbQnRZ2VIqUhspqznqQtU7F0/L1SaXl85FMffFqj1icNBKqkZfVV0C88fZs6is81PytK46i+QXa/LGWQmFldztvD/EGD7ha/YIVOxEN1xetOiC5G2jmsJtoAxpu0hvbptTXMUTxt5fpKHDhnruLUoSlUv7uNOj1do4ROnFy62d4Z0k0eRX6sbBtUt9OA63K19XOSkMYWJsi2xqpRLJGUNTGxKQXZQUDzveAlspCtbRGWDyRuX7laItWpV3NqgZCmc0LDXfOlB8iGkJQ5n1CuMrm3dsFd2y/TVFpYONhyyYHiyTNbTrgBLrbMeXphY6wn5xS1OMPUsz7MIF8r4XVQZGATOI5XnPSqcpn3dhdgzOKdrg52pHl+vG3vKKeDib+lxdLw4T80qq2/ORVs8HwfLSU6u1c2tgorOS4SDHscWMpq3eb9RyKRNYrm/5XbcOKHJmHSV8qKlDvajZQNsFO6e4Nvl+HpkYR04zECreKVibDnrF7XxXS1jXWrotTzZHwCuVuFqlKcCaYpvMBb7c7UNLXITb6rxc+EVsBaIdX+Y3dbAaU8qMYo81cgkzPCbz+ckILCrrus5HNarBaxX2trUqXb3TzIJDUUf5Wlit+JU0W4icq+NLY3q1jjqzvm2rbXNy+3ppDufGaALDz+fiSSWw6CBs83JpYqDYHCemN9XdHScqGEy8FRvbpXvLmsTHJr1GtJfjhWmuUzifkyZJLEks2LouxyhSqVArvD/hs3aYeVQNqGFxq2nH27ArxRJ5FKtOPECpxABUjynHxF9dkm6z18yZ5XfsgDNii68xkfbFi6U2e0akGjvSax4vEubISH20O67li3DVY5c9MkvGXMonVyAY+bqYWLPZcibR0Al7mvBmU5OGG3NFJbSZO8GajpBJtNbgNFjuCYaaSf3cvSxmwc1MYxqXqz1W7TWavk2nTSJOt3CsKGFmYNMpv5ywmmIDFrZETMXTdY1JjlAcytmiFMRuv75MpEZVhyA1xGQXyzAyh02uVkJ7CDH6lnPzIazniqjMXXJuhuCSNWdqOU8DzBIjrHXJnVRne3wmbJcOtjVdUUWBG4uG3s69ZWZSwEvoLkmrjSd6XJgOsUJtw6wuJywtzfWzQqPbLJsytVBQdLxbpzG7HPadPiFO7mnFnIOovmUOBEFqWSi7zdBW9IzudoJ6bpwhd9M1vdf5+jACWO9LkM1UmLIzVl8D43QaQtAtV7Gm6AN5OqmzeoOfaTLdQONch2h2mnkK8KpI7aYu6cmJLBPeP524BTkEcAO0y+upeSuIfmv16y2z3BPg5sq4E1QQf29+CNN5o+Sls4K7h6lfTbE6nZ8X1nwik3rQWpktZXCLs+3BJOpkwpKGGnYrZivHk1W9FMTWMKLYxTVbH24icaXnUpblWyyG1PZkZWenIRAXzDSIBrEK6rmvc2Z9FaGpDa5Ii3w5yH5u1rxO2G1YGUsBuEtDEnv2truakh+tJlIhUcrhvJ859KKuZarEAzHYwFEFZwh3D+Is3W4Vsl1MDNputAwW5BAtAE7gfIDzN6IjTqhry24Z4Oegkble3HfBcd7J09CaYJ217aM5wbLWoFjN+rxvyiBhUzLGsmvVdGDuyasQR3liIXkuyJRbXcW+4+Z0k6LlMTrD3Wdk76XS41oN94yJtei4rdSE0kJRm8bfWbyxJAVlEtpipu7OFwaWMpc3vUNFRzZrl341tNGqFebongYSL96yI+HSLJbRrjuhSEZkZ+aJFjpVnNBwEnUiciGwFi22ZjOssMA6GZOO5VQ8d+hSrnp2T2wIcze0W1ep2Ek8ma4jXpmc0GXNpiwrGutbolzEI7/Nw5WSaHCTYAdTrzqAq1yszpLte6yP09WpFylbVmewS4CynMUgoBcafxCCCO6LgxswC8/bEXhRr3BCtE+tpBkL37oKV2I5OWPodhZ066VWq9pNPTJ7cMUWztbmWpWQbScmpqBPZijNKRtnq3o7fV+WrU5OsnPKK1E3Jaq0Lrt4esNZhpwv7CoKlrWa1CEbsULpXdtErnDZknE7ZpVdy02qCNs1RXBoTUI6JSigRP6IBkqDlevltCXNTbVIpvFcZFE8wTXOPUnXPUlXMJunVljY0wFzwAxOk+fGNHVw1rW4p03/GDhnzZhO9NUgtRk4u/NMnJHMEptrt0HeE/Ui3giXvmM4v82vy+ltpVd5r7vDgVa887J1/Vs0CGsrccnYazKVFKfdCipN87Qezufzn39+en66v2t9+oyhsLc9P43n92+n8P/6ODcc4uL1jZ6gUfb56X/vBPJxGvj+Lu5+JA8c//Nd+ud/pdqvz0+lF0M1Hse+VdKEb0eN/+089dNfn+yONP3jZfD4evBWv7+gqJ3wftwcZ35T1WX/WuVJcz9sho5sqvEPP6rXt4P+p7sBaTG+NXhXGF463v3Y/bXOX/24KvIKPI1/mDG+8wJ+7NTvX8O3A/nnJ7+HEYm96pWgyFdQFqN5b2+CxpPX8VXQ0x//D60Hf4LAJgAA -->
