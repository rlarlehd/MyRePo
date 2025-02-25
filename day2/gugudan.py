def func_ggd():
    for i in range(2, 10):
        print(f"=== {i} ===")
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()

if __name__ == "__main__":
    func_ggd()
