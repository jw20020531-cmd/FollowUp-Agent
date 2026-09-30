const sampleFollowUps = [
  {
    contact: "Anonymous speaker lead",
    subject: "Workshop speaker invitation",
    summary: "Invitation was sent 4 days ago and no reply has arrived.",
    reason: "External event speaker conversation is waiting for a polite follow-up.",
    status: "needs follow-up",
    due: "Oct 2"
  },
  {
    contact: "Anonymous partner contact",
    subject: "Student project collaboration proposal",
    summary: "Proposal was sent after a meeting, but there has been no response.",
    reason: "The conversation may go cold if there is no next step soon.",
    status: "waiting",
    due: "Oct 3"
  },
  {
    contact: "Anonymous member",
    subject: "Onboarding question",
    summary: "A member asked a logistics question and no owner has replied yet.",
    reason: "The requester is waiting and the team needs a visible ownership status.",
    status: "needs follow-up",
    due: "Oct 1"
  }
];

export default function Home() {
  return (
    <main className="shell">
      <header className="header">
        <div><p className="eyebrow">FOLLOWUP AI</p><h1>Manual follow-up inbox</h1></div>
        <span className="status">MVP · Demo data</span>
      </header>
      <section className="intro"><p className="count">{sampleFollowUps.length} conversations need review</p><p className="muted">A focused workspace for pasted or imported email threads before Gmail sync is added.</p></section>
      <section className="cards" aria-label="Follow-up recommendations">
        {sampleFollowUps.map((item) => <article className="card" key={item.subject}>
          <div className="card-top"><span className="priority high">{item.status}</span><span className="muted">Due {item.due}</span></div>
          <h2>{item.subject}</h2><p className="detail">{item.contact}<br />{item.summary}</p>
          <p className="recommendation">Reason</p><p className="reason">{item.reason}</p>
        </article>)}
      </section>
    </main>
  );
}

