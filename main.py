logs = [
    "INFO: System started",
    "ERROR: Database connection failed",
    "WARNING: High memory usage",
    "ERROR: Timeout",
    "ERROR: Database connection failed",
    "INFO: Process completed"
]

error_count = {}
total_errors = 0

for log in logs:
    if "ERROR" in log:
        total_errors += 1
        error_type = log.split(":")[1].strip()
        error_count[error_type] = error_count.get(error_type, 0) + 1

print(f"\nTotal errors: {total_errors}\n")

print("Error breakdown:")
for k, v in error_count.items():
    print(f"{k}: {v}")
