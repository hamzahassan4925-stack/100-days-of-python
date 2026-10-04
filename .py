# 1. Ek simple list banana (Fruits/Phal)
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("--- Original List ---")
print(fruits)

# 2. List me naya item add karna (.append)
fruits.append("Grapes")
print("\n'Grapes' add karne ke baad:")
print(fruits)

# 3. List se item remove karna (.remove)
fruits.remove("Banana")
print("\n'Banana' remove karne ke baad:")
print(fruits)

# 4. List ke items ko ek ek karke print karna (for loop)
print("\n--- Sabhi Phal (Loop ke zariye) ---")
for fruit in fruits:
    print(f"Mujhe {fruit} pasand hai.")

# 5. Numbers ki list ke sath simple calculation
numbers = [10, 25, 5, 40, 15]

print("\n--- Numbers List ---")
print("Numbers:", numbers)
print("Sab se bara number (Max):", max(numbers))
print("Sab ka sum (Total):", sum(numbers))