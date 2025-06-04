from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def generate_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    x_margin = 40
    y_position = height - 50

    c.setFont("Helvetica-Bold", 20)
    c.drawString(x_margin, y_position, data['name'])

    c.setFont("Helvetica", 12)
    y_position -= 25
    c.drawString(x_margin, y_position, data['email'])
    y_position -= 20
    c.drawString(x_margin, y_position, data['phone'])
    y_position -= 30

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y_position, "Resumo Profissional")
    y_position -= 20

    c.setFont("Helvetica", 12)
    for line in data['summary'].split("\n"):
        c.drawString(x_margin, y_position, line)
        y_position -= 15

    y_position -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y_position, "Experiência Profissional")
    y_position -= 20

    c.setFont("Helvetica", 12)
    for job in data['experience']:
        c.drawString(x_margin, y_position, f"{job['role']} - {job['company']} ({job['years']})")
        y_position -= 15
        c.drawString(x_margin + 20, y_position, job['description'])
        y_position -= 30

    y_position -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y_position, "Educação")
    y_position -= 20

    c.setFont("Helvetica", 12)
    for edu in data['education']:
        c.drawString(x_margin, y_position, f"{edu['degree']} - {edu['institution']} ({edu['years']})")
        y_position -= 20

    y_position -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y_position, "Habilidades")
    y_position -= 20

    c.setFont("Helvetica", 12)
    c.drawString(x_margin, y_position, ", ".join(data['skills']))

    c.save()


if __name__ == "__main__":

    data = {
        "name": "João da Silva",
        "email": "joao.silva@email.com",
        "phone": "(11) 91234-5678",
        "summary": "Profissional com ampla experiência em desenvolvimento de software, focado em soluções eficientes e escaláveis.",
        "experience": [
            {
                "role": "Desenvolvedor Backend",
                "company": "Tech Solutions",
                "years": "2021-2024",
                "description": "Responsável por desenvolver APIs RESTful usando Python e Django."
            },
            {
                "role": "Estagiário em Desenvolvimento",
                "company": "InovaTI",
                "years": "2020-2021",
                "description": "Ajudou na manutenção de sistemas internos e correção de bugs."
            }
        ],
        "education": [
            {
                "degree": "Análise e Desenvolvimento de Sistemas",
                "institution": "FIAP",
                "years": "2018-2020"
            },
            {
                "degree": "Design Gráfico",
                "institution": "UNIP",
                "years": "2015-2017"
            }
        ],
        "skills": ["Python", "Django", "Git", "REST", "SQL", "Linux"]
    }

    filename = "curriculo_gerado.pdf"
    generate_pdf(data, filename)
    print(f"\n✅ Currículo gerado com sucesso: {filename}")
