# MedStudy Oman Content Workflow

Use the app's **Admin Content Panel** to scale the library without editing Python.

## Recommended Flow

1. Log in with an admin email.
2. Open **Admin** from the navigation.
3. Use **Bulk Upload** for CSV, Excel, JSON, or Markdown.
4. Import everything as `draft` or `reviewed`.
5. Use **Review & Publish** to publish content after checking accuracy.

## Bulk Columns

The safest CSV columns are:

`content_type, subject, chapter, topic, title, content, summary, point, explanation, front, back, stem, option_a, option_b, option_c, option_d, option_e, correct_option, difficulty, status, url, citation, resource_type`

Supported `content_type` values:

`note`, `high_yield_point`, `clinical_correlation`, `mnemonic`, `flashcard`, `mcq`, `osce_case`, `resource`

## Where Content Appears

- Published subjects/chapters/topics appear in **Med Hub / Library**.
- Published MCQs appear in **Question Bank**.
- Published flashcards appear in **Cards**.
- Bookmarks, completed topics, quiz attempts, flashcard reviews, and study activity are saved per logged-in user.

## Templates

- CSV starter: `content_templates/bulk_content_template.csv`
- Markdown starter: `content_templates/topic_markdown_template.md`

For large A-Z loading, create one CSV per subject or one Excel workbook exported to CSV, then upload it from Admin.
