import rich, time
from rich.progress import Progress

class PrimeNum:  # Prime number class
    def __init__(self):
        pass

    @staticmethod        
    def main():
        start_range = int(input("Enter the starting value of the prime range (>=2): "))
        end_range = int(input("Enter the ending value of the prime range (>=2): "))
        start_time = time.time()
        primes = PrimeNum.generate(start_range, end_range, show_progress=True)
        end_time = time.time()
        print(f"\nPrime number range: {start_range}-{end_range}")
        print(f"Number of primes: {len(primes)}")
        print(f"Elapsed time: {end_time - start_time:.4f} seconds")
        save = input("Save primes to file? (yes/no): ").strip().lower()
        if save == "yes" or save == "y":
            filename = f"{start_range}-{end_range}_primes.txt"
            with open(filename, "w") as f:
                for p in primes:
                    f.write(f"{p}\n")
            print(f"Saved to file: {filename}")
        else:
            print("File not saved.")

    @staticmethod
    def judge(num: int):
        if num < 2:
            return False  # Numbers less than 2 are not prime
        for i in range(2, int(num**0.5) + 1):  # Only check up to square root
            if num % i == 0:
                return False
        return True

    @staticmethod
    def generate(start: int, end: int, show_progress: bool = True):
        # Range check
        if start < 2:
            start = 2
        if end < start:
            return []

        is_prime = [True] * (end + 1)
        is_prime[0:2] = [False, False]

        total_steps = max(1, int(end ** 0.5) - 1)
        step_block = max(1, total_steps // 1000)

        if show_progress:
            with Progress() as progress:
                task = progress.add_task("[green]Sieve in progress...", total=total_steps)
                for i in range(2, int(end ** 0.5) + 1):
                    if is_prime[i]:
                        for j in range(i*i, end+1, i):
                            is_prime[j] = False
                    if (i-1) % step_block == 0:
                        progress.update(task, advance=step_block)
                progress.update(task, advance=total_steps - progress.tasks[0].completed)
        else:
            for i in range(2, int(end ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i*i, end+1, i):
                        is_prime[j] = False

        return [i for i in range(start, end + 1) if is_prime[i]]




 
#  _            _  _             _
# | |__    ___ (_)| |__    __ _ (_) _ __ ___    ___ 
# | '_ \  / _ \| || '_ \  / _` || || '_ ` _ \  / __|
# | |_) ||  __/| || | | || (_| || || | | | | || (__ 
# |_.__/  \___||_||_| |_| \__,_||_||_| |_| |_| \___|
#
# This Python program generates prime numbers within a given range.
# 
# To use this program, run the "main" function in the "PrimeNum" class.
# To generate prime numbers within a given range, call the "generate" function.
# To check if a number is prime, call the "judge" function.
# The "generate" function takes two arguments: start and end, which are the
# starting and ending values of the range to generate primes in.
# The "show_progress" argument is optional and defaults to True. If set to
# The program will prompt you to enter the start and end of the range,
# generate all primes in that range, display them, and optionally save to a file.
# 
# Example:
# >>> from prime_generator import PrimeNum
# >>> PrimeNum.main()
# Enter the starting value of the prime range (>=2): 10
# Enter the ending value of the prime range (>=2): 50
# Prime number range: 10-50
# Number of primes: 17
# Elapsed time: 0.0001 seconds
# Save primes to file? (yes/no): y

# Saved to file: 10-50_primes.txt
