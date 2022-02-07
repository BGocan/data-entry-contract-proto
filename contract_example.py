from pathlib import Path
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "my_contract_template.docx"
doc = DocxTemplate(document_path)


context = {"NAME":"Bruno"}
doc.render(context)
doc.save(Path(__file__).parent / "generated_doc.docx")