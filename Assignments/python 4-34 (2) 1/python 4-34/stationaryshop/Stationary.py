print("Cost of A4sheet:")
cost_a4sheet = float(input())

if cost_a4sheet < 0:
    print("Invalid input")
    exit(0)

print("Cost of pen:")
cost_pen = float(input())

if cost_pen < 0:
    print("Invalid input")
    exit(0)

print("Cost of pencil:")
cost_pencil = float(input())

if cost_pencil < 0:
    print("Invalid input")
    exit(0)

print("Cost of eraser:")
cost_eraser = float(input())

if cost_eraser < 0:
    print("Invalid input")
    exit(0)

# Display the item details
print("\nItems Details")
print(f"A4sheet:{cost_a4sheet:.2f}")
print(f"Pen:{cost_pen:.2f}")
print(f"Pencil:{cost_pencil:.2f}")
print(f"Eraser:{cost_eraser:.2f}")