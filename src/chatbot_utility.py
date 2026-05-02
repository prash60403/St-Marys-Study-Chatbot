import os

working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

def get_chapter_list(selected_subject):

    chapters_dir = f"{parent_dir}/text_books/{selected_subject}"

    chapters_list = os.listdir(chapters_dir)

    # Remove .pdf extension
    chapters_list = [
        x[:-4] for x in chapters_list if x.endswith(".pdf")
    ]

    # Simple alphabetical sorting
    chapters_list.sort()

    return chapters_list

