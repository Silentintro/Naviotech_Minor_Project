RISKS = [
    ("Phishing", 5, 4),
    ("Ransomware", 3, 5),
    ("Weak/reused passwords", 4, 3),
    ("Unpatched software", 3, 4),
    ("Insider threats", 2, 4),
    ("Misconfigured cloud storage", 2, 4),
    ("Lack of employee awareness", 3, 2),
]


def priority_band(score: int) -> str:
    
    if score >= 15:
        return "Critical/High"
    elif score >= 7:
        return "Medium"
    else:
        return "Low"


def assess_risks(risks):
    
    results = []
    for name, likelihood, impact in risks:
        score = likelihood * impact
        results.append({
            "risk": name,
            "likelihood": likelihood,
            "impact": impact,
            "score": score,
            "priority": priority_band(score),
        })
    results.sort(key=lambda r: r["score"], reverse=True)
    return results


def print_report(results):
    print(f"{'Risk':<32}{'Likelihood':<12}{'Impact':<10}{'Score':<8}{'Priority'}")
    print("-" * 80)
    for r in results:
        print(f"{r['risk']:<32}{r['likelihood']:<12}{r['impact']:<10}{r['score']:<8}{r['priority']}")


if __name__ == "__main__":
    results = assess_risks(RISKS)
    print_report(results)
