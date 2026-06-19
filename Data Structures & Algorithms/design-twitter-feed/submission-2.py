import heapq

class Twitter:

    def __init__(self):
        self.followers = {}
        self.news_feed = []
        heapq.heapify(self.news_feed)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        followers = self.followers
        news_feed = self.news_feed
        self.time += 1

        heapq.heappush(news_feed, (-1*self.time, userId, tweetId))
        if userId not in followers:
            followers[userId] = {userId}

    
    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = self.news_feed
        followers = self.followers
        put_back = []

        result = []
        while len(result) != 10 and news_feed != []:
            time, user, tweet = heapq.heappop(news_feed)
            if user not in followers:
                followers[user] = {userId}
            if userId in followers[user]:
                result.append(tweet)
            put_back.append((time, user, tweet))
        
        for unused in put_back:
            heapq.heappush(news_feed, unused)
        print(news_feed)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        followers = self.followers
        if followeeId not in followers:
            followers[followeeId] = {followerId}
        else:
            followers[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        followers = self.followers
        if followerId in followers[followeeId]:
            followers[followeeId].remove(followerId)
        
