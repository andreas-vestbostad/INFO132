import numpy as np
import matplotlib.pyplot as plt

# Parametre
a = 10  # Makspris
b = 1   # Etterspørselskoeffisient
C = 3   # Konstant enhetskostnad

# Funksjoner
def demand(x):
    return a - b * x

# Mengde i frikonkurranse og monopol
X_fri = (a - C) / b
X_monopol = (a - C) / (2 * b)

# Priser
P_fri = demand(X_fri)
P_monopol = demand(X_monopol)

# Data for plotting
X_values = np.linspace(0, 10, 100)
P_values = demand(X_values)

# Plotting
plt.figure(figsize=(10, 6))

# Etterspørselskurve
plt.plot(X_values, P_values, label='Etterspørsel (P(X))', color='blue')

# Frikonkurranse linje
plt.axvline(X_fri, linestyle='--', color='green', label=f'Frikonkurranse (X={X_fri:.2f})')
plt.plot(X_fri, P_fri, 'go')  # punkt på frikonkurranse

# Monopol linje
plt.axvline(X_monopol, linestyle='--', color='red', label=f'Monopol (X={X_monopol:.2f})')
plt.plot(X_monopol, P_monopol, 'ro')  # punkt på monopol

# Dødvektstapet (området mellom X_fri og X_monopol)
X_fill = np.linspace(X_monopol, X_fri, 100)
P_fill = demand(X_fill)
plt.fill_between(X_fill, P_fill, C, color='gray', alpha=0.5, label="Dødvektstap")

# Legende og etiketter
plt.xlabel("Mengde (X)")
plt.ylabel("Pris (P)")
plt.title("Dødvektstap ved monopoltilpasning vs. frikonkurranse")
plt.legend()

# Vis grafen
plt.grid(True)
plt.show()
