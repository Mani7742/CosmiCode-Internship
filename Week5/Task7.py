# Implement a class to handle basic file operations
#  (reading, writing, appending) for text files.

class TextFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def append(self, content):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(content)

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.read()

if __name__ == "__main__":
    handler = TextFileHandler("sample.txt")
    handler.write("Hello, world!\n")
    handler.append("This is appended text.\n")
    print("File operations completed.")