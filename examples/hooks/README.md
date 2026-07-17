# Optional Agent Hook

Agent hooks are a Preview feature that executes local commands with the same
permissions as VS Code. This repository keeps hook configuration under
`examples/` so cloning the starter does not execute a command automatically.

## Enable the Example

1. Review [validate-on-stop.json](validate-on-stop.json) and the referenced
   `scripts/validate_starter.py` before enabling it.
2. Confirm Python 3 is installed. On Windows, confirm the `py` launcher works.
3. Copy the JSON file to `.github/hooks/validate-on-stop.json`.
4. Run `Chat: Configure Hooks` or open Chat Customization Diagnostics and check
   that the hook is loaded without errors.
5. Start a disposable agent session and verify that stopping it runs the
   validator without changing files.

Remove the copied file to disable the hook.

## Safety

- Never put secrets in hook files, command arguments, stdout, or logs.
- Treat hook input as untrusted and validate it before using any field in a
  command.
- Do not auto-approve edits to hook configuration or scripts executed by hooks.
- Keep commands deterministic, short, and auditable.
- In remote development, commands run on the extension host, which may not be
  the same operating system as the local UI.
- Recheck the official VS Code hook schema before adoption because Preview
  behavior can change.

## Compatibility Notes

VS Code, Copilot CLI, and Claude-style hooks can expose different tool names and
input property casing. This example ignores stdin and only runs the repository
validator, avoiding those compatibility differences.
