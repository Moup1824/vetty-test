from flask import Flask, render_template, request
import os

app = Flask(_name_)

@app.route('/')
@app.route('/<selected_file>')
def display_selected_file(selected_file='file1'):
    selected_file += '.txt'  # Append the file extension
    start_line = request.args.get('start_line', type=int)
    end_line = request.args.get('end_line', type=int)
    
    try:
        selected_encoding = determine_file_encoding(selected_file)
        with open(selected_file, 'r', encoding=selected_encoding) as file_content:
            lines = file_content.readlines()
            if start_line is not None and end_line is not None:
                lines = lines[start_line - 1:end_line]
            elif start_line is not None:
                lines = lines[start_line - 1:]
            elif end_line is not None:
                lines = lines[:end_line]
            content = ''.join(lines)
            return render_template('file_display.html', content=content)
    except Exception as error:
        return render_template('error.html', error_message=str(error))

def determine_file_encoding(selected_file):
    if selected_file == 'file2.txt':
        return 'utf-16be'
    elif selected_file == 'file3.txt':
        return 'us-ascii'
    elif selected_file == 'file4.txt':
        return 'utf-16le'
    else:
        return 'utf-8'

if _name_ == '_main_':
    app.run(debug=True)
