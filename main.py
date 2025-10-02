from dotenv import load_dotenv
load_dotenv()

def get_text_length(text:str) -> int:
    """Returns the length of the text by character count"""
    return len(text)

if __name__ == "__main__":
    print("Hello ReAct Langchain!")
    print(get_text_length(text="Hello, world!"))