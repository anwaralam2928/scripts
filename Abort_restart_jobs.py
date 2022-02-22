import json
import urllib
import urllib2
import requests

RUNNING_JOBS_URL = "https://peppwebservice.qualcomm.com/api/rest/exemgr/jobsdisplay/?pool_name={}&state=running"
ABORT_URL = "https://peppwebservice.qualcomm.com/api/rest/exemgr/jobs/{}/abort"
RESTART_URL = "https://peppwebservice.qualcomm.com/api/rest/exemgr/jobs/{}/retry"

laf_sd_running_job = [3825729
,3825725
,3825724
,3825727]

def RunningJobs(pool_name):
    URL = RUNNING_JOBS_URL.format(pool_name)
    f = urllib.urlopen(URL)
    response = f.read()
    d = json.loads(response)
    running_jobs = []
    for i in range(d['count']):
        running_jobs.append(d['results'][i]['id'])
    return running_jobs
    
def AbortJob(jobId):
    URL = ABORT_URL.format(jobId)
    print URL
    f = urllib.urlopen(URL, " ")
    print str(jobId) + "-" + "status_code:" + str(f.code)
    
def RestartJob(jobId):
    URL = RESTART_URL.format(jobId)
    print URL
    payload = {"results":[{"status": "SUBMITTED","job_id": 3866182,"task_id": 3866182,"playlist_group_name": "LAF","report_url": "http://darts-reports.qualcomm.com/pepp/jobs/3766182","job_status_url": "https://peppwebservice.qualcomm.com/api/rest/exemgr/jobs/3866182/status","msg": "Successfully created job with id: 3866182"}]}   
    f = urllib.urlopen(URL,payload)
    print str(jobId) + "-" + "status_code:" + str(f.code)

def RestartJobWithpayload(jobId):
    URL = RESTART_URL.format(jobId)
    print URL
    postdata = {"results":[{"status": "SUBMITTED","job_id": 3866182,"task_id": 3866182,"playlist_group_name": "LAF"}]}
    req = urllib2.Request(URL)
    req.add_header('Content-Type','application/json')
    data = json.dumps(postdata)
    response = urllib2.urlopen(req,data)
    print str(jobId) + "-" + "status_code:" + str(response.code)
	
        
def main():
    #running_jobs =  RunningJobs("laf_sd")
    #print running_jobs
    for job in range(len(laf_sd_running_job)):
        AbortJob(laf_sd_running_job[job])
        #print "job {} is successfully aborted".format(job)
        #RestartJobWithpayload(laf_sd_running_job[job])
        #print "restarted job".format(job)
    
if __name__ == '__main__':
    main()