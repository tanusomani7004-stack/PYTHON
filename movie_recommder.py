movies = [
    {"name": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"name": "Interstellar", "genre": "Sci-Fi", "rating": 8.7},
    {"name": "3 Idiots", "genre": "Comedy", "rating": 8.4},
    {"name": "Dangal", "genre": "Sports", "rating": 8.3},
    {"name": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"name": "Avengers: Endgame", "genre": "Action", "rating": 8.4},
    {"name": "La La Land", "genre": "Romance", "rating": 8.0},
    {"name": "The Notebook", "genre": "Romance", "rating": 7.8},
]


def show_all_movies():
    print("\n========== ALL MOVIES ==========")

    for movie in movies:
        print(
            f"{movie['name']} | "
            f"{movie['genre']} | "
            f" {movie['rating']}"
        )


def search_by_genre():
    genre = input("Enter genre: ").strip().lower()

    results = [
        movie
        for movie in movies
        if movie["genre"].lower() == genre
    ]

    if not results:
        print(" No movies found.")
        return

    print(f"\n========== {genre.upper()} MOVIES ==========")

    for movie in results:
        print(
            f"{movie['name']} →  {movie['rating']}"
        )


def top_movies():
    top = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    print("\n========== TOP RATED MOVIES ==========")

    for movie in top[:5]:
        print(
            f"{movie['name']} → "
            f"{movie['genre']} → "
            f" {movie['rating']}"
        )


def recommend_movie():
    try:
        minimum_rating = float(
            input("Minimum rating (e.g. 8.5): ")
        )
    except ValueError:
        print(" Enter a valid rating.")
        return

    recommendations = [
        movie
        for movie in movies
        if movie["rating"] >= minimum_rating
    ]

    if not recommendations:
        print(" No movies match your rating.")
        return

    print("\n========== RECOMMENDATIONS ==========")

    for movie in recommendations:
        print(
            f"🎬 {movie['name']} | "
            f"{movie['genre']} | "
            f"{movie['rating']}"
        )


def main():

    while True:

        print("\n" + "=" * 40)
        print("        MOVIE RECOMMENDER")
        print("=" * 40)
        print("1. Show All Movies")
        print("2. Search by Genre")
        print("3. Top Rated Movies")
        print("4. Get Recommendations")
        print("5. Exit")
        print("=" * 40)

        choice = input("Enter choice: ")

        if choice == "1":
            show_all_movies()

        elif choice == "2":
            search_by_genre()

        elif choice == "3":
            top_movies()

        elif choice == "4":
            recommend_movie()

        elif choice == "5":
            print("\n Goodbye!")
            break

        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    main()
