def main():
    name = input("请输入你的名字: ").strip()
    if not name:
        name = "朋友"

    print(f"你好，{name}！欢迎使用这个简单的 Python 程序。")


if __name__ == "__main__":
    main()
