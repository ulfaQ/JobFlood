from files import files

#   class Job:
#       def __init__(self, details, products):
#           """ Details should contain a customer and addditional data i.e. comment """

class JobManager:
    def __init__(self):
        self.file = "job_list.txt"
        self.job_list = {}
#        self.job_list = files.get_job_list_from_file(self.file)

JM = JobManager()
