class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        print("Review added successfully!")

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Reviews:")

        if len(self.reviews) == 0:
            print("No reviews available.")
        else:
            for review in self.reviews:
                print("-", review)


book1 = Book("Wings of Fire", "A.P.J. Abdul Kalam")

book1.add_review("Very inspiring book.")
book1.add_review("Easy to understand and motivating.")

print("Total Reviews:", book1.count_reviews())

book1.display_reviews()