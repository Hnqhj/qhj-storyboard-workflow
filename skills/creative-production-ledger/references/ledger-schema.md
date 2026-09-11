# Ledger Schema

`production-ledger/ledger.yaml` uses schema version 1.

## Project

- `id`, `title`, `created_at`, `updated_at`
- paths are relative to the project root whenever possible

## Attempt

- `id`: monotonic `A001` identifier
- `created_at`, `status`
- `parent_attempt`: prior attempt for retries
- `prompt`: asset record
- `references`: asset records with explicit roles
- `model`, `mode`, `settings`
- `outputs`: generated asset records
- `changes`: isolated deltas from `parent_attempt`
- `notes`

## Review

- `id`: monotonic `R001` identifier
- `attempt_id`, `created_at`, `verdict`
- `evidence`: review JSON, contact sheet, frame, delivery report, or other asset records
- `issues`, `notes`

## Asset Record

- `path`, `kind`, optional `role`
- `exists`, `size_bytes`, `sha256`
- directories use a deterministic tree hash of sorted relative paths and file hashes

Never edit historical IDs. Add a new attempt or review instead.
