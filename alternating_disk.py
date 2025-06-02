def alternating_disk_alg(n, S): 
    if n == 1: # base case 
        S[0], S[1] = 1, 0
        return S, 1
    swaps = 0
    while True:
        # Left to right pass
        for i in range(0, 2 * n - 1):
            if S[i] == 0 and S[i + 1] == 1:  # If left is white and right is black
                S[i], S[i + 1] = S[i + 1], S[i]
                swaps += 1
        # Right to left pass
        for i in range(2 * n - 1, 0, -1):
            if S[i - 1] == 0 and S[i] == 1:  # If left is white and right is black
                S[i - 1], S[i] = S[i], S[i - 1]
                swaps += 1
        # Check if first n elements are all black
        all_black = True
        for i in range(n):
            if S[i] != 1:
                all_black = False
                break
        if all_black:
            break
    return S, swaps

    # Test case for alternating_disk_alg
if __name__ == "__main__":
    # Example: n = 3, S = [0, 1, 0, 1, 0, 1] (alternating white(0) and black(1))
    import time

    test_ns = [1,2,3,4,5,10,20,50]
    for n in test_ns:
        # Create alternating sequence: [0, 1, 0, 1, ..., 0, 1] of length 2n
        S = [0 if i % 2 == 0 else 1 for i in range(2 * n)]
        start_time = time.time()
        result, swaps = alternating_disk_alg(n, S.copy())
        elapsed = time.time() - start_time
        print(f"\nn = {n}")
        #print("Final arrangement:", result)
        print("Number of swaps:", swaps)
        print(f"Time taken: {elapsed:.6f} seconds")
