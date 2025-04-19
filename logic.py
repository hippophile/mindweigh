def calculate_scores(title1, scores1, title2, scores2):
    def analyze(scores):
        # Χωρισμός σε κατηγορίες
        motivation = (scores["Motivation"] + scores["Προσωπικό Νόημα"] + scores["Δύναμη Ιδέας"]) / 3
        practicality = (scores["Χρησιμότητα"] + scores["Πιθανότητα Επιτυχίας"]) / 2
        burden = (scores["Κόπος"] + scores["Συναισθηματικό Βάρος"] + scores["Χρόνος"]) / 3

        # Μικρή ποινή αν burden > 7
        penalty = 0.5 if burden > 7 else 0

        # Τελικό σκορ με βάση αυτά (60% motivation, 40% practicality - penalty)
        final_score = (0.4 * motivation + 0.6 * practicality) - penalty

        return {
            "final": round(final_score, 2),
            "motivation": round(motivation, 2),
            "practicality": round(practicality, 2),
            "burden": round(burden, 2)
        }

    analysis1 = analyze(scores1)
    analysis2 = analyze(scores2)

    result = (
        f"{title1}:\n"
        f"  - Κίνητρο: {analysis1['motivation']}\n"
        f"  - Πρακτικότητα: {analysis1['practicality']}\n"
        f"  - Βάρος: {analysis1['burden']}\n"
        f"  → Τελικό: {analysis1['final']}\n\n"
        f"{title2}:\n"
        f"  - Κίνητρο: {analysis2['motivation']}\n"
        f"  - Πρακτικότητα: {analysis2['practicality']}\n"
        f"  - Βάρος: {analysis2['burden']}\n"
        f"  → Τελικό: {analysis2['final']}\n\n"
    )

    if analysis1["final"] > analysis2["final"]:
        result += f"✅ Προτείνεται: {title1}"
    elif analysis2["final"] > analysis1["final"]:
        result += f"✅ Προτείνεται: {title2}"
    else:
        result += "➖ Ισοπαλία"

    return result
