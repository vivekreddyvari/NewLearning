def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    positive_words = set()
    negative_words = set()
    for word in positiveKeywords.split(" "):
        positive_words.add(word.lower())

    for word in negativeKeywords.split(" "):
        negative_words.add(word.lower())
    hotel_score = {}

    for i in range(0, len(reviews)):
        hotel = hotelIds[i]
        score = hotel_score.get(hotel, 0)
        review = reviews[i].split(" ")
        pos = 0
        neg = 0
        for word in review:
            if (word[-1] == '.' or word[-1] == ','):
                word = word[0:-1]
            if word.lower() in positive_words:
                pos += 1
            if word.lower() in negative_words:
                neg += 1

        hotel_score[hotel] = score + 3 * pos - neg

    result = sorted(hotel_score, key=hotel_score.get, reverse=True)

    return result[0:k]

if __name__ == "__main__":
    positivekeywords = 'breakfast beach city center location metro view staff price'
    negativekeywords = 'not'
    hotelIds = [6,2,8,4,1]
    reviews = [ "This hotel has a nice view of the city center. The location is perfect.",
                "The breakfast is ok. Regarding location, it is quite far from city center but the price is cheap so it is worth.",
                "Location is excellent, 5 minutes from the city center. There is also a metro station very close to the hotel.",
                "They said I couldn’t take my dog and there were other guests with dogs! That is not fair.",
                "Very friendly staff and a good cost-benefit ratio. Its location is a bit far from the city center."]
    print(len(reviews))
    k = 5

    p = awardTopKHotels(
        positiveKeywords=positivekeywords,
        negativeKeywords=negativekeywords,
        hotelIds=hotelIds,
        reviews=reviews,
        k=k
                    )
    print(p)
