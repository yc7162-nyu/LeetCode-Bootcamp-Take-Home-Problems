
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        day = 1

        # len = number of people how know
        # val is the day they knew
        knows = deque()
        knows.append((1,1)) # tuple: (day, number of people)

        start_sharing = {}
        start_sharing[1 + delay] = 1

        sharing = 0

        people = 1

        while day <= n:
            # Check if anyone forget
            # By checking front of knows
            if knows[0][0] + forget == day:
                # They will always be already sharing as delay < forget
                people -= knows[0][1]
                sharing -= knows[0][1]
                knows.popleft()
            
            # Check if any new people can start to share
            if day in start_sharing and start_sharing[day] != 0:
                sharing += start_sharing[day]
                del start_sharing[day]
    
            # add the number of new people to sharing
            if sharing != 0:
                knows.append((day, sharing))
                people += sharing

                # start_sharing stores day they can start sharing
                if (day + delay) not in start_sharing:
                    start_sharing[day + delay] = sharing
                else:
                    start_sharing[day + delay] += sharing
                    
            day += 1       

        return people % MOD
   

    # Lose on day knew + forget
    # Share on day: knew + delay
    # Delay < Forget
    # Check front of queue for forget
    # Separate map sharing when a person can start sharing
    # Have a varaible sharing of number of people who can currently share