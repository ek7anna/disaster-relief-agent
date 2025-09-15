import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def run_agent(alert_id: int) -> dict:
    """
    Connects to TiDB, fetches alert + resources,
    and returns a simple dispatch plan.
    """

    # Connect to TiDB
    conn = pymysql.connect(
        host=os.getenv("TIDB_HOST"),
        port=int(os.getenv("TIDB_PORT")),
        user=os.getenv("TIDB_USER"),
        password=os.getenv("TIDB_PASSWORD"),
        database=os.getenv("TIDB_DATABASE"),
        ssl={'ssl': {}}  # required for TiDB Cloud
    )

    with conn.cursor(pymysql.cursors.DictCursor) as cur:
        # Fetch alert info
        cur.execute("SELECT * FROM alerts WHERE id=%s", (alert_id,))
        alert = cur.fetchone()

        if not alert:
            return {"error": f"No alert found with id={alert_id}"}

        # Fetch available resources (for now, just 2)
        cur.execute("SELECT * FROM resources WHERE status='available' LIMIT 2;")
        resources = cur.fetchall()

    conn.close()

    # Build dispatch plan
    dispatch_plan = f"Dispatch {', '.join(r['name'] for r in resources)} to " \
                    f"{alert['latitude']}, {alert['longitude']}."

    return {
        "alert_text": alert["alert_text"],
        "resources": resources,
        "dispatch_plan": dispatch_plan
    }