import heapq

class Twitter:

    def __init__(self):
        self.followers = {}
        self.followed_by = {}
        self.time = 0
        self.user_posts = {} 
        self.user_news_feed = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        user_posts = self.user_posts

        if userId not in user_posts:
            user_posts[userId] = []
        user_posts[userId].append((-1*self.time, userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        print(userId)
        if userId not in self.followed_by:
            self.followed_by[userId] = {userId}
        followed_by = self.followed_by[userId]
        print(followed_by)
        user_posts = self.user_posts
        news_feed = []
        heapq.heapify(news_feed)

        for user in followed_by:
            if user not in user_posts:
                user_posts[user] = []
            their_posts = user_posts[user][-10:]
            for post in their_posts:
                heapq.heappush(news_feed, post)
        
        result = []
        while news_feed != [] and len(result) != 10:
            _, _, tweet = heapq.heappop(news_feed)
            result.append(tweet)

        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # edge case
        if followerId == followeeId:
            return
        followers = self.followers
        if followeeId not in followers:
            followers[followeeId] = {followerId, followeeId}
        else:
            followers[followeeId].add(followerId)

        followed_by = self.followed_by
        if followerId not in followed_by:
            followed_by[followerId] = {followeeId, followerId}
        else:
            followed_by[followerId].add(followeeId)


        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # edge case
        if followerId == followeeId:
            return
        followers = self.followers
        if followerId in followers[followeeId]:
            followers[followeeId].remove(followerId)

        followed_by = self.followed_by
        if followeeId in followed_by[followerId]:
            followed_by[followerId].remove(followeeId)
        
