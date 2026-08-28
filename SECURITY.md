# Security

RAR takes the security of its agent registry, generated skills, installers,
and publication pipeline seriously.

**Do not report security vulnerabilities through public GitHub issues,
Discussions, agent submissions, or pull requests.**

Use GitHub's private vulnerability-reporting flow:

https://github.com/kody-w/RAR/security/advisories/new

Include:

- the affected agent, skill, workflow, script, or URL;
- the exact version, commit, and SHA-256 when available;
- reproduction steps and expected impact;
- whether secrets, arbitrary code execution, supply-chain integrity, or user
  data are involved;
- a safe proof of concept that does not expose third-party data.

The maintainers will acknowledge the report through the private advisory,
investigate, coordinate remediation, and publish disclosure guidance when it
is safe to do so.

Never include credentials, tokens, private source, personal information, or
active exploit payloads in a public RAR surface.
