def solution(genres, plays):
    answer = []
    genre_total = {}
    for g, p in zip(genres, plays):
        genre_total[g] = genre_total.get(g, 0) + p

    sorted_genres = sorted(genre_total, key=genre_total.get, reverse=True)

    songs_by_genre = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if g not in songs_by_genre:
            songs_by_genre[g] = []
        songs_by_genre[g].append([i, p])

    for g in sorted_genres:
        songs = sorted(songs_by_genre[g], key=lambda x: x[1], reverse=True)
    
        for i in range(min(len(songs), 2)):
            answer.append(songs[i][0])
    return answer