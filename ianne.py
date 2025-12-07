from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# File path
pdf_path = "/mnt/data/MLBB_Tournament_Lobby_Proposal_Final_250k.pdf"

# Document setup
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=50, bottomMargin=40)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="HeadingCenter", fontSize=16, leading=20, spaceAfter=10, alignment=1, textColor=colors.darkblue))
styles.add(ParagraphStyle(name="SubHeading", fontSize=13, leading=18, spaceAfter=6, textColor=colors.darkblue))
body_style = styles["BodyText"]

content = []

# Title
content.append(Paragraph("Mobile Legends: Bang Bang Tournament Lobby Proposal", styles["HeadingCenter"]))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("<b>1. Introduction</b>", styles["SubHeading"]))
content.append(Paragraph("This proposal outlines the plan to organize a Mobile Legends: Bang Bang (MLBB) Tournament Lobby aimed at fostering camaraderie, showcasing player skills, and promoting the growth of the esports community. The event will serve as a platform for players to compete in a structured, fair, and exciting environment.", body_style))
content.append(Spacer(1, 8))

# Objectives
content.append(Paragraph("<b>2. Objectives</b>", styles["SubHeading"]))
objectives = [
    "To provide an organized competitive space for MLBB players.",
    "To encourage teamwork, strategy, and sportsmanship among participants.",
    "To identify and recognize top talents within the community.",
    "To strengthen community engagement and participation in esports events."
]
for obj in objectives:
    content.append(Paragraph(f"• {obj}", body_style))
content.append(Spacer(1, 8))

# Event Details
content.append(Paragraph("<b>3. Event Details</b>", styles["SubHeading"]))
data = [
    ["Event Name", "MLBB Tournament Lobby 2025"],
    ["Organizer", "ICT Department"],
    ["Platform", "Mobile Legends: Bang Bang (Official Game Lobby)"],
    ["Date", "November 30, 2025"],
    ["Time", "8:00 AM"],
    ["Venue/Server", "Online Custom Lobby"],
    ["Format", "5v5 Custom Tournament"],
    ["Game Mode", "Ranked Draft Pick"],
    ["Number of Teams", "15 Teams"],
    ["Eligibility", "Open to all registered players/organization members"],
    ["Registration Fee", "₱250 per team"]
]
table = Table(data, colWidths=[150, 300])
table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.grey), ('FONTSIZE', (0, 0), (-1, -1), 10)]))
content.append(table)
content.append(Spacer(1, 8))

# Rules
content.append(Paragraph("<b>4. Tournament Format and Rules</b>", styles["SubHeading"]))
rules = [
    "Elimination Type: Single Elimination",
    "Each match will be conducted in a custom lobby under Tournament Mode.",
    "All participants must use their registered in-game names.",
    "Teams must check in 15 minutes before their scheduled match.",
    "Unsportsmanlike behavior, cheating, or abusive language will result in disqualification.",
    "Officials: Tournament Director, Lobby Officials/Marshals, Technical Support."
]
for rule in rules:
    content.append(Paragraph(f"• {rule}", body_style))
content.append(Spacer(1, 8))

# Prizes
content.append(Paragraph("<b>5. Prizes and Recognition</b>", styles["SubHeading"]))
prize_data = [
    ["Champion", "₱100,000"],
    ["1st Runner-Up", "₱50,000"],
    ["2nd Runner-Up", "₱30,000"],
    ["3rd Runner-Up", "₱20,000"],
    ["Special Awards", "MVP, Best Tank, Best Assassin, etc. – ₱50,000 (combined)"],
    ["Total Prize Pool", "₱250,000"]
]
prize_table = Table(prize_data, colWidths=[150, 300])
prize_table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.grey), ('FONTSIZE', (0, 0), (-1, -1), 10)]))
content.append(prize_table)
content.append(Spacer(1, 8))

# Budget
content.append(Paragraph("<b>6. Budget Estimate</b>", styles["SubHeading"]))
budget_data = [
    ["Item", "Description", "Estimated Cost (₱)"],
    ["Prizes", "Cash rewards and in-game diamonds", "250,000"],
    ["Promotion", "Posters, online ads, etc.", "10,000"],
    ["Technical Needs", "Internet, devices, lobby setup", "10,000"],
    ["Miscellaneous", "Certificates, staff allowance", "5,000"],
    ["Total", "", "₱275,000"]
]
budget_table = Table(budget_data, colWidths=[150, 200, 100])
budget_table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                                  ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
                                  ('FONTSIZE', (0, 0), (-1, -1), 10)]))
content.append(budget_table)
content.append(Spacer(1, 8))

# Outcomes
content.append(Paragraph("<b>7. Expected Outcomes</b>", styles["SubHeading"]))
outcomes = [
    "Strengthened engagement among players and fans.",
    "Development of esports-related skills such as communication, leadership, and strategy.",
    "Potential discovery of skilled players for future competitions or sponsorships.",
    "Promotion of the ICT Department as a supporter of innovation and digital culture."
]
for out in outcomes:
    content.append(Paragraph(f"• {out}", body_style))
content.append(Spacer(1, 8))

# Conclusion
content.append(Paragraph("<b>8. Conclusion</b>", styles["SubHeading"]))
content.append(Paragraph("The MLBB Tournament Lobby organized by the ICT Department aims to deliver a competitive yet friendly environment for gamers to test their skills and enjoy the thrill of esports. With proper organization and community support, this event will contribute positively to the growth of local esports culture and the department’s reputation for promoting digital excellence.", body_style))

# Build PDF
doc.build(content)

pdf_path
