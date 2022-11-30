"""
Wiki
30/11/2022
This program displays wikipedia pages chosen by user input.
"""

import wikipedia


def main():
    """While user input is not blank, display wikipedia page summary or possible options if page does not exist."""
    page_input = input("Page: ")
    while page_input != "":
        try:
            page = wikipedia.page(page_input)
            title = page.title
            summary = page.summary
            url = page.url
            print(f"{title}\n{summary}\n{url}")
        except wikipedia.exceptions.PageError:
            print(f"Page \"{page_input}\" does not exist. Try another query!")
        except wikipedia.exceptions.DisambiguationError:
            print(f"Here are some disambiguation pages for {page_input}:")
            for item in wikipedia.search(page_input):
                print(item)
        page_input = input("\nPage: ")
    print("Goodbye!")


if __name__ == '__main__':
    main()
