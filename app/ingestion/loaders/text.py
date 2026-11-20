import logfire

def parse_text(file_path:str):
    """_summary_
    Parse the plane text files
    Args:
        file_path (str): _description_
    """

    with logfire.span("📄 Text Parsing....", file_name = file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            logfire.error(f"❌ Text parse failed:{e}")
            raise e

if __name__ ==  '__main__':
    file_path = r'DATA\true_data\parallel_work_queue.txt'

    result = parse_text(file_path=file_path)
    print(result)

