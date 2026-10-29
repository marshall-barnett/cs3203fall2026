def hasMinimumHistory(readingHistory, minHistoryThreshold):
    if not isinstance(readingHistory, list):
        raise TypeError("Reading history must be a list")
    if not isinstance(minHistoryThreshold, int) or minHistoryThreshold < 0:
        raise TypeError("Threshold must be a non-negative integer")
    return len(readingHistory) >= minHistoryThreshold

def generateRecommendations(readingHistory, preferences):
    if not isinstance(readingHistory, list):
        raise TypeError("Reading history must be a list")
    if not isinstance(preferences, dict):
        raise TypeError("Preferences must be a dictionary")
    
    catalog = {
        "sci-fi": ["Dune", "Neuromancer", "Foundation", "Snow Crash"],
        "fantasy": ["The Hobbit", "Mistborn"]
    }
    
    genre = preferences.get("genre")
    if not genre or not isinstance(genre, str):
        return []
    
    normalized_genre = genre.strip().lower()
    matched_books = catalog.get(normalized_genre, [])
    
    history_set = {b.strip().lower() for b in readingHistory}
    recommendations = [b for b in matched_books if b.strip().lower() not in history_set]
    
    return recommendations