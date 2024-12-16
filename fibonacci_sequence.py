def fibonacci_sequence(n):
    """Calcola la sequenza di Fibonacci fino al termine n."""
    sequence = [0, 1]  # I primi due numeri della sequenza
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

if __name__ == "__main__":
    n = int(input("Quanti numeri della sequenza di Fibonacci vuoi calcolare? "))
    print(f"Sequenza di Fibonacci ({n} termini): {fibonacci_sequence(n)}")
