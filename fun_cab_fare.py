def cab_fare(distance_km, rate_per_km):
    total_fare = distance_km * rate_per_km
    return total_fare

distance =float(input("Enter the distance travelled: "))
rate =float(input("Enter the rate per Km: "))
fare = cab_fare(distance, rate)
print("The total cab fare is:", fare)
