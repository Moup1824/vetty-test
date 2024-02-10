from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<filename>')
def display_file(filename='file1'):
    filename += '.txt'  # Append the file extension
    start_line = request.args.get('start_line', type=int)
    end_line = request.args.get('end_line', type=int)
    
    try:
        encoding = get_file_encoding(filename)
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()
            if start_line is not None and end_line is not None:
                lines = lines[start_line - 1:end_line]
            elif start_line is not None:
                lines = lines[start_line - 1:]
            elif end_line is not None:
                lines = lines[:end_line]
            content = ''.join(lines)
            return render_template('file_display.html', content=content)
    except Exception as e:
        return render_template('error.html', error=str(e))

def get_file_encoding(filename):
    if filename == 'file2.txt':
        return 'utf-16be'
    elif filename == 'file3.txt':
        return 'us-ascii'
    elif filename == 'file4.txt':
        return 'utf-16le'
    else:
        return 'utf-8'

if __name__ == '__main__':
    app.run(debug=True)

