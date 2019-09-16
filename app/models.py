
 
class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category



class Articles:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,title,image,description,url,date):
        self.title = title
        self.image = image
        self.description = description
        self.url = url
        self.date = date
# class Review:

#     all_reviews = []

#     def __init__(self,movie_id,title,imageurl,review):
#         self.news_id = news_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):

#         response = []

#         for review in cls.all_reviews:
#             if review.news_id == id:
#                 response.append(review)

#         return response        