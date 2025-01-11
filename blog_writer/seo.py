def seo_analysis(content, keywords):
    word_count = len(content.split())
    keyword_density = sum(content.lower().count(kw.lower()) for kw in keywords) / word_count * 100
    return {
        "word_count": word_count,
        "keyword_density": f"{keyword_density:.2f}%"
    }
