# Visible Agent Evaluation: Testing The Loop, Not The Demo

Agent demos often hide the part that matters most: the control loop. A model
appears to call tools, remember context, and finish a task, but the surrounding
runtime decides what gets parsed, which tools are allowed, how errors are
handled, and when execution stops.

The profile's agent projects keep that loop visible. `agent-framework` exposes
the small contract: plan, act, observe, remember, finish. `prompt-eval` treats
prompts as testable artifacts. PatchGym takes the next step by grading whether a
coding agent actually fixed a repository task under hidden tests.

That creates three layers of evaluation:

```text
prompt behavior -> agent loop behavior -> repository patch behavior
```

Each layer catches a different failure mode. Prompt tests catch regressions in
instructions and expected outputs. Agent-loop tests catch tool errors,
unbounded steps, and bad state transitions. Repository patch tests catch the
most concrete failure: the diff looked plausible but did not make the project
pass.

This is why the no-key demos matter. A deterministic local demo is not a
replacement for real model evaluation, but it makes the runtime testable in CI.
You can prove the evaluation harness works before introducing network calls,
model variance, or vendor-specific response formats.

The principle is simple: make the invisible state visible. Traces should be
plain data. Judges should be replaceable. Tool failures should be recorded, not
swallowed. Step limits should be explicit. A local test should be able to verify
the harness even when no API key is present.

Once the loop is visible, the question changes from "did the demo look good?" to
"which part of the system failed, and can we reproduce it?" That is the
difference between an impressive agent video and an agent system an engineering
team can trust.
