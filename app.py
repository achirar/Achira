import visibilities

def main():
    visibility = visibilities.visibility_data()
    
    print(len(visibility))

    positions = [i + 1 for i, char in enumerate(visibility) if char == '1']

    print(",".join(map(str, positions)))

if __name__ == "__main__":
    main()
