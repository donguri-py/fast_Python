try:
    with open("pico.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("ファイルが見つかりません", e)

except Exception as e:
    print(e)