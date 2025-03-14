import schedule
import time
import subprocess

def run_ai_research():
    """Trigger the AI Research Agent to generate a new report."""
    print("Running AI Research Agent...")
    subprocess.run(["python", "your_ai_research_script.py"])  # Replace with actual script filename
    print("AI Research Task Completed.")

# Schedule the AI research to run every Monday at 8 AM
schedule.every().monday.at("08:00").do(run_ai_research)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute before checking again
