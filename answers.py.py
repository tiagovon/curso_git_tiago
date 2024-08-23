from projeto.extraction import load_data


def main():
    df = load_data()
    print(df.head())

if __name__ == "__main__":
    main()