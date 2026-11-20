"""Run Live ATS Jobs API on Apify and print the first rows."""
import json, os, urllib.request

TOKEN = os.environ.get("APIFY_TOKEN")
if not TOKEN:
    raise SystemExit("Set APIFY_TOKEN first")

payload = {
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

req = urllib.request.Request(
    "https://api.apify.com/v2/acts/structlabs~live-ats-jobs-api/run-sync-get-dataset-items",
    data=json.dumps(payload).encode(),
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=300) as r:
    items = json.load(r)

for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
print(f"{len(items)} items")
