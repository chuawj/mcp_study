import threading
import time

# 작업(Job)을 처리하는 MCT (Master Control Task) 클래스 정의
class MCT(threading.Thread):
    def __init__(self, job_id, duration):
        super().__init__()
        self.job_id = job_id
        self.duration = duration  # 작업 소요 시간 (초)

    def run(self):
        print(f"[MCT-{self.job_id}] 작업 시작")
        time.sleep(self.duration)  # 작업 수행 중 (대기)
        print(f"[MCT-{self.job_id}] 작업 완료")

# MCP Executive 역할: 작업을 받아서 MCT 생성 후 실행 관리
class MCPExecutive:
    def __init__(self):
        self.tasks = []

    def submit_job(self, job_id, duration):
        print(f"사용자 작업 제출: Job-{job_id}")
        task = MCT(job_id, duration)
        self.tasks.append(task)
        task.start()  # MCT 실행

    def wait_for_all(self):
        for task in self.tasks:
            task.join()
        print("모든 작업이 완료되었습니다.")

# 메인 실행 예제
if __name__ == "__main__":
    mcp = MCPExecutive()

    # 사용자 작업 제출 (job_id, 수행시간)
    mcp.submit_job(1, 2)
    mcp.submit_job(2, 3)
    mcp.submit_job(3, 1)

    # 모든 작업이 완료될 때까지 대기
    mcp.wait_for_all()
