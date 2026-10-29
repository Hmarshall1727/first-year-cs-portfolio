films = []

for i in range(1, 6):
    film = input(f"Enter favourite film #{i}: ")
    films.append(film)

print("\n--- Film Summary ---")
print("Whole list:", films)
print("Number of films", len(films))
print("Film 1:", films[0])
print("Next Film:", films[len(films) - 1])
print("Top 3 films", films[0:3])
