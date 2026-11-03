# Regression Judge

Tells you when a change made your Brainstem worse.

1. "Record a baseline called daily with these questions: ..." (or from a Rooms conversation).
2. Change something: a new model, a new or edited agent, a new distro.
3. "Check daily." Every question is replayed on the live Brainstem and a teacher grades the
   new answer against the original: same, better, worse or broken. You get a one-page,
   side-by-side report, worst first.
4. Happy with the new answers? "Accept daily." Old baselines are always kept.

Works on this Brainstem, on any summoned distro by name, or on any http://127.0.0.1:<port>.
Each pair is graded twice with the order swapped; if the readings disagree the verdict is
"unsure", never a guess. Changes in which agents were used are reported as facts.
