---
name: sql-queries
description: Write, review, debug, and optimize SQL queries with explicit dialect, result grain, join cardinality, NULL handling, parameterization, and validation. Use when the user mentions SQL, database queries, wrong counts, slow queries, indexes, or EXPLAIN. Do not invent schemas or perform database mutations without explicit authorization.
license: MIT
metadata:
  source: https://github.com/arjunprabhulal/agent-skills/tree/main/skills/data/sql-queries
  upstream-skill: sql-queries
  adapted-for: OpenAgents Control OpenCode project
  runtime: Existing project database client or connector for live execution
---

# SQL queries

This project-local derivative preserves the upstream correctness checks and adds explicit
OpenCode execution, credential, and mutation boundaries.

## Establish context before writing

1. Determine the database engine and version. SQL dialect differences are part of correctness.
2. Inspect migrations, ORM models, schema files, or user-provided DDL. Never invent tables,
   columns, keys, or relationships. Ask for the missing schema when it cannot be discovered.
3. State the result grain, such as one row per order or one row per customer per month.
4. Identify parameters, time-zone and date-boundary rules, NULL semantics, and expected scale.
5. Keep credentials in the existing approved mechanism. Never print or place them in query files.

Drafting SQL from supplied schema is local work. Connecting to a remote database is a network
action. `INSERT`, `UPDATE`, `DELETE`, DDL, procedure calls with side effects, and transaction
control that changes persisted data are external writes and require explicit confirmation.

## Build the query

### Control join cardinality

- Know which side can be missing. An `INNER JOIN` silently removes unmatched rows.
- A right-side filter in `WHERE` can turn a `LEFT JOIN` into an inner join; put the condition
  in `ON` when unmatched left rows must remain.
- Aggregate a one-to-many side before joining when the join would multiply a measure.
- Use explicit join syntax and deliberate keys; never rely on comma joins.

Check the intended grain:

```sql
SELECT COUNT(*) FROM (...);
SELECT expected_key, COUNT(*)
FROM (...)
GROUP BY expected_key
HAVING COUNT(*) > 1;
```

### Handle NULL deliberately

- Use `IS NULL`; `NULL = NULL` is not true.
- `status <> 'done'` excludes rows where `status` is NULL unless handled explicitly.
- `COUNT(*)` counts rows; `COUNT(column)` counts non-NULL values.
- Aggregates generally skip NULL values.
- Prefer `NOT EXISTS` over a nullable `NOT IN` subquery.

### Keep filters and calculations precise

- Prefer half-open timestamp ranges: `>= start AND < end`.
- Cast before integer division when a fractional result is required.
- Avoid `SELECT *` in saved or production queries.
- Parameterize values; never assemble SQL from untrusted string concatenation.
- Use CTEs and window functions when they improve meaning, while accounting for the chosen
  engine's optimizer behavior.

## Analyze performance safely

- Start with plain `EXPLAIN` when execution cost or side effects are uncertain.
- Use `EXPLAIN ANALYZE` only for a read-only query, or inside a verified rollback-only workflow
  supported by that database. It executes the statement on many engines.
- Compare estimated and actual rows, scan type, join strategy, sorts, spills, and buffer reads.
- Check whether functions on indexed columns, implicit casts, leading wildcards, or an unusable
  composite-index prefix prevent index use.
- Recommend an index only after considering write amplification, storage, selectivity, and
  existing indexes.

## Validate before reporting

- Run read-only checks first and limit exploratory output.
- Compare row counts before and after each join.
- Test a known small case and boundary dates.
- Reconcile important totals with an independent query or trusted source.
- If execution is unavailable, return the SQL with its assumed dialect, schema assumptions,
  parameters, and exact validation commands.

## Mutations

Immediately before a live mutation, show the target database, affected objects, predicate,
estimated row count, transaction/rollback plan, and backup or recovery path when relevant.
Proceed only after explicit approval. Never broaden a predicate or retry a partial mutation
without inspecting the observed state.

Store disposable query work in `.tmp/sql-runs/<task-slug>/`. Put durable `.sql` files in the
project's existing migrations, queries, reports, or analytics location; do not create a new
top-level convention when the repository already has one.
