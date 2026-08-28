---
name: "rar-cowork-cookbook-demo-data-merge-cases"
description: "Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_merge_cases", "rar_sha256": "afebb2b58babef211975935e262c2e77768878d77261d55bf1ca07d3e391a73f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Demo Data Generator — Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_merge_cases_agent.py` and embedded as the fenced Python below (sha256 afebb2b58babef21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_merge_cases_agent.py` first:

```bash
python3 demo_data_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_merge_cases_agent.py   # or on stdin
python3 demo_data_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Demo Data Generator — Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_merge_cases',
    "version": '2.0.1',
    "display_name": 'Merge cases Demo Data Generator',
    "description": 'Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23620edfb71957ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMergeCases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMergeCases'
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
    print(DemoDataMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZPbxpLtX+Hr+WD5UmrsBKAbjhgSCxcQAEkQJADLIWHf951+/u+vQLJb9ti+MzfixVChbgKoyso8mXkyq9C/vphtE+TVy+cXxTWz2dpMkjBwq5mZOTMm7/MqBr/y2AL/Z3aeNVVotU1e1S8fXxy3tquwaMI8A9PXbuZWZuPW96l25d6/g19JWDehPXPcNAeXdl459czLq1nqVr47s80aDAuzmTmrwUQrH2aNm5lZcx/TVGaYhZl/l1mESd7Mahs8rsK8fgUquIOZFolbv3z++ZePLyH4/vL51xc7MWtw64UFS7JmY4rTSsy0EJiSmJkPnhUjMDsD14VbgZVScMtxvdnz6kPtJt7H2T/+Efdm5dc/fv6SzZ6fLy/Tv1ObzZrAnTW5WTcusNcsTCtMwmZ8nS2T3hwn05u2yurJMIBa5r8+Zn6XlBezn6ZnHx6LvPpu8+HLS15MMAJMv7z8OAMQfHmp2un76ySl+PDja5L3bvXhx+9y6taKXLuZhAGtX78+r59iwcDvQ0PvvupPQOrDe5b75eV3xk2fh96TnWDmy2uUh9mHh+CiyrvJN7b74ce/E2sHrh1PLv8fyf35IThwTQfY9FT8x493kH+ZzZ8Gvcv8+2UL4NZ/xxIw/G25j7MnUH8n+47/fxGdhBkI2zfE/1LcX02Y/zT7+W9t+1cTPs68LyCek7AD0WEl7ufZr1+VA8f8/IPz/eYPv/wGRP+3YpS8rey7hK+pmYWeWzdfv/78Q32//cMvP//QFiDWXDP92lbJX8n8K1zv6/wBweeoD3+cC9ZXszjL+2z2HumzX/Pi/1S/vc4ugCyc7/frz7Pf58v0mc8mI94WfUDwu5ypga6/w/HHl98AK2TAmta+PwZZ/h//MRNDu8rr3Gtmip23zQw4uAlTd1L+HISAjep7blcuwLUOAbDPcSD+Jw9PGufe7Nt/2nd+/GQ/+RGaKO6rAwjn653bvt657dvr7AyE5VXoh5mZzE7Lw+FLZvouoDiwUFG5tVt1gEKssXE/AfL5NH2ZGPHbX8r7ep/6Wozf7qQYPnjoxGwnDqrbxH2d7LgGbvbU2ga07g6u3QKpSW4DFbwQUOZHYF+dJx3gsMnmOg6TZOaEgKEBvY932QCXz5Owb9++WWYdfMkepInNHrxfQ2DAuzqzT5+ALV4S+kHzJXPtIJ/98OtvP8z+7+xfzboLn9Y4AMp+og403CmyNANZ1KZg2FQeAMmazh31X397IgrEgIozAz4KvdB9TAZRGLvOG7zKZvkJJRYzywWwAkjTIq+aqZqEzets683e9QWLTo8mrg7yugG1qnAzx83sEUg1gTnvSGZTBQKhVnvjx1lbu/dVv1lTmQIqpiCdzebbTGQOoDLkCfgxqXkfBCbnWQjgf3f+4z4QUv1Qz1ZvIl5n0hR3s8KszCKozOcanvnwC6gIb9OBcHOWuf2XbCp87gTVPQke8PhTPZ7q7t2lnyafgwKegox36re1/WfNdmbnex2rvmT1M8DNyr1Xa6DKOPPb0Jlo/5/PkKqDvE2cO35A00nS0wvO0yv3GBR/V+CnUjybavHs2SdMla1FYQSf/e83DpNyy/X6xK2XZ46dcdL5pD9AmzqcCdxHUwSq+UPYlCDfK/wbP7zR5JcsCUEEVOM/HyPvUD/HPKinrQAyp+XpLh8oBkCb5N7DcAqrqpoC2PySvfHxR2DVnXyAJ0DOgpieQultwenpm6YBSMzp+nttfmI1WQ5CbVa0VgJQ9FzXsUw7BlpVUyo9wQcx6U5p1QehHfzBqhmQDlwP5M+AEiFIDsDZd+ikHJgJoPWqPP0+PJx8BrRwWhtoC1pI93V2BdkwRUQNUhC0LdMYgMIPd1HAjQBjoOI7wnVgFg9lpq7zqaA5+SJPQUz83gPPh9/j967LpD6Qak6U+SXrJxJ13OHh2Xc9n74CyqZTxt0n/dHdT1tnvy8c//yS3XV8522QyMlUc38HDoi/Kn1E8cRDNeCS1H0GEIiEe3l9fVTIRwl+1+Xzn1rtD/9eN36veeofPfd5FjRNUX+GoEedeitTr4AFIBAjYeHW95L1acLr0z2rPt2z6g/CHth8nv17Cv1BxDOSP8+QV/gVnh7tQ5CMAIDnB9jPfFrpn/Dp6Zfs5H537NP7E3EmI6iR71XkbQgoJX7l+tPgR1Wpp2LUg/p3p1EA/Zfs3fnP1AAsnflTCazz36XsvZwCVz489c724FHWgLWdqc3y3WnbkUzq1+7L56xNko8vmZm6f7fdmGgcxCRAYNqZgPwArUoTuver97ZluvjjbuqeOSDlnfzzlEAfZ1OL+XH23i1+nL317/dtUNaCDczPU6c6LQmGgl/vY9+3apb7AnZJzVhM2j42JVOD9Gxc/6zElDdAY9udSnP+nojTin8SAr74vlv9WYh8/2ImTzaoG3MqtGHzlsM10NMBbcvHGfAXyK2J4M2sBRP+vAxYp3LLFlQ0ZzL3O37fzcoftvx2h6F57Ox+fXljhacPnl0cGA7S71M91TQIxCZYEFw/ogg8+5/1d89JgLxAqwFmmZ5rWahFUJYJ+g4UQWiSoDHCRReojbokSS4oiqQckkQXiEMQlofYJkw6mIvRiEliHpD3CMCvU7UOJ0Vc2JueoraDLVCCwGmERE3aMXHSNB0YiINJzwH8/n1qDJjvad3Dmgm691ZzQuFp5K8v1gIHIzd4vV0+PgxEX0zrClmnYD+vkvkwYIsjphZqnBBWttnOkc3V1rbLlDVuNq+rFbWzYqUpTbza2XBOyqK09OALpGvY/nBjCO8kJjJKiQ4sMo3hkjW57+ciKancUokui8IWDH5bLga8iIz1YSdfeIZWq7gw0sueoprD4XaZ+/EmLuNkPxjQTWgEBN4me/OyqLhEiC8KejPpXVRqXBDUZw4l4WtiF4l25uWL2toL7bY5HFM35SJrZZepxKpuBA92t68JL9vjpDdaskbOyTmDqyRt+KYm9OVWqUtSLRzrglSSBWw7MUNURgYUVsuMd9BlwVixaURxY1gFtehLTb5wIuNHZbFIhARv97DfJKyQqOMVQXk8VfkhvRaK551OrbEorz3iq5ZWVmeTYLa38XRBLwudjhLdkh1PAZnc5dFZKzZl2O2Q7WJYuwgGGpZxcVFS2dA4LrW5yFjss11yXu1t63AdwehNv5EJw8CZPvQFaFyM1/WI9NaiN9k9nPYLPUbdvkuKTGXlRikuwp5wRrhUnSvBV+zudrydjh41ijh706UARYLqUl3Pwe68yfg8TseOjn2mK64Fcb1ExFllVF7xCUTkLnK0Rnz6TF9Igkquh5aymX26WhiI5TRYJdmnlhgXOnbGnfo6AHONlERdI5I3+i3cbptsHx0j6zw31ItJSqdDQvruRdZCfX8JNtF+gzQrot2LtVBkQ3Lj5xxldxd15Ee6D7YWncryMVgN7iIIUsGFB/dARAji3GpzUfY1kdX4EdtlhJfuIoldrQMGvWQJZ5zF5qpSqCfMnUNG2P3Ik7SUsfhmQ15u1DmgeJZkxsY25aOXQGco9yKLXlRdkZEc3iaMI5MYKzkJIcy3jV1p6ul6yVg1ji+LRql0H9dLSK8lP3T3a/FIZXFOW8nBvyqNPWhjTPohQqRxVMVH1/Zl1jowp7JPeBuXG00zdkPPLxnqlGxUYn1Uw5M0yOM2WRZtzam3lbZUkv02L8KbzA71hgOsOObkcgE1W0KnC9y/wcf4aId0zHKbICI1h0CbA7erDi7uGkR5RU/j+naxDziTk2crOcuBAXXU0AQb7nTSdpTUhWWTeKOh8WRdD3XVrgPSPUmXRHJzONODm8bnq9I6HrdKx1hZu4mKMspVtOnnuQSHSn5OzOpwlF11GKuLyEU3ui+vVN0VfGYB38JzyBtvyk7jXXnDKzEDie31ystdY9ravDZ07oqsE15pD2fppsoGDq8EbVE75nF32ROSm2LmCtEEeaVn5TKHDwdfwcvxqozNObnlK4KEt9A6HTzkCIm1FgC6CQ9VqfUBFmxoI9mt2gZdEYcblNAcN7pr3aI4ASVXylDXzSljGWfbCWeBZK5yJlI4UmSCyYfXtkh4L+dwZ2Qohgi0VQjP9S4jqcI8WzlyGqACWSXlDs3Wc+wk7fwxJPpVol0Nbr5c4nRkI3Se1JeSzjF4wx32UdT3Nh2K243r6UvfXcNn4niqQJoGR+PELvozS2JqgI5unpJM6CqxrYrSjj9F9X7wr07dLjG+d0JzPgcxxS1tb9dquXvQRs0OpfNFstvj6nA2iIbA/aphqfVSJ6453ftrD5eAlqVkyadEbVCBS4IACewGYMVLKUrtSzQ3M3LB0OYlsk3hpprCRaoZfbQL/cIutWXBmSciDVNmJ21KJp9L7kBYvho79cKu9XWVqNcCbdrD7mqMhsuZi1tFzF3Nms9bmKjVM6QvxnXVdN5AXPDLQaBHG0kjSl4pjJAYPULPtyKvShiy2df7JTLIhw6jRkW+7Fux23RQUo+UQhwPvNUXpiZfHXKsZcZcHkkuKpg0dUeqL5exTGtyGd/8VUhhWHxjzoKxknrOVMyQdnKxWo+l0oxlLIUbPF2aV8XYlfnVEOwlqqSraikNfSfnkmCOOrWDxuJUGKZOQzwJAzVljBM30fyyvAEcrLry9UzQHFKasyGpJ6cjqR4PLX7Dt9G+Q8yk6fNMuRQ1Zh4To7pGuT+c0SKiMHzjxFV2vca9C+P+GRKNeuCP+hD4O/8iY3OvFG8FtotaKtPr9iolipnebEF1TqamCCzabhqiW+w7fnMMbXjYtvpuzVdotUeEi32JkdqzT410Lk9MAQp0T0vs7spd0kgcNpKDpqW5ZVZ2C/FRZeeN4XHcVWLUlIzW6E5SrJ4Dul6w4GhDEnF2Um/HM/CFVTGFiS1khQ5sLzY5Sl12cV0vzo3rbmxWyVcmLrmX7lKejRDJjroIcehS1TnuBnXzQ1YbKTzK8TYMNWZJUCc+aaq9lSz2+uWcb9OdkVd2dsZSpzwiwnY/d6RSD5w6My/U/qo1t1Un7TiwNbz4B8S6GugW4SM7UvVI3GE3LdYX2LxCwwo6ppSgJl4obApMiQme0VbKxd2qxp6XdbjALVxCiKspaAZMypyDrt1jfS0vpSBw20MAkegoFDVzdIOWI0ybxVpTjr1YP3H+1dS9Fu6aMqDgGElzgttndb7cuuxolb51W1dysdfbMO9TvdsfG4yCPNfegLYP5kURRleoLhywPHBZPVX8rDO5AUv3VYLYKaYSndHe+FFMVLfp2rMBSu54CVcidligOMPjisItN+KqFDt2kVwF22UhBVApurSYRMTDZjGXz/NIvm5rBTsprJ7D8IhjpXPy5VNPnpCKWRdqqfCwRDOh2BLIUumuYUMRBWaXyQhio7qMpW3xZBRsD/7IUwi0M/PRDpXId0QdXW80XsIYT7TlZMu5Cig7oyPm0pkQmfTI7hXteFa2jkYpFrI5V5VdtGvd4I12CSU3xY27bL3WM06hYsMiz52CrI8IJaC5LqSgAzYlgw/I7RHWcY7BEcfm4611hDBxyKTdeLJTBVFRwbJR6HjeUnhYANpfp9G2H6FjIFLb6zWzuLIrRl+Uc65ZKIRo8RfiZoy11qqjPZinyrqZlEZsjXpfHCP1ttzHBzjK+kTLquuqRDF+YHokrTe7aK+muE1J9QKKuYQ3s40ptzg8Rw7cKFFx4wrjngwYlU5BDeZxHrkiLEooohLwW/HsK5zhq1K0sWsnaud4ul+f8iKqtGXC7ANPXsX4jpc0QmeE8ESc9JG62fVhiC+xQy/PtHawMkfXA+GI2UtDki01cVUO7DsQ3cJWUugYy1UtrefwRoXZOkENv5Iz0qWPcnZiXPWkdNxY9CGKdeLGymFUPN44K2wkao+sRhjWBSPE7aFByuFik3LuEjv0JKTKGSnqBYjN9U2j4mp3jGJPE9DUTjTW2Sf6Tj4firNPcHmkM/6l3ET8ZWPUkWfs+v2p6gBl67c+YqEidnPgcwJD7XC+T2nFaUkxvex2/qkLsL0llvwaIuTy4CyE1nFzaAeDVB3Fbds5B1hf7nGTBLEoB61Cc5ccrfcuy8QHEDVnu/OnsI7g5lZ423XcBIG6Xw26cNv2Q7a4ipccNBnH246RRELu9uuUzBA0DMr6do2Xms8kyvwar9pUXmJNvFT7igkN/3Sg64V44Av+ulbUXdahuLmTNINWxdsRjsbIb8dyR6MwzKl7jFzYqiuhyOqiauOV3a4DtK23tKm2rjDXua0NqwchWGwdCtuYt113quyKhABMm3UONSXlInJxJdqSL9CYxpLeuJyhwartzBlEZyTseQ2jUmCt50TE8qetTDZg08O06iKNmZvHRn6fzodTL1hCaBd22gywHtEwDA+EBKXXPJDps7hw9OyyskJojnEsfGLV1S0USgrrelRZU2U7dhS7151Gnu+okVVJ7FDCm/kBns+blW/LbdT4OkYniScgl3UX5GeJlOfzhS8MKy872mSsoCGJOToLu3OFpBKChnofMku/JysPurHQ5jyih85xaEujEf9YCbQnmFf6WOZBuMmFAwOnPNfHgU1Vy1NbyLtDujIVXWIOGtXWu3BcwjjIv4GNT6BvO8u45LfyEeJje+PSNQy3mE2SmR6vSs01Wud8wtuldDTHy1mWzgWhaB1jO1sFFwj+tEvXXn8hPPPqztn9Ujl2ZFG2BwixRHbA1mfFWu8ozekDCgO9Kk8FntYMmamMlwW3Ooj81qsrnOzF9ZE9WbfcSrekfOIaljSbYXQqSDKhK0Tj9HFrqDw2cG7P8uHpYETUPvJdtCZPNDVw6F6rmuNhnRfVoQH7G2uDNZ0F9l6LMjKRmz/XkcUiigRNw8A+GfLTLdifi7cm8+09pae4tjQYjNtGTiDQqCfWfCmRTUUXRSz2Msey0OHkCOtFYUE7irZPmC0v5Uh2XdwON8vMRXzWGlrB7iV5jZ1sXKEX6Y0l+g3T6KPLSXRwdRAqw+iFtD7vUE5vfVpdoXuJvA4Q1Wrjdrtlb+txpQWchFrwjveJ+Loc2MDVwLb1dMZ0QwoFF2I5/Nxmng/qSmvJGEEm23pYYyFp3GC1Hk6rvOEPY2QhQ0Cy6tzY7gd03keQk66HDUBAMzqbbHuLHmrtWIzRol+vOozdoN1meQW9F9RVa6NaDWtjQEAVIbJ077rlCHZpq76/spZ6to/N0CxESGjHHVK0XbvQlHpkD5e2GEJ5n9lMd4EpTtal5VLV6J3gaV2ArkOREVYQu8FvcoTk6UC5ETueha5MXLipOewG1kDxE9tHDRmpR16CrKZrWk8i2gU5r11t5VEDYbPynj04kCcXRyrn7RBiSm5P8mh3uzHOqMNZSuZGDnk2GZHlwqZG+bY4eH7XUfqR7RJ6SXqD1lWCXywHKsf7lbNeFpRZkr4levgm0Plzs4Utq6riqlsK84o6ekWMsD6crBZtFw4D1PHqUTQozBlKfn+TDvUpXTQS3iW6EXfQOkxNJNT1ijosDtqxCqClL62R1ZpPrTLIyA7cK5JykWJnjbWQppjTjjTsRBzizYbppRXm0GR2UCkXZMxhs6JTRHJ5FgKEz+ZLvgqYuXb19zd5w5a8RiTa7qbepNzoyXG3FD2haSXlSI9t5VSyGe2XN0wWs+iKXXm0l+YQulTw/YqMcbDtk1Z0GMOdRl23HhHohyvBEjR6Sxh9scZ3gUfox9ayFeGKHKhSPbE0iKeFdSKt1mZvcqotaYp1xPMqr0QtWAUgFmpfF7wOpVZeIZzlnPLJyIJEe3P2962OWxsBJzQsrNsEp1cUDdrveTD6y+Xyp59ePr5MZ8fPE+B//cJ2Op77/3ZK+DjQe3vncz/8dU3n832tz/+NHr98fKnsEGjxOPOsk9Z/Hhb+lxPPT3/5emCaMj7edk4voYbm7Ry8Mf3pL3Fewsxp66Yav9Z50t4PWj++WG09/YVA/fV5oPxyVz8tHqfTT3WnU2uwwtcm/3p/Of02OcymVysu2OA27vPSf578gtkjQD+066/YgvjqVsVk3vONA7AKfYVfkZff/h+NmFAN6CQAAA== -->
