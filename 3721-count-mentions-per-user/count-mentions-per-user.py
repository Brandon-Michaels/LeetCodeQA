from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        # online_until[i] stores the timestamp when user i's current offline period ends.
        online_until = [0] * numberOfUsers

        # --- FIX 1: Correct Sorting Tie-breaker ---
        # OFFLINE (priority 0) must be processed BEFORE MESSAGE (priority 1) at the same timestamp.
        def get_priority(event_type):
            return 0 if event_type == "OFFLINE" else 1

        # Sort key: (timestamp, priority)
        events.sort(key=lambda x: (int(x[1]), get_priority(x[0]))) 
        # --------------------------------------------

        def is_online(user_id, current_time):
            # User is online if their 'offline ends' time is less than or equal to the current time.
            return online_until[user_id] <= current_time

        for event in events:
            event_type, timestamp_str, data = event
            timestamp = int(timestamp_str)

            if event_type == "OFFLINE":
                user_id = int(data)
                # User goes offline and will be online again at timestamp + 60
                online_until[user_id] = timestamp + 60

            else:  # MESSAGE
                tokens = data.split()
                
                # --- FIX 2 (Already Corrected in your submission): Iterate over all tokens ---
                for token in tokens:
                    if token == "ALL":
                        # 'ALL' mentions all users, regardless of online status.
                        for i in range(numberOfUsers):
                            mentions[i] += 1
                    elif token == "HERE":
                        # 'HERE' mentions all *online* users.
                        for i in range(numberOfUsers):
                            if is_online(i, timestamp):
                                mentions[i] += 1
                    elif token.startswith("id"):
                        # Individual ID mention.
                        user_id = int(token[2:])
                        mentions[user_id] += 1
                        
        return mentions