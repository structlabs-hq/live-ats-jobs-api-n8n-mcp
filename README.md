# Live ATS Jobs API — n8n Workflow & MCP Server

ATS jobs API for AI agents and automation. Greenhouse, Lever, Ashby and 5 more ATS boards. Live ATS jobs API for Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Recruitee, Personio and BambooHR.

- **Apify Actor:** [Live ATS Jobs API](https://apify.com/structlabs/live-ats-jobs-api)
- **MCP server:** `https://mcp.apify.com/?actors=structlabs/live-ats-jobs-api`
- **n8n workflow:** [`n8n/live-ats-jobs-api-workflow.json`](n8n/live-ats-jobs-api-workflow.json)
- **Pricing:** Gold: $2.125 per 1,000 jobs + $0.05 per 1,000 starts. [Full pricing](https://apify.com/structlabs/live-ats-jobs-api)

## Quick start with n8n

1. Download [`n8n/live-ats-jobs-api-workflow.json`](n8n/live-ats-jobs-api-workflow.json).
2. In n8n: **Workflows → Import from File**.
3. Add `APIFY_TOKEN` to the n8n environment (Settings → Environment Variables).
4. Open the workflow, adjust the schedule, and run once to test.
5. The HTTP Request node calls `run-sync-get-dataset-items` and returns the rows directly.

## Quick start with Python

```bash
export APIFY_TOKEN=apify_api_...
python examples/quickstart.py
```

## Quick start with Node.js

```bash
export APIFY_TOKEN=apify_api_...
node examples/quickstart.mjs
```

## Input

```json
{
  "queries": [
    "AI Engineer"
  ],
  "remoteOnly": false,
  "providers": [
    "greenhouse",
    "ashby",
    "lever",
    "bamboohr"
  ],
  "maxCompanies": 20,
  "maxJobs": 10
}
```

## Sample output

Real sanitized rows from a verified cloud run (emails and phone numbers masked):

```json
[
  {
    "id": "greenhouse:gusto:7369003",
    "provider": "greenhouse",
    "company": "Gusto",
    "company_slug": "gusto",
    "title": "Enterprise Application AI Engineer",
    "location": "San Francisco, CA - Hybrid",
    "locations": [
      "San Francisco, CA - Hybrid"
    ],
    "remote_status": "hybrid",
    "seniority": "unknown",
    "salary_min": null,
    "salary_max": null,
    "salary_currency": null,
    "salary_period": null,
    "department": null,
    "employment_type": null,
    "posted_at": "2026-11-18T13:37:01-05:00",
    "url": "https://job-boards.greenhouse.io/gusto/jobs/7369003",
    "fetched_at": "2026-11-20T08:30:42.994638+00:00"
  },
  {
    "id": "greenhouse:gusto:7760341",
    "provider": "greenhouse",
    "company": "Gusto",
    "company_slug": "gusto",
    "title": "Staff Software Engineer, Core AI Platforms",
    "location": "San Francisco, CA - Hybrid; Denver, CO - Hybrid; New York, NY - Hybrid",
    "locations": [
      "San Francisco, CA - Hybrid; Denver, CO - Hybrid; New York, NY - Hybrid"
    ],
    "remote_status": "hybrid",
    "seniority": "staff",
    "salary_min": null,
    "salary_max": null,
    "salary_currency": null,
    "salary_period": null,
    "department": null,
    "employment_type": null,
    "posted_at": "2026-11-18T13:37:01-05:00",
    "url": "https://job-boards.greenhouse.io/gusto/jobs/7760341",
    "fetched_at": "2026-11-20T08:30:42.994898+00:00"
  },
  {
    "id": "greenhouse:gusto:7986047",
    "provider": "greenhouse",
    "company": "Gusto",
    "company_slug": "gusto",
    "title": "Staff Software Engineer, Retirement AI",
    "location": "Denver, CO;San Francisco, CA;New York, NY",
    "locations": [
      "Denver, CO;San Francisco, CA;New York, NY"
    ],
    "remote_status": "unknown",
    "seniority": "staff",
    "salary_min": null,
    "salary_max": null,
    "salary_currency": null,
    "salary_period": null,
    "department": null,
    "employment_type": null,
    "posted_at": "2026-11-18T13:37:01-05:00",
    "url": "https://job-boards.greenhouse.io/gusto/jobs/7986047",
    "fetched_at": "2026-11-20T08:30:42.995117+00:00"
  }
]
```

## MCP configuration

Copy [`mcp/mcp_config.json`](mcp/mcp_config.json) into your MCP client (Claude Desktop, Cursor, Windsurf):

```json
{
  "mcpServers": {
    "apify-live-ats-jobs-api": {
      "url": "https://mcp.apify.com/?actors=structlabs/live-ats-jobs-api"
    }
  }
}
```

Then ask your agent to run the Actor and return the dataset rows.

## Links

- Apify Store: https://apify.com/structlabs/live-ats-jobs-api
- n8n: https://n8n.io
- MCP: https://modelcontextprotocol.io

## License

MIT
