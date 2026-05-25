# PatchGym: Local Coding-Agent Benchmarks From Real Git History

Public coding benchmarks are useful, but they answer a broad question: how does
an agent perform on a shared collection of tasks? Engineering teams often need a
more local question: can an agent fix the kinds of bugs that appear in this
repository, under this test suite, with this project's conventions?

PatchGym is built around that local question. It mines historical commits,
separates the fix from the tests, and turns the result into a hidden-test task.
The agent sees the base repository and task context. It does not see the hidden
tests or the oracle patch. A task is accepted only when the base version fails
with hidden tests applied and the oracle solution passes.

That split matters because it makes evaluation harder to bluff. A useful coding
agent should not merely produce a plausible diff. It should produce a patch that
survives the same validation loop maintainers care about: tests, changed files,
and repository-local expectations.

PatchGym deliberately stays local-first. It is not a hosted leaderboard, a model
ranking service, or a claim that one agent wins everywhere. It is a readable
reference harness for teams that want to build their own private evaluation
sets, inspect the tasks, and understand exactly what is being graded.

The design tradeoff is intentional: keep the harness small enough to audit, make
the task format explicit, and put safety warnings near the execution path. Local
evaluation is only trustworthy when the repository, tests, shell commands, and
agent process are all treated as part of the system under test.

The result is a practical loop:

```text
mine history -> build tasks -> verify hidden-test split -> run agent -> grade patch -> inspect report
```

That loop is the useful unit. It turns agent evaluation from a screenshot of a
demo into an engineering artifact that can be repeated, reviewed, and improved.
