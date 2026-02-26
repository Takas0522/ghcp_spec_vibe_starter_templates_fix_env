---
description: 'Documentation and content creation standards'
applyTo: '**/*.md'
---

## Markdown Content Rules

The following markdown content rules are enforced in the validators:

1. **Headings**: Use `#` (H1) as the first line of the file for the document title. Use `##` (H2), `###` (H3) etc. for section structure. Each file should have exactly one H1.
2. **Lists**: Use bullet points or numbered lists for lists. Ensure proper indentation and spacing.
3. **Code Blocks**: Use fenced code blocks for code snippets. Always specify the language for syntax highlighting (e.g., `typescript`, `bash`, `text`).
4. **Links**: Use proper markdown syntax for links. Ensure that links are valid and accessible.
5. **Images**: Use proper markdown syntax for images. Include alt text for accessibility.
6. **Tables**: Use markdown tables for tabular data. Ensure proper formatting and alignment. Add spaces around pipes in separator rows (e.g., `| --- | --- |` not `|---|---|`).
7. **Line Length**: Limit line length to 400 characters for readability.
8. **Whitespace**: Use appropriate whitespace to separate sections and improve readability.
9. **Front Matter**: Include YAML front matter at the beginning of the file with required metadata fields.
10. **Trailing Newline**: Files must end with a single newline character.

## Formatting and Structure

Follow these guidelines for formatting and structuring your markdown content:

- **Headings**: Use `#` for H1 (document title, first line only), `##` for H2 and `###` for H3. Ensure that headings are used in a hierarchical manner. Recommend restructuring if content includes H4, and more strongly recommend for H5.
- **Blank Lines Around Headings**: Always add a blank line before and after every heading. This prevents MD022 warnings.
- **Lists**: Use `-` for bullet points and `1.` for numbered lists. Indent nested lists with two spaces.
- **Blank Lines Around Lists**: Always add a blank line before and after every list block. This prevents MD032 warnings.
- **Code Blocks**: Use triple backticks (`) to create fenced code blocks. Always specify the language after the opening backticks for syntax highlighting (e.g., `typescript`, `bash`, `mermaid`, `text`). Use `text` for plain text blocks without specific syntax. This prevents MD040 warnings.
- **Blank Lines Around Code Blocks**: Always add a blank line before and after every fenced code block. This prevents MD031 warnings.
- **Links**: Use `[link text](URL)` for links. Ensure that the link text is descriptive and the URL is valid.
- **Images**: Use `![alt text](image URL)` for images. Include a brief description of the image in the alt text.
- **Tables**: Use `|` to create tables. Ensure that columns are properly aligned and headers are included. In separator rows, add spaces around dashes (e.g., `| --- | --- |` not `|---|---|`). This prevents MD060 warnings.
- **Line Length**: Break lines at 80 characters to improve readability. Use soft line breaks for long paragraphs.
- **Whitespace**: Use blank lines to separate sections and improve readability. Avoid excessive whitespace.
- **Trailing Newline**: Ensure every file ends with exactly one newline character. This prevents MD047 warnings.

## Validation Requirements

Ensure compliance with the following validation requirements:

- **Front Matter**: Include the following fields in the YAML front matter:

  - `post_title`: The title of the post.
  - `author1`: The primary author of the post.
  - `post_slug`: The URL slug for the post.
  - `microsoft_alias`: The Microsoft alias of the author.
  - `featured_image`: The URL of the featured image.
  - `categories`: The categories for the post. These categories must be from the list in /categories.txt.
  - `tags`: The tags for the post.
  - `ai_note`: Indicate if AI was used in the creation of the post.
  - `summary`: A brief summary of the post. Recommend a summary based on the content when possible.
  - `post_date`: The publication date of the post.

- **Content Rules**: Ensure that the content follows the markdown content rules specified above.
- **Formatting**: Ensure that the content is properly formatted and structured according to the guidelines.
- **Validation**: Run the validation tools to check for compliance with the rules and guidelines.

## Markdownlint Rules Reference

The following markdownlint rules are enforced in this project.
Always follow these to avoid warnings:

| Rule | Description | How to Fix |
| --- | --- | --- |
| MD022 | Headings should be surrounded by blank lines | Add a blank line before and after every heading |
| MD031 | Fenced code blocks should be surrounded by blank lines | Add a blank line before and after every fenced code block |
| MD032 | Lists should be surrounded by blank lines | Add a blank line before and after every list block |
| MD040 | Fenced code blocks should have a language specified | Add a language identifier after opening triple backticks |
| MD041 | First line in a file should be a top-level heading | Start every `.md` file with `# Title` |
| MD047 | Files should end with a single newline character | Ensure one trailing newline at end of file |
| MD060 | Table pipe spacing must be consistent | Use spaces around pipes in separator rows (`\| --- \|`) |
