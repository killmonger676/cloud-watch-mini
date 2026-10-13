# CloudWatch Mini — Server Monitoring Dashboard

A beginner-friendly Streamlit app that simulates CPU and memory monitoring for three servers and raises an alarm when CPU exceeds a chosen threshold.

## Requirements
- Python 3.9 or newer
- Internet connection for the first package install

## Run on Windows
1. Extract the ZIP file.
2. Open the extracted `cloudwatch_mini_project` folder.
3. Click the address bar in File Explorer, type `cmd`, and press Enter.
4. Run:

```bash
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

If `py` does not work, try `python` instead:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The browser should open automatically. If not, open the local URL printed in the terminal (usually `http://localhost:8501`).

## Demo
- Keep “Simulate a high-CPU incident” enabled to show an alarm.
- Change the CPU alarm threshold to see how the status changes.
- Turn off the simulated incident to show normal operation.
- Refresh the page for a new set of simulated readings.

## Important scope note
This is a local prototype using fictional, randomly generated metrics. It is inspired by Amazon EC2 and Amazon CloudWatch but is **not connected to AWS** and does not monitor real infrastructure.

## 30-second interview explanation
“I built CloudWatch Mini, a Python dashboard that simulates monitoring three servers. It displays CPU and memory usage, compares CPU usage with a configurable threshold, and shows an alarm with a suggested troubleshooting action. It helped me understand the relationship between EC2 instances, CloudWatch metrics and alarms, and how a notification service like SNS could be added. The current version uses simulated data and runs locally; connecting it to AWS would be a future improvement.”

## Possible next steps
- Connect to actual CloudWatch metrics from EC2 using a least-privilege IAM role.
- Create CloudWatch alarms instead of local threshold checks.
- Send alerts through Amazon SNS.
- Add metric history and incident logs.
