# Exercise 97 — Balance a chemical equation
# Uses the chempy library for symbolic chemical balancing.
# Requires: chempy (pip install chempy)
# ─────────────────────────────────────────────────────────────────────────────

def balance_equation(reactants: list, products: list):
    try:
        from chempy import balance_stoichiometry
        reac_dict = {r: None for r in reactants}
        prod_dict = {p: None for p in products}
        reac_bal, prod_bal = balance_stoichiometry(set(reactants), set(products))
        lhs = " + ".join(f"{v}{k}" for k, v in reac_bal.items())
        rhs = " + ".join(f"{v}{k}" for k, v in prod_bal.items())
        print(f"Balanced: {lhs} → {rhs}")
    except ImportError:
        print("chempy not installed. Run: pip install chempy")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Example: H2 + O2 → H2O")
    raw_r = input("Enter reactants separated by commas: ")
    raw_p = input("Enter products  separated by commas: ")
    reactants = [r.strip() for r in raw_r.split(",")]
    products  = [p.strip() for p in raw_p.split(",")]
    balance_equation(reactants, products)

if __name__ == "__main__":
    main()
