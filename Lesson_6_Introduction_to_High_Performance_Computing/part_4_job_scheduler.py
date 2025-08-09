class JobScheduler:
    def __init__(self):
        self.job_queue = []

    def add_job(self, job):
        self.job_queue.append(job)

    def run_jobs(self):
        while self.job_queue:
            current_job = self.job_queue.pop(0)
            print(f"Running job: {current_job}")
            # Simulate the job processing
            # In a real scenario, we would integrate with the HPC scheduler
           
scheduler = JobScheduler()
scheduler.add_job("Data Analysis")
scheduler.add_job("Model Training")
scheduler.add_job("Risk Assessment")

scheduler.run_jobs()
