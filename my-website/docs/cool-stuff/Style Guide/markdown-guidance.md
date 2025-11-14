---
title: 'Section 4: Markdown Guidance'
description: Guide to using markdown in documents
sidebar_position: 4
---

# Markdown Guidance

I only included a few basics here. For more markdown guidance go [here](https://www.markdownguide.org/basic-syntax/).

For details of the markdown features in Docusaurus see [Docusaurus Markdown Feature](https://docusaurus.io/docs/markdown-features)

## How to Format Links

### Add links to other pages in our site

Use standard markdown link syntax with a path relative to the docs root with a leading slash.

Examples:

- `[Link text](/about/)` \--\> goes to the `about.md` page in the root directory.
- `[Link text](/about.md\#how-does-MDS-work)` \--\> goes to an anchor on the Overview page.
- `[Link text](/MDS/notifications/)` \--\> goes to the notifications.md page in the MDS directory.

### Add links to external pages

Use standard markdown syntax: `[Link text](https://google.com)`

## How to Format Images

(See [“How to Annotate Screenshots”](/contributors/style-guide/formatting-and-annotations/#how-to-annotate-screenshots))

### Markdown format in file:

`![Image alt tag value](/img/filename.png)`

### Image Storage

Images are saved as .png files in the zmgt-docs/static/img folder.

File naming convention: tool-section-function-step.png (If any part of the naming convention in not applicable, simply omit it)

## How to Format Videos

Videos should adhere to the following conventions:

- No more than 3 minutes long.
- Always include narration that explains the visual content. Keep it simple and clear.
- Orient the user as to where they are in the UI \- page, tab, window
- Visual content should move slowly and smoothly, avoiding jumping and quick mouse moves.

The way to achieve the best result is to:

- Write out the script
- Practice the video before you produce
- Use a tool like Camtasia so content can be easily edited.

### To add videos content to a page

TBD

## How To Format Front Matter

The sidebar is automatically created from the front matter.

At the top of each page you must add the following, which provides the sidebar content and heading.

```yml
---
title: 'This is the Title'
sidebar_label: 'This is in the Sidebar'
description: >
  This is a short description of the contents of the page.

---
```

For more details one front matter see [Docusaurus API documentation](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-front-matter).

## How to Format Tables

To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. For compatibility, you should also add a pipe on either end of the row.

### Tables with uniform column widths

```
| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |
```

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

### Tables with different column widths

```
| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |
```

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

### Tables with Alignment Left, Center, and Right

```
| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |
```

| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |

## How to Format Code and Code Blocks

To generate a code block:

````
```json
{
	"firstName": "John",
	"lastName": "Smith",
	"age": 25
}
```
````

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

```markdown
To add code to a line of text, put tickmarks around the code you want formatted,  
like `"firstName": "John"` , and it will be displayed correctly.
```

To add code to a line of text, put tickmarks around the code you want formatted, like `"firstName": "John"` , and it will be displayed correctly.
