---
name: "rar-cowork-cookbook-adaptive-card-define-warehouse-management-kpis"
description: "Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_warehouse_management_kpis", "rar_sha256": "fc3c4822b021a590d9e07ec27f6c19465c8a47bce7b50cc2959c94252363ac37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_warehouse_management_kpis`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_warehouse_management_kpis_agent.py` and in the RCI capsule.

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

Define warehouse management KPIs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 fc3c4822b021a590…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_warehouse_management_kpis_agent.py` first:

```bash
python3 adaptive_card_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_warehouse_management_kpis_agent.py   # or on stdin
python3 adaptive_card_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_warehouse_management_kpis',
    "version": '2.0.0',
    "display_name": 'Define warehouse management KPIs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8d95805d858ecd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineWarehouseManagementKpis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineWarehouseManagementKpis'
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
    print(AdaptiveCardDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816adejxpLmX9G8/cF2U1ViE4i6554zSEILq4TYXfeU2UGsYgeP//skkuotu31v97hnPoxqkRCZkRFPRDwRmejXN7ttoqJ6+/x29e18cbDTNI78amHn3mJb9EWVgLciccC/hVvkTRU7bVNU9duHN8+v3Soum7jIwfRzVXit69cLe1H5bW07qb+gPRvc7vzF1q68BXuVxEWd22UdFc2iCBaeH8S5v+jtyo+KtvYXmZ3boZ/5ebPgzqd6UTd209aLoKgWfub4nhfn4SLOF55dR04BZNYfwA07TsE7GKP4dlZ/Apr5g52VqV+/ff75Hx/eYvD57fOvb25q1+Crt29azUrtHiro3zQQ3hXgyni2MbXzEEwpRwBSDq5LvwLaZOAroPzidfVj7afBh8W//3sCTAnrnz5/yRev15e3+Y/c5osm8hdNYdeN7y1cu7SdOI2b8dOCTnt7rAFmTVvlM3o1wDgPPz1nfpdUlIu/z/d+fC7yKfSbH7+8FUAFe/bAl7efZgi+vFXt/PnTLKX88adPadH71Y8/fZdTt87Nd5tZGND609fX9UssGPh9aBw8Vv07kPr0teN/efudcfPrqfdsJ5j59ulWxPmPT8FlVXR+bueu/+NP/0qsG/luksZ1838k9+en4Mi3PWDTS/GfPjxA/scCehn0LvNfL1sCt/4VS8Dwb8t9WLyA+leyH/j/B9EpiLH6HfF/Ku6fTYD+vvj5X9r2n034sAi+vO38FAR5NSfi58WvX69nZvvzD973L3/4x29A9H8p5lq0lfuQ8BWkZxz4dfP1688/1I+vf/jHzz+0JYg1kHlf2yr9ZzL/Ga6Pdf6A4GvUj3+cC9ZX8yQv+nzxHumLX4vyf1S/fVpodhp737+vPy9+ny/zC1rMRnxb9AnB73KmBrr+Dsef3n4DZJEDa1r3cRtk+b/920KI3aqoi6BZXN2ibRbAwU2c+bPyShTXC/B3zu3KB7jW8Ux7z3Eg/mcPzxoDrvvlf7oPNv3ovth0ab9o6KsLeOjrkwu/vnPh1+9c+DUBXPTLp4UCVimqOIxzO13I9Pn8ZR4BuBJoUFZ+7Vcd4BZnbPyPgJU+zh9msvzlry309SHzUzn+8qgB8ZO55O1pZq26Tf1Ps+V65OcvO11QNvzBd1uwXFq4QLcgBtz7ASBSFykg/2ZGqU7iNF14cQUgKarxIRsg+XkW9ssvvziA0b/kT5rFFs+6Ui/BgHd1Fh8/AiODNA6j5kvuu1Gx+OHX335Y/K/FfzbrIXxe4wy4/+UnoOGjFIG8a2ezgQuB0wGpPPz0628vqIGYHBRC4NU4iP3nZBC3ie99w/16pD+iK2Lh+ABvgHVWFlXzKFHNp8UpWLzrCxadb83sHhV1Awpf6eeen7sjkGoDc96RzEFlrEFw1sH4YTGXxHnVX5zKfqiYAQKwm18WwvYMakmRgv9mNR+DwOQijwH871Hx/B4IqX6oF5tvIj4txDlSF6Vd2WVU2a81AvvpF1BDvk0Hwu1F7vdf8rmCPiLkkTZPeMAggIz7cunH2eegQchANHn1t7UfY+y54imPyld9yetXSoDwA6i4oESARcM29uZC8bdXSIEGoU29B35A01nSywveyyuPGNz9V+3D9dk+/LEL+dKiMIIv/r9pV2ZL6MNBZg60wuwWjKjI5hPhud2aZT87NNAsPCQ/sul7A/GNfr6x8Jc8jUG4VOPfniMffnmNeTJbWwEYZVp+yAdBARCe5T5ido7Bqpqj3f6Sf6P7DwCjB7cBt4EEBwkwx923Bee73zSNgKHz9ffS//AxABNEBYjLRdk6KYiZwPc9x3YToFU1593LJyCA/RnoPord6A9WLYB0ECdA/gIoEYNMAiXhAZ1YADMBzEFVZN+Hx3NDVT5d7C1AP+t/WuggdebwqUG+gq5oHgNQ+OEhapH5AGOg4jvCdWSXT2XmFviloD37oshARP/eA6+b34P9ocusPpAKyLcBWPYzFXv+8PTsu54vXwFlszk9H5P+6O6XrYvf16W/fckfOr6zP8j69BHB38FZgGzL6gfNzqRVA+LJ/FcAgUh4VO9PzwL8rPDvunz+U9//41/bGjxKqvpHz31eRE1T1p+Xy2cZ/FYFPwHKWIIYiUu/fq+IH+dC9fGZbh/f0+3j93T7OBeqP6zyBO3z4q9p+gcRrxD/vEA+wZ/g+RYfu/4cw68XAGb7cWN+xOe7X3LZ/+7xV1jM9JuOoAS/16JvQ0BBCis/nAc/a1M9l7QeVNEHGQOffMnfo+KVM4Dr83AupHXxu1x+FGXg46cL32sGuJU3YG1vbu9Cf94FpbP6tf/2OW/T9MNbbmf+X9z9zDUCxDAAZt4/gXwCnVMT+4+r9y5qvvjjVvCRaYAivOLznHAfFnPH+2Hx3rx+WHzbTjw2a3kL9lM/z43zvCQYCt7ex77vMx3/DezlmrGcjXjukeZ+7dVH/1mJOc+AxoDi61mXb4k7r/gnIeBDGPrVn4VIjw92+mIPQPBzFY+bbzlfAz090BMBXu/mXATpBaK0BRP+vAxYp/LvLSiX3mzud/y+m1U8bfntAUPz3Gj++vaNRV4+eDWVYDhI14/1XDCXIGTBguD6GVzg3v9lu/mSBlgQNDhAXOBiLr5GUQdGEXtFwR7lw6TvomRAuAiFEyt3beOk4/qks4JdF6VWlEvh6ArFCMx2MRLIewbs17lHiGcNUdt21y6J4B5F2oTrY7CDuT6CIh6J+fCKwoL12scBWO9TE0ChL7OfZs6Yvne+Mzwv6399cwgcjDzi9Yl+vrZLSrMJjHfEyIEqIqDrG5U0A6d5N6/RmrxGjmqboahitVPt3e5tFGrslWFF5jJshpShQBLtKDon2XPr0Us6vuaHK9lOgtiedSFk3CM78R6J77gw3sKqhCB8ctVIVrUR0WEVc0zHFlGNJO1yckBO1XRNbWR/9Ut+W1F6kSo6KCcNQkH7K8UllM3WCcepjaYPZWJP5yqHnOAcuUhqen7GZGYJ515jNUh2RQSuMVMta8s1a1xaNcuN2twL0vpAI5sUMtcrnlVc9HhCpPzWr/ylkqwk/RZBvLxeeTmGB/FKu7ODdNGuloU0ip1WlVk3SFlxA2uN+yin6GGpWZG7J837SSdUwonVVWBDGXlTJVYPwjBF1EZPr7VhjXLGp1MkjTqL7M17vr9cjfJqO7cjDXfaFc1qGqoQrWzcdG+VLF9xK6EdUFHM762r3oh2vIn2yuDPe6Z3Dmx4ZbP8NI0dDve5eU/VQ90lzK3chJ24d7KNfjhH98o6I1OeMCzrOUmMhiFH9sR4P44W7uT08mBYVgbD2OEKAJUEPzPvCLc3qw6pTrPJDmN3giECHx6XQljLh95xyvtOrw2329o6z10RS0w6TJRT++5gqq1fE3O3ppSyl8udwYyppbqGe7z7IJ0kBkKhPM8vTMJcfNKtwb4ogLnaa4kt6mMU47eH60nS0KCxhvZo66qs3pvBFG4KOm6hRmdbcd0x22nVEsrmWrP1ZRWgvZaZjdLDLiX65jjky5jYT6yxmzb7qEJNPN9xvtKrtdsDhM+nQAxakrBjTNP2hgllo74Wzseqr+XaKsKTcQ3JZCKVsohxTyquNlVkSCXzlZSmhY4sGdTv2iDsz0F9DXa382AHUR7QklyRcmyzPRVQYSqeS42izkuc38BWfl9K/e1iCbsm5v1t2art/VZXbHIdPf2ubVv7yB9IZx/VjKeawx24CWGc7YRjSWUIWl/iJgN3lp/gq32VS0a4nvr9Zp+Iq8hGFJ1bub0tbE5HGqCFjnK5x0/c6uidbjSbNYyu0MblmvFmXd2n4y42Jf7gkql82CBLwulhx5vUNjZjBFYkUTtW2T2aFPXaHoxmwO5hslaE0V4Ka8RxTquddW+6xgtFmFPXZBzcz8tDH3XUURqudknpxwtKjO2qTiNKuFg4cooVR5dFrRGHYRCGW1bzmI2K4ZHGG1vLIT4sue4O45NFFMczLXByV6wr+ibn+9uxkUxuf70pm2aZ4pHfwS0h2y1cZOKym1aYGmuDcYtSte6DXhs8fvKz1FlppJo4p/5eeSFzPXti7ousQOzVCi09LmrL5U733GZPNBpNj9OwWdnHvLdctXZEUy9RXKSrNXKCCrvrYqYogsDXWbWAhXu+Yoh4q413jvGqRoOvgROoqz3LmkZTMHV7PORqaXldJh0JWbbS/bAVj5lruTYypdwWqxR1HCt4dK3VttW8dZWGNs/QEwLpjVXCJrqCyj3IdBZmjtLybK/YnGGEo9VYqRyJ3cXfQUVtQomL3fc2Rgr7EOKkyjt0I3TIN309kPdALHdHi1AZu3Qs0j1MPSQk/UghJ3+dcpzbQ1iC5Mx0mOJ6iDarofCK8bKOV0tZDc461W9tlyxSVrII/2zAltBQd/tGTuE9Z2sIdpNLvBbUkBW4zRguldVB07OTzNRyakrscXPapjLjDJLf3DGKl6ne4ezoRNBUZYfVzWJAGOGq3p/gVc9HsCBcE0FDwFaKK5gRtnC1GibEqOJtcmuy/b7bous2RCUKGdbXSVJ2461eE5BvVARxzlen4cTqmV1bN4UwNJaVYyPIxKGm4ou73TEExY3WcblKaB3Gzm7Q0qG3vx6Lbul3no8FbdkFLZaKLFSo5z2/LuzzwdRIopS2V1on6RurxLB/7ad7H0KUwZXJVOxIAcNqxVY4kRV7xrjYMeGHyya29qKxEq8nUYJYbrU1s7uNtLt+zydrNh0wQh0Pp2sm3CXM3vf4GWp2vLLpLkZnp6rZ4ISL2+pImkuKPF/2QnVbSqN3cMpQRsQE5PRwoKmN5U3i3TH3JcIaPXVf86C6eZ1JltLliIdOoqc33WiLuiDF4DYIOIxOB+N0Zg6CzaPXC4kJjFeSxnIINFOIkNxYb1jGsUTVLe5VnsKp2HmeIsgNfrsAECpyD4/7kh697qDUezceEA/34szQ5HN2xI432re00E1rkjv495ILk8O2wCumdRRNZNi2DbFIu2MsH+5OG36nI8KdlA+cw0QS3d4hu7VbPo8LOlNJMi5atrxGl1OdeuE5ZM4hCXHlyCmeRdSdMiRRwkQcdjmYueUjdoKajX0p2QRX+o3RuzIW8cSu0+7Ojbcv48Gr8a06XMatjxk6XFsnrXZP5uV6NMklKchSfSUOUH7T05PB86jljMh+JfXW6p5lmZqaZ0rXCDeubc6B9ZApDNEfiV0lGdC5vcQUpw5WbC8L+JJQBzvB4mtxX18mV9TOhTmsnYsE3epEVvoV557IYr8ebIyRiji+XXBNvni6pTb4le5DOOPX68AzzuVRhTk7tAk6aOFzExrxxfPJW2K2/rbY1Seeb0kLgwWYSKg7we04QhjpMyCmc7IKIKJgNiyB8BuDOfoZGeTbE+7lVXu1oeZWeSbUgt7DCZT7kJKCcSJSjwClFsUuIiQe6P3kU6SnXsKtw4W0aZ55EPy3SmOlTdfsyq2zERrl5G6uXodF8DXENJ0F27UL4oqBu0m5TthFKFCEtfvornFtjEup1nd8u7yoFVJUgWR7E1e6VXG6b8a7ayHUdDQ34XhY7zEeGe7MLTOJgAERxsapgtxCOEH2yUGErPaubqw+3EzmPin3rb2ipbtvnYkQGeFWRQ0Zukx10ZyO65YL0L3QD2d20LvyYFx3e85XfZ88taurpJ7ZIzME0Ol0FZIhxtOTEl1dHrsky+Wy57lClSooxS3eVZiyn1Q9sW19OEz01ULL/lqm0KaHl0W7F9DyBpUcPRSjZUk8PNRakNmsllGXOh3F8tAMTcV2CVL1HYo2PLMrLHRnrDKsqpFQOhBcez4IqQ3alkRRBtxgkG5/5u554Z9GTAHOSnaa3N+6lUodYIdMydTKlhnNrtNBkyXZ51H2GjNbOEMULLZUskuE4kjEpsOZ91XF2uYoGiLq0h7dahSWLYvrfj0WgBJD1K/yciVJEn+Bz+oRDbZ3ZKOmdMCqzYWhaK3IdRdthC18NOE9xCFi31VKwtTall1dVqWoKKlU2W5d88tz7mi7UC1tBh8Dd3uaQK/NbfbDwRLSawuRzWk17eoIXifJXfEQuRtZCsMzfqWG+jkoUcmMMZI9pZgm7rvqEmqA8C7bCOe8ca9JUa3oeIbTJYINZLj2cDkiJyIQLjJtwgGZGQ2MjlOD+MxYbjfa2qxAEYp8znUw3o4cAgJrFtEWlpn9zWSNq30MBzyYdCuTDY8aM8LLYMA8yiFYnaZDyYdm0UjHMsjUVhW3/HHnCrtD6DDxDnVD2KyGTNPDbAuYcrQCXama4Gazhzsp2fQGOcJot77D3FSsoAB1N8o2Oe1R/gAdpgoXpFw1L6ic6T4T4ortj6ayHi7wbbwx7XS33LMX8/eVRDjdIXHwaqszBg460VzXECvgT3Q4c8JWAdVzRRTESc2VsV9yxjrEXNrnXWJtUn03QDyMHM2lr93bzhvLlbsyDPLGW0cZ9IWB3m1HCt0MwS5VOswxpX3nHCMpsU7R9YpIiBuTSqyp1d0SpQk1+dOS7g/0kavcm7dBNpR2Q7AYAewNCywdq+lpKtexz0jYfonUdI6Hh+6WhZq26s7h1Gfrqovp/c69BGsfqlw9vKGsoSOmurySBKxtJpuQ9M0tGCBjXSKODR0iAasrh7zT1e5IEbubuzVCwye7jX+bRv6MYga23OzQyIhKQ18usyMkZWmz9IkVRRjELjUa4Dv5kHShuS+SAt+eB5dSuN0Ulq3V85q7pHNP3pwE6FxWmacyjLGzE1nwza6Q5Q2h+Pg5lLbycp8ER2ndwfAddUkyMen9aLRy7e1kssVFyx7li+T5wZh1vmoifTZ4/YlzBGFZOHEgwC6kn2j81Dpl3JyWAy5QCHyYruxhvVZFuoQMLLho686tHVKAo6ToEdorcJqyABWHphAe4mV+MXZK01/OMpTdAre6LqesQ7qlfpZgs9iSBX3G2fR0qureE7uwlSLSm9Z5mZxazKa8emMOm52plaNV2RCVDgEp58Z0iDzct8++600CFki4oZAbMWRAkqfO+bLW8Qg0TZeRaQWbxY615paMUssxZQUZX+YtE9LipLMEtHVVpL72nQav1xguwuaun25bIdjW44bWsRimiI0rs1Dlm/XacW4kfc5Dk0N2e/yyXR7iYzdcMDKfUN2LDnxx1mgvnvwrhg3p5Ms7IOOA0rzABEZThYW6O8rOTj0cKajPNY13I3F5nHicUyIJTyEepWy0Ibuqvmyxg+fv6ryT5UnAz/siglRSae2zvFLZMO4MmYyMFVxTtYg0h1YhVgiCT6vh5F5W/g1sD8W1aEoDbnJjRFMgjeleB+op5K3eBKf14EyYjskp3erbnuSiKhPrfSevCA0yJFFEKOyOawfTIhrEFeTBJUMPl47hbdoU262wvNsbHrZImBC23Ga9O65H6UbdI7kPbhQhc+c285OiO9/G3Ls17mnAL2gDk3wEGgkqb5u+y0iHh7aE5yCTFhw22x103J2plSuJl2VBXtBl4+/5qkE7bLn1tjd9ksXK44YU6zA9QFcrr+uD5Ur2Nv39sHYgBjWSJoAiegSNnlzGtL0WZRPx0AtkQ/TxNN4DVy4I607icRdCcLU29dDebs393Yb4IwattWEn15OKnUy3lVRo5MgMUMSo62gLMZysV8M+inPYh6Xz5RZCYe+HxcWKLQ7ihfOFbMa9rDhDM6Ke4gSdc/VCyA7iQafX/FXgi8AtoVzJ6HOEr89x1lR91SVH3ZRCWm8ZFm8b2sjWB4vRvJXijCZCT+Wkbk0L2u8sJxkIVWQd3e02NTVtXcvZ9BBxqPsztKzUvD9ow71XsMCeVgzbuG2BG9C0xVoR3fI8lXPTMrLpWIJ0TSJE9lDxITpYFMdw5XKExxwzBPKIbqRuGPBdsxF3ke119o65ipK2pRkyUBh2eWd3xG3kOvGMZ0N5JDFqcocevXtIC7l0igbH4rwal/BGEEHLRb99eJvPrl8n0P/N59HzOeD/s+PI58nht6dUj+Nn3/Y+P9b6/N9V8B8f3io3Buo9j2PrtA1fx5X/4TD241970jHLGp+Pf+cHbUPz7Ui/scP5N05vce61dVONX+sibR+Hwx/enLaef2RRf30dgr89DM7K+UT9Dwa+zT96mE+vCyCgKb6+fiLy+Hp+iOR7sd34r8vwdWb94c0bgTtjt/6KEauvflXO1r8eocyHu/MzlLff/jcRphYZXyYAAA== -->
