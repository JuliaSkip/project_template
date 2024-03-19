from app.io.input import input_from_console, read_file_builtin, read_file_with_pandas
from app.io.output import output_to_console, write_file_builtin, write_file_pandas

def main():
    input_text = input_from_console()
    file_text_builtin = read_file_builtin("data/example.txt")
    file_text_pandas = read_file_with_pandas("data/example.csv")

    output_to_console(input_text)
    output_to_console(file_text_builtin)
    output_to_console(file_text_pandas)

    write_file_builtin(input_text, "data/output.txt")
    write_file_builtin(file_text_builtin, "data/output_builtin.txt")
    write_file_pandas(file_text_pandas, "data/output_pandas.csv")

if __name__ == "__main__":
    main()
