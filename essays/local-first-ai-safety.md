# Safe Local-First AI Tooling: Small Systems With Hard Boundaries

Local-first AI tooling is attractive because it is inspectable. You can run it
without a service account, debug it without a dashboard, and read the source in
one sitting. But local-first does not automatically mean safe. It shifts more of
the safety boundary into the code you own.

That is why the lab emphasizes hard boundaries: parsers with explicit limits,
agent runtimes with bounded steps, evaluation tools that separate hidden tests
from visible prompts, and demos that do not require secrets. Small code is only
valuable when the failure modes are also small enough to reason about.

`safejson` is the clearest example. JSON parsing looks harmless until untrusted
payloads introduce duplicate keys, oversized strings, deep structures, or values
such as `NaN` that violate a stricter policy. Treating parsing as a boundary
means adding typed failures, resource limits, and policy decisions at the point
where data enters the system.

The same idea applies to agents. A tool-calling agent is a boundary between a
language model and local capabilities. Unknown tools should fail loudly. Tool
errors should appear in the trace. Dangerous commands should never be smuggled
into a friendly abstraction. A sandbox warning belongs near the execution path,
not buried in a separate document.

For evaluation tools, the boundary is trust. Hidden tests must stay hidden from
the agent. Reports should say what was run, what changed, and what passed.
Benchmark claims should be modest unless the harness can support the claim.

The pattern across these projects is conservative by design:

```text
explicit inputs -> typed policy -> bounded execution -> auditable output
```

That pattern will not make every tool production-ready. It does make each tool a
better teaching object, a better prototype, and a better starting point for
teams that want to replace magic with mechanisms they can inspect.
