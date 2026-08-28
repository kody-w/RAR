---
name: "rar-cowork-cookbook-adaptive-card-develop-product-roadmap"
description: "Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_product_roadmap", "rar_sha256": "048d36a6b6ef5b17968eca32e0b96237deba6ce59e7929d028280fa20e577bba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_product_roadmap`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_product_roadmap_agent.py` and in the RCI capsule.

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

Develop product roadmap Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 048d36a6b6ef5b17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_product_roadmap_agent.py` first:

```bash
python3 adaptive_card_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_product_roadmap_agent.py   # or on stdin
python3 adaptive_card_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_product_roadmap',
    "version": '2.0.0',
    "display_name": 'Develop product roadmap Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8ef07f7a09dac069',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopProductRoadmap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProductRoadmap'
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
    print(AdaptiveCardDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abPiSLLlX2Hu+1BVj8xEC0KQbW02aEFCQgIkhJbKsiwtoX1DK1JN/fcJATez6nX3m66xMRsy770IRXi4H3c/7hHitze7bcKievv8pgI7n3F2mkYhqGZ27s3ooi+qBP4pEgf+zNwib6rIaZuiqt8+vHmgdquobKIih9NPVeG1Lqhn9qwCbW07KZhtPRve7sCMtitvJqhHeVbndlmHRTMr/JkHOpAW5ax8TG1mVWF7mV3O6sZu2nrmF9UMZA7wvCgPZlE+8+w6dAooqv4Ab9hRCv/CMRdgZ/UnqBC421mZgvrt88+/fHiL4Pu3z7+9ualdw4/e3pWZdGGeKz91bpTnulBCaucBHFoOEJMcXpegglpk8CMP+LPX1Y81SP0Ps//8z6S3q6D+6fOXfPZ6fXmb/iltPmtCMGsKu26AN3Pt0naiNGqGT7Nt2ttDDSFq2iqfwKohpHnw6TnzuyQIy9+nez8+F/kUgObHL28FVMGeAP/y9tNk+pe3qp3ef5qklD/+9CktelD9+NN3OXXrxABiC4VBrT99fV2/xMKB34dG/mPVv0OpT9c64MvbH4ybXk+9JzvhzLdPcRHlPz4FQyd2ILdzF/z4078S64bATdKobv4tuT8/BYfA9qBNL8V/+vAA+ZfZ/GXQN5n/etkSuvWvWAKHvy/3YfYC6l/JfuD/X0SnUQ7z4B3xfyrun02Y/33287+07b+b8GHmf3ljQAqDu5ry7vPst6/qiaV//sH7/uEPv/wORf8fxahFW7kPCV8zO498UDdfv/78Q/34+Idffv6hLWGswYz72lbpP5P5z3B9rPMnBF+jfvzzXLi+lid50eezb5E++60o/0f1+6fZ1U4j7/vn9efZH/Nles1nkxHviz4h+EPO1FDXP+D409vvkCRyaA2kgOk2zPL/+I+ZFLlVURd+M1PdooWk1OZNlIFJ+UsY1TP4f8rtCjJIVUcTyz3HwfifPDxpDKnt1//pPsjzo/siz4X9op+vLuSfry/q+/qivq8v6vv10+wChRdVFES5nc6U7en0JbcDkDfTwmUFalB1kFKcoQEfIRl9nN5M3PjrvyX/60PUp3L49UHw0ZOnFHo/cVTdpuDTZKcegvxllQtrArgDt4WrpIULVfIjyLAfoP11kUJmbyZM6iRK05kXVRCAohoesiFunydhv/76qwN5+0v+JFV89iwa9QIO+KbO7ONHaJufRkHYfMmBGxazH377/YfZ/5r9d7Mewqc1TpDhX16BGj7qDMyyNoPDoMOgiyGFPLzy2+8vhKGYHFY56MPIj8BzMozSBHjvcKv89iNGrGYOgDBDiLOyqJpHIWo+zfb+7Ju+cNHp1sTlYVE3sKqVIPdA7g5Qqg3N+YZkDsteDUOx9ocPs7YGj1V/dSr7oWIG091ufp1J9AlWjiKFvyY1H4Pg5CKPIPzfguH5ORRS/VDPqHcRn2byFJez0q7sMqzs1xq+/fQLrBjv06Fwe5aD/ks+1UkwQfVIkic8cBBExn259OPkc1j9M8gIXv2+9mOMPdW3y6POVV/y+pUAdjW5woUFAS4atJE3lYW/vUIKVv829R74QU0nSS8veC+vPGKQ+Re9gfrsDf7cWXxpMQRdzv5/tyCT3luOU1hue2GZGStfFPOJ59Q5Tbg/my3YCDwkP3Lne3PwTi3vDPslTyMYHNXwt+fIhxdeY56s1VYQNGWrPOTDEIB4TnIfETpFXFVNsW1/yd+p/AOE5sFb0EkwnWG4T1H2vuB0913TEBo6XX8v6w+PQgxhDMAonJWtk8II8QHwHNtNoFbVlGUvV8BwBRO+fRi54Z+smkHpMCqg/BlUIoJ5A+n+AZ1cQDMhzH5VZN+HR1Oz9HQP1Ba2puDTTIeJMgVLDbMTdjzTGIjCDw9RswxAjKGK3xCuQ7t8KjN1sy8F7ckXRQbj948eeN38HtoPXSb1oVTIsA3Esp/41gP3p2e/6fnyFVQ2m5LxMenP7n7ZOvtjzfnbl/yh4zeKhzmePgL3OzgzmFtZ/SDViaJqSDMZeAUQjIRHZf70LK7P6v1Nl8//0ML/+Ne6/Ee51P7suc+zsGnK+vNi8Sxx7xXuEySIBYyRqAT1t2r3capGH19Z9vGVZR9fWfYn4U+sPs/+moJ/EvGK7M8z9BPyCZluHSIXTKH7ekE86I+U+XE53f2SK+C7o1/RMHFsOsDy+q3gvA+BVSeoQDANfhageqpbPSyVD8aFrviSfwuGV6pAQs+DqVrWxR9S+FF5oWufnvtWGOCtvIFre1PHFoBpQ5NO6tfg7XPepumHt9zOwL+5kZkKAAxZCMi0BYK4wyaoicDj6ltDNF38eRP3SCzICF7xecqvD7Opef0w+9aHfpi97wwe+628hVujn6ceeFoSDoV/vo39tkN0wBvcjjVDOSn/3O5MrderJf5HJaa0ghpDIq8nXd7zdFrxH4TAN0EAqn8Ucny8sdMXWUA+n0p01LyneA319GDDA2m8m1IPZhMkyRZO+Mdl4DoVuLWwFnqTud/x+25W8bTl9wcMzXPP+NvbO2m8fPDqD+FwmJ0f66kaLmCowgXh9TOo4L3/u87xJQRyHWxaoBRkufbwlb1yVsAnHJTcrNbAtXEMIM5mheGkBxx75QJiA8gNtvEQbI2tEd/GEECQpOPYUN4zPr9OdT+aFMNs2127JLr0NuQ0F0cc3AUohnokDhBig/vrNVhCjL5NTSBRvqx9WjdB+a2JnVB5Gf3bm7NawpH8st5vny96sbnapLF3mruxGVfeVh43ewFcVNVrk8JujrtdiuFm4sXzM5ag7JKb961KC/ahMQ8Vp+gFkawVYdlfNsK4BX0ueumx3BwFZZkVlEHd3cvieFL8w34bcpe1ig67CxWlYnrVBfNmRCvirJOSfNeyEks6hhn0iroYN6dGic3CtBe1IrKWtdILeb8eJStG42XTGaPorRGhS7nd7e4J5Kah2pjQbpkXc/sETbvMHKwhNzI0pFKBiAKplrqRhyWXcniT4IT1HOTWenPE082mUL3OuG8WOb43sjWrokqrcEuzWt+51DvU1W4YEws24Uf6Ph4DaxGLpkEZdkpt8SFT3HV+wDEWdVVlhPax7Gp3u+4zIxfmnn4SACGKqGlrBwxnqV7XiuGuxweXTFQsuYdp1ij2LR3SW57Qt1aGbBIj1+rEnAnBX0sFOhxyoArBiFwoP76fFDwEdyuVMPa2l4+OsDNUmjoC2jjqNMnfxsTNMu++5AagHy1GKvZbdI6Dc49p7W695pY3VGiwdbK01czVVkyulOfIkjfNkbprhFXt1nIijy5/v6PmGesrUw4RNGw0x4hD+cqn6RXIiU8aqZKrzSWSqy04hQDctL2IhPHNd9cyK1fCKl/e8NESj77XrzSFYpIxQjebRXExq+u4Ww8tv5zXTn6Xr5UDxnHvlDa6yyg+vZbHsNa8eemlnGPqpx2096prkckY3KEdeaVkd0fUwG6iJxqusYwRpKWkhSVhfWhe1pV7iXb8jhQ5ziw3yi5ZVKfu1hsOtzsVd2MA2F4XjLub2XHDK1JIQwhw+mIxd1Ebc2T9+tl4mEtI9MIKV7mWzukQ1OyCUeZsHPN9zCI7ZdUtqN0NjBU59xfnjCnwk9I2Lh/QKkmi0doci9LSeaQTlura11c7rrX5XdKtHMbcW8E9ZnGBsiVo8l0UqBZU/TU4iw0kU+E+iKcjDDAkD+Re3ltDsEIvnHh3e4KlXG6pKYZ+VEKWtCo3PiZqkPQYLaJRXxyVneScbiPPR+ax4lxyeeUodEFY/Xgj8Qugz1GMXMCe4HH1eN5InaV2NCognJeMfkmIua6sr6hGLvahKY97VlrNjY5ccARRNdd+mySmvysOKKhPBneru3tPc3TN9RF5EcW4SoEE17R16n69XXpjZ17cRe9ea3PeXEbmgm1jcF7Fy0FUs10igsgatwmr0IUSLgzfXqo5PvBeryYD4rH+abEZBamMupMqCla0uLb6MW4sCxniedmKLLA4pQ+Xvg235W48lAJxiS5nzfPoy2CPVVjnu2R/pmlgiuK5njPVECTEyBtSviPYLip5lFU2iRZbzGIVhWLKwrbUT5R2v/PFolCwhV7l9Ty7j5drEocAC9VhWe9cahjtsHblOowVoYpou+PQ9F4aklYctEY4V+yirOsi2RNXFGs1qkhC/GQQ4JodrNjJl4mGgcIobHkz96/2RdznvTTeRjGOzuvAxj3FsTZ7a6PbaIUYOLXS1seVfOpjlZmTytmST0csjARMY5GmtG6mk2/nUnJekcnemieiVPZSnN4Nac1V++KuCISDK7UYjAFx0q++v573kYZDPoVapMu1f0dtNFUMJ+08a6hOXtCxvEXt9md+a66LJmkNX6QKdOdQUcvv+oCVVZ0W9BXGaJfztbtVVSwwernl01KR0X28UwLbrkzWOBPDeORZogjEFTnIlMTqt54Qx35J5mHPqLurw2D5VleqGDuNCEHkBM5lyzjzPJ+UISuP6d3LBeqQqFkm1HNinqGqavqhk9pdkxdnJtF0SOb+2BNrJDgO7XITzC87ml2wes3n2H1e7Bfz+JAO9unULVRqGbo7xj/YqT6XmXMW7I73/ep8b/JOkOheOLTXSiilYusWzcaSkKWdLT2X4hC9og3zsDWxq83l1E0hQvROecIZqc5cqHvbpZKFtSQTQT5qOmcgGXtjgwWwtIt0ItfdUaaLhMJ8ORwzvr6LGDl3cAGc1Hmp0qJ4q3o+2u9aGYub5Cpnnd03auJKvHwvie4my2QRCKzthbKxTupic/Li8LhUM5xvylUvaf0FQ064Wm2w8JY1AE9IojQHHcGDIIiue+RqSRUMDN88HedyO4TL817LKXmTkRbdhxYYoj3JXWVeXPfrZTt3K+3sD4pzJrdp35vD1fRXeS1RmzUDqeFk2bl8YPnkaDmLMjykcUtFdEOXK5RwCyM9RB6/7dKiNrYGO/Y4pdKwwGoXNCnPHCsqXc9t6WM/DIO1GuOdR9QdP7AnV1Ts7MwZ8TW0U/XmRWshbkavZLfxXizJTblO8WzUlLTpLa7BJOpQNzpQed7xXJvmBgGV1IVSWIy/sDIhj4yzsd7cEIJeWkf54GZSp64sWEJvt2vhUIsCay/JNTryIEbOIb3D7Sa8KieEqetQSptCq5juZvHCQkkEGTYwMVNT9h5h5wGaD8V2haZWERzvSdnHWKAfqPKq1rqgCBJ3KrIoUhybDlAmLXtM5MnruFI2Mq0nnMiM0EmbenmaL0l1w+/v7loJOHF5EjFZQZFcWiVtdBPjU7laNxTujxuCtNf8QVSTq5oEZEL5JNXsKRZ0B4LA9GazDFdXH3YhiEy2lj5suMvNVzHc7mTMKWKFjU2O7TC8ZpV8K+1UqkYkxrmm9WGpKyYUpgnXiKPD6FgUjWGtfG1h3glaK409evFq9NjqNydnT5Jkn9OK2/FnV9duSz7E70tRWyVKl3rHJRG1iubIrSFW1q0rNGO7586LsJ0fNPZoHy2XKaNjpu2W5S25rPBtarXiXvLXl51e7gya5uVAV1l7pWnsqpSFOZvNlWRY4TdXy3Pz6pxPhKv5lbE432Xhfu3ag8ly2zNZjBZ6cUf2yJ7uvDh4c2uv6GXM3gUtOSZLfVvPB0dTuIOqefHtjp0zYVSRwy0PPYcFzTZvrDw88oZ5lC/HdpSyRvSTuyamnMxbmHtDb+K6KcWC7xhJN8/4PCny+cB5tK8dtIsbEwxREGvaIJZoLBGx7CGXgstkX8wzAa0xnb3iu9MyZ5ETW2NxVXp773pfxt5gzcUyRysdmYO5XccB75WRaBOqBKviXi524rp0hW1waefnKHDF8nJVd3K90jMxIoHqMl4faoelgXu2tKG1sW1241y+Ihv+QrOmLjpRtQ9jkMrCmR52ByU8SZouoEmqo4V9yU36IDg3SchURHI1tUzOecqoMXq62bfGy23qhM8v9N6LZO6cz69EQIg3gWEUEpNG1eSkruTOxzVCCh5zF24ZdmUvYADkIrgu98rt1CQOc1CMIuxTXEaZrjoH16Os7KnzChJudINRvr2tY4nTOLxTgtpbKiE5Dr7EjlsNulk3GkO/HZo70IaSCnWclMcedodtnw6kfE4X3n3XIo1QFbAQ10icykxvr7txlFChbImt4sWyYzCjOPrEfrSLKjCL5siX/k1tzyi1y/ilSaNbTKb4mtgm++vOWtX0/Txax92J0Bu53JBH4WpQqBIci3kW+qG+YXg2rw7mtuTAjnYodo6Neb/mEq3QNCUDYNsjZ/u4WV70IYKuZSmv0QcrI1j8NGySQ+dIABwpjbRBeztY1JZtVMpoVp58N45oTtEJWZu8os6RFDvzKi7mFO8fyEXkcQXBb1Ajw1DSq7KFxbX5ZdExQXa7kwnuWzzaH68Ls7335uGInRhPMRXKEtTNsByznL3lsFu+iYMTzPM5wwTuUT+5hks09BqNUeSM6sQJPxjbSEpFtGAjwMKmaXHvtnm1t6sM2UbkaPthvEVxAyDn7aFT8TO5ysf9ielUrKx6a5XgaOEw2R3x1gy3iMymcbw0NnV+bIe642rIqgdkuPImjZ8NsECDk1ISl46sDuMipoZz1SNVs1jcvQV/UbG886Q5VnEL5dCWJ6BwdBfwaRGpNpUv26NgUYR5bY2euZqbUF6Fw9msT3KVpxrLGIx93yYnyUDoRPMTPNou6Trz70AtGmRocana5UVNtTvdaje8suTYUzXadInTxZHwjU48und9p4577CzduqAaYq4hTMXol1uAp8amZ0p8eQi7WxsY2UUBeMb3B+inqhDnl/YyHwa5UIT1hoqbecRXbY+4zDENWiWyo5Xp8eSJUxatXizQ1CjyBWQ0V9IEgMgGSgk2JR5EPjeWBr9FG2Ju4SN7MVHft7e6pOxJGqvL3JrLJQlgs3ZlQOcVnCHPC/e+xut87TfrIMNoNd5eNvhNcagkJ5nD1WXMgwZDpbDPETHsCRABwl7cjJClmXq4r1vFG7gVjPeMcNuK4O0zsxywODuF51roDUQyYdfZmwK56zqhT8m4O57yLRB3UbWk9DsTLW7zvX9DYI91CjoG4bHgGFIHFbdJ39k2zNAv92xvmIIY2As305n4bF4SaWc3C3nF31axkwg8ObcMWkVojPWtU5s10ZEcSCtpkAyvCUFYG+7I0QS5tdI1bqXxYq7RrliNw2mtLhepX0XHeWzDWok43jI57OHGGsQMhS/kmOTCoBJZBicWJkPZbdCcsIODbZprgPBZ09Ei5Uq7ALO9LrYSLjfnqwqHrNY5eKVveFo7AhjFB8VS4Q5vzTLmdcloPHU00CFIN04TKSyV7hfhBamyBHH2iMcXvJkNzqrKN9SBcbEM7wcYiTbvdTDQeh/oG2+BH4gyxQ2PY1Zwvbk+no1hSSyaQ0gU/IZ2uK7g7le02hzWF5O7Kzej8pAR8/yKjJ1KAtgIcvLkB11HFArTXjc06VuNf0YZyYoJCg3p2566EJpOGpi5QA9cb8e2shy4qoJsdBbn8vyOnzfyVqLTvX/F1/PjcRMUIagckjjyagqsg7cWcMxqOCx1HMPfXCJUFbTaXTPHcLTXZxbhaCSlGRmFnT7Rr1gvs6vK0ZB2hVfOeCVtsorbO7a/7+keLRZ1uMHzG8Vb/fwYBa1oZh3bAROYW/2wvfbNcVfWWxcvhmLIu5uj5XIgLd2UTbhTqmI2IYGUP3f2mC7TwF2OUblEGqJoasaHUtgWIpse6fne0UyzlA/oYjfwc1tn0O48tAtzSOYmI7H3bl0IhnXbWw64zVlJOHdal9cZAjefxnY9lmlwOm29SugdEd0RZ1N1CnGv0znZj5SBK/tMA4pHVJu4NhL84qIKxnlIjer3YUXEibPYum60TMFOPG+3bx/epiPo10HyX3tkPB3r/T87XXweBL4/WnocIgPb+/xY6/Nf1OuXD2+VG0GtnmepddoGr0PH/3KS+vHfeioxiRiez2OnZ2H35v34vbGD6atFb1HutXVTDV/rIm0fB7of3py2nr7jUH99HVy/PczLyukU/E/mPE/FoyD/2hRfK9BEFXibvoYwPeMBXmQ375fB64wZjh+gvyK3/oqviK+gKieDX486plPZ6VnH2+//G2NBRH/JJQAA -->
