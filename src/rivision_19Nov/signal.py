signal = [10, 20, 30, 40, 50, 60, 70, 80]

# Step 1: Reverse every alternate element from end
step1 = signal[::-2]

# Step 2: Extract elements from index 1 to -1
step2 = step1[1:-1]

# Step 3: Slice with step -1
final = step2[::-1]

print(final)