# Exercise 88 — Create and import a module that calculates trip costs
# ─────────────────────────────────────────────────────────────────────────────

def fuel_cost(distance_km: float, consumption_l_per_100km: float,
              price_per_liter: float) -> float:
    """Calculate fuel cost for a trip."""
    liters_needed = (distance_km / 100) * consumption_l_per_100km
    return liters_needed * price_per_liter

def toll_cost(distance_km: float, toll_rate_per_km: float = 0.10) -> float:
    """Estimate toll cost."""
    return distance_km * toll_rate_per_km

def total_trip_cost(distance_km, consumption, price_per_liter, toll_rate=0.10):
    return fuel_cost(distance_km, consumption, price_per_liter) + \
           toll_cost(distance_km, toll_rate)

def main():
    d = float(input("Distance (km)                : "))
    c = float(input("Fuel consumption (L/100km)   : "))
    p = float(input("Fuel price (per liter)        : "))
    t = float(input("Toll rate per km (default 0.10): ") or "0.10")
    print(f"\nFuel cost  : {fuel_cost(d, c, p):.2f}")
    print(f"Toll cost  : {toll_cost(d, t):.2f}")
    print(f"Total cost : {total_trip_cost(d, c, p, t):.2f}")

if __name__ == "__main__":
    main()
