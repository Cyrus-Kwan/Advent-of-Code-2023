def current_dir():
    '''
    Returns the current directory of __main__
    '''
    pattern = r"^.*[/\\]"
    searches = re.search(pattern, __file__)
    groups = searches.group(0)
    return groups

def main():
    directory = current_dir()

if __name__ == "__main__":
    main()