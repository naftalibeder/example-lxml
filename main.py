from lxml import html, etree

filenames = [
  'example-a.html',
  'example-b.html',
  'example-c.html',
]

for i, filename in enumerate(filenames):
    input_str = open(filename, 'r', encoding='utf-8').read()
    output_tree = html.fromstring(input_str)
    output_str = etree.tostring(output_tree)

    print('{}\n'.format(filename))

    print('input:')
    print('{} characters'.format(len(input_str)))
    print('"{}"\n'.format(input_str.replace('\n', '')[:100]))

    print('output:')
    print('{} characters, {} nodes'.format(len(output_str), len(output_tree)))
    print('"{}"\n'.format(output_str[:200]))

    if i < len(filenames) - 1:
        print('-------------\n')
