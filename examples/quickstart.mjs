// Run Live ATS Jobs API on Apify and print the first rows.
const token = process.env.APIFY_TOKEN;
if (!token) throw new Error("Set APIFY_TOKEN first");

const input = {
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
};

const res = await fetch("https://api.apify.com/v2/acts/structlabs~live-ats-jobs-api/run-sync-get-dataset-items", {
  method: "POST",
  headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
  body: JSON.stringify(input),
});
if (!res.ok) throw new Error(`Apify ${res.status}: ${await res.text()}`);
const items = await res.json();
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
console.log(`${items.length} items`);
