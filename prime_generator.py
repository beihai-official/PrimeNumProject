import rich,time
from rich.progress import Progress
class PrimeNum:                 #质数类
    def __init__(self):
        start_range = int(input("请输入质数范围的起始值>=2: "))
        end_range = int(input("请输入质数范围的结束值>=2: "))
        start_time = time.time()
        primes = PrimeNum.generate(start_range, end_range)
        end_time = time.time()
        print(f"\n本次寻找质数的范围: {start_range}-{end_range}")
        print(f"质数数量: {len(primes)}")
        print(f"耗时: {end_time - start_time:.4f} 秒")
        save = input("是否保存质数到文件？(yes/no): ").strip().lower()
        if save == "yes" or save == "y":
            filename = f"{start_range}-{end_range}范围内的质数.txt"
            with open(filename, "w") as f:
                for p in primes:
                    f.write(f"{p}\n")
            print(f"已保存到文件: {filename}")
        else:
            print("未保存文件。")

    def judge(self, num: int):
        if num < 2:
            return False            #小于2的数不是质数
        for i in range(2, int(num**0.5) + 1):       #判断质数的算法，只需判断到平方根的整数部分即可
            if num % i == 0:
                return False
        return True

    
    def generate(start: int, end: int):
        if start < 1 or end < 1 or start > end:
            return "Invalid Input"
        
        is_prime = [True] * (end + 1)
        is_prime[0:2] = [False, False]

        with Progress() as progress:
            task = progress.add_task("[green]Sieve in progress...", total=end - 1)

            for i in range(2, int(end ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, end + 1, i):
                        is_prime[j] = False
                progress.update(task, advance=1)

        for i in range(start, end + 1):
            if is_prime[i]:
                print(i, end=" ")  # 横向打印，空格隔开
        print()  # 打印完换行
        return [i for i in range(start, end + 1) if is_prime[i]]
        
if __name__ == "__main__":
    PrimeNum()


#  _            _  _             _
# | |__    ___ (_)| |__    __ _ (_) _ __ ___    ___ 
# | '_ \  / _ \| || '_ \  / _` || || '_ ` _ \  / __|
# | |_) ||  __/| || | | || (_| || || | | | | || (__ 
# |_.__/  \___||_||_| |_| \__,_||_||_| |_| |_| \___|