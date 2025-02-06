from sklearn.tree import DecisionTreeClassifier

def train_classifier(data, labels):
    classifier = DecisionTreeClassifier()
    classifier.fit(data, labels)
    return classifier

def predict_class(classifier, features):
    prediction = classifier.predict([features])
    return prediction[0]

def main():
    # Data for classification: [Weight (lbs), Life-span (years), Sleep per day (hrs)]
    data = [
        # Dogs
        [50, 12, 12], [60, 10, 14], [25, 15, 10], [80, 9, 13], [45, 13, 11],
        # Cats
        [8, 15, 16], [10, 18, 14], [12, 14, 13], [9, 20, 15], [11, 16, 14],
        # Birds
        [1.5, 5, 10], [2, 6, 8], [3, 8, 7], [1.8, 4, 9], [2.5, 7, 8],
        # Fish
        [0.5, 3, 12], [1, 2, 13], [0.3, 4, 11], [0.7, 5, 12], [1.2, 6, 10]
    ]

    # Labels corresponding to each entry in the data
    labels = [
        "Dog", "Dog", "Dog", "Dog", "Dog",  # Dogs
        "Cat", "Cat", "Cat", "Cat", "Cat",  # Cats
        "Bird", "Bird", "Bird", "Bird", "Bird",  # Birds
        "Fish", "Fish", "Fish", "Fish", "Fish"  # Fish
    ]

    # Train the classifier
    classifier = train_classifier(data, labels)

    # Example predictions
    bird = predict_class(classifier, [2, 7, 6])
    print(f"Prediction for bird: {bird}")

    cat = predict_class(classifier, [8, 17, 15])
    print(f"Prediction for cat: {cat}")

    fish = predict_class(classifier, [0.8, 5, 8])
    print(f"Prediction for fish: {fish}")

    dog = predict_class(classifier, [40, 14, 12])
    print(f"Prediction for dog: {dog}")

if __name__ == "__main__":
    main()
