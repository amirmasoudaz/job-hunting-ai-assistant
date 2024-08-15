import os.path

from docx import Document
from docx2pdf import convert

from tools import DocxFormatting


class LetterBuilder:
    def __init__(self, template: str = "simple"):
        root = os.path.dirname(os.path.dirname(__file__))
        self.template_path = os.path.join(root, "letter", "templates", f"{template}.docx")

    def build(self, data: dict, path: str, file_name: str):
        doc = Document(self.template_path)
        replacer = DocxFormatting(doc)
        replacer.replace_keys(
            DATE=data['date'],
            NAME=data['recipient']['name'],
            OCCUPATION=data['recipient']['occupation'],
            COMPANY=data['recipient']['company'],
            CONTACT="\n".join(
                contact for contact in [
                    data['recipient'].get('email_address'),
                    data['recipient'].get('phone_number'),
                    data['recipient'].get('address')
                ] if contact),
            JOB_REFERENCE=data['letter']['job_reference'],
            OPENING=data['letter']['opening'],
            PARAGRAPH_ONE=data['letter']['paragraph_one'],
            PARAGRAPH_TWO=data['letter']['paragraph_two'],
            PARAGRAPH_THREE=data['letter']['paragraph_three'],
            PARAGRAPH_FOUR=data['letter'].get('paragraph_four', ''),
            APPRECIATION=data['letter']['appreciation'],
            CLOSING=data['letter']['closing'],
            SIGNATURE=data['letter']['signature'])

        docx_path = os.path.join(path, f"{file_name}.docx")
        pdf_path = os.path.join(path, f"{file_name}.pdf")
        doc.save(docx_path)
        convert(docx_path, pdf_path)


if __name__ == "__main__":
    from builders.letter.samples import sample as sample

    root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(root, "letter", "outputs")
    builder = LetterBuilder(template="simple")
    builder.build(data=sample, path=path, file_name="Sample")
