class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        
        # 각 사람들이 티켓을 사는 시간 계산
        for i in range(len(tickets)):
            if i <= k:
                # k 이전이나 k번째 사람
                time += min(tickets[i], tickets[k])
            else:
                # k 이후의 사람
                time += min(tickets[i], tickets[k] - 1)
        
        return time