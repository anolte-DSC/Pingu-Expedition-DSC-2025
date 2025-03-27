import pandas as pd
def csv_to_markdown(input_file, output_file):
    # Read the CSV file with tab delimiter
    df = pd.read_csv(input_file, delimiter='\t')

    # Create the Markdown header
    header = '| ' + ' | '.join(df.columns) + ' |'
    separator = '| ' + ' | '.join(['---'] * len(df.columns)) + ' |'

    # Create the Markdown rows
    rows = '\n'.join(['| ' + ' | '.join(map(str, row)) + ' |' for row in df.values])

    # Combine everything
    markdown_table = f"{header}\n{separator}\n{rows}"

    # Write to the output file
    with open(output_file, 'w') as f:
        f.write(markdown_table)

    print(f"Markdown table saved to {output_file}")

# Usage
csv_to_markdown('Data.csv', 'output.md')