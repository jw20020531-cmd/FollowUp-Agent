# Demo Data

The MVP uses anonymous synthetic examples until real interview evidence is available.

## Demo Follow-Ups

| Contact | Subject | Summary | Reason | Status |
|---------|---------|---------|--------|--------|
| Anonymous speaker lead | Workshop speaker invitation | Invitation was sent 4 days ago and no reply has arrived. | External event speaker conversation is waiting for a polite follow-up. | needs_follow_up |
| Anonymous partner contact | Student project collaboration proposal | Proposal was sent after a meeting, but there has been no response. | The conversation may go cold if there is no next step soon. | needs_follow_up |
| Anonymous member | Onboarding question | A member asked a logistics question and no owner has replied yet. | The requester is waiting and the team needs a visible ownership status. | needs_follow_up |

## API Endpoints

- `GET /api/follow-ups` lists demo and manually created follow-up candidates.
- `POST /api/follow-ups` creates a manual follow-up candidate.
- `PATCH /api/follow-ups/{id}` updates the candidate status.

## Status Values

- `needs_follow_up`
- `waiting`
- `replied`
- `closed`
