# MVP Scope

FollowUp Agent should prove one small workflow before adding Gmail OAuth, AI drafting, or sending.

## Target User

Student organization officers and student founders who manage important email follow-ups manually.

## Problem

Important email conversations can become buried under newer messages. Users may forget to follow up, follow up too late, duplicate follow-ups, or lose track of who is waiting on whom.

## MVP Workflow

The first MVP uses manual input instead of Gmail sync.

1. User pastes or imports a small set of email/thread examples.
2. App shows follow-up candidates.
3. Each candidate includes a short reason.
4. User can set a status: `needs follow-up`, `waiting`, `replied`, or `closed`.
5. App includes demo data so GitHub visitors can understand the workflow without connecting an email account.

## Why Manual Input First

Manual input is the smallest useful implementation because it:

- avoids OAuth setup during early validation,
- avoids asking users for mailbox access before trust exists,
- lets the project demonstrate product value quickly,
- keeps the MVP easy to run locally and review on GitHub.

## In Scope

- Demo follow-up inbox.
- Manual email/thread sample input.
- Follow-up status tracking.
- Simple reason labels.
- Local database schema for conversations and follow-up candidates.
- API endpoints for listing, creating, updating, and closing candidates.
- README instructions and demo data.

## Out Of Scope

- Gmail OAuth.
- Gmail sync.
- Automatic sending.
- Multi-user team permissions.
- Full CRM features.
- AI-generated email drafts.
- Production deployment.

## Future Milestones

1. Manual demo MVP.
2. Real user feedback from 3 interviews.
3. Gmail read-only sync if evidence supports it.
4. Draft generation after follow-up detection is useful.
5. Sending and reply detection only after trust and safety requirements are clear.

## Definition Of Done

- Project runs locally.
- Demo data shows realistic follow-up cases.
- Backend tests cover core API behavior.
- README explains what is real evidence and what is demo data.
- GitHub issue tracks evidence still needed before Gmail sync.
