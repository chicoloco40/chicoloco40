## Goal
Get my docs live on a published GitBook site. Done = you hand me the live URL and confirm it loads. Tell me clearly when a step needs me — do everything else yourself.

**First, check your tools:** if the gitbook MCP tools are already connected, skip the Connect step below. This prompt may have been pasted before (for example, after a restart) — if so, continue from where things left off instead of starting over.

## Prepare (start immediately)
Ask for my docs — a local folder or a repo. Verify the source before building: echo back exactly what you're reading and list its top-level contents so I can confirm it's right. If you can't access something I named (private repos return 404, same as nonexistent), stop and ask — never substitute a different source. Show me the site plan before creating anything in GitBook.

## Connect
Connect to GitBook's MCP server: `https://mcp.gitbook.com/mcp` (streamable HTTP, OAuth).

- **Claude Code**: `claude plugin marketplace add GitbookIO/gitbook-skills` then `claude plugin install gitbook@gitbook-skills` — I run `/reload-plugins` and `/mcp` to sign in.
- **Codex**: `codex mcp add gitbook --url https://mcp.gitbook.com/mcp`
- **Cursor**: add the URL under `mcpServers` in `.cursor/mcp.json`, then I enable it in Settings → MCP.
- **Chat app with no terminal**: tell me to add the URL as a custom connector in my app's settings.
- **Anything else**: fetch https://gitbook.com/docs/getting-started/ai-documentation/gitbook-mcp.md for setup instructions, or fall back to the REST API with a PAT from https://app.gitbook.com/account/developer.

Most tools don't load new MCP servers mid-session. If the gitbook tools don't appear after setup, tell me to restart the app and paste this prompt again — you'll detect the connection and continue. If you can run commands, also install GitBook's skills: `npx -y skills add GitbookIO/gitbook-skills -y`

If sign-in fails because I don't have an account, send me to https://app.gitbook.com/join to create one, then have me retry.

## Check before creating
Once connected, check whether these docs already have a GitBook site — look at the repo's Git Sync state and list my org's sites. If a site exists, don't create a duplicate: switch to updating it (edit locally and push if Git Sync is wired, or open a change request). Create a new site only if nothing exists.

## Build and publish
Create the site with the GitBook MCP tools, import my content, and publish. Skip Git Sync for this first publish — offer it once the site is live. Fetch the live URL to confirm it loads, then give it to me.
